# Database pengguna
users = {
    "fadhli": "password123",
    "anya": "admin456",
    "abdu": "dev789"
}

#Daftar login yang ingin dicek 
login_attempts = [
    ("fadhli", "password123"),
    ("katanya", "salahpassword"),
    ("abdu", "dev789"),
    ("budi", "abc123")
]

# Cek semua login 
for username, password in login_attempts:
    if username in users and users[username] == password:
        print("Login {username}: BERHASIL")
else:
    print("Login {username}: GAGAL - Username atau password salah")