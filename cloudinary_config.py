import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
import requests
from typing import Dict, Any
from datetime import datetime
import time

# Cloudinary configuration - NO DEFAULT VALUES
CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")

# Validate required environment variables
if not CLOUDINARY_CLOUD_NAME:
    raise ValueError("CLOUDINARY_CLOUD_NAME environment variable is required")
if not CLOUDINARY_API_KEY:
    raise ValueError("CLOUDINARY_API_KEY environment variable is required")
if not CLOUDINARY_API_SECRET:
    raise ValueError("CLOUDINARY_API_SECRET environment variable is required")

# Configure Cloudinary
cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET
)

async def upload_file_to_cloudinary(file_content: bytes, filename: str, user_id: int):
    """Upload file to Cloudinary and return public URL"""
    try:
        # Create a unique filename
        timestamp = int(time.time())
        safe_filename = filename.replace(' ', '_').replace('(', '').replace(')', '')
        unique_filename = f"user_{user_id}/{safe_filename}_{timestamp}"
        
        # Upload to Cloudinary with public read access
        upload_result = cloudinary.uploader.upload(
            file_content,
            public_id=unique_filename,
            folder=f"study_ai/user_{user_id}",
            resource_type="auto",
            # Ensure the file is publicly accessible
            type="upload",
            access_mode="public",
            # Add these parameters for better access
            secure=True,
            overwrite=True,
            invalidate=True
        )
        
        print(f"✅ File uploaded to Cloudinary: {upload_result['public_id']}")
        
        return {
            "url": upload_result["secure_url"],
            "public_id": upload_result["public_id"]
        }
        
    except Exception as e:
        print(f"❌ Cloudinary upload error: {str(e)}")
        raise Exception(f"Failed to upload file: {str(e)}")

def fetch_cloudinary_file(url: str, headers=None, timeout: int = 30) -> requests.Response:
    """GET a stored file, falling back to Cloudinary's signed download API.

    Cloudinary blocks public delivery of PDF and ZIP files by default on new
    accounts, so the public URL returns 401. The signed download endpoint is
    authenticated with the API key and secret, so it works either way.
    """
    import re
    import cloudinary.utils

    response = requests.get(url, headers=headers, timeout=timeout)
    if response.status_code not in (401, 403):
        return response

    match = re.match(
        r"https?://res\.cloudinary\.com/[^/]+/(image|raw|video)/(upload|private|authenticated)/(?:v\d+/)?(.+)$",
        url,
    )
    if not match:
        return response
    resource_type, delivery_type, path = match.groups()
    public_id, file_format = path, ""
    if resource_type != "raw" and "." in path.rsplit("/", 1)[-1]:
        public_id, file_format = path.rsplit(".", 1)
    signed_url = cloudinary.utils.private_download_url(
        public_id, file_format, resource_type=resource_type, type=delivery_type
    )
    return requests.get(signed_url, timeout=timeout)


def delete_file_from_cloudinary(public_id: str):
    """Delete file from Cloudinary"""
    try:
        result = cloudinary.uploader.destroy(public_id)
        return result
    except Exception as e:
        print(f"Error deleting from Cloudinary: {e}")
        return None

async def download_file_from_cloudinary(url: str) -> str:
    """Download and extract text content from Cloudinary URL"""
    try:
        # Import extraction functions here to avoid circular imports
        from functions import extract_text_from_pdf, extract_text_from_docx
        
        response = fetch_cloudinary_file(url)
        response.raise_for_status()
        
        # Determine file type and extract text
        if url.lower().endswith('.pdf'):
            return extract_text_from_pdf(response.content)
        elif url.lower().endswith(('.docx', '.doc')):
            return extract_text_from_docx(response.content)
        else:
            return response.text
            
    except Exception as e:
        raise Exception(f"Failed to download from Cloudinary: {str(e)}")
        raise Exception(f"Failed to download from Cloudinary: {str(e)}")
