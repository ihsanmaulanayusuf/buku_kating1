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
            "https://drive.google.com/uc?export=view&id=1HQ3eLyEdnan3O0d8vjn-CmvddPzzVOAV",# 5
            "https://drive.google.com/uc?export=view&id=157-PqUArCiusclvdIi6LbTzR3ONUhUFq",# 6
            "https://drive.google.com/uc?export=view&id=15A43GmlG9j4TXi9hqajZ18nJfCMSlIGY",# 7
            "https://drive.google.com/uc?export=view&id=159VkYNPiYdWkev85LGCmr2iDkAIdQllP",# 8
            "https://drive.google.com/uc?export=view&id=156Lb-l2AdrdyQv8nJdY9fpqwG-nITJHi",# 9
            "https://drive.google.com/uc?export=view&id=156y5bWZYw2J76E9mH9exYZJJz0MQk9hv",#10
            "https://drive.google.com/uc?export=view&id=15C73VM9UVl6ByrthN56L57k5NQDRFOlx",# 11
            "https://drive.google.com/uc?export=view&id=15Cv8mLfxLkglsdKQnO6stXTxT7rNEltV",# 12
            "https://drive.google.com/uc?export=view&id=1HQ_d0TJCofwMY0rDZHpwUNKJ29lCASIX",# 13
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
                "nama": "Claudhea Angeliani",
                "nim": "122450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "gemas dan random",  
                "pesan":"sehat selalu kakak gemass"# 5
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
                "pesan":"semangat menjalani perkuliahan Bang"# 6
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
                "pesan":"sukses terus kak"# 7
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
                "pesan":"semangat menjalani perkuliahan Bang"# 8
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
                "pesan":"semangat menjalani perkuliahan bang"# 9
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
                "pesan":"sukses terus kakak lucuu"# 10
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
                "pesan":"sehat selalu kakak gemass"# 11
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
                "pesan":"semangat terus kakak baikk"# 12
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
                "pesan":"semangat terus kakak baikk"# 13
            }
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
elif menu == "Departemen PSDA":
    def departemenpsda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13BpftEyugi_nRv8CIDEIsW1yQdpIp71u", #1
            "https://drive.google.com/uc?export=view&id=13BpmwuKnTQjMnD4ryi2uLsogzD1B-K4L", #2
            "https://drive.google.com/uc?export=view&id=12yUZvSEV9aUowxiQ9pN-2HQA7_5S5svZ", #3
            "https://drive.google.com/uc?export=view&id=136UJRINLiEB7RrXEMOrT4rzxhI4ibRbv", #4
            "https://drive.google.com/uc?export=view&id=135mjT7mM2uvxU0S5AUkxJ3qA8tB5pzlv", #5
            "https://drive.google.com/uc?export=view&id=12zOPuMl59yIcZIeqiCk46GRqu-Ensv3e", #6
            "https://drive.google.com/uc?export=view&id=12u2MFwJLQERa_onjNE426p6Z9KHqOR_q", #7
            "https://drive.google.com/uc?export=view&id=13-rqDTBmm4KOyZq4ecg-vAHZfIhTjqaS", #8
            "https://drive.google.com/uc?export=view&id=130b-gVC38gd_sl81U1nGK7jdAnn2bnfS", #9
            "https://drive.google.com/uc?export=view&id=12u5ntP021raozEk9bDZL1SwuF6ibvll_", #10
            "https://drive.google.com/uc?export=view&id=13-Xhcgkd23VSAccFUaWK1FZOWtXlao7b", #11
            "https://drive.google.com/uc?export=view&id=1370U9MU4g5ZeOQM0J7YsWHdqUtC8b-bE", #12
            "https://drive.google.com/uc?export=view&id=13BPlGIxGQoyXtolPHAGKG4qbAWsQ2uNd", #13
            "https://drive.google.com/uc?export=view&id=136eCdtwSL3NfGUMj8n0Bth7qxQj8O3Xk", #14
            "https://drive.google.com/uc?export=view&id=13ApcRlYZNxfwZmk0-2y6JTPDXZ7OMsTy", #15
            "https://drive.google.com/uc?export=view&id=135LuXCkCfiuzhaq4OLCB0NM5KZgYIDK2", #16
            "https://drive.google.com/uc?export=view&id=133oPZTYCLFkxGaW_xiTI4sANtMlHHr2i", #17
            "https://drive.google.com/uc?export=view&id=132tMDBhaqRMGJDbj5ihVFVTxaUn_5B8m", #18
            "https://drive.google.com/uc?export=view&id=132jT5V3scf-mcU4lpFBWMvhCQIydj-iS", #19
            "https://drive.google.com/uc?export=view&id=137HxddapiW0_cSOCrDlXuJfc7KMqHX3_", #20
            "https://drive.google.com/uc?export=view&id=136hwJD2xkkVClv4dHAwhf8QhJ_OG-TkY", #21
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
                "kesan": "(Sesuaikan dengan kalian)",
                "pesan": "(Sesuaikan dengan kalian)"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "(Sesuaikan dengan kalian)",
                "pesan": "(Sesuaikan dengan kalian)"
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal": "Riau",
                "alamat": "Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "(Sesuaikan dengan kalian)",
                "pesan": "(Sesuaikan dengan kalian)"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450033",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Sukarame",
                "hobbi": "Muter - Muter",
                "sosmed": "@afifahhnsrn",
                "kesan": "(Sesuaikan dengan kalian)",
                "pesan": "(Sesuaikan dengan kalian)"
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "(Sesuaikan dengan kalian)",
                "pesan": "(Sesuaikan dengan kalian)"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "Jl. Lapas",
                "hobbi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "(Sesuaikan dengan kalian)",
                "pesan": "(Sesuaikan dengan kalian)"
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo",
                "hobbi": "Main Game",
                "sosmed": "@kemasverii",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin Lomba Sihir",
                "sosmed": "@presiliamg",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobbi": "Nonton Jagad review",
                "sosmed": "@sahid_maulana",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Belajar",
                "sosmed": "@roselivnes__",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobbi": "Nongs",
                "sosmed": "@allyaislami_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Natar",
                "hobbi": "Nyari sinyal di gedung F",
                "sosmed": "@eksantyfebriana",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450051",
                "umur": "19",
                "asal": "Kayu Agung",
                "alamat": "Kedaton",
                "hobbi": "Nongki - nongki",
                "sosmed": "@dransyah_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Oktavia Nurwendah Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@oktavianrwnda",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Pangeran Senopati Raya 18",
                "hobbi": "Baca Kitab Suci",
                "sosmed": "@ferdy_kevin",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Bengong",
                "sosmed": "@farahanumafifahh",
                "kesan": "",
                "pesan": ""
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenpsda()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen MIKFES":
    def departemenmikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18hdAAefK2KsGzJGN6odfUSq5yfYMY5x7", #1
            "https://drive.google.com/uc?export=view&id=18dbSe8ThfxW3lLP9CCsEeREUrJ2iGAkx", #2
            "https://drive.google.com/uc?export=view&id=18ipTbf_DDUSaUd-TbDd4hi8phsh-BcSX", #3
            "https://drive.google.com/uc?export=view&id=18XUho29DrUdfkOLBkSQhXBPEXcPW02ec", #4
            "https://drive.google.com/uc?export=view&id=18bDO8Moyg9fyjofbajYru52t7IhxDlTS", #5
            "https://drive.google.com/uc?export=view&id=18dim6vnJ7OsPDynkX9GIgTME4wotaB-6", #6
            "https://drive.google.com/uc?export=view&id=18dVqqfDTu7lrzMZQyv6k7Lm489rvk4eG", #7
            "https://drive.google.com/uc?export=view&id=18i4FowhU0Sy3oA-f2Olyeecf3AU81Lm4", #8
            "https://drive.google.com/uc?export=view&id=18jgiR8wz-HHy6VhegAzzHfO1ltOsXGBG", #9
            "https://drive.google.com/uc?export=view&id=18XYc_AkAU7woyh9mFgx92Qr61PuBCxIt", #10
            "https://drive.google.com/uc?export=view&id=18i8dB_yuuo-xBbepuLkb_z7G9Vkq2oXg", #11
            "https://drive.google.com/uc?export=view&id=18_2SM5InLDP_vrmbqjU0bWugGhIzO4qv", #12
            "https://drive.google.com/uc?export=view&id=18etF4JagxrQNX7PpstseHVOmdBY61AiY", #13
            "https://drive.google.com/uc?export=view&id=18cIjC8VowFdcA0fONDGIbZs0rDCwegHH", #14
            "https://drive.google.com/uc?export=view&id=18_2SM5InLDP_vrmbqjU0bWugGhIzO4qv", #15
            "https://drive.google.com/uc?export=view&id=18gI8jrSZFJWeAJYbluyTs6AFXB1VuEm5", #16
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
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "",
                "sosmed": "@dindanababan_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Kelengkeng Raya",
                "hobbi": "Review jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Jl Nangka 3",
                "hobbi": "Berolahraga",
                "sosmed": "@randardn",
                "kesan": "",
                "pesan": ""
            }
        ]

        display_images_with_data(gambar_urls, data_list)
    departemenmikfes()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen Eksternal":
    def departemeneksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=171mQQpwb7IoOIR5o_TQ7tCB1BVrDE5bW", #1
            "https://drive.google.com/uc?export=view&id=170WZsJFSml2fV1fCWaihDL4ULNMbi9Aq", #2
            "https://drive.google.com/uc?export=view&id=16yfMV2F6tar9OL9C15d1JwW2IsrgpSU-", #3
            "https://drive.google.com/uc?export=view&id=16x5LaMCyRgS59vaBHYnWD9K-CfUJB4AS", #4
            "https://drive.google.com/uc?export=view&id=1724JRRZbPcXQyTWvcggr-RDnlMkhwQuV", #5
            "https://drive.google.com/uc?export=view&id=16xoOb4pR-Eym-VzwQQ4m2VO7QhlCgGD4", #6
            "https://drive.google.com/uc?export=view&id=16xjhTuM36dYNRbN_0_-McoMH-dYU_sIJ", #7
            "https://drive.google.com/uc?export=view&id=16wLHcz4Tbz5NPksr9uA009t0YBDNIEOw", #8
            "https://drive.google.com/uc?export=view&id=16zRhVbuU7HHg4S9Ls-qLR7_Ug7_fLX6q", #9
            "https://drive.google.com/uc?export=view&id=16w2N2czv2hmMS_ziH2UmoPaHRAjknxgp", #10
            "https://drive.google.com/uc?export=view&id=17--ma6mxF93yX3T5jnIxKusd7VIdj6vY", #11
            "https://drive.google.com/uc?export=view&id=172dMOOgCcWaMYWtUFqWkAU-FC0PVqqKU", #12
            "https://drive.google.com/uc?export=view&id=16z6YysQT3QKbZdiJRANUiFT6dWsmMc9B", #13
            "https://drive.google.com/uc?export=view&id=173ftfirDYW7VXUylMFQdciVFa7w7y0lT", #14
            "https://drive.google.com/uc?export=view&id=17560N2Gq68yOjokvq0pnhGeNXLzx02xZ", #15
            "https://drive.google.com/uc?export=view&id=16v-cMRRvnIF4KZtsUrVpXnwYrNotn3jZ", #16
            "https://drive.google.com/uc?export=view&id=16vxFGqr1cemW2II87Bwe5HEm6pL82_K1", #17
            "https://drive.google.com/uc?export=view&id=175ne3zzTkkhKm9nx6YXWYXirqJbdMIuz", #18
            "https://drive.google.com/uc?export=view&id=16tWn7qwW2HU0osxsenNjqE16vMgcasHl", #19
            "https://drive.google.com/uc?export=view&id=16rEQ_YdCUC-jlG1KH0O6ljIaXHHeAkKo", #20
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
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Nazwa Nabila",
                "nim": "121450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Kochpri",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Berkebun",
                "sosmed": "@deaa.rsn",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Surfing",
                "sosmed": "@nateee__15",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rizky Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Asa Do’a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Nemenin Tobias lari",
                "sosmed": "@rayths_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450127",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Way Dadi",
                "hobbi": "Olahraga",
                "sosmed": "@triayunanni",
                "kesan": "",
                "pesan": ""
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemeneksternal()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen Internal":
    def departemeninternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18IUGYN8XDj_PKjhQqZLqibK5QJfAAym2", #1
            "https://drive.google.com/uc?export=view&id=18VZ9-3hbux0V4b4j57QNv2L4msGfzVEV", #2
            "https://drive.google.com/uc?export=view&id=18Q41oCyPwUxpvwtR2o95ibckDX6D07AC", #3
            "https://drive.google.com/uc?export=view&id=18NwLy52otdSjr6RL_gbxNuqv2UO3xxCq", #4
            "https://drive.google.com/uc?export=view&id=18JHDOUofaz1PExraec8nlInXAXPwbdOr", #5
            "https://drive.google.com/uc?export=view&id=18OU0J4feGJUeYRcszqnAywdomNjXUt4r", #6
            "https://drive.google.com/uc?export=view&id=18VF810Sfhco5E9qbWq3lAJBtr-C9m28a", #7
            "https://drive.google.com/uc?export=view&id=18UMOSA-CcetN80Q4S6xDb82kSO0fBcEA", #8
            "https://drive.google.com/uc?export=view&id=18UFzb-S0K1ikKR3cJsq8F7HqbAUpiLPH", #9
            "https://drive.google.com/uc?export=view&id=18SMexfGUyfYH9PsWQ6DVI_IBpr6mZOVg", #10
            "https://drive.google.com/uc?export=view&id=18Sex_0--fg65Z4uXGUgY_3btgvDwl97X", #11
            "https://drive.google.com/uc?export=view&id=18TBDbisdE3UsgNxlpCTBhk9YU7oa3DG4", #12
            "https://drive.google.com/uc?export=view&id=18MGYNe15NMfU0oPUjqEye-bMolY3HnyY", #13
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
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Chatrine Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Pasaruntung",
                "hobbi": "Mengoleksi Dino",
                "sosmed": "@akbar_restika",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Renita Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Membaca dan Memancing",
                "sosmed": "@renita.shn",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Yosia Retare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi": "Nungguin ayam betina berkokok",
                "sosmed": "@yosiabanurea",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Ngejokes",
                "sosmed": "@josuapanggabean_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Azizah Kusuma Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@meirasty_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Berenang di Laut",
                "sosmed": "@rexander",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rani Puspita Ningrum",
                "nim": "122450022",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@rannipu",
                "kesan": "",
                "pesan": ""
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemeninternal()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen SSD":
    def departemenssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18WbGDT-i8p0aG119TgklWr-qTP5jBNRj", #1
            "https://drive.google.com/uc?export=view&id=16hJ1w-9SzPGI6jcRX7nXJ95lqhYnMVzn", #2
            "https://drive.google.com/uc?export=view&id=16dXaRl0csTDe3Z0IDXtjTOjKTX7bC7Cd", #3
            "https://drive.google.com/uc?export=view&id=16kqKF46BdO21zJyecQwfOvL0zmhMt7MW", #4
            "https://drive.google.com/uc?export=view&id=16k53TAgwZMRG6zmc4LiEADiU1lwH_sZ3", #5
            "https://drive.google.com/uc?export=view&id=16kz9jzGGCJ238H33-h-D_9xM9_AManGK", #6
            "https://drive.google.com/uc?export=view&id=16hZ5Scpq-buqEIdNytVQ83GjA8yqsvhE", #7
            "https://drive.google.com/uc?export=view&id=18W973aUG5X6dTNKvgbIpF1FTp4XMd5a-", #8
            "https://drive.google.com/uc?export=view&id=16j5ko3jbYtSdlZPVdyAQnQZOA6OQkA1l", #9
            "https://drive.google.com/uc?export=view&id=16jRZRMIiUTbW_wnpRyyYxsJ0vea9iGmw", #10
            "https://drive.google.com/uc?export=view&id=16gtgAjlS4mq5BbV-nvTiBCUafb22x06b", #11
        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumbangaol",
                "nim": "121450090",
                "umur": "21",
                "asal": "Panjibako",
                "alamat": "Jl. Bel",
                "hobbi": "Mencari Uang",
                "sosmed": "@andriangaol",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Adisty Syawaida Arianto",
                "nim": "121450136",
                "umur": "23",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Touring",
                "sosmed": "@dananghk_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Farel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukittingi",
                "alamat": "Airan 1",
                "hobbi": "Badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobbi": "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangkal",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Alvia Asrinda Br. Ginting",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobbi": "Nonton",
                "sosmed": "@Alifiagntg",
                "kesan": "",
                "pesan": ""
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenssd()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen MEDKRAF":
    def departemenmedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12JJW-fJm4yI7KmO3GvFZQ_7Tr9Pm8sHB", #1
            "https://drive.google.com/uc?export=view&id=12H49bczxog2EbLOoi1XETVs3uyEbewnm", #2
            "https://drive.google.com/uc?export=view&id=12I5ISPKSeCRufaqtCQY-DljrkuXssDvM", #3
            "https://drive.google.com/uc?export=view&id=12AxtsPIp-3SUaw2P_b8UsWFrhmG-Ly1f", #4
            "https://drive.google.com/uc?export=view&id=12J8pkMR0xlCtpvwy78YliERP7Jbhibxb", #5
            "https://drive.google.com/uc?export=view&id=12GlEr2UCpWYwRNi-XXsh7DNnMX__-R5W", #6
            "https://drive.google.com/uc?export=view&id=12DGhMPNdXdyvv1mOeDxeNO6l-aCmqX1j", #7
            "https://drive.google.com/uc?export=view&id=12If52dX9Gs4o677y-Gu04RrP0jto_VWR", #8
            "https://drive.google.com/uc?export=view&id=1265h-HwFutH6CYTZZW_sOTVGDRtBaz9U", #9
            "https://drive.google.com/uc?export=view&id=12GP7_192beNbzo72eO3IXQVfDVD1CMX_", #10
            "https://drive.google.com/uc?export=view&id=12IU7LU8qMkVmV3xPgZejiNoOp5trIkvG", #11
            "https://drive.google.com/uc?export=view&id=12Cy1pX1IAAHC5BhmFV1Rum1GsmsiTCyO", #12
            "https://drive.google.com/uc?export=view&id=12Bfn3FwhoPfSgPSmbO0YxxNuMx0Cgd3S", #13
            "https://drive.google.com/uc?export=view&id=1285Z3YCQUgdBPTgo_N28HKQP1IAavdGf", #14
            "https://drive.google.com/uc?export=view&id=128fHeAjsCpSDpmCtDHWMbYkx0z1dY7zT", #15
            "https://drive.google.com/uc?export=view&id=12DFQbstMEpTD1KIqDCZI7__8LkPatpsE", #16
            "https://drive.google.com/uc?export=view&id=12Ezv2515m1Ad0feKw2ddJqem2aLhGB5e", #17
            "https://drive.google.com/uc?export=view&id=127wFwJZ6woPYmnEHxU0ayRvb4H1qO2E5", #18
        ]
        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal": "Makassar",
                "alamat": "Sukarame",
                "hobbi": "Nonton",
                "sosmed": "@",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Nugas",
                "sosmed": "@arsyiah._",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Lagi Nyari",
                "sosmed": "@dino_kiper",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Muhammad Arsal Ranjana Putra",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 4",
                "hobbi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": "122450045",
                "umur": "20",
                "asal": "Natar, Lampung Selatan",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton Film",
                "sosmed": "@patriciadiajeng",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi": "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi": "Nonton Drakor",
                "sosmed": "@nsywanaf",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Baca Novel yang Bikin Nangis",
                "sosmed": "@prskslv",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa, Labuhan Dalam",
                "hobbi": "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "_akmal.faiz",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani)",
                "hobbi": "Bengong/Membaca Buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi": "Mengerjakan Tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "",
                "pesan": ""
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenmedkraf()
