import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("Visualisasi Data Peserta Magang CEO HMSD 2024")
st.write("Selamat datang!")

# Mengunggah file CSV
uploaded_file = st.file_uploader("Unggah file CSV", type=["csv"])

if uploaded_file is not None:
    # Membaca data dari file yang diunggah
    data_magang = pd.read_csv(uploaded_file)

    # 1. Cleaning 'Provinsi' column
    data_magang['1. Asal Provinsi'] = data_magang['1. Asal Provinsi'].str.strip()

    # 2. Filtering data
    data_lampung = data_magang[data_magang['1. Asal Provinsi'] == 'Lampung']
    data_luar_lampung = data_magang[data_magang['1. Asal Provinsi'] != 'Lampung']

    # 3. Displaying results
    st.write("Jumlah peserta dari Lampung:", len(data_lampung))
    st.write("Jumlah peserta dari luar Lampung:", len(data_luar_lampung))

    # Statistik dasar
    data_counts = [len(data_lampung), len(data_luar_lampung)]
    
    mean = np.mean(data_counts)
    median = np.median(data_counts)
    range_value = np.max(data_counts) - np.min(data_counts)
    variance = np.var(data_counts)
    std_dev = np.std(data_counts)
    quartiles = np.percentile(data_counts, [25, 50, 75])

    # Menampilkan statistik
    st.write("Rata-rata:", mean)
    st.write("Median:", median)
    st.write("Range:", range_value)
    st.write("Variansi:", variance)
    st.write("Standar Deviasi:", std_dev)
    st.write("Kuartil:", quartiles)

    # Visualisasi grafik batang
    st.subheader("Grafik Batang Jumlah Peserta")
    fig, ax = plt.subplots()
    jumlah_peserta = pd.Series(data_counts, index=['Lampung', 'Luar Lampung'])
    jumlah_peserta.plot(kind='bar', color=['pink', 'yellow'], ax=ax)
    ax.set_xlabel('Kategori Asal')
    ax.set_ylabel('Jumlah Peserta')
    ax.set_title('Perbandingan Jumlah Peserta Magang dari Lampung dan Luar Lampung')
    st.pyplot(fig)

    # Visualisasi scatter plot
    st.subheader("Scatter Plot Jumlah Peserta")
    fig, ax = plt.subplots()
    ax.scatter(jumlah_peserta.index, jumlah_peserta.values, color=['pink', 'yellow'], s=100)
    ax.set_xlabel('Kategori Asal')
    ax.set_ylabel('Jumlah Peserta')
    ax.set_title('Perbandingan Jumlah Peserta Magang dari Lampung dan Luar Lampung')
    ax.grid(True)
    st.pyplot(fig)

    # Visualisasi boxplot
    st.subheader("Boxplot Data Peserta")
    fig, ax = plt.subplots()
    ax.boxplot(data_counts, vert=True, patch_artist=True, boxprops=dict(facecolor="lightblue"))
    ax.axhline(y=mean, color='red', linestyle='--', label=f'Mean: {mean}')
    ax.axhline(y=median, color='green', linestyle='-', label=f'Median: {median}')
    ax.set_ylabel('Nilai')
    ax.set_title('Boxplot Data Magang')
    ax.legend()
    st.pyplot(fig)

else:
    st.write("Silakan unggah file CSV untuk melanjutkan.")
