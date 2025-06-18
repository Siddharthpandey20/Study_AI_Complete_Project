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
        
        response = requests.get(url)
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
