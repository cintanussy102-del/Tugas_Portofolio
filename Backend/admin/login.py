from flask import Blueprint, render_template, request, redirect, url_prefix, session, flash

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Contoh validasi sederhana (silakan sesuaikan dengan logika databasemu)
        if username == "admin" and password == "admin123":
            session['logged_in'] = True
            session.permanent = True
            return redirect('/admin/dashboard')
        else:
            flash("Username atau password salah!", "danger")
            
    # Mengarahkan ke Admin/login.html menggunakan huruf kapital sesuai struktur folder
    return render_template('Admin/login.html')

@login_bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/admin/login')