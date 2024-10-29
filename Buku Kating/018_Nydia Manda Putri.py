
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
            "container": {"padding": "0!important", "background-color": "#black"},
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
                "asal": "Palembang",
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
                "asal": "Payakumbuh",
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
            "https://drive.google.com/uc?export=view&id=1_Hk4Atl-RyiIiqIKB-wht1f35lJR7dWZ",
            "https://drive.google.com/uc?export=view&id=1_Di_li9QcSKFF85iZ_lnQbifB2xjga_B",
            "https://drive.google.com/uc?export=view&id=1_Qwv83dGmFIo06EyAk9EiSc80M6jtORR",
            "https://drive.google.com/uc?export=view&id=1DPQ7WDdGPhr8luyv3CF3eJt39NYJ2Gv9",
            "https://drive.google.com/uc?export=view&id=1ZyEnzEqaiQ-V-7G3_lnOtHLOQcXVlm7W",
            "https://drive.google.com/uc?export=view&id=1DLiUE4D6ivWAhdY1IzrTmErr0LRBm65g",
            "https://drive.google.com/uc?export=view&id=1ppa97a5LevilJVp6LMD9ngaUXApY3zff",
            "https://drive.google.com/uc?export=view&id=1pep2AGFpJib65LohK19x6VJ90KOqiFb8",
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
                "asal": "Lampung Timurr",
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
                "pesan":"semangat terus kuliahnya kakak !!!"
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
                "pesan":"Semangat terus kuliahnya kak!"
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

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1GlCneruH_gGV8ojJ06uwDr56Ejd59DxC",
            "https://drive.google.com/uc?export=view&id=1Gi5gS9LdgHRh0OAFXGkyFGY40sjBKq0i",
        ]
        data_list = [
            {
                "nama": "Anissa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal": "Lampung Tengah",
                "alamat": "Kos Putri Rahayu",
                "hobbi": "Bernyanyi",
                "sosmed": "@annisalutfia_",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
           
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()
    
elif menu == "Departemen PSDA":
    def departemenpsda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EKGPM1bj7a7KW_hQMxmIGVNu096PdJu0",
            "https://drive.google.com/uc?export=view&id=1DEq3m3j_mreF9Ssp_1MRKNx_gNwCCjM7",
            "https://drive.google.com/uc?export=view&id=1DT8d6LybqmSytmJGM4cNdD-xsuJmRK23",
            "https://drive.google.com/uc?export=view&id=1E5-jUdeQIeFSlvmYRMSvdY3GPQAaEA4d",
            "https://drive.google.com/uc?export=view&id=1DQEZNGNzhDUa24Df4LGD8ij4ESaNHhje",
            "https://drive.google.com/uc?export=view&id=1FB6nWOGF0ZOyJOrSvbUa0TF4qGbU3HO6",
            "https://drive.google.com/uc?export=view&id=1EqNUar5oYAIa5GKoop5Tz932lAwh62ru",
            "https://drive.google.com/uc?export=view&id=1DQrzI-Fhpxv1SJcHCSNDwumK2s9vx4Zk",
            "https://drive.google.com/uc?export=view&id=1DWHG_-1F9graeG88TSqJWkrwMBUliLIO",
            "https://drive.google.com/uc?export=view&id=1EKnhicNU_DzJtuuNyKLrooRzY8OuO-xI",
            "https://drive.google.com/uc?export=view&id=1F2YIqJadC8v2dYl1O_P7-IkciVtoR8Y-",
            "https://drive.google.com/uc?export=view&id=1DZ8vCVYuJvNUioUe4M9Wchl4L2cwiP_k",
            "https://drive.google.com/uc?export=view&id=1DoPclreLnjiPMwEHEDxTB5oDA92aIoOH",
            "https://drive.google.com/uc?export=view&id=1EJeF_natjo-zIVqgy4hW9yUYiapcrxrw",
            "https://drive.google.com/uc?export=view&id=1EVq3n0PRYYxibOM_bHPjKWBXHIwyB_Ct",
            "https://drive.google.com/uc?export=view&id=1DwFaWQMc5mfuhH1arySwiA6YH2AB92KI",
            "https://drive.google.com/uc?export=view&id=1DyLqfcNRMe_FKJnEqMeLpJx49HTgfK1U",
            "https://drive.google.com/uc?export=view&id=1EboxN_dnK6EPoeKrHX5egzJzSBRoAVLm",
            "https://drive.google.com/uc?export=view&id=1Db3b0-cmQi-wD2uaD2UHEld89w7xw_8D",
            "https://drive.google.com/uc?export=view&id=1F3-BG5YZlLYYBYcM-USexli-EFJpLno_",
            "https://drive.google.com/uc?export=view&id=1EOEawIg4Jl7GzSmPGN0XOhDmrdUCc3ZD",
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Khobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabeth",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal": "Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Marahin Orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyaislami_",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiyati",
                "nim": "122450001",
                "umur": "20",
                "asal": "Jawa Barat",
                "alamat": "Metro",
                "hobbi": "Nyopet",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Bengong",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Jalan Pangeran Senopati Raya 18",
                "hobbi": "Baca Kitab Suci",
                "sosmed": "@ferdy_kevin",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Kayu Agung",
                "alamat": "Jalan Pagar Alam Kedaton",
                "hobbi": "Ngukur Jalan",
                "sosmed": "@dransyh_",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Travelling",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "1214500148",
                "umur": "21",
                "asal": "Duri, Riau",
                "alamat": "Pulau Damar Kobam",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Asprak",
                "sosmed": "@johanneskrsjnnn",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Golf Asri",
                "hobbi": "Ngetik Print Hello Dunia",
                "sosmed": "@kemasverii",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Presillia",
                "nim": "122450081",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin The Adams",
                "sosmed": "@presilliamg",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450122",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Kota Depok, Jabar",
                "alamat": "Jalan Airan Raya",
                "hobbi": "Dengerin juicy luicy",
                "sosmed": "@sahid_maul19",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Minum Kopi, Belajar, Bikin Deyvan Senang",
                "sosmed": "@roselivness__",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
           {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@syalaisha.i_",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenpsda()
        
elif menu == "Departemen MIKFES":
    def departemenmikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ZG842FNxvXawVwQLjjwGvA8VflI0XYtQ",
            "https://drive.google.com/uc?export=view&id=1YyJcPovQqlK0pTJVFGz1IBtdPbsh7lNF",
            "https://drive.google.com/uc?export=view&id=1Z5zgN5xL54UHBvrnkx-B0_1vOrbzFTaA",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1Z6RvKc-Q5vG-uJ8Bjjl-Ko9_r5zm14is",
            "https://drive.google.com/uc?export=view&id=1ZDzBFM3vYNB9-2nUgpE9FQuEKQ1xrZhX",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1ZAowlmHqiemTlVD7kuCiT-j7qUoxOrL5",
            "https://drive.google.com/uc?export=view&id=1ZAqYi59fucEPHrzWmxrlXwIf1A-7KxYH",
            "https://drive.google.com/uc?export=view&id=1YvgOr-NcxQLXvgA1RdOX2zmjip5zCqyo",
            "https://drive.google.com/uc?export=view&id=1Z-30xbp2wj9SVhhrjwAd9SNEfXmqB-B8",
            "https://drive.google.com/uc?export=view&id=1ZOSWJeMOSjX-NGfrItfyzm9ZPMsmlZ8Q",
            "https://drive.google.com/uc?export=view&id=1ZM3IRx6W-LIEImcc4LasAoSk7EMKhmiC",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1Yr_OC2EGRL2PMrcEeHa4zC0yLz042cSb",
            "https://drive.google.com/uc?export=view&id=1ZXMWvyIpCRJrqW-7UpgBftyggn2-8Wsn",
            "https://drive.google.com/uc?export=view&id=1ZBbVjpccNuA0ZeAQjaoVkJx_a9-VBZfe",
            "https://drive.google.com/uc?export=view&id=1Z09sf--OfOLYkjWqK50G1RcNXJPYi_tq",
            "https://drive.google.com/uc?export=view&id=1Z3AUwc5VpBI4BDZockB8brgXUG5NsRuu",
        ]
        data_list = [
            {
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21",
                "asal": "Lubuk Linggau",
                "alamat": "Jl. Nangka 4",
                "hobbi": "Olahraga",
                "sosmed": "@rafadhilillahh13",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona ",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame ",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "121450107",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kemiling",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": "@natanaeloks",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Membaca Jurnal dari Bu Mika",
                "sosmed": "@dindanababan_",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": "121450128",
                "umur": "23",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenmikfes()

elif menu == "Departemen Eksternal":
    def departemeneksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bdfTXEZ631GALQlQQNP6qtPENA0vxmrn", 
            "https://drive.google.com/uc?export=view&id=1byIXcxp2GV9YjYd4ln9f9kTq1x19Hhst", 
            "https://drive.google.com/uc?export=view&id=1dS3UcbXaTiKLCDmd4lTamJip6f6vwU7t", 
            "https://drive.google.com/uc?export=view&id=1bewhQ2qX6bI2GZ3pKRX9N6R_1CnWVxc4", 
            "https://drive.google.com/uc?export=view&id=1bslvvI9MGDF5feznwJEJ5uoDdnWUKwAp", 
            "https://drive.google.com/uc?export=view&id=1dNS6DHIyLoF9iA6VCF0lM_S4hfZtktTA", 
            "https://drive.google.com/uc?export=view&id=1cHXHi2UFshSp4HB6qIm6iWbh4IZ33zU_", 
            "https://drive.google.com/uc?export=view&id=1dOzX7C8oWn6sYnBZSMEX-Bk-fa7IiBYG", 
            "https://drive.google.com/uc?export=view&id=1d1JSYXMi17W-FpNbOPJUdiFPp95XsQyK", 
            "https://drive.google.com/uc?export=view&id=1bk9g3iY9HsGLl0DaCLjNqUcr-B3qK8IO", 
            "https://drive.google.com/uc?export=view&id=1cFijrVWSQm6MLmV2Sy_ty7S6_os4PxCN", 
            "https://drive.google.com/uc?export=view&id=1KM63MIs1eIt8khcebWT6M1XX-CiCX-W9", 
            "https://drive.google.com/uc?export=view&id=1c9XQwLIx35zrnr_9YjO3jgG5qVmalyS_", 
            "https://drive.google.com/uc?export=view&id=1KGTbuBI7Jg3FS2KlkDMY8J5JmF5cel4Q", 
            "https://drive.google.com/uc?export=view&id=1KH0VG9srGGqRf6kOIpq7O5B39PP9hIpZ", 
            "https://drive.google.com/uc?export=view&id=1c0gInacqJ0xce0slgvLxR1pySb2lqYxI", 
            "https://drive.google.com/uc?export=view&id=1dEiRR7Y3yfNUS6ndASrGbGEBZY42ne-N", 
            "https://drive.google.com/uc?export=view&id=1KDb8e_Q0xyMQOF2M8xE1hxMuifzuv5q4",     
            "https://drive.google.com/uc?export=view&id=1cBbxt3zMlOZ12zLq0EQS3nb2VVazbeCF",     
            "https://drive.google.com/uc?export=view&id=1bznZYxQbYhF7K0fONyRgrk39DgagTCSF",
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Jatimulyo",
                "hobbi": "BAB setiap jam 7 pagi",
                "sosmed": "@yogyst",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Nazwa Nabila",
                "nim": "21450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Korpri",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Berkebun",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Surfing",
                "sosmed": "@nateee__15",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Rizky Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Asa Do’a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton Youtube, Main Game",
                "sosmed": "@alfaritziirvan",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Nemenin Tobias lari",
                "sosmed": "@rayths_",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450127",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Way Dadi",
                "hobbi": "Olahraga",
                "sosmed": "@triayunanni",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemeneksternal()

elif menu == "Departemen Internal":
    def departemeninternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1aiiKoXNNYUuS39atUiZdlYJlfW_87fsR", 
            "https://drive.google.com/uc?export=view&id=1ah62ZqZdD23VvzSjEzGFYwBmtI6rHsDW", 
            "https://drive.google.com/uc?export=view&id=1avdDpRGjxQVjuIg-IsfEx2vUAzF93Kfs", 
            "https://drive.google.com/uc?export=view&id=1an4jFRqzD3b72Kb7KFRrVEOYs3cF604E", 
            "https://drive.google.com/uc?export=view&id=1atHmqqZ1sU0M_XdZmgbsIssNQe8DAhFU", 
            "https://drive.google.com/uc?export=view&id=1atUpRuQl1De6AvMDs-2sHmJYSfX8uBXK", 
            "https://drive.google.com/uc?export=view&id=1ahkwUg1yoc3LZ7yTtFw5Z5IOV_a5a8U1", 
            "https://drive.google.com/uc?export=view&id=1bKAeTkIgx7yf8c_tfPbDFqNCoYsaOysG", 
            "https://drive.google.com/uc?export=view&id=1bKAeTkIgx7yf8c_tfPbDFqNCoYsaOysG", 
            "https://drive.google.com/uc?export=view&id=1bGqSJ9aduolUPygf54FMn_x7Q-5FGcdb", 
            "https://drive.google.com/uc?export=view&id=1bLPpfDmLf0wW_x4NgjUlKKljHQu-MLTe", 
            "https://drive.google.com/uc?export=view&id=1aqOeDkRcvzO7CI4w_zZkeqoXd17byqAm", 
        ]
        data_list = [
            {
                "nama": "Dimas Rizky Ramadhani",
                "nim": "121450027",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Way Kandis (Kobam)",
                "hobbi": "Menunggu ayam jantan bertelur",
                "sosmed": "@dimzrky_",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Chatrine Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Pasaruntung",
                "hobbi": "Mengoleksi Dino",
                "sosmed": "@akbar_restika",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Renita Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Membaca dan Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Menulis lagu",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Yosia Retare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi": "Nungguin ayam betina berkokok",
                "sosmed": "@yosiabanurea",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Ngejokes",
                "sosmed": "@josuapanggabean_",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Azizah Kusuma Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@meirasty_",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Berenang di Laut",
                "sosmed": "@rexander",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            }
        ]

        display_images_with_data(gambar_urls, data_list)
    departemeninternal()
