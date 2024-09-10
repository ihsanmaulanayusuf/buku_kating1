import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title=" Profil Kelompok",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/110_Ihsan Maulana Yusuf.py",
    title="110 - Ihsan Maulana Yusuf",
    icon=":material/person:",
)

Mahasiswa2 = st.Page(
    "Buku Kating/071_Khairunnisa Maharani.py",
    title="071 - Khairunnisa Maharani",
    icon=":material/person:",
)

Mahasiswa3 = st.Page(
    "Buku Kating/086_Sania Dwi Ayu Lestari.py",
    title="086 - Sania Dwi Ayu Lestari",
    icon=":material/person:",
)

Mahasiswa5 = st.Page(
    "Buku Kating/099_Khansa Anyaveda Liyantri.py",
    title="099 - Khansa Anyaveda Liyantri",
    icon=":material/person:",
)

Mahasiswa11 = st.Page(
    "Buku Kating/067_Qois Olifio.py",
    title="067 - Qois Olifio",
    icon=":material/person:",
)

Mahasiswa13 = st.Page(
    "Buku Kating/014_Romauli Oktavia Silaban.py",
    title="014 - Romauli Oktavia Silaban",
    icon=":material/person:",
)
#Perlu diperhatikan perubahannya
KREASI = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")

#Perlu diperhatikan perubahannya
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa5, Mahasiswa11, Mahasiswa13],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()