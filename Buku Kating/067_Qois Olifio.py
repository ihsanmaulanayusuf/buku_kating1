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
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#2a1018",
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
            st.write(f"Hobi: {data_list[i]['hobi']}")
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
            "https://drive.google.com/uc?export=view&id=15BFoMkeQYjrFgLK8K_66AyaC98B_XHCU", #1
            "https://drive.google.com/uc?export=view&id=1cYGyOgTF7EpcTFWGRDtiAdxAS8BHIvDw", #2
            "https://drive.google.com/uc?export=view&id=1-fnkYwxaHBS9S0dbUS1xwhN9E_6j5BT3", #3
            "https://drive.google.com/uc?export=view&id=1VCU_e1g8HVLphk3JZOiUaIvV4fUvHcM-", #4
            "https://drive.google.com/uc?export=view&id=1MpZjKbU1cW4FA8QfEF0DkmdJmCpiOt2M", #5
            "https://drive.google.com/uc?export=view&id=12j916Rn6fyv27tLyR39o2cKm9vP-0Vqc", #6
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pulau Damar",
                "hobi": "Dengerin musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Abangnya fun, berwawasan luas, dan jago publik speakingnya",  
                "pesan": "Semangat terus bang !!!"#1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal": "Bukit Kemuning",
                "alamat": "Pawen 2 Sukarame",
                "hobi": "Main gitar",
                "sosmed": "@pndrinsni21",
                "kesan": "Abangnya asik dan humoris juga",  
                "pesan": "Semangat terus kuliahnya bang !!!"#2
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kotabaru",
                "hobi": " Nonton Drakorr",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak ini baik dan cantik juga",  
                "pesan":"Semangat untuk kakak, semoga sehat selalu"#3
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak murah senyum dan suka ketawa.",  
                "pesan": "Semangat terus, Kak!"#4
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal": "Payakumbuh",
                "alamat": "Nangka 4",
                "hobi": "Dengerin  bang Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak yang selalu keliatan sabar dan santai nih.",  
                "pesan": "Jaga kesehatan dan semangat terus ya, Kak!"#5
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Kotabaru",
                "hobi": "Dengerin  bang Pandra Gitaran",
                "sosmed": "@nadillaadr26",
                "kesan": "Kakak nya ini pengertian, selalu memberikan masukan juga.",  
                "pesan": "Semoga kuliahnya lancar, kakak!"#6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LpC2wyjlx9g7aZSQfhEEJ8pvzP0Wj_la", #7
            "https://drive.google.com/uc?export=view&id=1M2ja3vLIR7p6j7C_gQxRQCWZ1UGmyA9N", #8
            "https://drive.google.com/uc?export=view&id=1M6yJL4WiqiB9qtSdQkXtWZgGNcpmuX15", #9
            "https://drive.google.com/uc?export=view&id=1LtkxwaztZPnt1G3zpiBMy4Qz5C3cjOma", #10
            "https://drive.google.com/uc?export=view&id=1Lq_InaNpaiGXFs9l3fGoHNBYB6b1HZXw", #11
            "https://drive.google.com/uc?export=view&id=1M2NApU9Hum-VAJBBlZ3ESrFDMhtcpua_", #12
            "https://drive.google.com/uc?export=view&id=1M8W2NJGZfSw4LUhTxsBrRMteBtll5nt3", #13
            "https://drive.google.com/uc?export=view&id=1PGX_9_hVTmiEPI8opW1X8JCcO7z6vamP", #14
            "https://drive.google.com/uc?export=view&id=1OkEmLFG4cFpUT44hXtD8Lu8WhNhzr886", #15
            "https://drive.google.com/uc?export=view&id=1LrtPKJt52CicH5RiGhRTD4b6zj30wxd0", #16
            "https://drive.google.com/uc?export=view&id=1LvbFuaTjq9hSwdEPfVmTshH1I7Z-lj73", #17
            "https://drive.google.com/uc?export=view&id=1M3cvYUFQsvALJalZY2nxqid67QYjr5-T", #18
            "https://drive.google.com/uc?export=view&id=1M-VPD-PirMZfN3PAecc9KCofEcBobHFV", #19
    
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Raden Saleh",
                "hobi": "Bertanya sama GPT",
                "sosmed": "@trimurniaa_",
                "kesan": "Kakak murah senyum, ramah, asik, dan mudah diajak ngobrol.",  
                "pesan": "Semoga kakak terus sukses dalam kuliahnya ya!" #7
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450124",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "Way Hui",
                "hobi": " Membaca",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak ini asik diajak tukar pikiran.",  
                "pesan": "Teruslah semangat belajar dan pantang menyerah kak!" #8
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Raden Saleh",
                "hobi": "Menonton Film",
                "sosmed": "@wlsbn0",
                "kesan": "Sikap positif kakak ini bikin suasana jadi lebih santai.",  
                "pesan": "Tetap semangat ya kakak!"#9
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jati Agung",
                "hobi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "Kakak ini suportif dan selalu memberi motivasi.",  
                "pesan": "Sukses selalu untuk kuliahnya kak!"#10
            },{
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal": "Bernung, Pesawaran",
                "alamat": "Bandar Lampung",
                "hobi": "Nonton Drakor",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak ini asik dan murah senyum juga nih.",  
                "pesan": "Semangat terus kuliahnya kakak!"#11
            },{
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Punya energi positif, abang asprak juga nih pasti pinter ngoding",  
                "pesan": "Semoga abang selalu diberi kelancaran dalam segala urusan."#12
            },{
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobi": "Baca Al-qur'an",
                "sosmed": "@fleurnsh",
                "kesan": "Kakak yang ramah, cantik dan mudah diajak ngobrol",  
                "pesan": "Semangat terus, Kak!"#13
            },{
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak ini punya style yang bagus juga.",  
                "pesan": "Semoga sukses di setiap langkah ke depannya, Kak!"#14
            },{
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abang nya baik dan jago main ML juga nih.",  
                "pesan": "Semoga selalu diberi kemudahan ya Bang!"#15
            },{
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal": "Ogan Ilir",
                "alamat": "Natar",
                "hobi": "Nyari Sinyal di Gedung F",
                "sosmed": "@_.dheamelia",
                "kesan": "Mudah bergaul dan punya gaya candaan tersendiri.",  
                "pesan": "Sukses selalu kakak!"#16
            },{
                "nama": "Muhammad Fahrul Aditya",
                "nim": "122450000",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Abang ini murah senyum dan informatif juga nih.",  
                "pesan": "Sukses terus dan semangat mengejar impiannya bang!"#17
            },{
                "nama": "Berliana Enda Putri",
                "nim": "122450000",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini sosok yang humble dan asik diajak bicara.",  
                "pesan": "Semangat terus kak!"#18
            },{
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Billabong, Gedong Air",
                "hobi": "Suka Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang yang selalu membawa aura positif, humoris dan jadi asprak juga nih.",  
                "pesan": "Semoga abang selalu diberi kemudahan dalam segala urusan ya!"#19
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LUmwFyshkcMGU4qaWvO05FPCx-XIVZXp", #1
            "https://drive.google.com/uc?export=view&id=1LU7V2sWISu3VzBL7P5_pRprYl2Fk3Tl3", #2
        ]
        data_list = [
            {
                "nama": "Annisa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal": "Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobi": "Dengerin bang Bintang nyanyi",
                "sosmed": "@annisalutfi_",
                "kesan": "Kakak nya cantik, asik dan energik banget nih",
                "pesan": "Semangat terus dan pantang menyerah kak!" #1
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kotabaru",
                "hobi": "Menyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abang kece nih, gampang senyum dan berwawasan luas juga",
                "pesan": "Semangat terus bang, semoga keinginan abang terkabulkan" #2
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen PSDA":
    def departemenpsda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1UMfrbEIZxotdFsZuvpPJxxgoo26FppaZ", #1
            "https://drive.google.com/uc?export=view&id=1PHgLzJM1CVhOX3jm86Rat6N4-DmbChRC", #2
            "https://drive.google.com/uc?export=view&id=1U302rWUidBFkVzfpK8pMg8X4R1UqcSBE", #3
            "https://drive.google.com/uc?export=view&id=1UwNzmROJ-GBuOE9vLbLVojhEVoOOv5D9", #4
            "https://drive.google.com/uc?export=view&id=1Mt-kTBzHQxM1gURybSGMmFQem6irX82g", #5
            "https://drive.google.com/uc?export=view&id=122zzMSGhiPH6nsURQVPzqShoR7QXml2c", #6
            "https://drive.google.com/uc?export=view&id=1GprQv7hrHbZY7QntY4Z0LaWPP_Rytf7a", #7
            "https://drive.google.com/uc?export=view&id=1fYXgJ4MDdZW0WQdRleylAwK6WTqK7IMN", #8
            "https://drive.google.com/uc?export=view&id=1C3OUxrpinWvyflFHfTSs9b5XQTONGlTa", #9
            "https://drive.google.com/uc?export=view&id=1rRJpH9kuNkkHQsqESKnX6dyFplhS6sV8", #10
            "https://drive.google.com/uc?export=view&id=1LF2dXA4lHzjxq6skRaMkKHbLxLCNt6-j", #11
            "https://drive.google.com/uc?export=view&id=1ZmruFmfbHOGYcmH9jznEVtcxF_wg5Tpj", #13
            "https://drive.google.com/uc?export=view&id=1G3xJVu2wJeJ4H5H5QZrFQiZDmkbRf-ap", #14
            "https://drive.google.com/uc?export=view&id=1gzRm6Cpdv3MvcxwZr3ArjR6jOQfAL-oL", #39
            "https://drive.google.com/uc?export=view&id=1eYDO8MDQwS_a83X16dCnp-yBp54EPEM6", #17
            "https://drive.google.com/uc?export=view&id=14BzUXr8h2xOBXgeHvoG0VadzfU5MnTTz", #16
            "https://drive.google.com/uc?export=view&id=1yle1sDxb2R2C80c4Z8P6Lfg5vs_0ljEG", #17
            "https://drive.google.com/uc?export=view&id=1cEweioo5BbI3z-8mXLWzHDKJolfl_8kX", #16
            "https://drive.google.com/uc?export=view&id=1_ezlmAXTGNe3mi-fYXjR0Jvt4rXH8Jwd", #17
            "https://drive.google.com/uc?export=view&id=1RjatjMsAN4gpGehgFz9qM7m8D71dpWwQ", #18
            "https://drive.google.com/uc?export=view&id=1kB6i98uPQ5MPj_kBcywRyV-o3EBWh0h3", #17
            
        ]
        data_list = [
           {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Khobam",
                "hobi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abang ini tegas, baik, dan jadi pemandu juga di kampus",  
                "pesan":"Semangat terus kuliahnya bang!" #22
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
                "sosmed": "@celisabeth",
                "kesan": "Kakak ini baik dan murah senyum loh",  
                "pesan":"Semangat terus dalam menggapain impiannya kak!" #23
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Marahin orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak ini cantik, baik, asik, dan friendly",  
                "pesan":"Semangat terus kak kuliahnya" #24
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobi": "Main",
                "sosmed": "@allyaislami_",
                "kesan": "Kakak ini keliatan tegas tapi asik dan suka bercanda juga nih",  
                "pesan":"Semangat terus dalam menggapai impiannya kak!" #25
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiyati",
                "nim": "122450001",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Metro",
                "hobi": "Nyopet",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini fun dan murah senyum juga nih",  
                "pesan":"Semangat terus ya kak!" #26
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobi": "Bengong",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini cantik, murah senyum dan baik juga",  
                "pesan":"Semangat terus dalam mengejar impiannya kakak!" #27
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Jalan Pangeran Senopati Raya 18",
                "hobi": "Baca Kitab Suci",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abang ini keliatan pendiam tapi sebenarnya baik dan asik diajak ngobrol",  
                "pesan":"Semangat terus bang kuliahnya!" #28
            },
            {
                "nama":  "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jalan Pagar Alam Kedaton",
                "hobi": "Ngukur jalan",
                "sosmed": "@dransyh_",
                "kesan": "Abang ini orang yang santai, baik, dan punya lawakan tersendiri",  
                "pesan":"Semangat terus bang kuliahnya!" #29
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Travelling",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakak ini kalem, baik dan murah senyum juga",  
                "pesan":"Semangat terus kuliahnya kakak!" #30
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "1214500148",
                "umur": "21",
                "asal":"Duri, Riau",
                "alamat": "Pulau Damar Kobam",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abangku ini baik, ramah, dan becanda mulu kerjaannya",  
                "pesan":"Semangat terus bang dalam menggapai impiannya!" #31
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobi": "Membaca",
                "sosmed": "@syalaisha.i_",
                "kesan": "Kakak ini asik dan ramah juga",  
                "pesan":"Semangat terus kak kuliahnya!" #32
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobi": "Asprak",
                "sosmed": "@johanneskrsjnnn",
                "kesan": "Abang ini keliatan tegas tapi sebenarnya friendly dan friendly juga",  
                "pesan":"Semangat terus bang. Semoga dapat mencapai apa yang diinginkan!" #34
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Golf Asri",
                "hobi": "Ngetik print hello dunia",
                "sosmed": "@kemasverii",
                "kesan": "Abang ini baik, pinter, dan sepuh ngoding nih",  
                "pesan":"Semangat terus bang. Semoga menjadi orang yang sukses!" #35
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobi": "Dengerin The Adams",
                "sosmed": "@presilliamg",
                "kesan": "Kakak ini baik dan murah senyum juga nih",  
                "pesan":"Semangat terus kak kuliahnya" #37
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450122",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak ini asik, baik dan kalem juga nih",  
                "pesan":"Semangat terus kuliahnya kakak" #38
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok, Jawa Barat",
                "alamat": "Jalan Airan Raya",
                "hobi": "Dengerin juicy luicy",
                "sosmed": "@sahid_maul19",
                "kesan": "Abang ini asik, informatif yang cocok untuk diajak diskusi",  
                "pesan":"Semangat terus ya bang!" #39
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Perum Korpri",
                "hobi": "Minum kopi, belajar, bikin Deyvan senang",
                "sosmed": "@roselivness__",
                "kesan": "Kakak ini tegas, tapi sebenarnya asik dan murah senyum loh",  
                "pesan":"Semangat terus kuliahnya kak!" #40
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Abang ini santai, asik, baik dan friendly juga nih",  
                "pesan":"Semangat terus ya bang kuliahnya. Semoga dapat meraih apa yang diinginkan!" #41
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "Abang ini kalem dan ramah juga",  
                "pesan":"Semangat terus ya bang!" #42
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv",
                "kesan": "Kakak ini asik dan public speaking juga bagus",  
                "pesan":"Semangat terus ya kak!" #43
            },
            {
                "nama":  "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Abang ini asik dan ramah",  
                "pesan":"Semangat terus ya bang!" #44
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenpsda()
    
elif menu == "Departemen MIKFES":
    def departemen_mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LUos93uL_iXqOsLmK7GJJ2JMeamqRBA8", #45
            "https://drive.google.com/uc?export=view&id=1LheC_cCG30Er9jjQ6Pj3aZp5_s5QewMi", #46
            "https://drive.google.com/uc?export=view&id=1LWxjxljVvP_TuLrpCoznA87upXD4HYUl", #47
            "https://drive.google.com/uc?export=view&id=1LXyc2GbsESW9EdAIoZHtMzh4kdESthMq", #48
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #49
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #50
            "https://drive.google.com/uc?export=view&id=1LmK1zY2eg9D9wyE2Ygvnx9DXgFfb5YEE", #51
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #52
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #53
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #54
            "https://drive.google.com/uc?export=view&id=1Lesn5JEsQ2KNDuOB5I-NCaVZvIAPYNeh", #55
            "https://drive.google.com/uc?export=view&id=1LkvLywfz5Rz3qF5ZSS_gQSSJsRtiot2q", #56
            "https://drive.google.com/uc?export=view&id=1L_aH6yZtPxKldcbMICxRglgWtD_J1qiC", #57
            "https://drive.google.com/uc?export=view&id=1Ld556zTIVa5mpw7tE_bktXHEj6riuLMO", #58
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #59
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #60
            "https://drive.google.com/uc?export=view&id=1LV2qsP1c5VnyIcs2WKl_l-3PpJI58a3b", #61
            "https://drive.google.com/uc?export=view&id=1LebqpW-lvqVmY6_Wxb5caktiLK3T6_XV", #62
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #63
            "https://drive.google.com/uc?export=view&id=1LYTS7tCHY94_HOMQE3LukUVAMb3T8oIr", #64
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #65
        ]
        data_list = [
            {
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21",
                "asal":"Lubuk Linggau, Sumatera Selatan",
                "alamat": "Jl. Nangka 4",
                "hobi": "Olahraga",
                "sosmed": "@rafadhlillahh13",
                "kesan": "Abang ini asik, baik, pemikirannya luas, dan seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya!" #45
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "19",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Sebesi",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Kakak ini asik, dan mempunyai pikiran yang bagus",  
                "pesan":"Semangat terus kak kuliahnya!" #46
            },
            {
                "nama": "Mujadid Choirus Surya",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": " ",
                "kesan": "Abang ini asik, dan public speaking yang bagus",  
                "pesan":"Semangat terus bang" #47
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "19",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobi": "Olahraga",
                "sosmed": "@",
                "kesan": "Abang ini asik dan informatif juga",  
                "pesan":"Semangat terus bang!" #48
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": " ",
                "kesan": "Abang ini baik dan mempunyai pikiran yang bagus",  
                "pesan":"Semangat terus bang!" #49
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl. Permadi",
                "hobi": "Ngasprak ADS",
                "sosmed": "@",
                "kesan": "Abang ini asik, baik, dan informatif juga",  
                "pesan":"Semangat terus bang!" #50
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Gg. Yudistira",
                "hobi": "Review jurnal Bu Mika",
                "sosmed": "@",
                "kesan": "Kakak ini asik, baik, dan murah senyum juga",  
                "pesan":"Semangat terus kak" #51
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv",
                "kesan": "Abang ini asik dan  ramah juga",  
                "pesan":"Semangat terus bang!" #52
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "19",
                "asal":"Bukittinggi",
                "alamat": "Korpri",
                "hobi": "ML (Machine Learning)",
                "sosmed": "@",
                "kesan": "Abang ini asik dan public speaking yang bagus juga",  
                "pesan":"Semangat terus bang" #53
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobi": "Resume Webinar",
                "sosmed": "@",
                "kesan": "Kakak ini asik, baik, dan public speaking yang bagus",  
                "pesan":"Semangat terus kak!" #54
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobi": "Membaca jurnal Bu Mika",
                "sosmed": "@dindanababan",
                "kesan": "Kakak ini asik, baik dan informatif",  
                "pesan":"Semangat terus kak!" #55
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review jurnal Bu Mika",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #56
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #57
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #58
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #59
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #60
            },
            {
                "nama": "Eggi satria",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #61
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #62
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #63
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #64
            },
            {
                "nama": "Vita Anggraini",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #65
            },
         ]
        display_images_with_data(gambar_urls, data_list)
    departemen_mikfes()

elif menu == "Departemen Eksternal":
    def departemeneksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1TUaDs254TwyhUL6qvxpS4faphQwurp8l", #66
            "https://drive.google.com/uc?export=view&id=1IY_acB3-HyQd4NCKFqe1WyOR6-sOCKxC", #67
            "https://drive.google.com/uc?export=view&id=1TPNhTlSPGANjZm0Eq4VARw2C7HhSsbQN", #68
            "https://drive.google.com/uc?export=view&id=1r5LxY08tJr54aM676aTjUGBznOAEx0OT", #69
            "https://drive.google.com/uc?export=view&id=16EAgl0XLMi3Vkl01OTiWHS1sWyXAnTHP", #70
            "https://drive.google.com/uc?export=view&id=1YWQ4V6v6BNf_f-F7Mb_PZhoLpV76uJ90", #71
            "https://drive.google.com/uc?export=view&id=1xJfFqKvC6GPupQlFwW_AhKKrlTZcJFpc", #72
            "https://drive.google.com/uc?export=view&id=1vfF5zxB8ldWUlUZooEHqwjsn9DeBPPDT", #73
            "https://drive.google.com/uc?export=view&id=1PIr3zZB00QDRepH5pGSgywHtNnq1ZuJI", #74
            "https://drive.google.com/uc?export=view&id=1nRmQNMzNUrBjen1uTByIeKIvhqmELfrv", #75
            "https://drive.google.com/uc?export=view&id=1-dR9yJr6kxZ5e-tUzQPLZDcoPazV5W_c", #76
            "https://drive.google.com/uc?export=view&id=1-V3XCObKO7vVPxoB01JD-yV6ZjLWEJI-", #77
            "https://drive.google.com/uc?export=view&id=1eVS3dIe6lqkpvCIbGfd75O8MXs4eiVUy", #78
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #79
            "https://drive.google.com/uc?export=view&id=1PJrsk01mseJKSSDVQ0L41J3asAulWx5A", #80
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #81
            "https://drive.google.com/uc?export=view&id=1XdsdJdEisylUKmV8sQL5m6exb13duDeT", #82
            "https://drive.google.com/uc?export=view&id=1ACDIoTt6OKzKHFLqB73Dnv9LJPG8XBku", #83
            "https://drive.google.com/uc?export=view&id=1jT2s8_I9aLZMOamfrHo3Uox7PIRlxdNM", #84
            "https://drive.google.com/uc?export=view&id=11vRqXapx8_kck2qZyepT3h6O8CR_Mryq", #85
            "https://drive.google.com/uc?export=view&id=1meFoMMZf2ONy8su1zIT1Y-Ft8rumv1jb", #86
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Jati Mulyo",
                "hobi": "Bangun Pagi",
                "sosmed": "@yogyyy",
                "kesan": "Abang ini asik, tegas, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #66
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450031",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "TVRI",
                "hobi": "Jalan-jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "Kakak ini asik, baik, pemikirannya luas, dan publik speakingnya bagus",  
                "pesan":"Semangat terus kak kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #67
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Way Kandis",
                "hobi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakak ini asik, baik, dan ramah",  
                "pesan":"Semangat terus kak kuliahnya, semoga semua nilai matkulnya diatas B" #68
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Belwis",
                "hobi": "Main Game",
                "sosmed": "@",
                "kesan": "Abang ini asik, baik, dan sepertinya seru diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya" #69
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobi": "Dengerin musik",
                "sosmed": "@deaarsn",
                "kesan": "Kakak ini asik, baik, ramah, dan murah senyum",  
                "pesan":"Semangat terus kak kuliahnya" #70
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450005",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Kirim BC-an",
                "sosmed": "@esteriars",
                "kesan": "Kakak ini asik, baik, ramah, dan murah senyum",  
                "pesan":"Semangat terus kak kuliahnya" #71
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450",
                "umur": "20",
                "asal":"Saburai",
                "alamat": "Belwis",
                "hobi": "Olahraga",
                "sosmed": "Tidur",
                "kesan": "Kakak ini asik, baik, ramah, dan murah senyum",  
                "pesan":"Semangat terus kakak kuliahnya" #72
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobi": "Jadi Humas",
                "sosmed": "@natee__15",
                "kesan": "Kakak ini asik, baik, ramah, dan murah senyum",  
                "pesan":"Semangat terus Kakak kuliahnya" #73
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobi": "Pulang malam",
                "sosmed": "@jasminednva",
                "kesan": "Kakak ini asik, ramah, dan murah senyum",  
                "pesan":"Semangat terus kakak kuliahnya" #74
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobi": "Berkebun",
                "sosmed": "@tobiassiagian",
                "kesan": "Abang ini asik, baik, santai tapi tegas, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga setiap hasil ujiannya memuaskan" #75
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Menimba ilmu",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak ini asik, baik, murah senyum, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus kak kuliahnya, semoga setiap hasil ujiannya memuaskan" #76
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": " ",
                "kesan": "Abang ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #77
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "121450143",
                "umur": "21",
                "asal":"Lubuk Linggau, Sumatera Selatan",
                "alamat": "Jl. Nangka 4",
                "hobi": "Olahraga",
                "sosmed": "@rafadhlillahh13",
                "kesan": "Abang ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #78
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal":"Muara enim",
                "alamat": "Korpri",
                "hobi": "Nyuci baju",
                "sosmed": "@-",
                "kesan": "Kakak ini asik, baik dan murah senyum",  
                "pesan":"Semangat terus kak kuliahnya" #80
            },
            {
                "nama": "Chalifia Wananda",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": " ",
                "kesan": "Abang ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #81
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobi": " ",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abang ini asik, baik, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya" #82
            },
            {
                "nama": "Izza Lutfia",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": " ",
                "kesan": "Abang ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #83
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "daplok kelompok 1",
                "sosmed": "@alyaavanefi",
                "kesan": "Kakak ini cantik, asik, baik, murah senyum, best lah",  
                "pesan":"Semangat terus kak kuliahnya, semoga hasil selalu bagus setiap ujian dengan matkul apapun itu" #84
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": " ",
                "kesan": " ",  
                "pesan":"Semangat terus kak kuliahnya" #85
            },
            {
                "nama": "Tria Yunanni",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": " ",
                "kesan": " ",  
                "pesan":"Semangat terus kak kuliahnya" #86
            },
         ]
        display_images_with_data(gambar_urls, data_list)
    departemeneksternal()
