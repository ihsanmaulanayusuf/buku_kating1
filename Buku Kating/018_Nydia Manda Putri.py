import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Baleg",
            "Senator",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
            "Departemen MEDKRAF",
        ],
        icons=[
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected

@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        st.error(
            f"Failed to fetch image from {url}, status code: {response.status_code}"
        )
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None
    
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # Menggunakan Streamlit untuk menampilkan gambar di tengah kolom
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Umur: {data_list[i]['umur']}")
            st.write(f"Asal: {data_list[i]['asal']}")
            st.write(f"Alamat: {data_list[i]['alamat']}")
            st.write(f"Hobbi: {data_list[i]['hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan: {data_list[i]['kesan']}")
            st.write(f"Pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XmU6aZqXxzS4aF3w-S__lDoyyWdIBrDH",
            "https://drive.google.com/uc?export=view&id=1Y4zMdGrTnJjXCPct5hXVM5_Z4ESq0bJX",
            "https://drive.google.com/uc?export=view&id=1XoiAEW7RicB3VABx2LH_bZdATZS5xkHC",
            "https://drive.google.com/uc?export=view&id=1Xms1vAF6QsdE4Q2GHRkST6WV8ga-ji1F",
            "https://drive.google.com/uc?export=view&id=1Y3JYtnq_pxvfahSDj5dHUFmARZItLe_U",
            "https://drive.google.com/uc?export=view&id=1Y1oQ5laCf5q2JyEOs7U49EdG9zZFTg37",
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar",
                "hobbi": "Dengerin musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal": "Bukit Kemuning",
                "alamat": "Pawen 2 Sukarame",
                "hobbi": "Main Gitar",
                "sosmed": "@pndrinsni21",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan":"Semangat terus kuliahnya kak!"# 1
            },
            {
               "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal": "Pagar Alam",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"# 1
            },
             {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Bang Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan":"Semangat terus kuliahnya kak!"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin Bang Pandra Gitaran",
                "sosmed": "@nadillaadr26",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"# 1
            }, 
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_XZ8lZH9gpp9wu4PTFPdC2qPJRFZYu1S",
            "https://drive.google.com/uc?export=view&id=1DLiUE4D6ivWAhdY1IzrTmErr0LRBm65g",
            "https://drive.google.com/uc?export=view&id=1_Di_li9QcSKFF85iZ_lnQbifB2xjga_B",
            "https://drive.google.com/uc?export=view&id=1_Qwv83dGmFIo06EyAk9EiSc80M6jtORR",
            "https://drive.google.com/uc?export=view&id=1DPQ7WDdGPhr8luyv3CF3eJt39NYJ2Gv9",
            "https://drive.google.com/uc?export=view&id=1ZyEnzEqaiQ-V-7G3_lnOtHLOQcXVlm7W",
            "https://drive.google.com/uc?export=view&id=1_Hk4Atl-RyiIiqIKB-wht1f35lJR7dWZ",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1_BQe9hTTF8l491BiRW4w3P7wMsyrovwn",
            "https://drive.google.com/uc?export=view&id=1ZwqgPkuC3flXEZbZYBgjiIMrKaSBrYGm",
            "https://drive.google.com/uc?export=view&id=1HUOvAdj0r3j1YB6IS16LqVocfntilfxf",
            "https://drive.google.com/uc?export=view&id=1_6mOZDW4Aa-3bKkWQBukpYPel8lR3uUo",
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Bertanya sama GPT",
                "sosmed": "@trimurniaa_",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
           
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450124",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "Way Hui",
                "hobbi": "Membaca",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
           
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton Film",
                "sosmed": "@wlsbn0",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
           
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
           
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal": "Bernung, Pesawaran",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
           
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
           
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Baca Al-quran",
                "sosmed": "@fleurnsh",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
           
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
           
           
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
           
           
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal": "Ogan Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari Sinyal di Gedung F",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
           
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450126",
                "umur": "22",
                "asal": "Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Melukis",
                "sosmed": "@fhrul.pdf",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
           
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal": "Sumatra Barat",
                "alamat": "Way Huwi",
                "hobbi": "Baca Buku, Ngoding, Ibadah",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },

            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Billabong, Gedong Air",
                "hobbi": "Suka Bengong",
                "sosmed": "@jeremia_s",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
