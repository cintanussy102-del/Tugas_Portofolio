import pymysql
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from config import Config

message_admin_bp = Blueprint('messages_admin', __name__)

@message_admin_bp.route('/admin/messages')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('admin.login'))
        
    messages_list = []
    
    try:
        connection = pymysql.connect(
            host=Config.TIDB_HOST,
            user=Config.TIDB_USER,
            password=Config.TIDB_PASSWORD,
            port=getattr(Config, 'TIDB_PORT', 4000),
            database='test',  # Tetap dikunci di 'test'
            cursorclass=pymysql.cursors.DictCursor
        )
    except Exception as e:
        print(f"Koneksi Database Admin Pesan Gagal: {e}")
        connection = None

    if connection:
        try:
            with connection.cursor() as cursor:
                # Mengambil semua pesan, yang terbaru muncul paling atas
                cursor.execute("SELECT * FROM messages ORDER BY created_at DESC")
                messages_list = cursor.fetchall()
        except Exception as e:
            print(f"Error fetching messages: {e}")
        finally:
            connection.close()
        
    return render_template('admin/messages.html', messages=messages_list)

# ==========================================
# FITUR BARU: HAPUS PESAN
# ==========================================
@message_admin_bp.route('/admin/messages/delete/<int:msg_id>', methods=['POST'])
def delete_message(msg_id):
    if not session.get('logged_in'):
        return redirect(url_for('admin.login'))
        
    try:
        connection = pymysql.connect(
            host=Config.TIDB_HOST,
            user=Config.TIDB_USER,
            password=Config.TIDB_PASSWORD,
            port=getattr(Config, 'TIDB_PORT', 4000),
            database='test',
            cursorclass=pymysql.cursors.DictCursor
        )
        
        with connection.cursor() as cursor:
            # Perintah SQL untuk menghapus pesan berdasarkan ID
            cursor.execute("DELETE FROM messages WHERE id = %s", (msg_id,))
            connection.commit()
            
    except Exception as e:
        print(f'Gagal menghapus pesan: {e}')
    finally:
        if 'connection' in locals() and connection:
            connection.close()
            
    # Setelah dihapus, segarkan halaman secara otomatis
    return redirect(url_for('message_admin.index'))