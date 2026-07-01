import os
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv

# Memastikan file .env dibaca dengan benar
load_dotenv()

def configure_cloudinary():
    """Mengonfigurasi SDK Cloudinary langsung membaca dari file .env via os.getenv"""
    cloudinary.config(
        cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME'),
        api_key = os.getenv('CLOUDINARY_API_KEY'),
        api_secret = os.getenv('CLOUDINARY_API_SECRET')
    )

def upload_image_to_cloudinary(file_to_upload):
    """Mengunggah file gambar ke Cloudinary dan mengembalikan URL gambar online"""
    try:
        configure_cloudinary()
        # Melakukan upload ke folder khusus portfolio
        upload_result = cloudinary.uploader.upload(file_to_upload, folder="portfolio_cinta")
        # Mengembalikan URL aman (HTTPS) dari Cloudinary
        return upload_result.get('secure_url')
    except Exception as e:
        print(f"Error uploading to Cloudinary: {e}")
        return None