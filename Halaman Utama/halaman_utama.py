import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO


# JANGAN DIUBAH
@st.cache_data
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = ImageOps.exif_transpose(img)
    return img


def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # menampilkan gambar di tengah
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"Sebagai: {data_list[i]['sebagai']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Fun Fact: {data_list[i]['fun_fact']}")
            st.write(f"Motto Hidup: {data_list[i]['motto_hidup']}")


# JANGAN DIUBAH

st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 5.5em;'>WEBSITE KATING</h1>
        <p style='font-size: 2em;'>CEO HMSD Adyatama ITERA 2024</p>
    </div>
    """,
    unsafe_allow_html=True,
)


url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"


def layout(url):
    col1, col2, col3 = st.columns([1, 2, 1])  # Menggunakan kolom dengan rasio 1:2:1
    with col1:
        st.write("")  # Menyisakan kolom kosong
    with col2:
        st.image(load_image(url), use_column_width="True", width=350)
    with col3:
        st.write("")  # Menyisakan kolom kosong


layout(url)
layout(url1)


def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#050505"},
            "icon": {"color": "white", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#2a1018",
            },
            "nav-link-selected": {"background-color": "#562c3a"},
        },
    )
    return selected


menu = streamlit_menu()

if menu == "Home":

    def home_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h1 class='centered-title'>Deskripsi Kelompok</h1>", unsafe_allow_html=True
        )
        st.markdown(
            """<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                    uis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
                    laborum.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                    uis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
                    laborum.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)

    home_page()

elif menu == "About Us":

    def about_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown("<h1 class='centered-title'>About Us</h1>", unsafe_allow_html=True)
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1PN7eJgfVsTXJTlpKewK_Wbpw8AZCJrdW",
            "https://drive.google.com/uc?export=view&id=1dG3saD1v1svC9qOBCURzLdQPm8lIIxpt",
            "https://drive.google.com/uc?export=view&id=18eqn8Q5fIikdFfwb4MKJcMxCNx_iOiUp",
            "https://drive.google.com/uc?export=view&id=18_Us-qRt-xWdIIhD_K4AzwBOkjESCoNa",
            "https://drive.google.com/uc?export=view&id=1RtnVwiRw0QeKthU_Z8Xz4gCVt7MPc-Gg",
            "https://drive.google.com/uc?export=view&id=1cahQXYq7jDVlEkLM2MgZPZFINcn9_BFe",
            "https://drive.google.com/uc?export=view&id=1d9UQTot_hzldBH2bWB8MiHGTpBFyjfgE",
            "https://drive.google.com/uc?export=view&id=1WZScsJ1fzfznd-fvmaVyOQyRZahgUrrX",
            "https://drive.google.com/uc?export=view&id=14EOtOghvGGvR98Ympg2tndzoHFo97iNU",
            "https://drive.google.com/uc?export=view&id=1ck4eAmxfk3SNRjrD2CGlSUAjPJj_Ajuw",
            "https://drive.google.com/uc?export=view&id=1jyPINzk7dkpsmA2zAfHtEu_rTl--QDQp",
            "https://drive.google.com/uc?export=view&id=1kMlvs0orwtOHIDbhW0FJnNszS8NcBdTb",
            "https://drive.google.com/uc?export=view&id=1d5NWYIrEVOBeauFCEMrlUkLkoFrK7aHO",
        ]
        data_list = [
            {
                "nama": "Ihsan Maulana Yusuf",
                "sebagai": "Pak Lurah",
                "nim": "123450110",
                "fun_fact": "Sebelum tidur goyang kaki",
                "motto_hidup": "Datang, kerjakan, lupakan",
            },
            {
                "nama": "Khairunnisa Maharani",
                "sebagai": "Bu Lurah",
                "nim": "123450071",
                "fun_fact": "Bisa sedikit bahasa cina",
                "motto_hidup": "Everyone hates what i love, everyone love what i hate",
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "sebagai": "Anggota",
                "nim": "123450086",
                "fun_fact": "Suka dingin tapi alergi dingin",
                "motto_hidup": "Live to learn, act to inspire",
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "sebagai": "Anggota",
                "nim": "123450060",
                "fun_fact": "Sering cek hp, padahal ga ada notif",
                "motto_hidup": "Kita tidak bisa mengarahkan angin, tetapi kita bisa mengatur layar kapal",
            },
            {
                "nama": "Khansa Anyaveda Liyantri",
                "sebagai": "Anggota",
                "nim": "123450099",
                "fun_fact": "Love cats",
                "motto_hidup": "Hidup tanpa menaruh ekspektasi pada orang lain",
            },
            {
                "nama": "Gracia Yoan Eunika Nababan",
                "sebagai": "Anggota",
                "nim": "123450120",
                "fun_fact": "Suka nyemilin es batu",
                "motto_hidup": "Isaiah 41:10",
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "sebagai": "Anggota",
                "nim": "123450040",
                "fun_fact": "Tidur gaya trenggeling",
                "motto_hidup": "Proverbs 19:21",
            },
            {
                "nama": "Nayla Shafira Roza",
                "sebagai": "Anggota",
                "nim": "123450017",
                "fun_fact": "Suka seblak",
                "motto_hidup": "The more you learn, the more you'll earn",
            },
            {
                "nama": "Nydia Manda Putri",
                "sebagai": "Anggota",
                "nim": "123450018",
                "fun_fact": "Suka makan pedas",
                "motto_hidup": "All I do is try, try, try",
            },
            {
                "nama": "Anadia Carana",
                "sebagai": "Anggota",
                "nim": "123450019",
                "fun_fact": "Ga suka makan jagung",
                "motto_hidup": "First u learn, then u remove the l",
            },
            {
                "nama": "Qois Olifio",
                "sebagai": "Anggota",
                "nim": "123450067",
                "fun_fact": "Bisa habisin air 3 liter sehari",
                "motto_hidup": "Berpikir positif, bertindak positif, dan menerima hasil positif",
            },
            {
                "nama": "Kevin Antoni Junior",
                "sebagai": "Anggota",
                "nim": "123450109",
                "fun_fact": "Saya aslinya 2 orang",
                "motto_hidup": "Listen to your mom",
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "sebagai": "Anggota",
                "nim": "123450014",
                "fun_fact": "Pengkoleksi rok",
                "motto_hidup": "Listen to music",
            },
            {
                "nama": "Nydia Manda Putri",
                "sebagai": "Anggota",
                "nim": "123450018",
                "fun_fact": "suka makan pedas",
                "motto_hidup": "all do is try, try, try",
            },
{
                "nama": "Nydia Manda Putri",
                "sebagai": "Anggota",
                "nim": "123450018",
                "fun_fact": "suka makan pedas",
                "motto_hidup": "all do is try, try, try",
            },
{
                "nama": "Nydia Manda Putri",
                "sebagai": "Anggota",
                "nim": "123450018",
                "fun_fact": "suka makan pedas",
                "motto_hidup": "all do is try, try, try",
            },
{
                "nama": "Nydia Manda Putri",
                "sebagai": "Anggota",
                "nim": "123450018",
                "fun_fact": "suka makan pedas",
                "motto_hidup": "all do is try, try, try",
            },



        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()
