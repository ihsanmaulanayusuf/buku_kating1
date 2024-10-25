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
            "https://drive.google.com/uc?export=view&id=1uo5kAfE594xZePhKdD74P_2XohO_9D7g",
            "https://drive.google.com/uc?export=view&id=1pk4ixKU5pRlPvMkg9PAdJd-kvKnfECor",
            "https://drive.google.com/uc?export=view&id=1gy4Q7Q0V11rDaCRFQMmV9E7jk8qN8bxj",
            "https://drive.google.com/uc?export=view&id=14G8zNfhKT0hC7hJfSXtL95q9iYLayokR",
            "https://drive.google.com/uc?export=view&id=1500EYvcckq8FJc2PooTEJ-OFFCs-v2zz",
            "https://drive.google.com/uc?export=view&id=1vAG_ihI0HJ_DnoJEBIa_966bTuCldOqY",
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
                "kesan": "Kakaknya keren magang di telkom dan asik diajak diskusi",  
                "pesan": "Sukses selalu kak!"# 1
            },
            {
                "nama"     : "Pandra Insani Putra Azwar",
                "nim"      : "121450137",
                "umur"     : "21",
                "asal"     : "Bukit Kemuning",
                "alamat"   : "Pawen 2 Sukarame",
                "hobbi"    : "Main gitar",
                "sosmed"   : "@pndrinsni21",
                "kesan"    : "Abangnya seru, santai tapi profesional",  
                "pesan"    : "Semoga lancar terus kedepannya kak!"# 2
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kotabaru",
                "hobbi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakaknya ramah",  
                "pesan":"semangat terus kak"# 3
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin  bang Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakaknya baik banget",  
                "pesan":"semoga sukses kak"# 4
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak ini lucu dan agak pendiam",
                "pesan":"jaga kesehatan kak!!!"# 5
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Kotabaru",
                "hobbi": "Dengerin bang Pandra Gitaran",
                "sosmed": "@nadillaadr26",
                "kesan": "Kakak seru banget kalo ngobrol",
                "pesan":"semangat menggapai cita-cita!!!"# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1gux73vMm-6AgK0Sa47VL6QUFfKIJd96e",
            "https://drive.google.com/uc?export=view&id=1Jj4Cc7PW9FXZbZyUvnEXn-Ia5XNshxbf",
            "https://drive.google.com/uc?export=view&id=1rVnhRYy-X8KD5RXAJ1SargEjOp06HsS-",
            "https://drive.google.com/uc?export=view&id=1-Ip-p2G6pDretXHluvm3S3VaYUvgB8Mm",
            "https://drive.google.com/uc?export=view&id=1VmSAGmiMtdY2vEhhetp1WGSYDA6fbCbe",
            "https://drive.google.com/uc?export=view&id=1dtTPgALOVMRmchxFMS6whh40oCQBC8Bc",
            "https://drive.google.com/uc?export=view&id=1Z87M68gLK-IJrsu_Es6BCy-LrDIKuMlE",
            "https://drive.google.com/uc?export=view&id=1AWuQTDTrycbS_1i0CAgd1yTqI4abWczZ",
            "https://drive.google.com/uc?export=view&id=1Q-LnpRhPLz6oCY1n5eHUHdYumYrU33KI",
            "https://drive.google.com/uc?export=view&id=12dXMfgax4MdR7EfNM_RfT6Wmu0u0vXqA",
            "https://drive.google.com/uc?export=view&id=1YLxMZM5I5OEJMQeHqScmVis2v4ap33_T",
            "https://drive.google.com/uc?export=view&id=18rC4QlmrUv01qpTD0lsEhxIDnWsUd5Up",
            "https://drive.google.com/uc?export=view&id=14Os4Bk7LEJY_-YHCupGRB1lOiiGF_14x",

        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Bertanya sama GPT",
                "sosmed": "@trimurniaa_",
                "kesan": "Kakak selalu ramah dan mudah diajak ngobrol, suasananya jadi nyaman.",  
                "pesan":"Semoga kakak terus sukses dalam kuliahnya dan selalu semangat menggapai impian!"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450124",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Way Hui",
                "hobbi": " Membaca",
                "sosmed": "@annisacahyanisurya",
                "kesan": "kakak ini bisa diajak cerita apa aja",  
                "pesan":"Semangat belajarnya kak"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton Film",
                "sosmed": "@wlsbn0",
                "kesan": "Kakaknya punya vibes positif yang bikin tenang",  
                "pesan":"Semangat untuk menebarkan hal positif kak!"# 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "Peka sama lingkungan, supportif banget.",  
                "pesan":"Terus kasih kita dukungan ya kak, semangat!"# 1
            },
             {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bernung, Pesawaran",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@ansftynn_",
                "kesan": "Kakaknya asik diajak bicara",  
                "pesan":"semangat menggapai cita-citanya kak !!!"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Belwis",
                "hobbi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Bawaannya tenang kalo liat kakakf",  
                "pesan":"Semoga kakak selalu diberi kesehatan!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Baca Al-qur'an",
                "sosmed": "@fleurnsh",
                "kesan": "Kakak ini bisa bangun suasana nyaman",  
                "pesan":"Semangat kuliahnya kak!"# 1
            },
         {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak orangnya tenang tapi tetap asik",  
                "pesan":"Sukses selalu kak"# 1
            },
         {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Kakaknya baik",  
                "pesan":"Jaga kesehatan biar tetap semangat ya kak!!"# 1
            },
         {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Ogan Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari Sinyal di Gedung F",
                "sosmed": "@_.dheamelia",
                "kesan": "Mudah dalam bergaul, kakaknya asik",  
                "pesan":"Tetep humble terus ya kak!"# 1
            },
           { 
                "nama": "Muhammad Fahrul Aditya",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@fhrul.pdf",
                "kesan": "Kakaknya punya vibes lucu tapi  tenang dan pinter",  
                "pesan":"Semoga kuliahnya lancar terus ya kak!"# 1
            },
           {
                "nama": "Berliana enda putri",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya bisa bikin seneng semua orang",  
                "pesan":"Semoga kakak selalu diberkahi kebahagiaan!"# 1
            },
           {
               "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Billabong, Gedong Air",
                "hobbi": "Suka Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "Kakak selalu buat orang lain ketawa",  
                "pesan":"Terus menghibur orang sekitar ya kak!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tyyuYpAwS1S5tkcHgEPIRwrP0NVN5cPi",
            "https://drive.google.com/uc?export=view&id=15UOg9j_79297AHxq3EKOyoNrP9oYfZng",
        ]
        data_list = [
            {
                "nama"    : "Anissa Luthfi Alifia",
                "nim"     : "121450093",
                "umur"    : "22",
                "asal"    : "Lampung Tengah",
                "alamat"  : "Kos Putri Rahayu",
                "hobbi"   : "Bernyanyi",
                "sosmed"  : "@anissaluthfi_",
                "kesan"   : "Pembawaan kakaknya tegas, keren banget",  
                "pesan"   : "Semangat dalam menjalankan tugasnya kak!"
            },
            {
                "nama"    : "Rian Bintang Wijaya",
                "nim"     : "122450094",
                "umur"    : "20",
                "asal"    : "Palembang",
                "alamat"  : "Kota Baru",
                "hobbi"   : "Tidur",
                "sosmed"  : "@bintangtwinkle",
                "kesan"   : "Abang ini aktif di organisasi dan kepanitiaan",  
                "pesan"   : "Semangat kuliahnya bang!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def departemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1oU_VbxLR6fUM7920Yd5SM1e5hG-VYiM4",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=16gh_Av-Hs0cJ96_yShBspgNkg1Rt_1FD",
            "https://drive.google.com/uc?export=view&id=1aW8-X29lu2un3Mxn1oYcgtYtNBtUtU7z",
            "https://drive.google.com/uc?export=view&id=18SK8-OI48FVI-cPyTIfhnZc5gwsRpnY-",
            "https://drive.google.com/uc?export=view&id=1wVA8muyBBYpyoAbzX-mZu3Pe4bK-uPkp",
            "https://drive.google.com/uc?export=view&id=1hQAVu34HfV1yX02yF8maO2oO4BZD3z6Y",
            "https://drive.google.com/uc?export=view&id=1uSxDXUtOtFbTBtKG5DeC0h4bCH77idVa",
            "https://drive.google.com/uc?export=view&id=1mC1V0MbtCd2vBAMTplUcJctsiA823D1j",
            "https://drive.google.com/uc?export=view&id=1F-CWJoSvbEwOmy92FRKs7MaKT06NRhAq",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=13RkHrdS6D7uqwqkMJkm_IFyJ7J89RZL6",
            "https://drive.google.com/uc?export=view&id=1aYN9z5gM3h4kUUgUIMuEOVWGQh3owG55",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=156jSV4SZUhkhjUmhZWOKqAF5fvvBVpz0",
            "https://drive.google.com/uc?export=view&id=1v4jB3AnI1j3d4oGAbQqBS28uH5XIKw9B",
            "https://drive.google.com/uc?export=view&id=1bv3c8h-WWIWDBmB3C_K4O18nyrkpLka9",
            "https://drive.google.com/uc?export=view&id=1bbbT48DIMnrSWK_ik8Tw7vZz10-DFiEN",
            "https://drive.google.com/uc?export=view&id=15Ce45_vykMbhPpmk9YneQi3aJ-H6-Pgx",
            "https://drive.google.com/uc?export=view&id=10enUWBdgMJGQAfdbTZGGgEB7hJd_2lEv",
            "https://drive.google.com/uc?export=view&id=1HyUMPIF4LUHxgVdEjgcBb-EHWUY3kHOX",
            "https://drive.google.com/uc?export=view&id=1HhtlbUq-yXwBjNwZn4N8--2OS70IsKFD",
            "https://drive.google.com/uc?export=view&id=13yLe0UcXu_ZtDJucWiXSMLUHmJ-rQOIT",
          
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
                "kesan"    : "Kakak ini public speakingnya bagus",  
                "pesan"    : "Semangat kuliahnya kakak!"
            },
            {
                "nama"     : "Elisabeth Claudia Simanjuntak",
                "nim"      : "122450123",
                "umur"     : "18",
                "asal"     : "Tangerang",
                "alamat"   : "Kemiling",
                "hobbi"    : "Bernafas",
                "sosmed"   : "@celisabeth",
                "kesan"    : "Kakak asik, dan ramah",  
                "pesan"    : "Semangat kuliahnya kak!"
            },
            {
                "nama"     : "Nisrina Nur Afifah",
                "nim"      : "122450052",
                "umur"     : "19",
                "asal"     : "Jawa Barat",
                "alamat"   : "Sukarame",
                "hobbi"    : "Marahin orang",
                "sosmed"   : "@afifahhnsrn",
                "kesan"    : "Kakak ini baik, asik, ramah",  
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
                "kesan"    : "Kakak ini asik, ramah, dan lucuu",  
                "pesan"    : "Semangat terus kuliahnya kakak!"
            },
            {
                "nama"     : "Eksanty Febriana Sugma Islamiyati",
                "nim"      : "122450001",
                "umur"     : "20",
                "asal"     : "Jawa Barat",
                "alamat"   : "Metro",
                "hobbi"    : "Nyopet",
                "sosmed"   : "@eksantyfebriana",
                "kesan"    : "Kakak ini pinter, asik, dan ramah",  
                "pesan"    : "Semangat kuliahnya kak!"
            },
            {
                "nama"     : "Farahanum Afifah Ardiansyah",
                "nim"      : "122450056",
                "umur"     : "20",
                "asal"     : "Padang",
                "alamat"   : "Sukarame",
                "hobbi"    : "Bengong",
                "sosmed"   : "@arahanumafifahh",
                "kesan"    : "Kakak ini asik, ramah, dan keren",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"

              },
            {
                "nama"     : "Ferdy Kevin Naibaho",
                "nim"      : "122450107",
                "umur"     : "19",
                "asal"     : "Medan",
                "alamat"   : "Jalan Pangeran Senopati Raya 18",
                "hobbi"    : "Baca kitab suci",
                "sosmed"   : "@ferdy_kevin",
                "kesan"    : "Abang ini baik, asik, dan lucuu",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "M. Deriansyah Okutra",
                "nim"      : "122450101",
                "umur"     : "19",
                "asal"     : "Kayu Agung",
                "alamat"   : "Jalan Pagar Alam Kedaton",
                "hobbi"    : "Ngukur jalan",
                "sosmed"   : "@dransyh_",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Oktavia Nurwenda Puspita",
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
                "asal"     : "Duri, Riau",
                "alamat"   : "Pulau Damar Kotebaru",
                "hobbi"    : "Belajar",
                "sosmed"   : "@depanloo",
                "kesan"    : "Abang ini lucu, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Ibnu Farhan Al-Ghifari",
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
                "nama"     : "Johannes Krisjon Silitonga",
                "nim"      : "122450043",
                "umur"     : "19",
                "asal"     : "Tangerang",
                "alamat"   : "Jalan Lapas",
                "hobbi"    : "Asprak",
                "sosmed"   : "@johanneskrsjnnn",
                "kesan"    : "Abang ini suka supporteran",  
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
                "kesan"    : "Abang ini pinta, sabar, dan keren",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Leonard Andreas Napitupulu",
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
                "nama"     : "Presilia",
                "nim"      : "122450081",
                "umur"     : "20",
                "asal"     : "Bekasi",
                "alamat"   : "Kota Baru",
                "hobbi"    : "Dengerin The Adams",
                "sosmed"   : "@presilliamg",
                "kesan"    : "Kakak ini asik, ramah, dan kalem",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Rafa Aqilla Jungjunan",
                "nim"      : "122450122",
                "umur"     : "20",
                "asal"     : "Pekanbaru",
                "alamat"   : "Belwis",
                "hobbi"    : "Baca Webtoon",
                "sosmed"   : "@rafaaqilla",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kak!"
            },
            {
                "nama"     : "Sahid Maulana",
                "nim"      : "122450109",
                "umur"     : "21",
                "asal"     : "Kota Depok, Jabar",
                "alamat"   : "Jalan Airan Raya",
                "hobbi"    : "Dengerin juicy luicy",
                "sosmed"   : "@sahid_maul19",
                "kesan"    : "Abang ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya bang Sahid!"
            },
            {
                "nama"     : "Vanessa Olivia Rose",
                "nim"      : "121450108",
                "umur"     : "20",
                "asal"     : "Jakarta",
                "alamat"   : "Perum Korpri",
                "hobbi"    : "Minum kopi, belajar, bikin deyvan senang",
                "sosmed"   : "@roselivness_",
                "kesan"    : "Kakak ini jago basket, keren",  
                "pesan"    : "Sukses selalu kak!"
            },
            {
                "nama"     : "M. Farhan Athaulloh",
                "nim"      : "121450117",
                "umur"     : "21",
                "asal"     : "Lampung",
                "alamat"   : "Kota Baru",
                "hobbi"    : "@menolong",
                "sosmed"   : "@mfarhan.ath",
                "kesan"    : "abang ini asik, ramah, dan baik bangett",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Gede Moana",
                "nim"      : "121450014",
                "umur"     : "21",
                "asal"     : "Bekasi",
                "alamat"   : "Korpri Raya",
                "hobbi"    : "Belajar, Game, Baca Komik",
                "sosmed"   : "@@gedemoenaa",
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
                "sosmed"   : "jaclinaclcv",
                "kesan"    : "Kakak ini bak dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Rafly Prabu Darmawan",
                "nim"      : "122450140",
                "umur"     : "20",
                "asal"     : "Bangka Belitung",
                "alamat"   : "Sukarame",
                "hobbi"    : "Main Game",
                "sosmed"   : "@@raflyy_pd",
                "kesan"    : "Abang ini baik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Syalaisha Andini Putriansyah",
                "nim"      : "1",
                "umur"     : "2",
                "asal"     : "Lampung",
                "alamat"   : "Kos",
                "hobbi"    : " ",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenPSDA()

elif menu == "Departemen MIKFES":
    def departemenMIKFES():
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
                "nama"     : "Wahyudiyanto",
                "nim"      : "121450040",
                "umur"     : "21",
                "asal"     : "Makassar, Sulsel",
                "alamat"   : "Sukarame",
                "hobbi"    : "Nonton",
                "sosmed"   : "@",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Elok Fiola",
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
                "nama"     : "Arsyiah Azahra",
                "nim"      : "121450035",
                "umur"     : "21",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Tanjung Senang",
                "hobbi"    : "Nugas",
                "sosmed"   : "@arsyiah._",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Cintya Bella",
                "nim"      : "122450066",
                "umur"     : "20",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Teluk",
                "hobbi"    : "Ngegym",
                "sosmed"   : "@cintyabella28",
                "kesan"    : "Kakak ini baik, tinggi, dan wangi",  
                "pesan"    : "Semangat selalu kuliahnya kak!"
            },
            {
                "nama"     : "Eka Fidiya Putri",
                "nim"      : "122450045",
                "umur"     : "20",
                "asal"     : "Natar",
                "alamat"   : "Natar",
                "hobbi"    : "Menyibukkan diri",
                "sosmed"   : "@ekafdyaptri",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Najla Juwairia",
                "nim"      : "122450037",
                "umur"     : "19",
                "asal"     : "Sumatera Utara",
                "alamat"   : "Airan",
                "hobbi"    : "Nulis, baca, fangirling",
                "sosmed"   : "@nanana.minjoo",
                "kesan"    : "Kak juju ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kak!"
            },
            {
                "nama"     : " Patricia Leondrea Diajeng",
                "nim"      : "122450050",
                "umur"     : "20",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Jatimulyo",
                "hobbi"    : "Nonton film",
                "sosmed"   : "@patriciadiajeng",
                "kesan"    : "Kakak ini perhatian dan ceria banget",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Rahma Neliyana",
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
                "nama"     : "Try Yani Rizki Nur Rohmah",
                "nim"      : "122450020",
                "umur"     : "20",
                "asal"     : "Lampung Barat",
                "alamat"   : "Korpri",
                "hobbi"    : "Bernyanyi dan menonton",
                "sosmed"   : "@tryyaniciaaa",
                "kesan"    : "Kakak ini lucu, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : " Muhammad Kaisar",
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
                "nama"     : "Dwi Ratna Anggraeni",
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
                "nama"     : "Gymnastiar Al Khoarizmy",
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
                "nama"     : "Nasywa Nur Afifah",
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
                "nama"     : "Priska Silvia Ferantiana",
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
                "nama"     : "Muhammad Arsal Ranjana",
                "nim"      : "121450111",
                "umur"     : "21",
                "asal"     : "Depok",
                "alamat"   : "Nangka 3",
                "hobbi"    : " ",
                "sosmed"   : "@@arsal.utama",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Abit Ahmad Oktarian",
                "nim"      : "122450042",
                "umur"     : "19",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Rajabasa, Labuhan Dalam",
                "hobbi"    : "Ngoding, gaming",
                "sosmed"   : "anitahmad",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Akmal Faiz Abdillah",
                "nim"      : "122450114",
                "umur"     : "20",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Perumahan Griya Sukarame",
                "hobbi"    : "Main HP ",
                "sosmed"   : "@_akmal.faiz",
                "kesan"    : "Abang ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Hermawan Manurung",
                "nim"      : "122450069",
                "umur"     : "20",
                "asal"     : "Bogor",
                "alamat"   : "Wisma Hana Hani",
                "hobbi"    : "Bengong/ Membaca buku",
                "sosmed"   : "@",
                "kesan"    : "Abang ini baik, lucu, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Khusnun Nisa",
                "nim"      : "122450078",
                "umur"     : "20",
                "asal"     : "Lampung Selatan",
                "alamat"   : "Belwis",
                "hobbi"    : "Mengerjakan Tugas",
                "sosmed"   : "@@khusnun_nisa335",
                "kesan"    : "Kakak ini lucu, ramah, dan public speakingnya bagus",  
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
