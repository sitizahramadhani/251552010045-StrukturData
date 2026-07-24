def balik_string(teks):
    stack = []

    #Langkah 1: PUSH setiap karakter ke stack
    for char in teks:
        stack.append(char)

    #Langkah 2: POP karakter - keluar urutan terbaik (LIFO)
    hasil = ''
    while stack:

        hasil += stack.pop()

    return hasil

# === Contoh Penggunaan ===
print(balik_string('halo'))
print(balik_string('python'))
print(balik_string('rececar'))
