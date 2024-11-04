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
            "https://drive.google.com/uc?export=view&id=1uo5kAfE594xZePhKdD74P_2XohO_9D7g",
            "https://drive.google.com/uc?export=view&id=1pk4ixKU5pRlPvMkg9PAdJd-kvKnfECor",
            "https://drive.google.com/uc?export=view&id=1gy4Q7Q0V11rDaCRFQMmV9E7jk8qN8bxj",
            "https://drive.google.com/uc?export=view&id=1500EYvcckq8FJc2PooTEJ-OFFCs-v2zz",
            "https://drive.google.com/uc?export=view&id=14G8zNfhKT0hC7hJfSXtL95q9iYLayokR",
            "https://drive.google.com/uc?export=view&id=1vAG_ihI0HJ_DnoJEBIa_966bTuCldOqY", 
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
                "asal": "Pagar Alam",
                "alamat": "Kotabaru",
                "hobbi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakaknya ramah",  
                "pesan":"semangat terus kak"# 3
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakaknya baik banget",  
                "pesan": "semoga sukses kak"# 4
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal": "Payakumbuh, Sumatra Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak ini lucu",
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
            "https://drive.google.com/uc?export=view&id=1gux73vMm-6AgK0Sa47VL6QUFfKIJd96e", #1
            "https://drive.google.com/uc?export=view&id=1Jj4Cc7PW9FXZbZyUvnEXn-Ia5XNshxbf", #2
            "https://drive.google.com/uc?export=view&id=1rVnhRYy-X8KD5RXAJ1SargEjOp06HsS-", #3
            "https://drive.google.com/uc?export=view&id=1-Ip-p2G6pDretXHluvm3S3VaYUvgB8Mm", #4
            "https://drive.google.com/uc?export=view&id=1vyF51h5f1tsyMFUJHFg521GrS4b1rxsf", #5 
            "https://drive.google.com/uc?export=view&id=1YLxMZM5I5OEJMQeHqScmVis2v4ap33_T", #6 
            "https://drive.google.com/uc?export=view&id=1KSNB68psloidEVMXV33-wvJI2TOd86W8", #7
            "https://drive.google.com/uc?export=view&id=1ju57v-IuAcDOy-jiGDyygBov9ZMPNVHT", #8
            "https://drive.google.com/uc?export=view&id=1KBEwm601FMY3r5mNdCbX6dH8xR5YZ5DK", #9
            "https://drive.google.com/uc?export=view&id=10bHB4wpBcVD1R7lAEz5ODSHyN7jwlJzw", #10
            "https://drive.google.com/uc?export=view&id=12dXMfgax4MdR7EfNM_RfT6Wmu0u0vXqA", #11
            "https://drive.google.com/uc?export=view&id=10caxzcPGlFJDO_9rrAxzioSe9oNvyL2_", #12
            "https://drive.google.com/uc?export=view&id=10dr6B3lm-AC1HyDLogeFAZicDUy6VfKF", #13

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
                "kesan": "Kakak selalu ramah dan mudah diajak ngobrol, suasananya jadi nyaman.",  
                "pesan": "Semoga kakak terus sukses dalam kuliahnya dan selalu semangat menggapai impian!"#1
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450124",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "Way Hui",
                "hobbi": " Membaca",
                "sosmed": "@annisacahyanisurya",
                "kesan": "kakak ini bisa diajak cerita apa aja",  
                "pesan": "Semangat belajarnya kak"#2
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton Film",
                "sosmed": "@wlsbn0",
                "kesan": "Kakaknya punya vibes positif yang bikin tenang",  
                "pesan": "Semangat untuk menebarkan hal positif kak!"#3
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "Peka sama lingkungan, supportif banget.",  
                "pesan": "Terus kasih kita dukungan ya kak, semangat!"#4
            },
             {
                "nama": "Claudhea Angeliani",
                "nim": "1214500124",
                "umur": "19",
                "asal": "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Baca jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakaknya asik diajak bicara",  
                "pesan": "semangat menggapai cita-citanya kak !!!"#5
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal": "Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Melukis",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abangnya punya vibes lucu tapi  tenang dan pinter",  
                "pesan": "Semoga kuliahnya lancar terus ya bang!"#6
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal": "Bernung Pesawaran",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton drakor",
                "sosmed": "@ansftynn_",
                "kesan": "Kakaknya punya vibes lucu tapi  tenang dan pinter",  
                "pesan": "Semoga kuliahnya lancar terus ya kak!"#7
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Solat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya pendiam tapi tetap seru",  
                "pesan": "Lancar selalu kuliahnya bang"#8
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Baca Al-Quran",
                "sosmed": "@myrrinn",
                "kesan": "Kakaknya baik, dan pintar",  
                "pesan": "Jaga kesehatan biar tetap semangat ya kak!!"#9
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "1224500018",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main kucing",
                "sosmed": "@myrriinn",
                "kesan": "Abangnya baik dan ramah banget",  
                "pesan": "Selalu berbuat kebaikan ya!"#10
            },
            { 
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal": "Ogan Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari sinyal di gedung F",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakaknya punya lucu dan selalu bikin orang lain tertawa",  
                "pesan": "Semoga hidup kakak baik-baik terus ya!"#11
            },
            {
                "nama": "Berliana enda putri",
                "nim": "122450000",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya bisa bikin seneng semua orang",  
                "pesan": "Semoga kakak selalu diberkahi kebahagiaan!"#12
            },
            {
               "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Billabong, Gedong Air",
                "hobbi": "Suka Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "Kakak selalu buat orang lain ketawa",  
                "pesan": "Terus menghibur orang sekitar ya kak!"#13
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tyyuYpAwS1S5tkcHgEPIRwrP0NVN5cPi", #1
            "https://drive.google.com/uc?export=view&id=15UOg9j_79297AHxq3EKOyoNrP9oYfZng", #2
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
                "pesan"   : "Semangat dalam menjalankan tugas senat kak!" #1
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
                "pesan"   : "Semangat jadi bagian senat bang!" #2
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def departemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1oU_VbxLR6fUM7920Yd5SM1e5hG-VYiM4", #1
            "https://drive.google.com/uc?export=view&id=1QjXY4nVal4Btj2Y1M4u6k3mt5EllBSyb", #2
            "https://drive.google.com/uc?export=view&id=1F-CWJoSvbEwOmy92FRKs7MaKT06NRhAq", #3
            "https://drive.google.com/uc?export=view&id=1UOdh8qL5y7DO8dJ9Y1oJPRcI_eDE-IPf", #4
            "https://drive.google.com/uc?export=view&id=15Ce45_vykMbhPpmk9YneQi3aJ-H6-Pgx", #5
            "https://drive.google.com/uc?export=view&id=1GArDgE5JlQVRrkfY7Bc8QSIZQ98eA43S", #6
            "https://drive.google.com/uc?export=view&id=1hcjnIUWvPBFmju-RHQWeTomvc6YkwMio", #7
            "https://drive.google.com/uc?export=view&id=156jSV4SZUhkhjUmhZWOKqAF5fvvBVpz0", #8
            "https://drive.google.com/uc?export=view&id=15Db6AQCC0gSrgaZ87Iqbe7GGg4YbpymP", #9
            "https://drive.google.com/uc?export=view&id=1bv3c8h-WWIWDBmB3C_K4O18nyrkpLka9", #10
            "https://drive.google.com/uc?export=view&id=1bbbT48DIMnrSWK_ik8Tw7vZz10-DFiEN", #11
            "https://drive.google.com/uc?export=view&id=1aW8-X29lu2un3Mxn1oYcgtYtNBtUtU7z", #12
            "https://drive.google.com/uc?export=view&id=18SK8-OI48FVI-cPyTIfhnZc5gwsRpnY-", #13
            "https://drive.google.com/uc?export=view&id=1uSxDXUtOtFbTBtKG5DeC0h4bCH77idVa", #14
            "https://drive.google.com/uc?export=view&id=1mC1V0MbtCd2vBAMTplUcJctsiA823D1j", #15
            "https://drive.google.com/uc?export=view&id=10enUWBdgMJGQAfdbTZGGgEB7hJd_2lEv", #16
            "https://drive.google.com/uc?export=view&id=1geACR4ngsu3wOQdXPTBIMLH455KJQCKq", #17
            "https://drive.google.com/uc?export=view&id=1HhtlbUq-yXwBjNwZn4N8--2OS70IsKFD", #18
            "https://drive.google.com/uc?export=view&id=13yLe0UcXu_ZtDJucWiXSMLUHmJ-rQOIT", #19
           
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
                "kesan"    : "Abang ini public speakingnya bagus",  
                "pesan"    : "Semangat jadi kadep psda bang!!"#1
            },
            {
                "nama"     : "Elisabeth Claudia Simanjuntak",
                "nim"      : "122450123",
                "umur"     : "18",
                "asal"     : "Tangerang",
                "alamat"   : "Kemiling",
                "hobbi"    : "Bernafas",
                "sosmed"   : "@celisabethh_",
                "kesan"    : "Kakak cantik, baik, dan ramah",  
                "pesan"    : "Semangat jadi sekretaris psda ya kak!!"#2
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
                "pesan"    : "Tetap santai tapi tegas ya bang!"#3
          
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
                "pesan"    : "Semangat dalam menjalankan tugas sebagai ketuplak kader kak!"#4
          
            },
            {
                "nama"     : "M. Farhan Athaulloh",
                "nim"      : "121450117",
                "umur"     : "21",
                "asal"     : "Lampung",
                "alamat"   : "Kota Baru",
                "hobbi"    : "@menolong",
                "sosmed"   : "@mfarhan.ath",
                "kesan"    : "abang Ateng ini baik bangett suka menolong yang lagi kesusahan",  
                "pesan"    : "Sehat selalu orang baik!"#5
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
                "pesan"    : "Semangat menuntut ilmu bang!!"#6
            },
            {
                "nama"     : "Kemas Veriandra Ramadhan",
                "nim"      : "122450016",
                "umur"     : "19",
                "asal"     : "Bekasi",
                "alamat"   : "Golf Asri",
                "hobbi"    : "Ngetik print hello dunia",
                "sosmed"   : "@kemasverii",
                "kesan"    : "Bang Kemas ini pj tugas kelompok 1 yang pandai mengarahkan",  
                "pesan"    : "Lanjutkan jadi aspraknya ya bang, soalnya cocok!"#7
            },
            {
                "nama"     : "Presilia",
                "nim"      : "122450081",
                "umur"     : "20",
                "asal"     : "Bekasi",
                "alamat"   : "Kota Baru",
                "hobbi"    : "Dengerin The Adams",
                "sosmed"   : "@presilliamg",
                "kesan"    : "Kakak ini ramah, dan kalem",  
                "pesan"    : "Tetap jadi fans the adams di era gempuran bernadya ya kak!"#8
            },
            {
                "nama"     : "Rafa Aqilla Jungjunan",
                "nim"      : "122450122",
                "umur"     : "20",
                "asal"     : "Pekanbaru",
                "alamat"   : "Belwis",
                "hobbi"    : "Baca Webtoon",
                "sosmed"   : "@rafaaqilla",
                "kesan"    : "Kakak ini baik dan cantikk",  
                "pesan"    : "Semangat baca webtoon disela padatnya kuliah ini kak Rafa!"#9
            },
            {
                "nama"     : "Sahid Maulana",
                "nim"      : "122450109",
                "umur"     : "21",
                "asal"     : "Kota Depok, Jabar",
                "alamat"   : "Jalan Airan Raya",
                "hobbi"    : "Dengerin juicy luicy",
                "sosmed"   : "@sahid_maul19",
                "kesan"    : "Abang ini baik dan terlihat pendiam",  
                "pesan"    : "Juicy luicy emang seenak itu kan bang Sahid!"#10
            },
            {
                "nama"     : "Vanessa Olivia Rose",
                "nim"      : "121450108",
                "umur"     : "20",
                "asal"     : "Jakarta",
                "alamat"   : "Perum Korpri",
                "hobbi"    : "Minum kopi, belajar, bikin deyvan senang",
                "sosmed"   : "@roselivness_",
                "kesan"    : "Kakak ini jago basket, keren sampe menang",  
                "pesan"    : "Semoga keterampilan olahraganya meningkat ya kak!"#11
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
                "pesan"    : "Semangat terus kak Allya"#12
            },
            {
                "nama"     : "Eksanty Febriana Sugma Islamiyati",
                "nim"      : "122450001",
                "umur"     : "20",
                "asal"     : "Jawa Barat",
                "alamat"   : "Metro",
                "hobbi"    : "Nyopet",
                "sosmed"   : "@eksantyfebriana",
                "kesan"    : "Kakak ini nim akhirnya 1 dan pernah jadi asprak fisdas",  
                "pesan"    : "Semangat dan terus sabar ya kak ngajarnya!"#13
            },
            {
                "nama"     : "M. Deriansyah Okutra",
                "nim"      : "122450101",
                "umur"     : "19",
                "asal"     : "Kayu Agung",
                "alamat"   : "Jalan Pagar Alam Kedaton",
                "hobbi"    : "Ngukur jalan",
                "sosmed"   : "@dransyh_",
                "kesan"    : "Abang ini menyampaikan materi dengan baik",  
                "pesan"    : "Terus menjelaskan dengan bahasa yang santai tapi mudah dipahami ya bang!!"#14
            },
            {
                "nama"     : "Oktavia Nurwenda Puspita",
                "nim"      : "122450041",
                "umur"     : "20",
                "asal"     : "Lampung Timur",
                "alamat"   : "Way Huwi",
                "hobbi"    : "Travelling",
                "sosmed"   : "@_oktavianrwnda_",
                "kesan"    : "Kakak ini cara bicaranya tertata banget",  
                "pesan"    : "Semoga kakak diberkahi rezeki agar bisa terus travelling!"#15
            },
            {
                "nama"     : "Gede Moena",
                "nim"      : "121450014",
                "umur"     : "21",
                "asal"     : "Bekasi",
                "alamat"   : "Korpri Raya",
                "hobbi"    : "Belajar, Game, Baca Komik",
                "sosmed"   : "@gedemoenaa",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"#16
            },
             {
                "nama"     : "Jaclin Alcavella",
                "nim"      : "122450015",
                "umur"     : "19",
                "asal"     : "Sumatera Selatan",
                "alamat"   : "Korpri",
                "hobbi"    : "Berenang",
                "sosmed"   : "jaclinaclcv",
                "kesan"    : "Kakak ini baik dan keliatan sibuk",  
                "pesan"    : "Semangat ngatur waktunya kak!"#17
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
                "pesan"    : "Semangat selalu kuliahnya bang!"#18
            },
            {
                "nama"     : "Syalaisha Andini Putriansyah",
                "nim"      : "122450111",
                "umur"     : "21",
                "asal"     : "Tangerang",
                "alamat"   : "Kos",
                "hobbi"    : "Baca",
                "sosmed"   : "@syalaisha.i__",
                "kesan"    : "Awalnya bingun karna kek pernah ngeliat kakaknya berulang kali",  
                "pesan"    : "Kalo kembar, mending satu kos apa misah kak?"#19
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenPSDA()


# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen MIKFES":
    def departemenmikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1PujWWhHQxNlfXAlAzu8l-QwK6bkukNil", #1
            "https://drive.google.com/uc?export=view&id=1QQQze-9DGOjRIjQsONvyJvvwhWnMRLba", #2
            "https://drive.google.com/uc?export=view&id=1QHdUDlTMeK8-Wr9cg3xBjBJOKIiQJwwY", #3
            "https://drive.google.com/uc?export=view&id=1uMs1D52GtdCRXagLUpj2lB_CTDzcO9rC", #4
            "https://drive.google.com/uc?export=view&id=1RWCaoJg0Uz37sQx6ZdPE7NWkbbsZS6dq", #5
            "https://drive.google.com/uc?export=view&id=1CmoDj3S_8VPtxaCGFNtvV8f8v58K2KWO", #6
            "https://drive.google.com/uc?export=view&id=1o5RNFiP-EJGFzaqdjEFSv0G6yj0kh6dv", #7
            "https://drive.google.com/uc?export=view&id=1xz7wTjLoh2cJtEkH41ZFvsqFC3HmMqQT", #8
            "https://drive.google.com/uc?export=view&id=1uHmeTA_wFSNxUlC0qUPBePJLSR-D4gmM", #9
            "https://drive.google.com/uc?export=view&id=1MMkpjdOolNJCRYsv1b-wHkAYZR3RIjcc", #10
            "https://drive.google.com/uc?export=view&id=1MtXDUBOhC6h6fXrzG78W7uOmzbcPL7o7", #11
            "https://drive.google.com/uc?export=view&id=1rF0WO08ZjmM-89zTDxcW335vcTW9NwBg", #12
            "https://drive.google.com/uc?export=view&id=1eI02sBTFNejfKB29vY67oj8_3sEKBaUC", #13
            "https://drive.google.com/uc?export=view&id=1Jxie1IoliIwtAtDa6Zgw9ehsL-VZ-1gX", #14
            "https://drive.google.com/uc?export=view&id=1QtMI5-qUOzE2AGdMozbOjvYFgfVUFkNZ", #15
            "https://drive.google.com/uc?export=view&id=1WAWQxHM1SH7gotdGFXm0-A64ryngkb95", #16
            
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
                "kesan": "Abangnya pinter dan profil linkedinnya bagus",
                "pesan": "Semangat menjalani peran sebagai kadep mikfes bang!",#1
               
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Kak Annisa kerenn",
                "pesan": "Semangat menjalani hari-hari yang indah kak!",#2
               
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Abangnya punya vibes kalem",
                "pesan": "Semangat olahraga bang!",#3
               
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "Bang Regi baik dan murah senyum",
                "pesan": "Semangat jadi admin mikfes bang!",#4
                
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Mirip banget sama kembarannya ",
                "pesan": "Baik-baik ya kakak kembar!",#5
               
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "Abangnya terlihat pendiam dan tenang",
                "pesan": "Semangat bermain ML bang!",#6
               
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "Kak deva ekstrovert",
                "pesan": "Tetap jadi orang yang ramah ya kak!",#7
                
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Membaca jurnal dari Bu Mika",
                "sosmed": "@dindanababan_",
                "kesan": "Kakaknya baik dan ramah sekali",
                "pesan": "Semoga kak Dinda lulus tepat waktu!",#8
              
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Kakaknya cantik dan keliatan seperti cewe kue",
                "pesan": "Kakak cocok banget memakai outfit warna terang",#9
               
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakaknya lucu pake outfit blackpink",
                "pesan": "Terimakasih sudah menyebarkan aura positif kak!",#10
               
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya mirip sama seseorang",
                "pesan": "Seamangat di departemen mikfes kak!",#11
              
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "Abangnya lucu dan rajin",
                "pesan": "Semangat menimba ilmu kak!",#12
               
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "Abangnya pasti pinter ngoding",
                "pesan": "Semangat menggapai cita-citanya kak!",#13
               
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakaknya cewe bumi",
                "pesan": "Ada rekomendasi drakor yang harus ditonton sekali seumur hidup ga kak? ",#14
               
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": " Abangnya udah keliatan gamers",
                "pesan": "Jangan lupa bahagia ya bang",#15
               
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Jl Nangka 3",
                "hobbi": "Berolahraga",
                "sosmed": "@randardn",
                "kesan": "Asisten tutorial matdas pas tpb",
                "pesan": "Semoga ilmu yang diajarkan jadi amal jariyah buat bang Randa!",#16
            },
        ]

        display_images_with_data(gambar_urls, data_list)
    departemenmikfes()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen Eksternal":
    def departemeneksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1o0QQLEsTG4pcXcyRPumAEVjyJxHQpvFm", #1
            "https://drive.google.com/uc?export=view&id=1giKIlu-oVDFaAgCVQbHBhdLPpP2Aa3tp", #2
            "https://drive.google.com/uc?export=view&id=1AZWKzoqdoTT6LN7WTYdlVYd9bQwGqGYB", #3
            "https://drive.google.com/uc?export=view&id=1OR1mh2S_d8tWvg79V0b5zCt_0xDiQ8ug", #4
            "https://drive.google.com/uc?export=view&id=1RHJFT-Ajz-MfWyHTt-ZgXOMowCA8OIVn", #5
            "https://drive.google.com/uc?export=view&id=1udEaPHMGPDLSl0F7FhvqzZ5t85IeGl-q", #6
            "https://drive.google.com/uc?export=view&id=1YGTDKEpJKQHx2b_PobgnW-_6UOG_WLjX", #7
            "https://drive.google.com/uc?export=view&id=1LN95NPIDtkKYxdlNAplsqLuJ3ZWkJ7Ae", #8
            "https://drive.google.com/uc?export=view&id=1W50xn2x1SmAvwEDPnrKBomkQxHEcNG5j", #9
            "https://drive.google.com/uc?export=view&id=1bVF-QioDNCXf4D6UJlSAwCaJsw6NOONZ", #10
            "https://drive.google.com/uc?export=view&id=1M77iNkW8ZtuND6EQWjPTc4F68GpJzk0R", #11
            "https://drive.google.com/uc?export=view&id=1f3pLCHQM_RDpX9AQCzp7wjicAIQRWpGm", #12
            "https://drive.google.com/uc?export=view&id=1n5k7OllS1uZOobGq1icHQ_B_62I6aeKJ", #13
            "https://drive.google.com/uc?export=view&id=12uS9hWtLkZpckK42L7pH_JtJG4nNAMBD", #14
            "https://drive.google.com/uc?export=view&id=1U-C5sQUidN2CeCM1X409O1w4lW-4eOvo", #15
            "https://drive.google.com/uc?export=view&id=1NitSQWovubYfmHitVaFf_VxshoruFG8_", #16
            "https://drive.google.com/uc?export=view&id=1DTQRB4YzsZiB_fOJTh7RmOErqon9Zw_C", #17
            "https://drive.google.com/uc?export=view&id=1BvOG2gOC4Sbw2eVzB3iZrLYd6XTJLeJD", #18
            "https://drive.google.com/uc?export=view&id=1fNZCiSGrwJl3RxxCM6MXEg-tiZ3lQkRX", #19
            "https://drive.google.com/uc?export=view&id=14whG8epEsGufZzIkIpORPGPfF5VmDle0", #20
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
                "kesan": "Abangnya baik",
                "pesan": "Sukses ya bang!",#1
            
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "Kakaknya keren tapi lucu jugaa",
                "pesan": "Semangat terus kak",#2
                
            },
            {
                "nama": "Nazwa Nabila",
                "nim": "121450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Kochpri",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakaknya keren",
                "pesan": "Tetap keren dan terus semangat ya kak!",#3
               
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "Abangnya baik baik dan terlihat kalem",
                "pesan": "Tetap semangat bang!",#4
                
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Berkebun",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakaknya cantik, baik, dan pintar",
                "pesan": "Keren selalu ya kak!",#5
        
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan": "Kakaknya lucu dan menarik banget",
                "pesan": "Sehat dan bahagia selalu ya kak!",#6
               
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Surfing",
                "sosmed": "@nateee__15",
                "kesan": "Kak nate lucuu, baik, dan pengertian banget",
                "pesan": "Kak nate semangat jadi imtek yaa!",#7
                
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kakaknya baik dan kalem",
                "pesan": "Sehat selalu ya!",#8
                
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Pulang malam",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya aktif di berbagai kegiatan",
                "pesan": "Sukses selalu kak!",#9
               
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan": "Bang tobias keliatan lucu tapi tegas juga",
                "pesan": "Semangat ya bang kuliahnya",#10
               
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "Kakaknya tegas",
                "pesan": "Semangat dan sabar terus ya kakk",#11
               
            },
            {
                "nama": "Rizky Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "Abangnya baik dan keren",
                "pesan": "Semangat jadi eksternal kak!",#12
                
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "Abangnya baik dan ramah",
                "pesan": "Sehat selalu ya bang",#13
               
            },
            {
                "nama": "Asa Do’a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "Kakaknya lucu mirip di kartun",
                "pesan": "Semangat ya kak kuliahnya!",#14
                
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan": "Kakaknya baikk",
                "pesan": "Semangat kuliahnya kak!",#15
                
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya baik dan ramah",
                "pesan": "Semangat bang!",#16
               
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan": "Kak Izza baik, ramah, dan pinter banget",
                "pesan": "Semangat untuk terus aktif kak!",#17
                
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "Kakak daplok kelompok 1 nih",
                "pesan": "Semangat jadi daplok kita ya kak!",#18
                
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Nemenin Tobias lari",
                "sosmed": "@rayths_",
                "kesan": "Abangnya keren",
                "pesan": "Semangat ya bang!",#19
               
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450127",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Way Dadi",
                "hobbi": "Olahraga",
                "sosmed": "@triayunanni",
                "kesan": "Kakaknya baik, dan ramah",
                "pesan": "Semangat untuk terus aktif kak",#20
            
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemeneksternal()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen Internal":
    def departemeninternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VT4gR3S6tOqmKL5lMIvr3cZTw5gFMw23", #1
            "https://drive.google.com/uc?export=view&id=1WG2PseHITrF3MKvpYMC3PeYNlOh3dzoQ", #2
            "https://drive.google.com/uc?export=view&id=1VdjhJRtOSsZth-PohAam3ikLBKaeAjKc", #3
            "https://drive.google.com/uc?export=view&id=1VpupJEAc-_v-wUp4TYJ0l-2KMuzvsMZB", #4
            "https://drive.google.com/uc?export=view&id=1W6lSIVo7azM5SpazfqOwpfyYdUbTAwb_", #5
            "https://drive.google.com/uc?export=view&id=1VV5iB56XxCmwQfL9zqHlxvYZT3-nvnQw", #6
            "https://drive.google.com/uc?export=view&id=1Vg9y47Oo3D1dvz0RH_bZfQ8BW0yiJh0T", #7
            "https://drive.google.com/uc?export=view&id=1W0KD1s62-6HcKaCVTdpgh3XUTVJXYVkp", #8
            "https://drive.google.com/uc?export=view&id=1IZmpZVLf110ESlLKLG1aYqzxrRFzrl5H", #9
            "https://drive.google.com/uc?export=view&id=1VUwoEANQwlsP_3dNXYdXs2CzdIXHtlxT", #10
            "https://drive.google.com/uc?export=view&id=1VWt5Mk423j4_CgM1d_jMjBc95BKcwP1h", #11
            "https://drive.google.com/uc?export=view&id=1Vex7bPU_YkJmi31_89Fj12yHeLVItwl7", #12
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
                "kesan": "Abangnya lucu dan keren banget",
                "pesan": "Semangat jadi kadep internal ya bang!",#!
                
            },
            {
                "nama": "Chatrine Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "Kakaknya cantik dan keliatan cocok di dept internal",
                "pesan": "Semangat belajar terus kak!",#2
              
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Pasaruntung",
                "hobbi": "Mengoleksi Dino",
                "sosmed": "@akbar_restika",
                "kesan": "Abangnya keren sekalii",
                "pesan": "Semoga abang sehat selalu!",#3
                
            },
            {
                "nama": "Renita Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Membaca dan Memancing",
                "sosmed": "@renita.shn",
                "kesan": "Kakaknya ramah, baik dan lucuu",
                "pesan": "Terusin sifat ramahnya ya kak!",#4
               
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "Kakaknya murah senyum",
                "pesan": "Jangan lupa senyum setiap mengawali hari kak!",#5
          
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "Abangnya jadi asprak strukdat dan super duper ramah",
                "pesan": "Tetep semangat menjadi humas ya kak!",#6
            
            },
            {
                "nama": "Yosia Retare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi": "Nungguin ayam betina berkokok",
                "sosmed": "@yosiabanurea",
                "kesan": "Abangnya baik dan keren",
                "pesan": "Semaoga abang diberi kelancaran dalam mengerjakan apapun!",#7
           
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "Vibes abangnya mewakili internal banget",
                "pesan": "Semangat futsalnya bang!",#8
            
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Ngejokes",
                "sosmed": "@josuapanggabean_",
                "kesan": "Abangnya suka bikin orang ketawa",
                "pesan": "Semangat buat jokes yang fresh bang!",#9
           
            },
            {
                "nama": "Azizah Kusuma Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "Kakaknya pasti rajin",
                "pesan": "Semangat berkebun kak!",#10
          
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@meirasty_",
                "kesan": "Kakaknya baik dan adem banget diliatnya",
                "pesan": "Kak Meira harus nonton film netflix!",#11
               
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Berenang di Laut",
                "sosmed": "@rexander",
                "kesan": "Abangnya baik dan terlihat cocok di kerohanian",
                "pesan": "Semangat bang!",#12
               
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemeninternal()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen SSD":
    def departemenssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dTtk5R7zwzEs6jqP0GIPN115iqaA1FLp", #1
            "https://drive.google.com/uc?export=view&id=1MBHgmXLgJvUPUvFyufQ34pA2XYn33QpA", #2
            "https://drive.google.com/uc?export=view&id=1MRqKCWonONYJrTfn3EqK1-IUOK9EJoNR", #3
            "https://drive.google.com/uc?export=view&id=1MD0w0B0dO2vJnzATXVuaXdXo-XdF6pEI", #4
            "https://drive.google.com/uc?export=view&id=1MD-cYR_OWGUGTTv2QRvDSr6_AT_KKGAX", #5
            "https://drive.google.com/uc?export=view&id=1MIRnZNJDmdNNyugHGK52wLR-UiBcHj5F", #6
            "https://drive.google.com/uc?export=view&id=1M4krNepyCSUMWYvmhShF-Db1Twl5e7oF", #7
            "https://drive.google.com/uc?export=view&id=1ZbQvA6kHtDH24G0PBOuQRpqaTNrcCOFo", #8
            "https://drive.google.com/uc?export=view&id=1MOuxAs4ANb7XHLhak-lHqIBNF6vVF3pY", #9
            "https://drive.google.com/uc?export=view&id=1MNopagTDI3P8SL4UWiGtlpRJTbvv31r9", #10
            "https://drive.google.com/uc?export=view&id=1MMzCR0jT2Aq1_CeKKtFja_o7ekE3zLUy", #11
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
                "kesan": "Abangnya baik dan ngejelasin mengenai departemen dapat dipahami",
                "pesan": "Semangat jadi pemimpin ssd bang!",#1
            
            },
            {
                "nama": "Adisty Syawaida Arianto",
                "nim": "121450136",
                "umur": "23",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan": "Kakaknya ramah dan lucu",
                "pesan": "Semangat terus dalam setiap aktivitas ya kak!",#2
                
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "Kakaknya bisa manage keuangan",
                "pesan": "Semangat menghitung uang kak!",#3
             
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Touring",
                "sosmed": "@dananghk_",
                "kesan": "Daplok jordan nih",
                "pesan": "Tetap semangat berkarya bang!",#4
           
            },
            {
                "nama": "Farel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "Abangnya supportif banget",
                "pesan": "Tetap semangat damaskus bang!",#5
     
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukittingi",
                "alamat": "Airan 1",
                "hobbi": "Badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "Linkedin abangnya bagus",
                "pesan": "Semoga kuliahnya memuaskan kak!",#6
             
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakaknya lucu dan baikk bener",
                "pesan": "Tetap semangat dan terus berjuang kak!",#7
           
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Kakaknya ramah dan kalem",
                "pesan": "Semangat kuliah terus kak",#8
              
            },
            {
                "nama": "Alvia Asrinda Br.Ginting",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobbi": "Nonton Windah",
                "sosmed": "@alviagnting",
                "kesan": "Kakaknya asik dan senyumnya manis",
                "pesan": "Makasih kak udah sharing ilmunya!",#9
    
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangkal",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya baik dan ramah",
                "pesan": "Semangat bang Dhafin!",#10
              
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobbi": "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan": "Kakaknya seruu di setiap perbincangan",
                "pesan": "Semangat terus ya kak untuk kuliah dan organisasinya!",#11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenssd()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen MEDKRAF":
    def departemenmedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1x8j3W_txOOtNWa2sPU8Ka8KfsQdw9SpB", #1
            "https://drive.google.com/uc?export=view&id=1CSSHv8CNOX--9R-nPIiTU98DaSFQYMmS", #2
            "https://drive.google.com/uc?export=view&id=1nch9siwHCAZJYB_p_Z_7ioA7eUvzyrkb", #3
            "https://drive.google.com/uc?export=view&id=1jmYCvSkAy-MMXIPmq-D9XdpDWeQ0z3wX", #4
            "https://drive.google.com/uc?export=view&id=1fRRaBZQh0smpURrrxjcoJQ0gS1OXcssN", #5
            "https://drive.google.com/uc?export=view&id=1c55ZnMAT8aKGgOPRmamGjF05QJ5I1U4T", #6
            "https://drive.google.com/uc?export=view&id=10Z0EbejZQlLmfpQjAETHjqi5mBHvm-yV", #7
            "https://drive.google.com/uc?export=view&id=1Ac9pHvNDuoAzm5sQNjoy0E5QLxRBwuab", #8
            "https://drive.google.com/uc?export=view&id=1A7HY5NNwOQ8CSTzzrjpc_CQsipYitjyQ", #9
            "https://drive.google.com/uc?export=view&id=1Ont2knB8ksHIpEw79NtspnpyKd2EEhtT", #10
            "https://drive.google.com/uc?export=view&id=1Nw5E6Lah_QF_EqhR8GhjrGFdAAQ2pZW1", #11
            "https://drive.google.com/uc?export=view&id=14QJeV_6okqld7k9b0jTuQey5iD_Kp8ar", #12
            "https://drive.google.com/uc?export=view&id=1N_xSz0syJRyI4-vwqLuSsPY89K9stqyZ", #13
            "https://drive.google.com/uc?export=view&id=1vBP6PIXc3frzuNWVqvlVJcgob6lNUZig", #14
            "https://drive.google.com/uc?export=view&id=1ALdvTuiLlZm1kpqfb8_AAuJB-R6ydPF2", #15
            "https://drive.google.com/uc?export=view&id=1cfoUHBfhkXVg7nO-7QXeeUuQbFn7E-ml", #16
            "https://drive.google.com/uc?export=view&id=1DhthbUUYpOFXwfiUEY0adJc-3E-O-bL2", #17
            "https://drive.google.com/uc?export=view&id=1CZ0tybeOrOaO-dSEDsHbw8ZqFt29GydW", #18
            "https://drive.google.com/uc?export=view&id=1dJ4RXVHDUdxdGpjLH4A13cmuitpGLPFP", #19
        ]
        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal": "Makassar",
                "alamat": "Sukarame",
                "hobbi": "Nonton",
                "sosmed": "@wayyulaja",
                "kesan": "Abangnya asik dan baik",
                "pesan": "Jangan kapok jadi medkraf ya bang!",#1
             
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "Kakaknya cantik, pinter, dan ramah",
                "pesan": "Semoga lulus kuliah tepat waktu ya kak, semangat!",#2
              
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Nugas",
                "sosmed": "@arsyiah._",
                "kesan": "Kakaknya lucu, baik, dan ramah",
                "pesan": "Semoga targetnya tercapai ya kak!",#3
               
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Lagi Nyari",
                "sosmed": "@dino_kiper",
                "kesan": "Abangnya santai",
                "pesan": "Tetap semangat ya bang!",#4
                
            },
            {
                "nama": "Muhammad Arsal Ranjana Putra",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 4",
                "hobbi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "Abangnya baik dan ramah",
                "pesan": "Semangat merangkai kode bang!",#5
              
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Kakaknya kayak model, tinggi semampai",
                "pesan": "Semangat kuliahnya kak!",#6
           
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": "122450045",
                "umur": "20",
                "asal": "Natar, Lampung Selatan",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "Kakaknya seru, baik dan ramah",
                "pesan": "Semoga bahagia terus ya kak!",#7
           
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "Kakaknya lucu dan ramah",
                "pesan": "Semangat kak Juju!",#8
               
            },
            {
                "nama": "Patricia Leondra Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton Film",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kak cia words of affirmation sekalii",
                "pesan": "Semangat menjalani hidup kak",#9
             
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan": "Kakaknya baikk, ramah bener dan keren sekalii",
                "pesan": "Sehat dan bahagia terus ya kak!",#10
            
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakaknya baik dan ramah",
                "pesan": "Semangat mendalami hobinya kak",#11
              
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi": "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan": "Kakakanya baik kalem dan teduh",
                "pesan": "Sehat selalu kak!",#12
            
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "Abangnya lucu dan kreatif",
                "pesan": "Semaangat baca komik bang!",#13
     
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi": "Nonton Drakor",
                "sosmed": "@nsywanaf",
                "kesan": "Kakaknya asik dan baik hati",
                "pesan": "Semangat ngedrakor kak!",#14
          
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Baca Novel yang Bikin Nangis",
                "sosmed": "@prskslv",
                "kesan": "Kakaknya baik dan buat nyaman saat diajak bicara",
                "pesan": "Jangan keseringan baca novel angst ya kak",#15
            
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa, Labuhan Dalam",
                "hobbi": "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan": "Abangnya lucu, jago desain",
                "pesan": "Semangat ngegame dan ngodingnya bang!",#16
            
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "_akmal.faiz",
                "kesan": "Perhatian dan daplokable bangett",
                "pesan": "Semoga hal baik selalu dateng ke abang",#17
            
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani)",
                "hobbi": "Bengong/Membaca Buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Abang asprak alproo",
                "pesan": "Semangat desain bang!",#18

            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi": "Mengerjakan Tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Kak nun lucu bangett, pinter jugaa",
                "pesan": "Semangat meraih mimpi dan cita-cita kak",#19
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenmedkraf()
