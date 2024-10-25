import streamlit as st
import random

st.title("Permainan Tebak Angka 🎲")
st.write("Selamat datang! Coba tebak angka rahasia yang disimpan oleh komputer antara 1 hingga 100!")

# Inisialisasi angka rahasia di sesi Streamlit
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)

if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

# Input tebakan user
guess = st.number_input("Masukkan tebakan kamu:", min_value=1, max_value=100, step=1)

# Tombol untuk submit tebakan
if st.button("Cek Tebakan"):
    st.session_state.attempts += 1
    if guess < st.session_state.secret_number:
        st.write("Terlalu rendah! Coba angka yang lebih besar.")
    elif guess > st.session_state.secret_number:
        st.write("Terlalu tinggi! Coba angka yang lebih kecil.")
    else:
        st.write(f"Selamat! Kamu berhasil menebak angka {st.session_state.secret_number} dalam {st.session_state.attempts} percobaan!")
        # Reset permainan
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.write("Angka baru telah di-generate. Ayo main lagi!")

# Tombol untuk mulai ulang permainan
if st.button("Mulai Ulang"):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.write("Permainan telah di-reset. Silakan tebak angka baru!")

