user = {"name:" "Fadhli", "age: 27"}

#Menggunakan get agar aman dar iKeyError 
email = user.get("email", "Email belum tersedia")
print(email)

#Menambahkan key jika belum ada dengan setdefault
user.setdefault("email", "fadhli@example.com") 

#Update data
user.update({"age": 28, "role": "devOps"})

#Menghapus key 
age = user.pop("age")

#Menampilkan semua key dan values 
print(user.keys())
print(user.values())

#Menyalin dictionary
user_copy = user.copy()
print(user_copy)

print(user)
print(user_copy)

