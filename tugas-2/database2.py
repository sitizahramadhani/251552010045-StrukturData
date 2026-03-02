# Database pengguna 
users = {
    "fadhli": "password123",
    "anya": "admin456", 
    "abdu" : "dev789"
}

print("=== Login Manual ===")
input_username = input("Masukkan username:")
input_password = input("MAsukkan password:")

if input_username in users and users[input_username] == input_password:
    print("Login {input_username}: BERHASIL")
else:
    print("Login {input_username}: GAGAL - Username atau password salah")
    