#!/usr/bin/env python3
import os
import sys
import subprocess
import time

def create_directories():
    """Create necessary directories"""
    directories = ['static', 'templates', 'uploads']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✓ Created directory: {directory}")

def check_dependencies():
    """Check if all dependencies are installed"""
    try:
        import fastapi
        import uvicorn
        import google.generativeai
        import PyPDF2
        import docx
        import pandas
        import authlib
        import sqlalchemy
        import cloudinary
        print("✓ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        print("Installing requirements...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        return True

def setup_environment():
    """Setup environment variables"""
    env_file = ".env"
    if not os.path.exists(env_file):
        print("📝 Creating .env file...")
        with open(env_file, 'w') as f:
            f.write("""# Google OAuth Configuration
GOOGLE_CLIENT_ID=your_google_client_id_here
GOOGLE_CLIENT_SECRET=your_google_client_secret_here

# Cloudinary Configuration
CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret

# Security Configuration
SECRET_KEY=your_super_secret_jwt_key_change_in_production

# Database Configuration
DATABASE_URL=sqlite:///./study_ai.db

# AI/ML APIs
GEMINI_API_KEY=your_gemini_api_key_here

# Application Configuration
NODE_ENV=development
PORT=8000
DEBUG=false

# Optional APIs
YOUTUBE_API_KEY=your_youtube_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
""")
        print("✓ Created .env file - Please update with your actual credentials")
        print("⚠️  IMPORTANT: Add your real API keys to the .env file before running the application!")
    else:
        print("✓ .env file exists")

def create_basic_template():
    """Create basic HTML template if it doesn't exist"""
    template_path = "templates/index.html"
    if not os.path.exists(template_path):
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smart Study Tool - Loading...</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            text-align: center; 
            margin-top: 50px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            min-height: 100vh;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }
        .loading {
            font-size: 1.5rem;
            margin: 2rem 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🧠 Smart Study Tool</h1>
        <div class="loading">API is running successfully!</div>
        <p>Visit <a href="/docs" style="color: #a5f3fc;">/docs</a> to see the API documentation</p>
        <p>The frontend will be available once the full template is loaded.</p>
        
        <div style="margin-top: 3rem;">
            <h3>Available Features:</h3>
            <ul style="text-align: left; max-width: 500px; margin: 0 auto;">
                <li>🔥 Smart Flashcards Generation</li>
                <li>📝 MCQ Quiz Creation</li>
                <li>🧠 Interactive Mind Maps</li>
                <li>🎯 Learning Path Generator</li>
                <li>🎨 Smart Sticky Notes (Color-coded)</li>
                <li>🏆 Exam Question Predictor</li>
            </ul>
        </div>
    </div>
</body>
</html>""")
        print("✓ Created basic HTML template")

def main():
    """Main startup function"""
    print("🚀 Starting Smart Study Tool with Authentication...")
    print("=" * 60)
    
    # Create directories
    create_directories()
    
    # Check dependencies
    check_dependencies()
    
    # Setup environment
    setup_environment()
    
    # Create basic template
    create_basic_template()
    
    print("=" * 60)
    print("✓ Setup complete!")
    print("🔐 Authentication: Google OAuth enabled")
    print("☁️  Storage: Cloudinary integration ready")
    print("🌟 Starting the application...")
    print("📱 Access the app at: http://localhost:8000")
    print("📚 API Documentation: http://localhost:8000/docs")
    print("=" * 60)
    
    # Start the application
    try:
        import uvicorn
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        print("💡 Try running: python main.py")

if __name__ == "__main__":
    main()
