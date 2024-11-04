import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Judul Aplikasi
st.title("Analisis Data Peserta Magang CEO HMSD 2024")

# Penjelasan Umum
st.write("""
Selamat datang di artikel analisis data peserta magang CEO HMSD 2024 oleh Kelompok 1 Jordan. 
Pada analisis ini, kita akan melihat dan menjelaskan data peserta magang yang berasal dari berbagai daerah dan melakukan analisis statistik 
deskriptif serta visualisasi data untuk memberikan gambaran mengenai peserta magang ini.
""")

# 1. Membaca Dataset
st.header("1. Membaca Dataset")
st.write("Dataset diambil dari file CSV yang berisi data peserta magang CEO HMSD 2024.")
# Link CSV dari GitHub
data_magang = pd.read_csv('https://raw.githubusercontent.com/ihsanmaulanayusuf/buku_kating1/refs/heads/main/Pendataan%20Peserta%20Magang%20CEO%20HMSD%202024%20(Responses)%20-%20Form%20Responses%201%20-%20Pendataan%20Peserta%20Magang%20CEO%20HMSD%202024%20(Responses)%20-%20Form%20Responses%201.csv.csv')
st.dataframe(data_magang)  # Menampilkan beberapa baris data untuk referensi

# 2. Membersihkan Data
st.header("2. Membersihkan Data")
st.write("Membersihkan kolom 'Provinsi' untuk memastikan data konsisten.")
data_magang['1. Asal Provinsi'] = data_magang['1. Asal Provinsi'].str.strip()  # Membersihkan data provinsi

# 3. Analisis Statistika Deskriptif
st.header("3. Analisis Statistika Deskriptif")
st.write("""
Pada bagian ini, kita akan melihat statistik deskriptif dari jumlah peserta magang berdasarkan asal provinsi.
Kami akan menghitung jumlah peserta dari Lampung dan luar Lampung, serta nilai statistik lainnya seperti mean, median, range, 
variansi, standar deviasi, dan kuartil.
""")

# Menghitung jumlah peserta dari Lampung dan luar Lampung
data_lampung = data_magang[data_magang['1. Asal Provinsi'] == 'Lampung']
data_luar_lampung = data_magang[data_magang['1. Asal Provinsi'] != 'Lampung']

jumlah_peserta = [len(data_lampung), len(data_luar_lampung)]
mean = np.mean(jumlah_peserta)
median = np.median(jumlah_peserta)
range_value = np.max(jumlah_peserta) - np.min(jumlah_peserta)
variance = np.var(jumlah_peserta)
std_dev = np.std(jumlah_peserta)
quartiles = np.percentile(jumlah_peserta, [25, 50, 75])

# Menampilkan hasil analisis statistik deskriptif
st.write("Jumlah peserta dari Lampung:", len(data_lampung))
st.write("Jumlah peserta dari luar Lampung:", len(data_luar_lampung))
st.write("Rata-rata jumlah peserta:", mean)
st.write("Median jumlah peserta:", median)
st.write("Range jumlah peserta:", range_value)
st.write("Variansi jumlah peserta:", variance)
st.write("Standar deviasi jumlah peserta:", std_dev)
st.write("Kuartil:", quartiles)

st.write("""
Dari data yang didapatkan, bisa dilihat bahwa peserta magang dari luar Lampung (63 orang) lebih banyak dibandingkan peserta dari Lampung (49 orang). Hal ini menunjukkan bahwa program ini menarik banyak peserta dari berbagai daerah di luar Lampung.
Rata-rata dan median yang sama di angka 56 menunjukkan bahwa distribusi jumlah peserta cenderung simetris, atau dengan kata lain, tidak ada kelompok yang dominan secara drastis.
""")

# 4. Visualisasi Data
st.header("4. Visualisasi Data")
st.write("""
Visualisasi data peserta magang ini dilakukan untuk memahami distribusi peserta berdasarkan asal provinsi.
Grafik batang menunjukkan perbandingan jumlah peserta dari Lampung dan luar Lampung, 
sementara boxplot menampilkan sebaran data untuk analisis distribusi.
""")

# Visualisasi dalam grafik batang
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x=['Lampung', 'Luar Lampung'], y=jumlah_peserta, palette='pastel', ax=ax)
ax.set_xlabel('Kategori Asal')
ax.set_ylabel('Jumlah Peserta')
ax.set_title('Perbandingan Jumlah Peserta Magang dari Lampung dan Luar Lampung')
st.pyplot(fig)

st.write("""
Pada grafik batang, kita bisa melihat dengan jelas bahwa batang untuk peserta dari luar Lampung lebih tinggi dibandingkan batang peserta dari Lampung, yang mengonfirmasi bahwa jumlah peserta dari luar Lampung memang lebih besar.
""")

# Visualisasi Boxplot
fig, ax = plt.subplots(figsize=(6, 8))
ax.boxplot(jumlah_peserta, vert=True, patch_artist=True, boxprops=dict(facecolor="lightblue"))
ax.axhline(y=mean, color='red', linestyle='--', label=f'Mean: {mean}')
ax.axhline(y=median, color='green', linestyle='-', label=f'Median: {median}')
ax.set_ylabel('Jumlah Peserta')
ax.set_title('Boxplot Jumlah Peserta Berdasarkan Asal')
ax.legend()
st.pyplot(fig)

st.write("""
Pada boxplot, distribusi data terlihat cukup merata dengan sedikit rentang antara peserta dari Lampung dan luar Lampung. Hal ini menunjukkan bahwa perbedaan jumlah peserta antara kedua kelompok tidak terlalu besar dan data cenderung simetris tanpa adanya outlier yang signifikan.
""")

st.write("""
Dari analisis ini, kita bisa menyimpulkan bahwa yang mengikuti program magang CEO HMSD 2024 dan yang masuk Prodi Sains Data menarik banyak minat dari luar Lampung dan memiliki persebaran jumlah peserta yang cukup merata di antara kedua kelompok Luar Lampung dan dari Lampung.
""")

st.write("""
Terima kasih telah membaca analisis data peserta magang CEO HMSD 2024 dari kelompok 1 Jordan ini ya!.""")