elif menu == "Departemen Internal":
    def departemeninternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LI3ZocH98THXhGmqbR4iqQPXWyW5SDGi", #87
            "https://drive.google.com/uc?export=view&id=1L0e_u5XLlZXhHdP3USwyxCPeNFuenh8X", #88
            "https://drive.google.com/uc?export=view&id=1LEWNSz4s-o9IKXw8BMbu6RnAVkEwsemF", #89
            "https://drive.google.com/uc?export=view&id=1LFxEKftMRjFR-GisxlSWqZKd8jiALjAr", #90
            "https://drive.google.com/uc?export=view&id=1LFxEKftMRjFR-GisxlSWqZKd8jiALjAr", #91
            "https://drive.google.com/uc?export=view&id=1nrs4kPPxWNyrYyrPvfFMPTwsO_Jt4ZuF", #92
            "https://drive.google.com/uc?export=view&id=1L5srgbiAa37elW4AIr6cU-BP2RjFHNMY", #93
            "https://drive.google.com/uc?export=view&id=1nrs4kPPxWNyrYyrPvfFMPTwsO_Jt4ZuF", #94
            "https://drive.google.com/uc?export=view&id=1nrs4kPPxWNyrYyrPvfFMPTwsO_Jt4ZuF", #95
            "https://drive.google.com/uc?export=view&id=1nrs4kPPxWNyrYyrPvfFMPTwsO_Jt4ZuF", #96
            "https://drive.google.com/uc?export=view&id=1nrs4kPPxWNyrYyrPvfFMPTwsO_Jt4ZuF", #97
            "https://drive.google.com/uc?export=view&id=1nrs4kPPxWNyrYyrPvfFMPTwsO_Jt4ZuF", #98
            "https://drive.google.com/uc?export=view&id=1L3muJthZh0tlVIaS8_hte2POMHeDGc9E", #99
            "https://drive.google.com/uc?export=view&id=1nrs4kPPxWNyrYyrPvfFMPTwsO_Jt4ZuF", #100

        ]
        data_list = [
            {
                "nama": "Dimas Rizky Ramadhani",
                "nim": "121450027",
                "umur": "20",
                "asal":"Pamulang, Tangerang Selatan",
                "alamat": "Way Kandis Kobam",
                "hobi": "Manjat tower sutet",
                "sosmed": "@dimzrky",
                "kesan": "Abang ini asik, tegas, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #87
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca novel",
                "sosmed": "@Catherine.sinaga",
                "kesan": "Kakak ini asik, tegas, baik, dan ramah",  
                "pesan":"Semangat terus kak kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #88
            },
            {
                "nama": "Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Labuhan Dalam",
                "hobi": "Memelihara Dino",
                "sosmed": "@akbar_resdika",
                "kesan": "Abang ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #89
            },
            {
                "nama": "Rani Puspita sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Kakak ini asik, baik, seru diajak diskusi",  
                "pesan":"Semangat terus kak kuliahnya" #90
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobi": "Nulis lagu",
                "sosmed": "@rendaepr",
                "kesan": "Abang ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya" #91
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawarn",
                "alamat": "Airan raya",
                "hobi": "Ngeliat cogan",
                "sosmed": "@slwfn_694",
                "kesan": "kakak ini asik, tegas, baik, dan lucu",  
                "pesan":"Semangat terus kak kuliahnya" #92
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450",
                "umur": "23",
                "asal":"Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobi": "Main Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "Abang ini asik, tegas, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #93
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Jati Mulyo",
                "hobi": "Bangun Pagi",
                "sosmed": "@azizahksmh15",
                "kesan": "Kakak ini asik, baik dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus kak kuliahnya" #94
            },
            {
                "nama": "Dearni Monica Br Manik",
                "nim": "121450",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Jati Mulyo",
                "hobi": "Bangun Pagi",
                "sosmed": "@yogyyy",
                "kesan": "Abang ini asik, tegas, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #95
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan Raya",
                "hobi": "Menghalu",
                "sosmed": "@meiraln",
                "kesan": "Kakak ini asik baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus kakak kuliahnya" #96
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Gunawan",
                "hobi": "menyanyi",
                "sosmed": "@alexanderr",
                "kesan": "Abang ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya" #97
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450112",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakak ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus kakak kuliahnya" #98
            },
            {
                "nama": "Yosia Letare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal":"Dairi, Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobi": "Bawa motor pake kaki",
                "sosmed": "@yosiabanurea",
                "kesan": "Abang ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya" #99
            },
            {
                "nama": "Josua Panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal":"Pematang Siantar",
                "alamat": "Bia Kost",
                "hobi": "Ngawinin cupang",
                "sosmed": "josuapanggabean16_",
                "kesan": "Abang ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus abang kuliahnya" #100
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemeninternal()

elif menu == "Departemen SSD":
    def departemenssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LLFd89uDrv1_SLRa4Uy6--BYUl69dLD6", #101
            "https://drive.google.com/uc?export=view&id=1M9iv_EdaVlTZgkWOy-a1pyAdhwgVAoj8", #102
            "https://drive.google.com/uc?export=view&id=1LOKsxB8wsNs2Sz-LJWH3VVJyvkzLK7e8", #103
            "https://drive.google.com/uc?export=view&id=1MGmN0PE-SMJ3orlW-LvhSkhM4iPUlV_6", #104
            "https://drive.google.com/uc?export=view&id=1MG_FvyBKzpE2_w5NKgRpwF52BGFfmQax", #105
            "https://drive.google.com/uc?export=view&id=1MFWYqJEtJMVD0syHCzLqhSWSV2cglr-L", #106
            "https://drive.google.com/uc?export=view&id=1LSAeq5OnSoWGnYkmzKTHkqnTF3aPa3cN", #107
            "https://drive.google.com/uc?export=view&id=1KxqmaVgtTq6W3esjMXHPXM6uD9Nn_pzt", #108
            "https://drive.google.com/uc?export=view&id=1LNgXR_ZaGsrpqAjhkTWFvv7_VgAKeWDx", #109
            "https://drive.google.com/uc?export=view&id=1M9Q1fubQeJFDTaJFXzmrB8TW7PhzwKec", #110
            "https://drive.google.com/uc?export=view&id=1LR7-xkfwfU6yMSjWLXJ5accDWuRqTh1K", #111

        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "21",
                "asal":"Panjibako",
                "alamat": "Jl. Bel",
                "hobi": "Mencari Uang",
                "sosmed": "@andriangaol",
                "kesan": "Abang ini asik, tegas, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #101
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Kakak ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus Kakak kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #102
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal":"Simalungun, Sumut",
                "alamat": "Airan",
                "hobi": "Hitung uang",
                "sosmed": "@zhjung_",
                "kesan": "Kakak ini asik, tegas, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus kak kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #103
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Bukittinggi",
                "alamat": "Airan",
                "hobi": "Badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "Abang ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya" #104
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Airan",
                "hobi": "Nyuruh-nyuruh",
                "sosmed": "@dananghk_",
                "kesan": "Abang ini asik, tegas, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga hasil ujian selalu memuaskan" #105
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Lapas",
                "hobi": "Apa aja",
                "sosmed": "@farrel_julio",
                "kesan": "Abang ini asik, tegas, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya" #106
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Simalungun, Sumut",
                "alamat": "Pemda",
                "hobi": "Suka nulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakak ini asik, baik, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus kak kuliahnya" #107
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal":"Kedaton",
                "alamat": "Kedaton",
                "hobi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Kakak ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus kak kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #108
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobi": "Nonton windah",
                "sosmed": "@alviagnting",
                "kesan": "Kakak ini asik, baik, ramah dan lucu",  
                "pesan":"Semangat terus kak kuliahnya" #109
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Balam",
                "alamat": "Jalan Nangka 1",
                "hobi": "Tidur",
                "sosmed": "@dhafinrzqa",
                "kesan": "Abang ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya" #110
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobi": "Badminton",
                "sosmed": "@meylanielia",
                "kesan": "Kakak ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus kakak kuliahnya" #111
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenssd()
            
elif menu == "Departemen MEDKRAF":
    def departemenmedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1j-ZW3r6GGZ8v_I8N3u-0b77yWsVEngwO", #112
            "https://drive.google.com/uc?export=view&id=1p5zhW6HRQ5OliBouY_faF--f5opY00pZ", #113
            "https://drive.google.com/uc?export=view&id=1NIQeGsF_Fg7P9qkNWGCklduWg_uxevw7", #114
            "https://drive.google.com/uc?export=view&id=1m7Ore9EuJeOOrAFzzMLMw_KdLxJzmmwa", #115
            "https://drive.google.com/uc?export=view&id=1ZF1u9MiZ9EkxC5TAJUwmljtGjJ13d8-h", #116
            "https://drive.google.com/uc?export=view&id=147wXRTDkbcFdA_1letGHeId6SdWeyt2-", #117
            "https://drive.google.com/uc?export=view&id=1VzWkCJwc-Eb7AzxZg4Rnr1wRG9pmCzLd", #118
            "https://drive.google.com/uc?export=view&id=1ccjIKUwjRnT8VapsjmhMANP2vCOdKGKT", #119
            "https://drive.google.com/uc?export=view&id=18dbfOng-l1WzJevXltk5-BrcNs2e7T_Q", #120
            "https://drive.google.com/uc?export=view&id=1rNe6b67oCITao-wRccVGO00Zi7RCI9xd", #121
            "https://drive.google.com/uc?export=view&id=1ERh64oI6xmA585KlApAF8NIm8-xluzX8", #122
            "https://drive.google.com/uc?export=view&id=1EvELtYHdDYI92ObxPNGCxQNJ4XXJBLAq", #123
            "https://drive.google.com/uc?export=view&id=11CttWtQ1U2-00HiVuUnOfBsQb9bW6XK6", #124
            "https://drive.google.com/uc?export=view&id=1eW7vkNuwQVw8VxHvyPsYfzqQAfn_QibZ", #125
            "https://drive.google.com/uc?export=view&id=1crW4P6_rwapuHzK12Ruq0AemiYqp4Maq", #126
            "https://drive.google.com/uc?export=view&id=1A7r4N-O1ez97uc7lM6oCH5Ega6Wsstsf", #127
            "https://drive.google.com/uc?export=view&id=1zUeL3RmH6NMVC33MStWjWo_h-S5WVmey", #128
            "https://drive.google.com/uc?export=view&id=1oyO8gJMkhAjFdWnRrj9FDepVIazLaCo5", #129
            "https://drive.google.com/uc?export=view&id=1uP66-dno3LXLkwR0i12Qc6Db5-d7nZFq", #130
            
        ]
        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal":"Makassar, Sulawesi Selatan",
                "alamat": "Sukarame",
                "hobi": "Nonton",
                "sosmed": "@",
                "kesan": "Abang ini tegas, baik, sepertiya juga disiplin, serta seru untuk diajak diskusi",  
                "pesan":"Semangat bang semoga bisa cepat lulus, dan mendapatkan pekerjaan yang bagus, sesuai kemampuan dan minat abang" #112
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "Kakak ini cantik, asik, baik, murah senyum, dan sekit tegas, asik juga diajak diskusi ataupun ngobrol biasa",  
                "pesan":"Semangat kak kuliahnya, jangan lupa senyum, semoga setiap nilai yang keluar dari ujian matkul apapun itu, hasilnya memuaskan" #113
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobi": " Nugas",
                "sosmed": "@arsyiah._",
                "kesan": "Kakak ini friendly, cutie, asik diajak ngobrol, dan baik tentunya",  
                "pesan":"Semoga cepat lulus dengan hasil bagus serta mendapatkan pekerjaan yang kakak impikan kak" #114
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Cantik, baik, friendly, lucu, seru diajak ngobrol dan diskusi",  
                "pesan":"Semangat kak kuliahnya, semoga selalu mendapatkan hasil yang bagus, dan juga jangan lupa senyum" #115
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": "122450045",
                "umur": "20",
                "asal":"Natar",
                "alamat": "Natar",
                "hobi": "Menyibukkan diri",
                "sosmed": "@ekafdyaptri",
                "kesan": " ",  
                "pesan":" " #116
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Nulis, baca, fangirling",
                "sosmed": "@nanana.minjoo",
                "kesan": " ",  
                "pesan":" " #117
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobi": "Nonton film",
                "sosmed": "@patriciadiajeng",
                "kesan": "Cantik, positive vibes, baik, seru diajak ngobrol, dan ramah juga, serta murah senyum",  
                "pesan":"Semangat kak kuliahnya, jangan lupa senyum, bahagia selalu, dan mendapatkan nilai yang bagus untuk matkul apapun itu" #118
            },
            {
                "nama": "Rahma Neliyana",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": " ",
                "kesan": " ",  
                "pesan":" " #119
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobi": "Bernyanyi dan menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": " ",  
                "pesan":" " #120
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar",
                "hobi": "Lagi Nyari",
                "sosmed": "@dino_kiper",
                "kesan": "Abang ini lucu, suka bercanda, baik, seru diajak ngobrol juga ",  
                "pesan":"Semangat bang terus bang kuliahnya, semoga bisa cepat lulus, sehat selalu, dan mendapatkan pekerjaan sesuai yang abang mau" #121
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": " ",
                "kesan": " ",  
                "pesan":" " #122
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": " ",
                "kesan": " ",  
                "pesan":" " #123
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": " ",
                "kesan": " ",  
                "pesan":" " #124
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": " ",
                "kesan": " ",  
                "pesan":" " #125
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobi": "-",
                "sosmed": "@arsal.utama",
                "kesan": " ",  
                "pesan":" " #126
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Belwis",
                "hobi": "Mengerjakan tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "positive vibes, baik, ramah, dan friendly ",  
                "pesan":"semangat kak kuliahnya, kurangi ngeluh, dan semoga hasil nilai yang didapat selalu memuaskan " #127
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa Labuhan dalam",
                "hobi": "Ngoding, gaming",
                "sosmed": "@anitahmad",
                "kesan": "Abang ini asik, lucu, baik, friendly, pintar juga",  
                "pesan":"Semangat terus bang kuliahnya, semoga ga pernah ngulang lagi bang" #128
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "121450090",
                "umur": "21",
                "asal":"Panjibako",
                "alamat": "Jl. Bel",
                "hobi": "Mencari Uang",
                "sosmed": "@andriangaol",
                "kesan": "Abang ini asik, tegas, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #129
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Wisma Hana Hani",
                "hobi": "Bengong/ Membaca buku",
                "sosmed": "linkedin",
                "kesan": "Abang ini asik, tegas, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #130
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenmedkraf()
