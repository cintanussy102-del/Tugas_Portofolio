from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from model import get_experiences, add_experience, delete_experience

experience_admin_bp = Blueprint('experience_admin', __name__)

@experience_admin_bp.route('/admin/experience', methods=['GET', 'POST'])
def manage_experience():
    if not session.get('logged_in'):
        return redirect(url_for('admin.login'))
        
    if request.method == 'POST':
        action = request.form.get('action')
        
        # PROSES TAMBAH DATA (Create)
        if action == 'add':
            year = request.form.get('year')
            title = request.form.get('title')
            place = request.form.get('place')
            desc = request.form.get('desc')
            
            if year and title and place and desc:
                if add_experience(year, title, place, desc):
                    flash('Experience successfully added!', 'success')
                else:
                    flash('Failed to add experience.', 'danger')
                    
        # PROSES HAPUS DATA (Delete)
        elif action == 'delete':
            exp_id = request.form.get('id')
            if exp_id:
                if delete_experience(exp_id):
                    flash('Experience successfully deleted!', 'success')
                    
        return redirect(url_for('experience_admin.manage_experience'))

    all_experiences = get_experiences()
    return render_template('admin/experience.html', experiences=all_experiences)