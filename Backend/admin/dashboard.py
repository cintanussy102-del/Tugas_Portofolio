from flask import Blueprint, render_template, session, redirect

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    # Proteksi halaman admin agar harus login dulu
    if not session.get('logged_in'):
        return redirect('/admin/login')
        
    # Mengarahkan ke Admin/dashboard.html
    return render_template('Admin/dashboard.html')