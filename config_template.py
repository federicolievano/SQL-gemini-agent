# Configuration template - Copy this to config.py and update with your values
# IMPORTANT: Never commit your actual API keys or passwords to Git!

import os
from dotenv import load_dotenv

load_dotenv()

# Database configuration
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),  # Set this in .env file
    "database": os.getenv("DB_NAME", "world"),  # Set this in .env file
    "charset": "utf8mb4",
}

# Gemini API Key - Set this in .env file
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY", "")

# Example .env file content (create this file locally, never commit it):
# DB_HOST=localhost
# DB_PORT=3306
# DB_USER=root
# DB_PASSWORD=your_actual_password
# DB_NAME=world
# GOOGLE_API_KEY=your_actual_gemini_api_key
