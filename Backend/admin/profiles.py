from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from model import get_profile, update_profile

profiles_admin_bp = Blueprint('profiles_admin', __name__)

@profiles_admin_bp.route('/admin/profiles', methods=['GET', 'POST'])
def manage_profile():
    # Proteksi: Jika belum login, tendang balik ke login page
    if not session.get('logged_in'):
        return redirect(url_for('admin.login'))
        
    if request.method == 'POST':
        nama = request.form.get('nama')
        peran = request.form.get('peran')
        deskripsi = request.form.get('deskripsi')
        sub_deskripsi = request.form.get('sub_deskripsi')
        
        # Eksekusi update data ke TiDB Cloud
        if update_profile(nama, deskripsi, peran, sub_deskripsi):
            flash('Profile successfully updated!', 'success')
        else:
            flash('Failed to update profile.', 'danger')
            
        return redirect(url_for('profiles_admin.manage_profile'))

    # Ambil data profil saat ini untuk ditampilkan di dalam kotak form input (Read)
    current_profile = get_profile()
    return render_template('admin/profiles.html', profile=current_profile)