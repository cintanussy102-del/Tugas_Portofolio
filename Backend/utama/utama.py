from flask import Blueprint, render_template
# Jika kamu menggunakan model atau database, import di sini (misal: from model import ...)

utama_bp = Blueprint('utama', __name__)

@utama_bp.route('/')
def home():
    # Mengarahkan template ke subfolder Utama/index.html tanpa mengubah isi tampilannya
    return render_template('Utama/index.html')