# service_user.py
from cryptography.fernet import Fernet
import psycopg2

# Kunci enkripsi
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_data(data):
    return cipher.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data):
    return cipher.decrypt(encrypted_data.encode()).decode()

def create_user(username, password):
    encrypted_password = encrypt_data(password)
    # Simpan data user ke database dengan password terenkripsi
    # Kode untuk menyimpan data ke database PostgreSQL

def get_user(username):
    # Ambil data user dari database berdasarkan username
    # Kode untuk mengambil data dari database PostgreSQL
    # Dekripsi password sebelum dikembalikan
    return decrypted_user_data

def update_user(username, new_password):
    encrypted_password = encrypt_data(new_password)
    # Perbarui password user di database dengan password terenkripsi
    # Kode untuk memperbarui data di database PostgreSQL

def delete_user(username):
    # Hapus data user dari database berdasarkan username
    # Kode untuk menghapus data dari database PostgreSQL


# service_log.py
import psycopg2

def log_action(username, action):
    # Catat log ke database
    # Kode untuk mencatat log ke database PostgreSQL


# main.py (menggunakan Flask sebagai contoh framework)
from flask import Flask, request
import service_user
import service_log

app = Flask(__name__)

@app.route('/create_user', methods=['POST'])
def create_user():
    username = request.json['username']
    password = request.json['password']
    service_user.create_user(username, password)
    service_log.log_action(username, 'Create User')
    return 'User berhasil dibuat'

# Implementasi rute untuk operasi CRUD lainnya

if __name__ == '__main__':
    app.run(debug=True)
