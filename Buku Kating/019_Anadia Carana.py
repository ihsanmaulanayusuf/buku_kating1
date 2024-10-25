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
            st.write(f"Nama        : {data_list[i]['nama']}")
            st.write(f"NIM         : {data_list[i]['nim']}")
            st.write(f"Umur        : {data_list[i]['umur']}")
            st.write(f"Asal        : {data_list[i]['asal']}")
            st.write(f"Alamat      : {data_list[i]['alamat']}")
            st.write(f"Hobbi       : {data_list[i]['hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan       : {data_list[i]['kesan']}")
            st.write(f"Pesan       : {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mNrex_khHrnihHo5ObIpi-T-SfqHuIzs",
            "https://drive.google.com/uc?export=view&id=1sfKcCmrMeFrH7Lcwt5ksKzS0Hm9FZkp7",
            "https://drive.google.com/uc?export=view&id=1hgdzNSs0b1cncc_7GZnFX1Qj8kmTA5vE",
            "https://drive.google.com/uc?export=view&id=1LgNq02tgdwNvaPdyPZxp1l8MAKVkqr28",
            "https://drive.google.com/uc?export=view&id=10cmHseL59luvqFjTcO3yw-DcGWDL0wgC",
            "https://drive.google.com/uc?export=view&id=1_w4moRgKLCiU_t-34F5kHxTldlIq83T0",
        ]
        data_list = [
            {
                "nama"     : "Kharisma Gumilang",
                "nim"      : "121450142",
                "umur"     : "21",
                "asal"     :"Palembang",
                "alamat"   : "Pulau Damar",
                "hobbi"    : "Dengerin musik",
                "sosmed"   : "@gumilangkharisma",
                "kesan"    : "Abangnya humble dan banyak pengalamannya yang membuat saya banyak belajar",  
                "pesan"    : "Terima kasih ilmunya dan semangat terus kuliahnya bang!"# 1
            },
            {
                "nama"     : "Pandra Insani Putra Azwar",
                "nim"      : "121450137",
                "umur"     : "21",
                "asal"     : "Bukit Kemuning",
                "alamat"   : "Pawen 2 Sukarame",
                "hobbi"    : "Main gitar",
                "sosmed"   : "@pndrinsni21",
                "kesan"    : "Abangnya seru dan saya dapat ilmu baru dari abangnya",  
                "pesan"    : "Terima kasih ilmunya dan semangat terus kuliahnya bang!"# 1
            },
            {
                "nama"     : "Meliza Wulandari",
                "nim"      : "121450065",
                "umur"     : "20",
                "asal"     : "Pagar Alam",
                "alamat"   : "Kotabaru",
                "hobbi"    : "Nonton Drakor",
                "sosmed"   : "@wulandarimeliza",
                "kesan"    : "Kakak ini baik, seru, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"# 1
            },
            {
                "nama"     : "Putri Maulida Chairani",
                "nim"      : "121450050",
                "umur"     : "21",
                "asal"     : "Payakumbuh",
                "alamat"   : "Nangka 4",
                "hobbi"    : "Dengerin  bang Pandra Gitaran",
                "sosmed"   : "@ptrimaulidaaa_",
                "kesan"    : "Kakak ini baik, sangat suportif, dan terbuka",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"# 1
            },
            {
                "nama"     : "Hartiti Fadilah",
                "nim"      : "121450031",
                "umur"     : "21",
                "asal"     : "Palembang",
                "alamat"   : "Pemda",
                "hobbi"    : "Nyanyi",
                "sosmed"   : "@hrtfdlh",
                "kesan"    : "Kakak ini baik, humble, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"# 1
            },
            {
                "nama"     : "Nadilla Andhara Putri",
                "nim"      : "121450003",
                "umur"     : "21",
                "asal"     : "Metro",
                "alamat"   : "Kotabaru",
                "hobbi"    : "Dengerin  bang Pandra Gitaran",
                "sosmed"   : "@nadillaadr26",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Nsu9ZZFaBrTftT2vYhSyW86oNMZw9B59",
            "https://drive.google.com/uc?export=view&id=1RG93yUlOqDb3WN0hw-x8MYSygYf1aqaA",
            "https://drive.google.com/uc?export=view&id=1vBgbMN4TwNW1v8Eh3tJ_8sZ5XHiwY0_S",
            "https://drive.google.com/uc?export=view&id=105H-xR1sK2XnzvBjOz1Bn5U2knJOgmiY",
            "https://drive.google.com/uc?export=view&id=1V8BrNSBTlQslNH8aEXGGAIBtbkZrsq5a",
            "https://drive.google.com/uc?export=view&id=1jmlpKulaa5reHn2JLr4nlOgQlTnPeq4a",
            "https://drive.google.com/uc?export=view&id=1edK109nRD7bJk9Ymm0pWiZGprsSBB-mf",
            "https://drive.google.com/uc?export=view&id=1jDaf0UW8L8IqaAjtqSi3nZD64CEK0l06",
            "https://drive.google.com/uc?export=view&id=1pMh-Bw0t13Mo_qaKmGvQsdVWNGSk_HsB",
            "https://drive.google.com/uc?export=view&id=1eWbRyxh43nliGzY9AInRf6yIBLMolE5W",
            "https://drive.google.com/uc?export=view&id=16oQfW4ePnVazmsqcpCd0purBFxlYyH5l",
            "https://drive.google.com/uc?export=view&id=1GJl32SfNIwoQpFYOchIdeyARbmIclE5L",
            "https://drive.google.com/uc?export=view&id=1ymnlzK2EhAU9lRGFApqS86I1dEsKE6EM",
        ]
        data_list = [
            {
                "nama"     : "Tri Murniya Ningsih",
                "nim"      : "121450038",
                "umur"     : "21",
                "asal"     : "Bogor",
                "alamat"   : "Raden Saleh",
                "hobbi"    : "Bertanya sama GPT",
                "sosmed"   : "@trimurniaa_",
                "kesan"    : "Kakak ini asik, baik, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Annisa Cahyani Surya",
                "nim"      : "121450124",
                "umur"     : "21",
                "asal"     : "Tangerang Selatan",
                "alamat"   : "Way Hui",
                "hobbi"    : "Membaca",
                "sosmed"   : "@annisacahyanisurya",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Wulan Sabina",
                "nim"      : "121450150",
                "umur"     : "21",
                "asal"     : "Medan",
                "alamat"   : "Raden Saleh",
                "hobbi"    : "Menonton Film",
                "sosmed"   : "@wlsbn0",
                "kesan"    : "Kakak ini baik, asik, serta banyak insight dan pengalaman menarik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Anisa Dini Amalia",
                "nim"      : "121450081",
                "umur"     : "20",
                "asal"     : "Tangerang",
                "alamat"   : "Jati Agung",
                "hobbi"    : "Nonton Dracin",
                "sosmed"   : "@anisadini10",
                "kesan"    : "Kakak ini baik, care, seru diajak ngobrol, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Anisa Fitriyani",
                "nim"      : "122450019",
                "umur"     : "19",
                "asal"     : "Bernung, Pesawaran",
                "alamat"   : "Bandar Lampung",
                "hobbi"    : "Nonton Drakor",
                "sosmed"   : "@ansftynn_",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Feryadi Yulius",
                "nim"      : "122450087",
                "umur"     : "20",
                "asal"     : "Padang",
                "alamat"   : "Belwis",
                "hobbi"    : "Sholat Dhuha",
                "sosmed"   : "@fer_yulius",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            }, 
            {
                "nama"     : "Renisha Putri Giani",
                "nim"      : "122450079",
                "umur"     : "21",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Teluk Betung",
                "hobbi"    : "Baca Al-qur’an",
                "sosmed"   : "@fleurnsh",
                "kesan"    : "Kakak ini ramah dan membuat wawancara terasa asik serta penuh ilmu",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Claudhea Angeliani",
                "nim"      : "121450124",
                "umur"     : "21",
                "asal"     : "Lampung Timur",
                "alamat"   : "Lampung Timur",
                "hobbi"    : "Baca Jurnal",
                "sosmed"   : "@dylebee",
                "kesan"    : "-",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Mirzan Yusuf Rabbani",
                "nim"      : "122450118",
                "umur"     : "20",
                "asal"     : "Jakarta",
                "alamat"   : "Korpri",
                "hobbi"    : "Main Kucing",
                "sosmed"   : "@myrrinn",
                "kesan"    : "-",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Dhea Amelia Putri",
                "nim"      : "122450004",
                "umur"     : "20",
                "asal"     : "Ogan Ilir",
                "alamat"   : "Natar",
                "hobbi"    : "Nyari Sinyal di Gedung F",
                "sosmed"   : "@_.dheamelia",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Muhammad Fahrul Aditya",
                "nim"      : "121450126",
                "umur"     : "22",
                "asal"     : "Surakarta",
                "alamat"   : "Sukarame",
                "hobbi"    : "Melukis",
                "sosmed"   : "@fhrul.pdf",
                "kesan"    : "Abang ini baik dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Berliana Enda Putri",
                "nim"      : "122450065",
                "umur"     : "20",
                "asal"     : "Sumatra Barat",
                "alamat"   : "Way Huwi",
                "hobbi"    : "Baca Buku, Ngoding, Ibadah",
                "sosmed"   : "@berlyyanda",
                "kesan"    : "Kakak ini baik, seru, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Jeremia Susanto",
                "nim"      : "122450022",
                "umur"     : "20",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Billabong, Gedong Air",
                "hobbi"    : "Suka Bengong",
                "sosmed"   : "@jeremia_s_",
                "kesan"    : "Abang ini baik, asik, dan humble",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1WHyeA41zi0ZoHQVileQKKaLEGY-1xBHL",
            "https://drive.google.com/uc?export=view&id=1YEq-iuqGiEFd58N-ALDINq4iB52B8p0F",
        ]
        data_list = [
            {
                "nama"     : "Anissa Luthfi Alifia",
                "nim"      : "121450093",
                "umur"     : "22",
                "asal"     : "Lampung Tengah",
                "alamat"   : "Kos Putri Rahayu",
                "hobbi"    : "Bernyanyi",
                "sosmed"   : "@annisalutfia_",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Rian Bintang Wijaya",
                "nim"      : "122450094",
                "umur"     : "20",
                "asal"     : "Palembang",
                "alamat"   : "Kota baru",
                "hobbi"    : "Tidur",
                "sosmed"   : "@bintangtwinkle",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def departemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mZk8AR87moMjJnO7R_shthrY2XqesBnw",
            "https://drive.google.com/uc?export=view&id=1ZCRPuYT8y2xlbLwWnm_geVy_QyhFYQrU",
            "https://drive.google.com/uc?export=view&id=1Sq18kDThGA6OFzSvkefYUVp2ffReFXfV",
            "https://drive.google.com/uc?export=view&id=1oFvBA92gpTnnNsi4U8rmsw1ZuLh6jKGG",
            "https://drive.google.com/uc?export=view&id=1S7U_xk_zae88YhaC-ToiMFbBl8z_BXZJ",
            "https://drive.google.com/uc?export=view&id=1eSjyhly9s0WGGsV6-WppyTJj6Wuh57a7",
            "https://drive.google.com/uc?export=view&id=1KvL0qwUhrn1Hx3DvsP3IfV3krX5GFdZV",
            "https://drive.google.com/uc?export=view&id=1F-LzppnygJOlkff6YWUAtxoIG6x812Wz",
            "https://drive.google.com/uc?export=view&id=18e4J0nyeYoXcR9gv6jsQArnvAu1eCwTp",
            "https://drive.google.com/uc?export=view&id=11TF5Yt9Hc3Pg6yFVqM6vl8jG-a8chH2r",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1xDBeUZYdB1gCXlzzPXu89AAflzN2Dbbp",
            "https://drive.google.com/uc?export=view&id=1V0OC7han4V0YaKxOaMO0rirzOQNfXL21",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1-AmWrAv-LC_aA_8RuNeD9qCsEAyIROnK",
            "https://drive.google.com/uc?export=view&id=1-OudVyuHuzWJOj7KQTeddIHfEmNjyiBH",
            "https://drive.google.com/uc?export=view&id=1nNMjPy7GFC3J-xdnKj1Q9GqXEQ2sl-Aa",
            "https://drive.google.com/uc?export=view&id=1VfMDzKgrEpn7IGJGi-I-DcY4-4w5elq9",
            "https://drive.google.com/uc?export=view&id=13cSwCdn-ItTlxVdj2DsYbXVduJrgiLnV",
            "https://drive.google.com/uc?export=view&id=1wT2iwhI5Ma69RWeh6ZsvQcdC29mwSzuv",
            "https://drive.google.com/uc?export=view&id=1c4pSo0wR2HCvCgcNu5OfI1ORZO2y-NDL",
            "https://drive.google.com/uc?export=view&id=1JskD46pQ-NG9t5zoHXbHGzBCPV_55eYB",
            "https://drive.google.com/uc?export=view&id=1oa7si9-lqdg44v-VDf1DzG-bxkIm4Kee",
        ]
        data_list = [
            {
                "nama"     : "Ericson Chandra Sihombing",
                "nim"      : "121450026",
                "umur"     : "21",
                "asal"     : "Bekasi",
                "alamat"   : "Khobam",
                "hobbi"    : "Travelling",
                "sosmed"   : "@ericsonchandra99",
                "kesan"    : "Abang ini tegas, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Elisabeth Claudia Simanjuntak",
                "nim"      : "122450123",
                "umur"     : "18",
                "asal"     : "Tangerang",
                "alamat"   : "Kemiling",
                "hobbi"    : "Bernafas",
                "sosmed"   : "@celisabeth",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Nisrina Nur Afifah",
                "nim"      : "122450052",
                "umur"     : "19",
                "asal"     : "Jawa Barat",
                "alamat"   : "Sukarame",
                "hobbi"    : "Marahin orang",
                "sosmed"   : "@afifahhnsrn",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Allya Nurul Islami Pasha",
                "nim"      : "122450033",
                "umur"     : "20",
                "asal"     : "Sumatera Barat",
                "alamat"   : "Gg. Perwira Belwis",
                "hobbi"    : "Main",
                "sosmed"   : "@allyaislami_",
                "kesan"    : "Kakak ini baik, asik, dan tegas",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Eksanty Febriana Sukma Islamiaty",
                "nim"      : "122450001",
                "umur"     : "20",
                "asal"     : "Jawa Barat",
                "alamat"   : "Metro",
                "hobbi"    : "Nyopet",
                "sosmed"   : "@eksantyfebriana",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Farahanum Afifah Ardiansyah",
                "nim"      : "122450056",
                "umur"     : "20",
                "asal"     : "Padang",
                "alamat"   : "Sukarame",
                "hobbi"    : "Bengong",
                "sosmed"   : "@farahanumafifahh",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Ferdy Kevin Naibaho",
                "nim"      : "122450107",
                "umur"     : "19",
                "asal"     : "Medan",
                "alamat"   : "Jalan Pangeran Senopati Raya 18",
                "hobbi"    : "Baca Kitab Suci",
                "sosmed"   : "@ferdy_kevin",
                "kesan"    : "Abang ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "M. Deriansyah Okutra",
                "nim"      : "122450101",
                "umur"     : "19",
                "asal"     : "Kayu Agung",
                "alamat"   : "Jalan Pagar Alam Kedaton",
                "hobbi"    : "Ngukur Jalan",
                "sosmed"   : "@dransyh_",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Oktavia Nurwenda Puspita Sari",
                "nim"      : "122450041",
                "umur"     : "20",
                "asal"     : "Lampung Timur",
                "alamat"   : "Way Huwi",
                "hobbi"    : "Travelling",
                "sosmed"   : "@_oktavianrwnda_",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Deyvan Loxefal",
                "nim"      : "1214500148",
                "umur"     : "21",
                "asal"     : "Duri, Riau ",
                "alamat"   : "Pulau Damar Kobam",
                "hobbi"    : "Belajar",
                "sosmed"   : "@deyvanloo",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Ibnu Farhan Al-Ghifari",
                "nim"      : " ",
                "umur"     : " ",
                "asal"     : " ",
                "alamat"   : " ",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Johannes Krisjon Silitonga",
                "nim"      : "122450043",
                "umur"     : "19",
                "asal"     : "Tangerang",
                "alamat"   : "Jalan Lapas",
                "hobbi"    : "Asprak",
                "sosmed"   : "@johanneskrsjnnn",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Kemas Veriandra Ramadhan",
                "nim"      : "122450016",
                "umur"     : "19",
                "asal"     : "Bekasi",
                "alamat"   : "Golf Asri",
                "hobbi"    : "Ngetik print hello dunia",
                "sosmed"   : "@kemasverii",
                "kesan"    : "Abang ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Leonard Andreas Napitupulu",
                "nim"      : " ",
                "umur"     : " ",
                "asal"     : " ",
                "alamat"   : " ",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Presilia",
                "nim"      : "122450081",
                "umur"     : "20",
                "asal"     : "Bekasi",
                "alamat"   : "Kota Baru",
                "hobbi"    : "Dengerin The Adams",
                "sosmed"   : "@presilliamg",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Rafa Aqilla Jungjunan",
                "nim"      : "122450122",
                "umur"     : "20",
                "asal"     : "Pekanbaru",
                "alamat"   : "Belwis",
                "hobbi"    : "Baca webtonn",
                "sosmed"   : "@rafaaqilla",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Sahid Maulana",
                "nim"      : "122450109",
                "umur"     : "21",
                "asal"     : "Kota Depok, Jabar",
                "alamat"   : "Jalan Airan Raya",
                "hobbi"    : "Dengerin juicy luicy",
                "sosmed"   : "@sahid_maul19",
                "kesan"    : "Abang ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Vanessa Olivia Rose",
                "nim"      : "121450108",
                "umur"     : "20",
                "asal"     : "Jakarta",
                "alamat"   : "Perum Korpri",
                "hobbi"    : "Minum kopi, belajar, bikin deyvan senang",
                "sosmed"   : "@roselivness__",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "M. Farhan Athaulloh",
                "nim"      : "121450117",
                "umur"     : "21",
                "asal"     : "Lampung",
                "alamat"   : "Kota Baru",
                "hobbi"    : "Menolong",
                "sosmed"   : "@mfarhan.ath",
                "kesan"    : "Abang ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Gede Moana",
                "nim"      : "121450014",
                "umur"     : "21",
                "asal"     : "Bekasi",
                "alamat"   : "Korpri Raya",
                "hobbi"    : "Belajar, Game, Baca Komik",
                "sosmed"   : "@gedemoenaa",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Jaclin Alcavella",
                "nim"      : "122450015",
                "umur"     : "19",
                "asal"     : "Sumatera Selatan",
                "alamat"   : "Korpri",
                "hobbi"    : "Berenang",
                "sosmed"   : "@jaclinaclcv",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Rafly Prabu Darmawan",
                "nim"      : "122450140",
                "umur"     : "20",
                "asal"     : "Bangka Belitung",
                "alamat"   : "Sukarame",
                "hobbi"    : "Main Game",
                "sosmed"   : "@raflyy_pd",
                "kesan"    : "Abang ini baik dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Syalaisha Andini Putriansyah",
                "nim"      : "122450111",
                "umur"     : "21",
                "asal"     : "Tangerang",
                "alamat"   : "Sukarame",
                "hobbi"    : "Membaca",
                "sosmed"   : "@syalaisha.i_",
                "kesan"    : "Kakak ini baik dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenPSDA()

elif menu == "Departemen MIKFES":
    def departemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1K3KuZNCNwDAJj1eiJX5HIbzwTZQEN5oB",
            "https://drive.google.com/uc?export=view&id=1Q6-jORSeK7FNRiFjhKq8m5xnQVt0eaOR",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=18lUZMFKCqZDsxTX7dXimkCciVZXz861v",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tG61x0sqWXf2yU69xoS-R27jkEGsfiDA",
            "https://drive.google.com/uc?export=view&id=1zRYsiAnvB5t0azZkDTgNwpC3n-YXJG3n",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1eNnc_EyUA5nVclGULWGjojt7aiPht8kI",
            "https://drive.google.com/uc?export=view&id=1Fwl57uRAzz2Ar86UYBV9vpexuVyaLqRu",
            "https://drive.google.com/uc?export=view&id=14Z_fipgAzus8YtKVm_UQ_w8TWy4FthuH",
            "https://drive.google.com/uc?export=view&id=1tOHgKp16ptWT4G7aefaTt2STo6WlX5z-",
            "https://drive.google.com/uc?export=view&id=1zADuM3nfEu3XhO2ERdOP5cGF00tj0Sb7",
            "https://drive.google.com/uc?export=view&id=1RwWH6Hoelmke-g-lybUQsgKD0BATWCIb",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1BQ4uGE-8wY-wuMurb20YYR7TGs7vjQ2l",
            "https://drive.google.com/uc?export=view&id=1J-Z6XqvSGjd0X6bZBNMa8egs3ZDKh2Xj",
            "https://drive.google.com/uc?export=view&id=1PgKtQ6NcWsx_TZC_keyMRxOKewicuYB2",
            "https://drive.google.com/uc?export=view&id=1wzs015fw4nPWe0ew5aDHPSvTQqoZm6EY",
            "https://drive.google.com/uc?export=view&id=1GEwiHh5EhHrHlG7btGr1XOiSWzkk11In",
        ]
        data_list = [
            {
                "nama"     : "Rafi Fadhlillah",
                "nim"      : "121450143",
                "umur"     : "21",
                "asal"     : "Lubuk Linggau, Sumatera Selatan",
                "alamat"   : "Jl. Nangka 4",
                "hobbi"    : "Olahraga",
                "sosmed"   : "@rafadhlillahh13",
                "kesan"    : "Abang ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Annisa Novantika",
                "nim"      : "121450005",
                "umur"     : "21",
                "asal"     : "Lampung Utara",
                "alamat"   : "Jl. Pulau Sebesi",
                "hobbi"    : "Memasak",
                "sosmed"   : "@anovavona",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Mujadid Choirus Surya",
                "nim"      : " ",
                "umur"     : " ",
                "asal"     : " ",
                "alamat"   : " ",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Ahmad Sahidin Akbar",
                "nim"      : "122450044",
                "umur"     : "20",
                "asal"     : "Tulang Bawang",
                "alamat"   : "Sukarame",
                "hobbi"    : "Olahraga",
                "sosmed"   : "@sahid22__",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Fadhil Fitra Wijaya",
                "nim"      : " ",
                "umur"     : " ",
                "asal"     : " ",
                "alamat"   : " ",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya abang!"
            },
            {
                "nama"     : "Muhammad Regi Abdi Putra Amanta",
                "nim"      : "122450031",
                "umur"     : "19",
                "asal"     : "Palembang",
                "alamat"   : "Jl. Permadi",
                "hobbi"    : "Ngasprak ADS",
                "sosmed"   : "@mregiiii_",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Syalaisha Andina Putriansyah",
                "nim"      : "122450121",
                "umur"     : "21",
                "asal"     : "Tangerang",
                "alamat"   : "Gg. Yudistira",
                "hobbi"    : "Review jurnal Bu Mika",
                "sosmed"   : "@dkselsd_31",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Natanael Oktavianus Partahan Sihombing",
                "nim"      : " ",
                "umur"     : " ",
                "asal"     : " ",
                "alamat"   : " ",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Anwar Muslim",
                "nim"      : "122450117",
                "umur"     : "21",
                "asal"     : "Bukittinggi",
                "alamat"   : "Korpri",
                "hobbi"    : "ML (Machine Learning)",
                "sosmed"   : "@here.am.ai",
                "kesan"    : "Abang ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Deva Anjani Khayyuninafsyah",
                "nim"      : "122450014",
                "umur"     : "21",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Kemiling",
                "hobbi"    : "Resume Webinar",
                "sosmed"   : "@anjaniiidev",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Dinda Nababan",
                "nim"      : "122450120",
                "umur"     : "20",
                "asal"     : "Medan",
                "alamat"   : "Jl. Lapas",
                "hobbi"    : "Membaca jurnal Bu Mika",
                "sosmed"   : "@dindanababan",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Marleta Cornelia Leander",
                "nim"      : "122450092",
                "umur"     : "20",
                "asal"     : "Depok",
                "alamat"   : "Gg. Nangka 3",
                "hobbi"    : "Review jurnal Bu Mika",
                "sosmed"   : "@marletacornelia",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Rut Junita Sari Siburian",
                "nim"      : "122450103",
                "umur"     : "20",
                "asal"     : "Kepulauan Riau",
                "alamat"   : "Gg. Nangka 3",
                "hobbi"    : "Menghitung akurasi",
                "sosmed"   : "@junitaa_0406",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Syadza Puspadari Azhar",
                "nim"      : "122450074",
                "umur"     : "20",
                "asal"     : "Palembang",
                "alamat"   : "Belwis",
                "hobbi"    : "Membangkitkan bilangan",
                "sosmed"   : "@puspadrr",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Abdurrahman Al-atsary",
                "nim"      : " ",
                "umur"     : " ",
                "asal"     : " ",
                "alamat"   : " ",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Aditya Rahman",
                "nim"      : "122450113",
                "umur"     : "20",
                "asal"     : "Metro",
                "alamat"   : "Korpri",
                "hobbi"    : "Ngoding wisata",
                "sosmed"   : "@rahm.adityaa",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Eggi satria",
                "nim"      : "122450032",
                "umur"     : "20",
                "asal"     : "Sukabumi",
                "alamat"   : "Korpri",
                "hobbi"    : "Ngoding wisata",
                "sosmed"   : "@_egistr",
                "kesan"    : "Abang ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Febiya Jomy Pratiwi",
                "nim"      : "122450074",
                "umur"     : "20",
                "asal"     : "Tulang Bawang",
                "alamat"   : "Jl. Kelengkeng Raya",
                "hobbi"    : "Review jurnal",
                "sosmed"   : "@pratiwifebiya",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Happy Syahrul Ramadhan",
                "nim"      : "122450013",
                "umur"     : "20",
                "asal"     : "Lampung Timur",
                "alamat"   : "Karang Anyar",
                "hobbi"    : "Main game",
                "sosmed"   : "@sudo.syahrulramadhan",
                "kesan"    : "Abang ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Randa Andriana Putra",
                "nim"      : "122450083",
                "umur"     : "21",
                "asal"     : "Banten",
                "alamat"   : "Sukarame ",
                "hobbi"    : "Tidur dan Berkembang",
                "sosmed"   : "@randaandriana_",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Vita Anggraini",
                "nim"      : " ",
                "umur"     : " ",
                "asal"     : " ",
                "alamat"   : " ",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenMIKFES()

elif menu == "Departemen Eksternal":
    def departemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenEksternal()

elif menu == "Departemen Internal":
    def departemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenInternal()

elif menu == "Departemen SSD":
    def departemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RogDzeGNfVQNCk4d2x2c1yLes2oXAteQ",
            "https://drive.google.com/uc?export=view&id=1nNr9nqVU9NJHuA3SCS5X1HYWMV8Z5VqC",
            "https://drive.google.com/uc?export=view&id=1rRlk5sMRpaS_QapQHICdyTA0ioxTo0Ld",
            "https://drive.google.com/uc?export=view&id=1ggarDPW_kKKTY9HFbxXhoqh2WJoPoi_R",
            "https://drive.google.com/uc?export=view&id=1zvIO0u2HPGOCpJaMneB2qtW7rMpQp9no",
            "https://drive.google.com/uc?export=view&id=1M7P7TEPjzCaUc0JClwElTi70uA-ML8pn",
            "https://drive.google.com/uc?export=view&id=1B6aOjB38XAs2613lLJ6IdHW3LGTGV8xR",
            "https://drive.google.com/uc?export=view&id=11F9XyUKbPNcZUUYXy7BQbS_WzVf7qdVu",
            "https://drive.google.com/uc?export=view&id=1mQfLsCW5Bf_V5VdOJ3pXedTsDhhgKq5a",
            "https://drive.google.com/uc?export=view&id=1jNuYdZONQChIbEU6BqI3EyysKuAz2-D_",
            "https://drive.google.com/uc?export=view&id=1lBIlSd3UJj7d_cw9Xi27AQdQFV8OvAkJ",
        ]
        data_list = [
            {
                "nama"     : "Andrian Agustinus Lumban Gaol",
                "nim"      : "121450090",
                "umur"     : "21",
                "asal"     : "Panjibako",
                "alamat"   : "Jl. Bel",
                "hobbi"    : "Mencari Uang",
                "sosmed"   : "@andriangaol",
                "kesan"    : "Abang ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Adisty Syawaida Ariyanto",
                "nim"      : "121450136",
                "umur"     : "22",
                "asal"     : "Metro",
                "alamat"   : "Sukarame",
                "hobbi"    : "Nonton film",
                "sosmed"   : "@adistysa_",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Nabila Azhari",
                "nim"      : "121450029",
                "umur"     : "21",
                "asal"     : "Simalungun, Sumut",
                "alamat"   : "Airan",
                "hobbi"    : "Hitung uang",
                "sosmed"   : "@zhjung_",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Ahmad Rizqi",
                "nim"      : "122450138",
                "umur"     : "20",
                "asal"     : "Bukittinggi",
                "alamat"   : "Airan 1",
                "hobbi"    : "Badminton",
                "sosmed"   : "@ahmad.ris45",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Danang Hilal Kurniawan",
                "nim"      : "122450085",
                "umur"     : "21",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Airan",
                "hobbi"    : "Nyuruh-nyuruh",
                "sosmed"   : "@dananghk_",
                "kesan"    : "Abang ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Farrel Julio Akbar",
                "nim"      : "122450110",
                "umur"     : "20",
                "asal"     : "Bogor",
                "alamat"   : "Lapas",
                "hobbi"    : "Apa aja",
                "sosmed"   : "@farrel_julio",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Tessa Kania Sagala",
                "nim"      : "122450040",
                "umur"     : "20",
                "asal"     : "Simalungun, Sumut",
                "alamat"   : "Pemda",
                "hobbi"    : "Suka nulis",
                "sosmed"   : "@tesakanias",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Nabilah Andika Fitriati",
                "nim"      : "121450139",
                "umur"     : "20",
                "asal"     : "Kedaton",
                "alamat"   : "Kedaton",
                "hobbi"    : "Tidur",
                "sosmed"   : "@nabilahanftr",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Alvia Asrinda Br.Gintng",
                "nim"      : "122450077",
                "umur"     : "20",
                "asal"     : "Binjai",
                "alamat"   : "Korpri",
                "hobbi"    : "Nonton windah",
                "sosmed"   : "@alviagnting",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Dhafin Razaqa Luthfi",
                "nim"      : "122450133",
                "umur"     : "20",
                "asal"     : "Balam",
                "alamat"   : "Jalan Nangka 1",
                "hobbi"    : "Tidur",
                "sosmed"   : "@dhafinrzqa",
                "kesan"    : "Abang ini ramah dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Elia Meylani Simanjuntak",
                "nim"      : "122450026",
                "umur"     : "20",
                "asal"     : "Bekasi",
                "alamat"   : "Korpri",
                "hobbi"    : "Badminton",
                "sosmed"   : "@meylanielia",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenSSD()

elif menu == "Departemen MEDKRAF":
    def departemenMEDKRAF():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "A",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "B",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenMEDKRAF()
# Tambahkan menu lainnya sesuai kebutuhan
