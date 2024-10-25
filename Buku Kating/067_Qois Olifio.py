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
                "kesan": "Abannyag asik dan humoris juga",  
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
                "kesan": "Kakak ini baik dan cantik ",  
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
                "kesan": "Kakak yang selalu keliatan sabar dan perhatian.",  
                "pesan": "Jaga kesehatan dan semangat terus ya, Kak! S"#5
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Kotabaru",
                "hobi": "Dengerin  bang Pandra Gitaran",
                "sosmed": "@nadillaadr26",
                "kesan": "Pengertian, selalu memberikan masukan yang bermanfaat.",  
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
                "kesan": "Kakak ini asik diajak tukar pikiran, selalu ada solusi buat setiap masalah.",  
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
                "kesan": "Sikap positif kakaknya bikin suasana jadi lebih santai.",  
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
                "kesan": "Sangat suportif dan selalu memberi motivasi.",  
                "pesan": "Sukses selalu untuk kuliahnya kak!"#10
            },{
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal": "Bernung, Pesawaran",
                "alamat": "Bandar Lampung",
                "hobi": "Nonton Drakor",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak ini asik banget.",  
                "pesan": "Semangat terus kuliahnya kakak!"#11
            },{
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Punya energi positif tersendiri nih",  
                "pesan": "Semoga abang selalu diberi kelancaran dalam segala urusan."#12
            },{
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobi": "Baca Al-qur'an",
                "sosmed": "@fleurnsh",
                "kesan": "Ramah dan mudah diajak ngobrol",  
                "pesan": "Semangat terus, Kak!"#13
            },{
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak punya sikap yang menyenangkan hehe.",  
                "pesan": "Semoga sukses di setiap langkah ke depannya, Kak. Teruslah bersinar!"#14
            },{
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Kakak yang selalu ceria dan bisa bikin orang lain moodnya naik juga nih.",  
                "pesan": "Jaga kesehatan dan semoga selalu diberi kemudahan ya Kak!"#15
            },{
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal": "Ogan Ilir",
                "alamat": "Natar",
                "hobi": "Nyari Sinyal di Gedung F",
                "sosmed": "@_.dheamelia",
                "kesan": "Mudah bergaul dan selalu membawa suasana jadi nyaman.",  
                "pesan": "Sukses selalu kakak!"#16
            },{
                "nama": "Muhammad Fahrul Aditya",
                "nim": "122450000",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini selalu bisa diandalkan, baik dalam situasi santai maupun serius.",  
                "pesan": "Sukses terus dan semangat mengejar impiannya kak!"#17
            },{
                "nama": "Berliana enda putri",
                "nim": "122450000",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini sosok yang humble dan asik diajak bicara.",  
                "pesan": "Semoga kakak selalu diberkahi kemudahan dalam segala urusan!"#18
            },{
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Billabong, Gedong Air",
                "hobi": "Suka Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "Kakak selalu membawa aura positif dan humoris juga.",  
                "pesan": "Semoga kakak selalu diberi kemudahan dalam segala urusan!"#19
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
                "kesan": "Kakak nya asik dan energik banget nih",
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
                "kesan": "Abang kece nih, berwawasan luas juga",
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
            "https://drive.google.com/uc?export=view&id=1rRJpH9kuNkkHQsqESKnX6dyFplhS6sV8", #3
            "https://drive.google.com/uc?export=view&id=1U302rWUidBFkVzfpK8pMg8X4R1UqcSBE", #4
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #5
            "https://drive.google.com/uc?export=view&id=1ZmruFmfbHOGYcmH9jznEVtcxF_wg5Tpj", #6
            "https://drive.google.com/uc?export=view&id=1G3xJVu2wJeJ4H5H5QZrFQiZDmkbRf-ap", #7
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #8
            "https://drive.google.com/uc?export=view&id=1eYDO8MDQwS_a83X16dCnp-yBp54EPEM6", #9
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #10
            "https://drive.google.com/uc?export=view&id=1yle1sDxb2R2C80c4Z8P6Lfg5vs_0ljEG", #11
            "https://drive.google.com/uc?export=view&id=1UwNzmROJ-GBuOE9vLbLVojhEVoOOv5D9", #12
            "https://drive.google.com/uc?export=view&id=1Mt-kTBzHQxM1gURybSGMmFQem6irX82g", #13
            "https://drive.google.com/uc?export=view&id=1fYXgJ4MDdZW0WQdRleylAwK6WTqK7IMN", #14
            "https://drive.google.com/uc?export=view&id=1C3OUxrpinWvyflFHfTSs9b5XQTONGlTa", #15
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #16
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #17
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #18
            "https://drive.google.com/uc?export=view&id=1LF2dXA4lHzjxq6skRaMkKHbLxLCNt6-j", #19
            
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
                "kesan": "Abang ini asik sekali, punya pemikiran yang luas, public speakingnya bagus, tegas, dan seru untuk diajak diskusi tentang apapun",  
                "pesan":"Semangat terus kuliahnya bang, semoga bisa cepat lulus dengan hasil yang memuaskan" #22
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
                "sosmed": "@celisabeth",
                "kesan": "Kakak ini asik, dan murah senyum",  
                "pesan":"Semangat terus kak, jangan lupa tersenyum" #23
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Marahin orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak ini asik, friendly dan mempunyai pikiran serta public speaking yang bagus",  
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
                "kesan": "Kakak ini asik, dan murah senyum",  
                "pesan":"Semangat terus kak kuliahnya, semoga hasil yang didapat sesuai dengan kemauan kakak" #25
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiyati",
                "nim": "122450001",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Metro",
                "hobi": "Nyopet",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak, jangan lupa untuk tersenyum" #26
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobi": "Bengong",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini murah senyum, baik, dan seru untuk diajak ngobrol ataupun diskusi",  
                "pesan":"Semangat kuliahnya kakak" #27
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Jalan Pangeran Senopati Raya 18",
                "hobi": "Baca Kitab Suci",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abang ini asik, baik, dan murah senyum, seru diajak ngobrol",  
                "pesan":"Semangat terus bang kuliahnya, semoga hasil yang didapat bagus" #28
            },
            {
                "nama":  "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jalan Pagar Alam Kedaton",
                "hobi": "Ngukur jalan",
                "sosmed": "@dransyh_",
                "kesan": "Abang ini asik, baik, dan murah senyum, seru diajak ngobrol",  
                "pesan":"Semangat terus bang" #29
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Travelling",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakak ini asik, baik, dan murah senyum",  
                "pesan":"Semangat terus kuliahnya kak" #30
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "1214500148",
                "umur": "21",
                "asal":"Duri, Riau",
                "alamat": "Pulau Damar Kobam",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abang ini asik, baik, ramah, friendly, dan suka ngelawak, seru diajak ngobrol",  
                "pesan":"Semangat terus bang kuliahnya, semoga cepat lulus dan mendapatkan pekerjaan sesuai dengan apa yang diinginkang bang" #31
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobi": "Membaca",
                "sosmed": "@syalaisha.i_",
                "kesan": "Kakak ini asik, baik dan ramah",  
                "pesan":"Semangat terus kak kuliahnya" #32
            },
            {
                "nama": " Ibnu Farhan Al-Ghifari",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@-",
                "kesan": "Abang ini asik",  
                "pesan":"Semangat terus bang" #33
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobi": "Asprak",
                "sosmed": "@johanneskrsjnnn",
                "kesan": "Abang ini tegas, asik, murah senyum, dan friendly",  
                "pesan":"Semangat terus bang kuliahnya" #34
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Golf Asri",
                "hobi": "Ngetik print hello dunia",
                "sosmed": "@kemasverii",
                "kesan": "Abang ini pinter, suhunya codingan, baik, asik juga, seru diajak ngobrol dan diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga apa yang di cita-citakan bisa terwujud" #35
            },
            {
                "nama": "Leonard Andreas Napitupulu",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@-",
                "kesan": "Abang ini tegas, asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus bang" #36
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobi": "Dengerin The Adams",
                "sosmed": "@presilliamg",
                "kesan": "Kakak ini asik, baik, dan murah senyum",  
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
                "kesan": "Kakak ini asik, mempunyai pikiran serta public speaking yang bagus, dan murah senyum",  
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
                "kesan": "Abang ini asik, mempunyai pikiran serta public speaking yang bagus, dan cocok diajak diskusi",  
                "pesan":"Semangat terus bang" #39
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Perum Korpri",
                "hobi": "Minum kopi, belajar, bikin Deyvan senang",
                "sosmed": "@roselivness__",
                "kesan": "Kakak ini tegas, asik, mempunyai pikiran serta public speaking yang bagus, serta murah senyum",  
                "pesan":"Semangat terus kuliahnya kak" #40
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Abang ini, asik, orangnya santai, friendly, suka menolong dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa cepat lulus dengan hasil yang memuaskan" #41
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "Abang ini asik, baik, dan ramah",  
                "pesan":"Semangat terus bang kuliahnya semoga cepat lulus dengan nilai yang bagus" #42
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #43
            },
            {
                "nama":  "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Abang ini asik, baik, dan ramah",  
                "pesan":"Semangat terus bang kuliahnya" #44
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenpsda()
    
elif menu == "Departemen MIKFES":
    def departemen_mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LPWD-gDJpIV_wn3_-gpvlFbwocQ1cPOH", #45
            "https://drive.google.com/uc?export=view&id=1TWpkXvYOFkIFg4d4HqvK-IXC059wWBlf", #46
            "https://drive.google.com/uc?export=view&id=1yyIb4HueVQljI_EYzDmwOgFSiP8B_VSR", #47
            "https://drive.google.com/uc?export=view&id=1MC6kdaqg2Nlb6V0-H6SAermZ8pAa_bNL", #48
            "https://drive.google.com/uc?export=view&id=1nrs4kPPxWNyrYyrPvfFMPTwsO_Jt4ZuF", #49
            "https://drive.google.com/uc?export=view&id=1u3ObS1xNusM40hJenMg1z7Dd6gwPi7iT", #50
            "https://drive.google.com/uc?export=view&id=1uPqY_7qlxg0J-D5nSgabEQ70-_Ko2Qck", #51
            "https://drive.google.com/uc?export=view&id=1nrs4kPPxWNyrYyrPvfFMPTwsO_Jt4ZuF", #52
            "https://drive.google.com/uc?export=view&id=14wRDE4igCAEn46UsW8HxdBqp6iCNRZGK", #53
            "https://drive.google.com/uc?export=view&id=1SLQH-VW9FNWP29o0nVVRnkyUYRKLq56H", #54
            "https://drive.google.com/uc?export=view&id=1fbpkSmskM4wgfCcnztr9KHNi4e3i6oNS", #55
            "https://drive.google.com/uc?export=view&id=1uYGw5mc6Bb3nvAj3tNCxMCIuHbskXcVm", #56
            "https://drive.google.com/uc?export=view&id=1xsAwn3ZngdXr-cjQfSOIb50HeoaNHEg0", #57
            "https://drive.google.com/uc?export=view&id=1dzCL700jm3frrMLHeiuRVHGqg3UVinXM", #58
            "https://drive.google.com/uc?export=view&id=1nrs4kPPxWNyrYyrPvfFMPTwsO_Jt4ZuF", #59
            "https://drive.google.com/uc?export=view&id=1VFnk7hatyzE7LQEKnkaDyH-X-1ldq4A_", #60
            "https://drive.google.com/uc?export=view&id=1N5Quim5BZzCJ37WQnKxVjuCtMogpCyFh", #61
            "https://drive.google.com/uc?export=view&id=1mVPv4BFpoiFYlmPStnc9nY1Ild96ccZr", #62
            "https://drive.google.com/uc?export=view&id=1nrs4kPPxWNyrYyrPvfFMPTwsO_Jt4ZuF", #63
            "https://drive.google.com/uc?export=view&id=1bdBEZVaGVFImxosV17agg-rIx7ZkGKdb", #64
            "https://drive.google.com/uc?export=view&id=1nrs4kPPxWNyrYyrPvfFMPTwsO_Jt4ZuF", #65
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
                "kesan": "Abang ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #45
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "19",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Sebesi",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak kuliahnya, semoga setelah lulus nanti bisa mendapatkan pekerjaan sesuai dengan yang kakak mau" #46
            },
            {
                "nama": "Mujadid Choirus Surya",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": " ",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #47
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "19",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobi": "Olahraga",
                "sosmed": "@",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #48
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": " ",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #49
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl. Permadi",
                "hobi": "Ngasprak ADS",
                "sosmed": "@",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #50
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Gg. Yudistira",
                "hobi": "Review jurnal Bu Mika",
                "sosmed": "@",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
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
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #52
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "19",
                "asal":"Bukittinggi",
                "alamat": "Korpri",
                "hobi": "ML (Machine Learning)",
                "sosmed": "@",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #53
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobi": "Resume Webinar",
                "sosmed": "@",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #54
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobi": "Membaca jurnal Bu Mika",
                "sosmed": "@dindanababan",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #55
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
            "https://drive.google.com/uc?export=view&id=1bPLIPW1A5KkyEmXsLsoU8os_uGKiVvRY", #66
            "https://drive.google.com/uc?export=view&id=10acMfFkqrpUvYlYRf5cnDyvlFL6HqzDa", #67
            "https://drive.google.com/uc?export=view&id=1nkBWzEDdFTh2pySvmLUeE-DhLnHDrXeF", #68
            "https://drive.google.com/uc?export=view&id=1666oWCFY0ZVObrEvIldvX99Mjv-GkQBk", #69
            "https://drive.google.com/uc?export=view&id=1i5MIiPXwvTcanmp4vWOxFn3WXeMBqNPx", #70
            "https://drive.google.com/uc?export=view&id=1pFyetHn-y6l0B2tF0jNDtabrS7nzhhDI", #71
            "https://drive.google.com/uc?export=view&id=1-zK-h9nDknOjmUjxUY9EEOzme3JJYQNh", #72
            "https://drive.google.com/uc?export=view&id=1rtFVxvMVu5tPo4i2iHbragC-_gl6anYW", #73
            "https://drive.google.com/uc?export=view&id=1nrs4kPPxWNyrYyrPvfFMPTwsO_Jt4ZuF", #74
            "https://drive.google.com/uc?export=view&id=1I25ugGkPs-fLLJJa7GLi7zvvEVWRjNR0", #75
            "https://drive.google.com/uc?export=view&id=1hh-XuS2CU8uc06vnnClK2mYWKyFCrnla", #76
            "https://drive.google.com/uc?export=view&id=1-V3XCObKO7vVPxoB01JD-yV6ZjLWEJI-", #77
            "https://drive.google.com/uc?export=view&id=1nrs4kPPxWNyrYyrPvfFMPTwsO_Jt4ZuF", #78
            "https://drive.google.com/uc?export=view&id=1nrs4kPPxWNyrYyrPvfFMPTwsO_Jt4ZuF", #79
            "https://drive.google.com/uc?export=view&id=1FdojfegX55UIuyt5zdX3ITjXQKu0vblE", #80
            "https://drive.google.com/uc?export=view&id=1SwDQXl-3z1zDJkWeZREk317kinfUyYP_", #81
            "https://drive.google.com/uc?export=view&id=11qSDYGatUP0hoqya_7rL_pYpNzqagByd", #82
            "https://drive.google.com/uc?export=view&id=1CsPUtsQ9qtbQhXWv-opOEXFg4RL1AL8E", #83
            "https://drive.google.com/uc?export=view&id=1yVnVDuZjUpcQPUrtHXwbxIDb27FvfktU", #84
            "https://drive.google.com/uc?export=view&id=1n_7XlLMpIja_uOWQ-cWsulrM8XFlbTD8", #85
            "https://drive.google.com/uc?export=view&id=17bnsy9xoP5mVo4z8gdbGLdhhMykTTN-t", #86
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
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Way huwi",
                "hobi": "Imam TVRI",
                "sosmed": "@-",
                "kesan": "Abang ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya" #79
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
