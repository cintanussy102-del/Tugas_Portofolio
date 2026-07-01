import pymysql
import os
from config import Config

def get_db_connection():
    # Mengambil kredensial dari config dengan aman lewat environment variables
    return pymysql.connect(
        host=Config.TIDB_HOST,
        user=Config.TIDB_USER,
        password=Config.TIDB_PASSWORD,
        database=Config.TIDB_DATABASE,
        port=4000, # Default port untuk TiDB Cloud
        ssl_verify_cert=True, # Mengaktifkan koneksi aman SSL bawaan TiDB Cloud
        ssl_verify_identity=True,
        cursorclass=pymysql.cursors.DictCursor # Hasil query otomatis berbentuk Dictionary {} biar gampang dibaca Flask
    )

# ==========================================
# 1. MANAGEMENT DATA PROFIL
# ==========================================
def get_profile():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM profile LIMIT 1")
            return cursor.fetchone()
    finally:
        connection.close()

# ==========================================
# 2. CRUD DATA SKILLS
# ==========================================
def get_skills():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM skills")
            return cursor.fetchall()
    finally:
        connection.close()

def add_skill(name, img_url):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO skills (name, img) VALUES (%s, %s)"
            cursor.execute(sql, (name, img_url))
        connection.commit()
        return True
    except Exception as e:
        print(f"Error adding skill: {e}")
        return False
    finally:
        connection.close()

def delete_skill(skill_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM skills WHERE id = %s"
            cursor.execute(sql, (skill_id,))
        connection.commit()
        return True
    except Exception as e:
        print(f"Error deleting skill: {e}")
        return False
    finally:
        connection.close()

# ==========================================
# 3. CRUD DATA PENGALAMAN (EXPERIENCES)
# ==========================================
def get_experiences():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM experiences ORDER BY id DESC")
            return cursor.fetchall()
    finally:
        connection.close()

def add_experience(year, title, place, desc):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO experiences (year, title, place, `desc`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (year, title, place, desc))
        connection.commit()
        return True
    except Exception as e:
        print(f"Error adding experience: {e}")
        return False
    finally:
        connection.close()

def delete_experience(exp_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM experiences WHERE id = %s"
            cursor.execute(sql, (exp_id,))
        connection.commit()
        return True
    except Exception as e:
        print(f"Error deleting experience: {e}")
        return False
    finally:
        connection.close()

# ==========================================
# 4. CRUD DATA PROYEK (PROJECTS)
# ==========================================
def get_projects():
    connection = get_db_connection()
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM projects"
            cursor.execute(sql)
            rows = cursor.fetchall()
                         
            projects = []
            for row in rows:
                projects.append({
                    'id': row.get('id'),
                    'title': row.get('title'),
                    'description': row.get('desc'), # Memetakan 'desc' ke 'description' untuk HTML
                    'cover': row.get('img'),         # Memetakan 'img' ke 'cover' untuk HTML
                    'tags': row.get('tags')
                })
            return projects
    except Exception as e:
        print(f"Error fetching projects: {e}")
        return []
    finally:
        connection.close()

def add_project(title, description, cover, tags):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO projects (title, `desc`, img, tags) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (title, description, cover, tags))
        connection.commit()
        return True
    except Exception as e:
        print(f"Error adding project: {e}")
        return False
    finally:
        connection.close()

def delete_project(project_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM projects WHERE id = %s"
            cursor.execute(sql, (project_id,))
        connection.commit()
        return True
    except Exception as e:
        print(f"Error deleting project: {e}")
        return False
    finally:
        connection.close()

# ==========================================
# 5. MANAJEMEN UTK FORM KONTAK & LOGIN
# ==========================================
def save_contact_message(name, email, message):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, email, message))
        connection.commit()
        return True
    except Exception as e:
        print(f"Error saving contact: {e}")
        return False
    finally:
        connection.close()

def verify_admin_login(username, password):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM admin_users WHERE username = %s AND password = %s"
            cursor.execute(sql, (username, password))
            return cursor.fetchone()
    finally:
        connection.close()

# Memperbarui data profil dari halaman admin (Kueri disesuaikan untuk TiDB Cloud tanpa klausa LIMIT)
def update_profile(nama, deskripsi, peran, sub_deskripsi):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
                UPDATE profile 
                SET nama = %s, deskripsi = %s, peran = %s, sub_deskripsi = %s
            """
            cursor.execute(sql, (nama, deskripsi, peran, sub_deskripsi))
        connection.commit()
        return True
    except Exception as e:
        print(f"Error updating profile: {e}")
        return False
    finally:
        connection.close()