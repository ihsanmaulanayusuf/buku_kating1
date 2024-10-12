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
            "https://drive.google.com/uc?export=view&id=151iYJpuIdkm-bU_5rX1Puw_12bub9AXf",# 1
            "https://drive.google.com/uc?export=view&id=151UwaScsvKhi30bJ2hLeh0oH4c8Kyjmj",# 2
            "https://drive.google.com/uc?export=view&id=1540ux8D6-fGiU0iDbpuyN9vdHN7QZL-I",# 3
            "https://drive.google.com/uc?export=view&id=151sC0kOm2X20V6lWxf9yLyBoH9v8Uxem",# 4
            "https://drive.google.com/uc?export=view&id=152sV2D_Oo4wdZdKG175Oo32yxGidokQt",# 5
            "https://drive.google.com/uc?export=view&id=152QQBffwirZqfZIIWzSg6ISc1-X3ZHPn",# 6
            
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar",
                "hobbi": "Dengerin musik",
                "sosmed": "@amsirahk",
                "kesan": "Abang ini mirip bang Pandra",  
                "pesan":"Semangat menjalani perkuliahan bang kahim !!!"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450077",
                "umur": "21",
                "asal":"Bukit Kemuning, Lampung Utara",
                "alamat": "Bawean 2",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Abang ini mirip bang Gumi",  
                "pesan":"semangat terus kuliahnya bang Sekjen"# 2
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimelinza",
                "kesan": "kakaknya imut banget",  
                "pesan":"semangat menjalani perkuliahan kakak sekre cantikk "# 3
            },
            {
                "nama": "Hartiti Fadhilah",
                "nim": "12145031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "kakak ini baik dan sedikit pendiam",  
                "pesan":"semangat menjalani perkuliahan BUNDAhara"# 4
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "kakaknya baik dan sedikit pendiam seperti kak Hartiti",  
                "pesan":"semangat terus kuliahnya kakak sekre 1"# 5
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin Bang Pandra gitaran kaya kak Putri",
                "sosmed": "@nadillaandr26",
                "kesan": "kakaknya keren dan tegas bangett",  
                "pesan":"semangat terus kuliahnya kakak bendahara 1!"# 6
            }, 
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15BLGseVaYlVEfi7beBYG6Y6d9ofR4T3u",# 1
            "https://drive.google.com/uc?export=view&id=158mbC7-s_hbg2-NUrhWyshll0bSVL8gw",# 2
            "https://drive.google.com/uc?export=view&id=158k_5TL_FMFYfe1D5M4wB5orr6LvScCz",# 3
            "https://drive.google.com/uc?export=view&id=15CfgkXCIRPy5iXV4yKSSwqILtLTyuTY2",# 4
            "https://drive.google.com/uc?export=view&id=157-PqUArCiusclvdIi6LbTzR3ONUhUFq",# 5
            "https://drive.google.com/uc?export=view&id=15A43GmlG9j4TXi9hqajZ18nJfCMSlIGY",# 6
            "https://drive.google.com/uc?export=view&id=159VkYNPiYdWkev85LGCmr2iDkAIdQllP",# 7
            "https://drive.google.com/uc?export=view&id=156Lb-l2AdrdyQv8nJdY9fpqwG-nITJHi",# 8
            "https://drive.google.com/uc?export=view&id=156y5bWZYw2J76E9mH9exYZJJz0MQk9hv",# 9
            "https://drive.google.com/uc?export=view&id=15C73VM9UVl6ByrthN56L57k5NQDRFOlx",# 10
            "https://drive.google.com/uc?export=view&id=15Cv8mLfxLkglsdKQnO6stXTxT7rNEltV",# 11
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Nanya ke GPT",
                "sosmed": "@trimurniaa_",
                "kesan": "Kakak ramah sekali",  
                "pesan":"semangat terus kuliahnya kakak cantikkk!!!"# 1
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Way Huwi",
                "hobbi": "Membaca, menonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak ini ramah dan baik hati",  
                "pesan":"semangat terus kuliahnya kakak baik hati !!!"# 2
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Belajar, nonton film, tidur",
                "sosmed": "@wlsbn0",
                "kesan": "baik banget",  
                "pesan":"sukses terus kakak cantikk"# 3
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Drachin",
                "sosmed": "@anisadini10",
                "kesan": "Kakak ini imut", 
                "pesan":"semangat terus kuliahnya imut !!!"# 4
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "seru",  
                "pesan":"semangat menjalani perkuliahan Bang"# 5
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Jualan pancing",
                "sosmed": "@fleurnsh",
                "kesan": "Manis",  
                "pesan":"sukses terus kak"# 6
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Melukis, olahraga",
                "sosmed": "@fhrul.pdf",
                "kesan": "baik",  
                "pesan":"semangat menjalani perkuliahan Bang"# 7
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang ini aktif menjawab pertanyaan",  
                "pesan":"semangat menjalani perkuliahan bang"# 8
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi": "Duduk di tepi pantai sambil galauin bintang ynag tinggal satu",
                "sosmed": "@berlyyanda",
                "kesan": "lucu dan seru",  
                "pesan":"sukses terus kakak lucuu"# 9
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Ogan Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari Sinyal di gedung F",
                "sosmed": "@_.dheamelia",
                "kesan": "gemas dan random",  
                "pesan":"sehat selalu kakak gemass"# 10
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bernung, Pesawaran",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton drakor",
                "sosmed": "@ansftynn_",
                "kesan": "kakak ini baik dan sedikit pendiam",  
                "pesan":"semangat terus kakak baikk"# 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=176h671cwnUjLgn9O2m1FQFXQ9oK7po8M",# 1
            "https://drive.google.com/uc?export=view&id=176cdKNA6b6ztCyMX2xLcvJ3Z6UqJqxXz",# 2
        ]
        data_list = [
            {
                "nama": "Anissa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal":"Lampung Tengah",
                "alamat": "Kos Putri Rahayu",
                "hobbi": "Bernyanyi",
                "sosmed": "@anissaluthfi_",
                "kesan": "Kakak ini cantik dan keren parahhh",  
                "pesan":"Semangat mengemban jabatannya kakak kerenn!!!"# 1
            },
            {
                "nama": "Ryan Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abang ini kece abiezz",  
                "pesan":"semangat terus kuliahnya bang !!!"# 2
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()
# Tambahkan menu lainnya sesuai kebutuhan
