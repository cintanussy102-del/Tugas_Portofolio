import os
from flask import Flask
from datetime import timedelta
from dotenv import load_dotenv

# Load environment variables dari file .env
load_dotenv()

app = Flask(
    __name__, 
    template_folder='Frontend',          # Mengarah ke induk agar Admin & Utama bisa diakses
    static_folder='Frontend/Utama',       # Tetap mengunci static di Utama agar tampilan tidak berubah
    static_url_path='/Frontend/Utama'     # URL path untuk aset static
)

# Konfigurasi Secret Key dan Session
app.secret_key = os.getenv("SECRET_KEY", "bukan_rahasia_123")
app.permanent_session_lifetime = timedelta(minutes=30)

# ==============================================================================
# IMPORT & REGISTRASI BLUEPRINT (Sesuaikan dengan nama blueprint asli kamu)
# ==============================================================================

# 1. Blueprint untuk Halaman Utama/Frontend
from Backend.utama.utama import utama_bp
app.register_blueprint(utama_bp)

# 2. Blueprint untuk Halaman Admin (Login, Dashboard, dll)
from Backend.admin.login import login_bp
from Backend.admin.dashboard import dashboard_bp
from Backend.admin.skills import skills_bp
from Backend.admin.projects import projects_bp
from Backend.admin.profiles import profiles_bp
from Backend.admin.experience import experience_bp
from Backend.admin.settings import settings_bp

app.register_blueprint(login_bp, url_prefix='/admin')
app.register_blueprint(dashboard_bp, url_prefix='/admin')
app.register_blueprint(skills_bp, url_prefix='/admin')
app.register_blueprint(projects_bp, url_prefix='/admin')
app.register_blueprint(profiles_bp, url_prefix='/admin')
app.register_blueprint(experience_bp, url_prefix='/admin')
app.register_blueprint(settings_bp, url_prefix='/admin')

if __name__ == '__main__':
    # Menjalankan server di mode debug untuk localhost
    app.run(debug=True, port=5000)