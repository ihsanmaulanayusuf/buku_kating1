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

Mahasiswa6 = st.Page(
    "Buku Kating/120_Gracia Yoan Eunika Nababan.py",
    title="120 - Gracia Yoan Eunika Nababan",
    icon=":material/person:",
)

Mahasiswa7 = st.Page(
    "Buku Kating/040_Aprilia Dewi Hutapea.py",
    title="040 - Aprilia Dewi Hutapea",
    icon=":material/person:",
)

Mahasiswa8 = st.Page(
    "Buku Kating/017_Nayla Shafira Roza.py",
    title="017 - Nayla Shafira Roza",
    icon=":material/person:",
)

Mahasiswa9 = st.Page(
    "Buku Kating/018_Nydia Manda Putri.py",
    title="018 - Nydia Manda Putri",
    icon=":material/person:",
)

Mahasiswa10 = st.Page(
    "Buku Kating/019_Anadia Carana.py",
    title="019 - Anadia Carana",
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
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa5, Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10, Mahasiswa11, Mahasiswa13],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()