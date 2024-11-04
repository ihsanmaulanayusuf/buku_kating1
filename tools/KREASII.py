import pandas as pd
data_magang = pd.read_csv('/content/Pendataan Peserta Magang CEO HMSD 2024 (Responses) - Form Responses 1.csv')
data_magang

# 1. Cleaning 'Provinsi' column
data_magang['1. Asal Provinsi'] = data_magang['1. Asal Provinsi'].str.strip()

# 2. Filtering data
data_lampung = data_magang[data_magang['1. Asal Provinsi'] == 'Lampung']
data_luar_lampung = data_magang[data_magang['1. Asal Provinsi'] != 'Lampung']

# 3. Displaying results
print("Jumlah peserta dari Lampung:", len(data_lampung))
print("Jumlah peserta dari luar Lampung:", len(data_luar_lampung))

import numpy as np
data_magang = [50, 62]
mean = np.mean(data_magang)
print("Rata-rata:", mean)

median = np.median(data_magang)
print("Median:", median)

range_value = np.max(data_magang) - np.min(data_magang)
print("Range:", range_value)

variance = np.var(data_magang)
print("Variansi:", variance)

std_dev = np.std(data_magang)
print("Standar Deviasi:", std_dev)

quartiles = np.percentile(data_magang, [50, 62])
print("Kuartil:", quartiles)

import pandas as pd
import matplotlib.pyplot as plt

# Misalkan ini adalah dataset Anda (silakan ganti dengan dataset asli)
data_magang = pd.DataFrame({
    '1. Asal Provinsi': ['Lampung'] * 50 + ['Luar Lampung'] * 62  # Contoh 50 dari Lampung dan 62 dari Luar Lampung
})

# 1. Membersihkan kolom 'Provinsi'
data_magang['1. Asal Provinsi'] = data_magang['1. Asal Provinsi'].str.strip()

# 2. Menghitung jumlah peserta dari masing-masing kategori
jumlah_peserta = data_magang['1. Asal Provinsi'].value_counts()

# Menampilkan hasil
print("Jumlah peserta dari Lampung:", jumlah_peserta.get('Lampung', 0))
print("Jumlah peserta dari luar Lampung:", jumlah_peserta.get('Luar Lampung', 0))

# 3. Membuat visualisasi dalam bentuk grafik batang
plt.figure(figsize=(8, 6))  # Ukuran gambar 8x6 inci
jumlah_peserta.plot(kind='bar', color=['pink', 'yellow'])
plt.xlabel('Kategori Asal')
plt.ylabel('Jumlah Peserta')
plt.title('Perbandingan Jumlah Peserta Magang dari Lampung dan Luar Lampung')
plt.xticks(rotation=0)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Misalkan ini adalah dataset Anda (silakan ganti dengan dataset asli)
data_magang = pd.DataFrame({
    '1. Asal Provinsi': ['Lampung'] * 50 + ['Luar Lampung'] * 62  # Contoh 50 dari Lampung dan 62 dari Luar Lampung
})

# 1. Membersihkan kolom 'Provinsi'
data_magang['1. Asal Provinsi'] = data_magang['1. Asal Provinsi'].str.strip()

# 2. Menghitung jumlah peserta dari masing-masing kategori
jumlah_peserta = data_magang['1. Asal Provinsi'].value_counts()

# Menampilkan hasil
print("Jumlah peserta dari Lampung:", jumlah_peserta.get('Lampung', 0))
print("Jumlah peserta dari luar Lampung:", jumlah_peserta.get('Luar Lampung', 0))

# 3. Membuat visualisasi dengan titik
plt.figure(figsize=(8, 6))  # Ukuran gambar 8x6 inci
plt.scatter(jumlah_peserta.index, jumlah_peserta.values, color=['pink', 'yellow'], s=100)  # s untuk ukuran titik

# Menambahkan label dan judul
plt.xlabel('Kategori Asal')
plt.ylabel('Jumlah Peserta')
plt.title('Perbandingan Jumlah Peserta Magang dari Lampung dan Luar Lampung')

# Menambahkan grid untuk memudahkan pembacaan
plt.grid(True)

# Menampilkan grafik
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Data magang
data_magang = [50, 62]

# Menghitung Mean
mean = np.mean(data_magang)
print("Rata-rata:", mean)

# Menghitung Median
median = np.median(data_magang)
print("Median:", median)

# Menghitung Range
range_value = np.max(data_magang) - np.min(data_magang)
print("Range:", range_value)

# Menghitung Variance
variance = np.var(data_magang)
print("Variansi:", variance)

# Menghitung Standar Deviasi
std_dev = np.std(data_magang)
print("Standar Deviasi:", std_dev)

# Menghitung Quartiles
quartiles = np.percentile(data_magang, [25, 50, 75])  # 25%, 50% (median), dan 75%
print("Kuartil:", quartiles)

# Membuat boxplot
plt.figure(figsize=(6, 8))
plt.boxplot(data_magang, vert=True, patch_artist=True, boxprops=dict(facecolor="lightblue"))

# Menambahkan garis mean dan median pada boxplot
plt.axhline(y=mean, color='red', linestyle='--', label=f'Mean: {mean}')
plt.axhline(y=median, color='green', linestyle='-', label=f'Median: {median}')

# Menambahkan label dan judul
plt.ylabel('Nilai')
plt.title('Boxplot Data Magang')

# Menambahkan legenda
plt.legend()

# Menampilkan boxplot
plt.show()

