-- 1. Tabel Profil
CREATE TABLE IF NOT EXISTS profile (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    deskripsi TEXT NOT NULL,
    peran VARCHAR(100) NOT NULL,
    sub_deskripsi TEXT NOT NULL
);

-- 2. Tabel Skill
CREATE TABLE IF NOT EXISTS skills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    img VARCHAR(255) NOT NULL
);

-- 3. Tabel Pengalaman (Experience)
CREATE TABLE IF NOT EXISTS experiences (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year VARCHAR(50) NOT NULL,
    title VARCHAR(150) NOT NULL,
    place VARCHAR(150) NOT NULL,
    `desc` TEXT NOT NULL
);

-- 4. Tabel Proyek (Projects)
CREATE TABLE IF NOT EXISTS projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    `desc` TEXT NOT NULL,
    img VARCHAR(255) NOT NULL,
    tags VARCHAR(255) NOT NULL -- Disimpan dalam format teks pisahan koma (contoh: "SQL, Database, Logistics")
);

-- 5. Tabel Kontak (Untuk menampung pesan masuk dari form)
CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. Tabel Admin (Untuk keperluan autentikasi Login halaman admin)
CREATE TABLE IF NOT EXISTS admin_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL -- Menggunakan text biasa dulu sesuai default tugas "admin123"
);

-- ==========================================
-- ISI DATA AWAL (DUMMY SEEDER) AGAR WEB TIDAK KOSONG
-- ==========================================

INSERT INTO profile (nama, deskripsi, peran, sub_deskripsi) VALUES 
('Cinta Imanuela Alessandria Nussy', 'An Information Systems student interested in data analysis, Oracle SQL management, and the development of integrated enterprise system solutions.', 'Information Systems Student', 'I have a deep passion for technology implementations, exploring database architectures, and analyzing enterprise process workflows to bridge business goals with robust technical solutions.');

INSERT INTO admin_users (username, password) VALUES 
('admin', 'admin123'); -- Sesuai dengan spesifikasi login di dokumen tugas [cite: 44, 45]