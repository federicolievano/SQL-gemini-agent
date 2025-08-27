# Example configuration file - Copy this to config.py and update with your values

import os

from dotenv import load_dotenv

load_dotenv()

# Database configuration
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "tu_contraseña_aqui"),  # UPDATE THIS
    "database": os.getenv(
        "DB_NAME", "sakila"
    ),  # UPDATE THIS if using different database
    "charset": "utf8mb4",
}

# Gemini API Key - UPDATE THIS
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY", "tu_api_key_de_gemini_aqui")

# Example .env file content:
# DB_HOST=localhost
# DB_PORT=3306
# DB_USER=root
# DB_PASSWORD=tu_contraseña_real
# DB_NAME=sakila
# GOOGLE_API_KEY=tu_api_key_real_de_gemini
