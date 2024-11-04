# Import library yang diperlukan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Menampilkan Judul dan Deskripsi Aplikasi
st.title("Analisis Data Magang CEO HMSD 2024")
st.write("Analisis ini bertujuan untuk memahami persebaran peserta magang CEO HMSD 2024 berdasarkan data statistik deskriptif dan visualisasi yang mendukung.")

# 1. Membaca Dataset
# Baca file CSV yang diunggah
data_magang = pd.read_csv('https://raw.githubusercontent.com/ihsanmaulanayusuf/buku_kating1/refs/heads/main/Pendataan%20Peserta%20Magang%20CEO%20HMSD%202024%20(Responses)%20-%20Form%20Responses%201%20-%20Pendataan%20Peserta%20Magang%20CEO%20HMSD%202024%20(Responses)%20-%20Form%20Responses%201.csv.csv')

# Menampilkan Dataset
st.subheader("Dataset Peserta Magang")
st.write(data_magang)

# 2. Analisis Statistik Deskriptif
st.subheader("Analisis Statistik Deskriptif")

# Membersihkan kolom yang diperlukan
data_magang['1. Asal Provinsi'] = data_magang['1. Asal Provinsi'].str.strip()

# Menghitung jumlah peserta dari masing-masing provinsi
jumlah_peserta = data_magang['1. Asal Provinsi'].value_counts()

# Statistik deskriptif pada kolom usia jika ada
if 'Umur' in data_magang.columns:
    rata_umur = np.mean(data_magang['Umur'])
    median_umur = np.median(data_magang['Umur'])
    range_umur = np.max(data_magang['Umur']) - np.min(data_magang['Umur'])
    variance_umur = np.var(data_magang['Umur'])
    std_dev_umur = np.std(data_magang['Umur'])
    quartiles_umur = np.percentile(data_magang['Umur'], [25, 50, 75])

    # Menampilkan hasil analisis statistik
    st.write("Rata-rata Umur:", rata_umur)
    st.write("Median Umur:", median_umur)
    st.write("Range Umur:", range_umur)
    st.write("Variansi Umur:", variance_umur)
    st.write("Standar Deviasi Umur:", std_dev_umur)
    st.write("Kuartil Umur:", quartiles_umur)
else:
    st.write("Data usia peserta tidak tersedia.")

# 3. Visualisasi Data
st.subheader("Visualisasi Data")

# Grafik Bar untuk Jumlah Peserta Berdasarkan Provinsi
st.write("Grafik Bar Jumlah Peserta dari Setiap Provinsi")
st.bar_chart(jumlah_peserta)

# Grafik Boxplot untuk Distribusi Umur (jika data umur tersedia)
if 'Umur' in data_magang.columns:
    fig, ax = plt.subplots()
    ax.boxplot(data_magang['Umur'], vert=True, patch_artist=True, boxprops=dict(facecolor="lightblue"))
    ax.axhline(y=rata_umur, color='red', linestyle='--', label=f'Mean: {rata_umur}')
    ax.axhline(y=median_umur, color='green', linestyle='-', label=f'Median: {median_umur}')
    ax.set_ylabel('Umur')
    ax.set_title('Boxplot Distribusi Umur Peserta Magang')
    ax.legend()
    st.pyplot(fig)
else:
    st.write("Tidak ada data umur untuk membuat visualisasi boxplot.")

# 4. Kesimpulan Analisis
st.subheader("Kesimpulan")
st.write("""
Berdasarkan analisis data, terdapat perbedaan jumlah peserta magang dari masing-masing provinsi. Jika data usia tersedia, kita juga dapat melihat distribusi usia peserta dan memahami variansi serta penyebaran data umur mereka.
""")
