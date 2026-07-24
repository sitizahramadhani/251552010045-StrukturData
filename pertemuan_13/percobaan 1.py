import pandas as pd
import matplotlib.pyplot as plt

# Data penjualan selama 6 hari pertama (10 baris)
data = [
    {"Tanggal": "2025-07-01", "Warna": "Merah", "Ukuran": "M", "Jumlah": 2, "Harga": 25000},
    {"Tanggal": "2025-07-01", "Warna": "Putih", "Ukuran": "L", "Jumlah": 1, "Harga": 30000},
    {"Tanggal": "2025-07-02", "Warna": "Hitam", "Ukuran": "XL", "Jumlah": 3, "Harga": 35000},
    {"Tanggal": "2025-07-03", "Warna": "Merah", "Ukuran": "S", "Jumlah": 4, "Harga": 20000},
    {"Tanggal": "2025-07-04", "Warna": "Putih", "Ukuran": "M", "Jumlah": 2, "Harga": 25000},
    {"Tanggal": "2025-07-04", "Warna": "Hitam", "Ukuran": "L", "Jumlah": 1, "Harga": 30000},
    {"Tanggal": "2025-07-05", "Warna": "Merah", "Ukuran": "XL", "Jumlah": 1, "Harga": 35000},
    {"Tanggal": "2025-07-05", "Warna": "Putih", "Ukuran": "S", "Jumlah": 3, "Harga": 20000},
    {"Tanggal": "2025-07-06", "Warna": "Hitam", "Ukuran": "S", "Jumlah": 2, "Harga": 20000},
    {"Tanggal": "2025-07-06", "Warna": "Merah", "Ukuran": "L", "Jumlah": 3, "Harga": 30000},
]

df = pd.DataFrame(data)
df["Total"] = df["Jumlah"] * df["Harga"]

total_penjualan = df["Total"].sum()

warna_order = ["Merah", "Putih", "Hitam"]
warna_terjual = df.groupby("Warna")["Jumlah"].sum().reindex(warna_order)
total_kaos = warna_terjual.sum()

probabilitas = (warna_terjual / total_kaos) * 100

print("Total Penjualan Selama 6 Hari: Rp {:,.0f}".format(total_penjualan))
print("\nProbabilitas Warna Paling Sering Dibeli:")
for warna, prob in probabilitas.items():
    print(f" {warna}: {prob:.2f}%")

warna_grafik = ["red", "white", "black"]
plt.figure(figsize=(8, 5))
plt.bar(probabilitas.index, probabilitas.values, color=warna_grafik, edgecolor='gray')
plt.title("Probabilitas Pembelian Kaos Per warna (6 Hari)")
plt.ylabel("Presentase (%)")
plt.xlabel("warna")
plt.ylim(0, 50)
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig('grafik_probabilitas.png')

warna_data = list(zip(warna_terjual.index, warna_terjual.values))

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][1] < data[j + 1][1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

sorted_data = bubble_sort(warna_data)

print("\nHasil Pengurutan (Bubble Sort) Berdasarkan Jumlah Terbanyak:")
for warna, jumlah in sorted_data:
    print(f" {warna}: {jumlah} kaos")

plt.figure(figsize=(8, 5))
sorted_warna, sorted_jumlah = zip(*sorted_data)
warna_grafik_sorted = ["red" if w == "Merah" else "White" if w == "Putih" else "black" for w in sorted_warna]

plt.bar (sorted_warna, sorted_jumlah, color=warna_grafik_sorted, edgecolor="gray")
plt.title("Hasil Bubble Sort: Warna Kaos Paling Banyak Terjual")
plt.ylabel("Jumlah Kaos")
plt.xlabel("Warna")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("grafik-zahra.png")
plt.show()