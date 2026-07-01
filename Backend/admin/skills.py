from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from model import get_skills, add_skill, delete_skill

# Menyamakan nama variabel dengan yang di-import oleh app.py
skills_admin_bp = Blueprint('skills_admin', __name__)

@skills_admin_bp.route('/admin/skills', methods=['GET', 'POST'])
def manage_skills():
    # Proteksi: Jika belum login, tendang kembali ke login page
    if not session.get('logged_in'):
        return redirect(url_for('admin.login'))
        
    if request.method == 'POST':
        action = request.form.get('action')
        
        # PROSES TAMBAH DATA SKILL (Create)
        if action == 'add':
            name = request.form.get('name')
            img = request.form.get('img') 
            
            if name and img:
                if add_skill(name, img):
                    flash('Skill successfully added!', 'success')
                else:
                    flash('Failed to add skill.', 'danger')
                    
        # PROSES HAPUS DATA SKILL (Delete)
        elif action == 'delete':
            skill_id = request.form.get('id')
            if skill_id:
                if delete_skill(skill_id):
                    flash('Skill successfully deleted!', 'success')
                    
        return redirect(url_for('skills_admin.manage_skills'))

    # Ambil data langsung dari TiDB Cloud (Read)
    all_skills = get_skills()
    return render_template('admin/skills.html', skills=all_skills)