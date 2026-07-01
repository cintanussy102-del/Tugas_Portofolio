from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from model import get_projects, add_project, delete_project
# Menggunakan helper upload media Cloudinary kita
from .upload import upload_image_to_cloudinary

projects_admin_bp = Blueprint('projects_admin', __name__)

@projects_admin_bp.route('/admin/projects', methods=['GET', 'POST'])
def manage_projects():
    if not session.get('logged_in'):
        return redirect(url_for('admin.login'))
    # SCRIPT SEMENTARA UNTUK CEK NAMA KOLOM ASLI
    from model import get_db_connection
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("DESCRIBE projects")
        columns = cursor.fetchall()
        print("--- STRUKTUR TABEL PROJECTS KAMU ---")
        for col in columns:
            print(col)
        print("------------------------------------")
    conn.close()
    
    if request.method == 'POST':
        action = request.form.get('action')
        
        # PROSES UNGGAH DAN SIMPAN PROJECT BARU
        if action == 'add':
            title = request.form.get('title')
            description = request.form.get('description')
            cover_file = request.files.get('cover_file') # Tangkap berkas gambar
            tags = request.form.get('tags')
            
            if title and description and cover_file and tags:
                # 1. Kirim file cover ke Cloudinary server
                cloudinary_url = upload_image_to_cloudinary(cover_file)
                
                if cloudinary_url:
                    # 2. Masukkan alamat URL awan ke TiDB Cloud
                    if add_project(title, description, cloudinary_url, tags):
                        flash('Project successfully added with Cloudinary Cover!', 'success')
                    else:
                        flash('Failed to save project data to database.', 'danger')
                else:
                    flash('Failed to upload cover image to Cloudinary.', 'danger')
                    
        # PROSES PENGECEKAN HAPUS
        elif action == 'delete':
            project_id = request.form.get('id')
            if project_id:
                if delete_project(project_id):
                    flash('Project successfully deleted!', 'success')
                    
        return redirect(url_for('projects_admin.manage_projects'))

    all_projects = get_projects()
    return render_template('admin/projects.html', projects=all_projects)