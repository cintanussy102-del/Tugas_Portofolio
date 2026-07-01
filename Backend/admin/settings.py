import pymysql
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from config import Config

settings_admin_bp = Blueprint('settings_admin', __name__)

@settings_admin_bp.route('/admin/settings', methods=['GET', 'POST'])
def index():
    if not session.get('logged_in'):
        return redirect(url_for('admin.login'))
        
    if request.method == 'POST':
        new_username = request.form.get('username')
        new_password = request.form.get('password')
        current_user = session.get('username')
        
        # Menggunakan koneksi database langsung lewat atribut Class Config asli
        try:
            connection = pymysql.connect(
                host=Config.TIDB_HOST,
                user=Config.TIDB_USER,
                password=Config.TIDB_PASSWORD,
                port=getattr(Config, 'TIDB_PORT', 4000),
                database=getattr(Config, 'TIDB_DB_NAME', Config.TIDB_USER),
                cursorclass=pymysql.cursors.DictCursor
            )
        except Exception as e:
            print(f"Koneksi Database Gagal: {e}")
            connection = None

        if connection:
            try:
                with connection.cursor() as cursor:
                    # Update data admin baru ke database
                    # Catatan: ganti 'admin_users' sesuai nama tabel user admin di database TiDB-mu jika berbeda
                    sql = "UPDATE admin_users SET username = %s, password = %s WHERE username = %s"
                    cursor.execute(sql, (new_username, new_password, current_user))
                    connection.commit()
                    
                    # Perbarui session username yang aktif
                    session['username'] = new_username
                    flash('Username atau Password berhasil diperbarui!')
            except Exception as e:
                flash(f'Gagal memperbarui pengaturan: {e}')
            finally:
                connection.close()
            
        return redirect(url_for('settings_admin.index'))
        
    return render_template('admin/settings.html')