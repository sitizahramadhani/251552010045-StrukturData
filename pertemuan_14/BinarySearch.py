def binary_search(arr, key):
    low = 0
    high = len(arr) -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid -1
        else:
            low = mid + 1
    return -1

data = [2, 4, 6, 10, 12, 14] 
print("Array saat ini:", data)
cari = int(input("Masukkan angka yang ingin dicari: "))
hasil = binary_search(data, cari)

if hasil != -1:
    print("Angka ditemukan di index:", hasil)
else:
    print("Angka tidak ditemukan dalam array.")