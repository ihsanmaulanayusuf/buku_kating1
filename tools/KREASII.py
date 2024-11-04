import streamlit as st

# Set up the title and header
st.title("Kreasi Jordan")
st.header("Selamat datang di halaman kreasi kami!")

# Penjelasan tentang konsep Jordan
st.subheader("Apa itu Konsep Jordan?")
st.write("""
Konsep Jordan adalah pendekatan yang digunakan dalam berbagai disiplin ilmu, termasuk matematika dan seni, yang berfokus pada struktur dan hubungan yang harmonis. 
Kami mengaplikasikan konsep ini dalam kreasi kami untuk menciptakan karya yang tidak hanya indah secara visual, tetapi juga memiliki makna yang dalam.
""")

# Menambahkan gambar atau karya seni
st.subheader("Karya Seni Kami")
st.image("path_to_your_image.jpg", caption="Karya seni yang terinspirasi oleh konsep Jordan")

# Menampilkan elemen interaktif
st.subheader("Interaksi dengan Pengunjung")
user_input = st.text_input("Apa pendapat Anda tentang konsep Jordan?")
if st.button("Kirim"):
    st.write(f"Terima kasih atas pendapat Anda: {user_input}")

# Menambahkan beberapa konten tambahan
st.subheader("Karya Lainnya")
karya_lain = ["Karya 1", "Karya 2", "Karya 3"]
for karya in karya_lain:
    st.write(karya)

# Footer
st.markdown("---")
st.write("Dibuat dengan ❤️ oleh Kelompok 1")
