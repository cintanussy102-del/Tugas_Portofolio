import os
from dotenv import load_dotenv

# Memuat file .env (untuk localhost)
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'super_rahasia_kamu_123')
    
    TIDB_HOST = os.environ.get('TIDB_HOST') or os.environ.get('DB_HOST')
    TIDB_USER = os.environ.get('TIDB_USER') or os.environ.get('DB_USER')
    TIDB_PASSWORD = os.environ.get('TIDB_PASSWORD') or os.environ.get('DB_PASSWORD')
    TIDB_DATABASE = os.environ.get('TIDB_DATABASE') or os.environ.get('DB_NAME')
    
    CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL')
    RESEND_API_KEY = os.environ.get('RESEND_API_KEY')