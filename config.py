import os
from dotenv import load_dotenv

load_dotenv()

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'Magister12345#'),
    'database': os.getenv('DB_NAME', 'world'),
    'charset': 'utf8mb4'
}

# Gemini API Key
GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY', 'AIzaSyB4dW2wzsPy6tj9unFMgpY0or5k9237oJE') 