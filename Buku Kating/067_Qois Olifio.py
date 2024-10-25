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
                "hobbi": "Dengerin bang Bintang nyanyi",
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
                "hobbi": "Menyanyi",
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
        "asal": "Bekasi",
        "alamat": "Khobam",
        "hobbi": "Travelling",
        "sosmed": "@ericsonchandra99",
        "kesan": "(Sesuaikan dengan kalian)",
        "pesan": "(Sesuaikan dengan kalian)",
        "jabatan": "Kepala Departemen PSDA"
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
        "pesan": "(Sesuaikan dengan kalian)",
        "jabatan": "Sekretaris Departemen PSDA"
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
        "pesan": "(Sesuaikan dengan kalian)",
        "jabatan": "Kepala Divisi Manajemen Minat dan Bakat"
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
        "pesan": "(Sesuaikan dengan kalian)",
        "jabatan": "Kepala Divisi Kaderisasi"
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
        "pesan": "(Sesuaikan dengan kalian)",
        "jabatan": "Kepala Divisi Olahraga dan Perlombaan"
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
        "pesan": "(Sesuaikan dengan kalian)",
        "jabatan": "Staff Divisi Manajemen Minat dan Bakat"
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
        "pesan": "",
        "jabatan": "Staff Divisi Manajemen Minat dan Bakat"
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
        "pesan": "",
        "jabatan": "Bendahara Divisi Manajemen Minat dan Bakat"
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
        "pesan": "",
        "jabatan": "Staff Divisi Manajemen Minat dan Bakat"
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
        "pesan": "",
        "jabatan": "Staff Divisi Manajemen Minat dan Bakat"
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
        "pesan": "",
        "jabatan": "Staff Divisi Manajemen Minat dan Bakat"
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
        "pesan": "",
        "jabatan": "Staff Divisi Kaderisasi"
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
        "pesan": "",
        "jabatan": "Staff Divisi Kaderisasi"
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
        "pesan": "",
        "jabatan": "Staff Divisi Kaderisasi"
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
        "pesan": "",
        "jabatan": "Staff Divisi Kaderisasi"
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
        "pesan": "",
        "jabatan": "Staff Olahraga dan Perlombaan"
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
        "pesan": "",
        "jabatan": "Staff Olahraga dan Perlombaan"
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
        "pesan": "",
        "jabatan": "Staff Olahraga dan Perlombaan"
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
        "pesan": "",
        "jabatan": "Staff Olahraga dan Perlombaan"
    }
]
        display_images_with_data(gambar_urls, data_list)
    departemenpsda()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen MIKFES":
    def departemenmikfes():
        gambar_urls = [
              "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #1
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #2
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #3
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #4
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #5
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #6
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #7
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #8
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #9
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #10
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #11
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #12
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #13
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #14
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #15
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #16
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #17
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #18
        ]
        data_list = [
    {
        "Nama": "Rafi Fadhlillah",
        "NIM": "121450143",
        "Umur": 21,
        "Asal": "Lubuk Linggau",
        "Alamat Sekarang": "Jl. Nangka 4",
        "Hobi": "Olahraga",
        "Sosial Media": "@rafadhilillahh13",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Kepala Departement"
    },
    {
        "Nama": "Annisa Novantika",
        "NIM": "121450005",
        "Umur": 21,
        "Asal": "Lampung Utara",
        "Alamat Sekarang": "Jl. Pulau Sebesi, Sukarame",
        "Hobi": "Memasak",
        "Sosial Media": "@anovavona",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Sekretaris Departement"
    },
    {
        "Nama": "Ahmad Sahidin Akbar",
        "NIM": "122450044",
        "Umur": 20,
        "Asal": "Tulang Bawang",
        "Alamat Sekarang": "Sukarame",
        "Hobi": "Olahraga",
        "Sosial Media": "@sahid22__",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Club dan Komunitas"
    },
    {
        "Nama": "Fadhil Fitra Wijaya",
        "NIM": "122450082",
        "Umur": 20,
        "Asal": "Bekasi",
        "Alamat Sekarang": "Teluk Betung",
        "Hobi": "Main Game",
        "Sosial Media": "@fadhilfwee",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Club dan Komunitas"
    },
    {
        "Nama": "Muhammad Regi Abdi Putra Amanta",
        "NIM": "122450031",
        "Umur": 19,
        "Asal": "Palembang",
        "Alamat Sekarang": "Jl. Permadi Sukarame",
        "Hobi": "Jadi admin ig mikfes.hmsd",
        "Sosial Media": "@mregiiii_",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Club dan Komuitas"
    },
    {
        "Nama": "Syalaisha Andina Putriansyah",
        "NIM": "122450121",
        "Umur": 21,
        "Asal": "Tangerang",
        "Alamat Sekarang": "Gg Yudhistira",
        "Hobi": "Baca Novel",
        "Sosial Media": "@dkselsd_31",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Club dan Komunitas"
    },
    {
        "Nama": "Natanael Oktavianus Partahan Sihombing",
        "NIM": "121450107",
        "Umur": 20,
        "Asal": "Jakarta",
        "Alamat Sekarang": "Kemiling",
        "Hobi": "Membuka Wisata HMSD",
        "Sosial Media": "@natanaeloks",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Kepala Divisi Pusat Inovasi dan Kajian Akademik"
    },
    {
        "Nama": "Anwar Muslim",
        "NIM": "122450117",
        "Umur": 21,
        "Asal": "Bukittinggi",
        "Alamat Sekarang": "Korpri",
        "Hobi": "ML (Machine Learning)",
        "Sosial Media": "@here.am.ai",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Pusat Inovasi dan Kajian Akademik"
    },
    {
        "Nama": "Deva Anjani Khayyuninafsyah",
        "NIM": "122450014",
        "Umur": 21,
        "Asal": "Bandar Lampung",
        "Alamat Sekarang": "Kemiling",
        "Hobi": "Menonton Film",
        "Sosial Media": "@anjaniiidev",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Pusat Inovasi dan Kajian Akademik"
    },
    {
        "Nama": "Dinda Nababan",
        "NIM": "122450120",
        "Umur": 20,
        "Asal": "Medan",
        "Alamat Sekarang": "Jl. Lapas",
        "Hobi": "",
        "Sosial Media": "@dindanababan_",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Pusat Inovasi dan Kajian Akademik"
    },
    {
        "Nama": "Marleta Cornelia Leander",
        "NIM": "122450092",
        "Umur": 20,
        "Asal": "Depok, Jawa Barat",
        "Alamat Sekarang": "Gg. Nangka 3",
        "Hobi": "Liatin Jurnal",
        "Sosial Media": "@marletacornelia",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Pusat Inovasi dan Kajian Akademik"
    },
    {
        "Nama": "Rut Junita Sari Siburian",
        "NIM": "122450103",
        "Umur": 20,
        "Asal": "Batam, Kep.Riau",
        "Alamat Sekarang": "Gg. Nangka 3",
        "Hobi": "Resume Jurnal",
        "Sosial Media": "@junitaa_0406",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Pusat Inovasi dan Kajian Akademik"
    },
    {
        "Nama": "Syadza Puspadari Azhar",
        "NIM": "122450072",
        "Umur": 20,
        "Asal": "Palembang",
        "Alamat Sekarang": "Belwis",
        "Hobi": "Membaca",
        "Sosial Media": "@puspadrr",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Pusat Inovasi dan Kajian Akademik"
    },
    {
        "Nama": "Abdurrahman Al-atsary",
        "NIM": "121450128",
        "Umur": 23,
        "Asal": "Bandar Lampung",
        "Alamat Sekarang": "Perumnas Way Kandis",
        "Hobi": "Membaca",
        "Sosial Media": "@rahmn_abdr",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Kepala Divisi Survei dan Riset"
    },
    {
        "Nama": "Aditya Rahman",
        "NIM": "122450113",
        "Umur": 20,
        "Asal": "Lampung Timur",
        "Alamat Sekarang": "Korpri",
        "Hobi": "Ngoding WISATA",
        "Sosial Media": "@rahm_adityaa",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Survei dan Riset"
    },
    {
        "Nama": "Eggi Satria",
        "NIM": "122450032",
        "Umur": 20,
        "Asal": "Sukabumi",
        "Alamat Sekarang": "Korpri",
        "Hobi": "Ngoding dan buat konten WISATA",
        "Sosial Media": "@egistr",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Survei dan Riset"
    },
    {
        "Nama": "Febiya Jomy Pratiwi",
        "NIM": "122450074",
        "Umur": 20,
        "Asal": "Tulang Bawang",
        "Alamat Sekarang": "Jl Kelengkeng Raya",
        "Hobi": "Nonton K-Drama",
        "Sosial Media": "@pratiwifebiya",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Survei dan Riset"
    },
    {
        "Nama": "Happy Syahrul Ramadhan",
        "NIM": "122450013",
        "Umur": 20,
        "Asal": "Lampung",
        "Alamat Sekarang": "Karang Anyar",
        "Hobi": "Main Game",
        "Sosial Media": "@sudo.syahrulramadhannn",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Survei dan Riset"
    },
    {
        "Nama": "Randa Andriana Putra",
        "NIM": "122450083",
        "Umur": 21,
        "Asal": "Banten",
        "Alamat Sekarang": "Jl Nangka 3",
        "Hobi": "Berolahraga",
        "Sosial Media": "@randardn",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Survei dan Riset"
    }
]

        display_images_with_data(gambar_urls, data_list)
    departemenmikfes()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen Eksternal":
    def departemeneksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #1
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #2
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #3
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #4
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #5
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #6
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #7
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #8
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #9
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #10
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #11
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #12
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #13
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #14
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #15
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #16
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #17
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #18
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #19
            
        ]
        data_list = [
[
    {
        "Nama": "Yogy Sae Tama",
        "NIM": "121450041",
        "Umur": 21,
        "Asal": "Tangerang",
        "Alamat Sekarang": "Jatimulyo",
        "Hobi": "BAB setiap jam 7 pagi",
        "Sosial Media": "@yogyst",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Kepala Departemen"
    },
    {
        "Nama": "Ramadhita Atifa Hendri",
        "NIM": "121450131",
        "Umur": 21,
        "Asal": "Bandar Lampung",
        "Alamat Sekarang": "Rajabasa",
        "Hobi": "Jalan - Jalan",
        "Sosial Media": "@ramadhitaatifa",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Sekretaris Departemen"
    },
    {
        "Nama": "Nazwa Nabila",
        "NIM": "121450122",
        "Umur": 21,
        "Asal": "Jakarta Selatan",
        "Alamat Sekarang": "Kochpri",
        "Hobi": "Main Golf",
        "Sosial Media": "@nazwanbilla",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Kepala Divisi Hubungan Luar"
    },
    {
        "Nama": "Bastian Heskia Silaban",
        "NIM": "122450130",
        "Umur": 21,
        "Asal": "Batam, Kep. Riau",
        "Alamat Sekarang": "Belwis",
        "Hobi": "Menggambar",
        "Sosial Media": "@bastiansilaban_",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Hubungan Luar"
    },
    {
        "Nama": "Dea Mutia Risani",
        "NIM": "122450099",
        "Umur": 20,
        "Asal": "Sumatera Barat",
        "Alamat Sekarang": "Korpri",
        "Hobi": "Berkebun",
        "Sosial Media": "@deaa.rsn",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Hubungan Luar"
    },
    {
        "Nama": "Esteria Rohanauli Sidauruk",
        "NIM": "122450025",
        "Umur": 19,
        "Asal": "Jakarta Selatan",
        "Alamat Sekarang": "Belwis",
        "Hobi": "Main golf bareng kadiv",
        "Sosial Media": "@esteriars",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Hubungan Luar"
    },
    {
        "Nama": "Natasya Ega Lina",
        "NIM": "122450024",
        "Umur": 19,
        "Asal": "Jakarta Selatan",
        "Alamat Sekarang": "Belwais",
        "Hobi": "Surfing",
        "Sosial Media": "@nateee__15",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Hubungan Luar"
    },
    {
        "Nama": "Novelia Adinda",
        "NIM": "122450104",
        "Umur": 21,
        "Asal": "Jakarta Timur",
        "Alamat Sekarang": "Belwis",
        "Hobi": "Tidur",
        "Sosial Media": "@nvliaadinda",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Hubungan Luar"
    },
    {
        "Nama": "Ratu Keisha Jasmine Deanova",
        "NIM": "122450106",
        "Umur": 20,
        "Asal": "Jakarta Selatan",
        "Alamat Sekarang": "Way Kandis",
        "Hobi": "Main sepak takraw",
        "Sosial Media": "@jasminednva",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Hubungan Luar"
    },
    {
        "Nama": "Tobias David Manogari",
        "NIM": "122450091",
        "Umur": 20,
        "Asal": "Sumatera Utara",
        "Alamat Sekarang": "Pemda",
        "Hobi": "Jogging",
        "Sosial Media": "@tobiassiagian",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Hubungan Luar"
    },
    {
        "Nama": "Yohana Manik",
        "NIM": "122450126",
        "Umur": 19,
        "Asal": "Jakarta Selatan",
        "Alamat Sekarang": "Belwais",
        "Hobi": "Main Bowling",
        "Sosial Media": "@yo_annamnk",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Hubungan Luar"
    },
    {
        "Nama": "Rizky Adrian Bennovry",
        "NIM": "121450073",
        "Umur": 21,
        "Asal": "Bekasi",
        "Alamat Sekarang": "TVRI",
        "Hobi": "Bikin portofolio",
        "Sosial Media": "@rzkdrnnn",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Kepala Divisi Pengabdian Masyarakat"
    },
    {
        "Nama": "Arafi Ramadhan Maulana",
        "NIM": "122450002",
        "Umur": 20,
        "Asal": "Bandung",
        "Alamat Sekarang": "Way Huwi",
        "Hobi": "Bertani",
        "Sosial Media": "@rafiramadhanmaulana",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Pengabdian Masyarakat"
    },
    {
        "Nama": "Asa Do’a Uyi",
        "NIM": "122450005",
        "Umur": 20,
        "Asal": "Muara Enim",
        "Alamat Sekarang": "Korpri",
        "Hobi": "Tepuk Semangat",
        "Sosial Media": "@u_yippy",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Pengabdian Masyarakat"
    },
    {
        "Nama": "Chalifia Wananda",
        "NIM": "122450076",
        "Umur": 20,
        "Asal": "Padang",
        "Alamat Sekarang": "Sukarame",
        "Hobi": "Q Time",
        "Sosial Media": "@chlfawww",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Pengabdian Masyarakat"
    },
    {
        "Nama": "Irvan Alfaritzi",
        "NIM": "122450093",
        "Umur": 21,
        "Asal": "Sumatera Barat",
        "Alamat Sekarang": "Sukarame",
        "Hobi": "Nonton youtube, main game",
        "Sosial Media": "@alfaritziirvan",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Pengabdian Masyarakat"
    },
    {
        "Nama": "Izza Lutfia",
        "NIM": "122450090",
        "Umur": 20,
        "Asal": "Bandar Lampung",
        "Alamat Sekarang": "Teluk Betung",
        "Hobi": "Main Rubik",
        "Sosial Media": "@izzalutfia",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Pengabdian Masyarakat"
    },
    {
        "Nama": "Khaalishah Zuhrah Alyaa Vanefi",
        "NIM": "122450034",
        "Umur": 20,
        "Asal": "Bandar Lampung",
        "Alamat Sekarang": "Rajabasa",
        "Hobi": "Mengaji",
        "Sosial Media": "@alyaavanevi",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Pengabdian Masyarakat"
    },
    {
        "Nama": "Raid Muhammad Naufal",
        "NIM": "122450027",
        "Umur": 20,
        "Asal": "Lampung Tengah",
        "Alamat Sekarang": "Sukarame",
        "Hobi": "Nemenin Tobias lari",
        "Sosial Media": "@rayths_",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Pengabdian Masyarakat"
    },
    {
        "Nama": "Tria Yunanni",
        "NIM": "122450127",
        "Umur": 20,
        "Asal": "Palembang",
        "Alamat Sekarang": "Way Dadi",
        "Hobi": "Olahraga",
        "Sosial Media": "@triayunanni",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Divisi Pengabdian Masyarakat"
    }
]
        display_images_with_data(gambar_urls, data_list)
    departemeneksternal()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen Internal":
    def departemeninternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #1
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #2
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #3
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #4
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #5
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #6
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #7
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #8
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #9
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #10
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #11
        ]
        data_list = [
    {
        "Nama": "Dimas Rizky Ramadhani",
        "NIM": "121450027",
        "Umur": 20,
        "Asal": "Tangerang Selatan",
        "Alamat Sekarang": "Way Kandis (Kobam)",
        "Hobi": "Menunggu ayam jantan bertelur",
        "Sosial Media": "@dimzrky_",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Kepala Departemen Internal"
    },
    {
        "Nama": "Chatrine Sinaga",
        "NIM": "121450071",
        "Umur": 20,
        "Asal": "Sumatera Utara",
        "Alamat Sekarang": "Airan",
        "Hobi": "Baca Novel",
        "Sosial Media": "@cathrine.sinaga",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Sekretaris Departemen Internal"
    },
    {
        "Nama": "M. Akbar Restika",
        "NIM": "121450066",
        "Umur": 20,
        "Asal": "Lampung Barat",
        "Alamat Sekarang": "Pasaruntung",
        "Hobi": "Mengoleksi Dino",
        "Sosial Media": "@akbar_restika",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Kadiv Keharmonisasian"
    },
    {
        "Nama": "Renita Siahaan",
        "NIM": "122450070",
        "Umur": 21,
        "Asal": "Sumatera Utara",
        "Alamat Sekarang": "Gerbang Barat",
        "Hobi": "Membaca dan Memancing",
        "Sosial Media": "@renita.shn",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Keharmonisasian"
    },
    {
        "Nama": "Salwa Farhanatussaidah",
        "NIM": "122450055",
        "Umur": 20,
        "Asal": "Pesawaran",
        "Alamat Sekarang": "Airan",
        "Hobi": "Nonton",
        "Sosial Media": "@slwfhn_694",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Keharmonisasian"
    },
    {
        "Nama": "Rendra Eka Prayoga",
        "NIM": "122450112",
        "Umur": 20,
        "Asal": "Bekasi",
        "Alamat Sekarang": "Jl. Lapas Raya",
        "Hobi": "Menulis lagu",
        "Sosial Media": "@rendraepr",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Keharmonisasian"
    },
    {
        "Nama": "Yosia Retare Banurea",
        "NIM": "121450149",
        "Umur": 20,
        "Asal": "Sumatera Utara",
        "Alamat Sekarang": "Perum Griya Indah",
        "Hobi": "Nungguin ayam betina berkokok",
        "Sosial Media": "@yosiabanurea",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Keharmonisasian"
    },
    {
        "Nama": "Ari Sigit",
        "NIM": "121450069",
        "Umur": 23,
        "Asal": "Lampung Barat",
        "Alamat Sekarang": "Labuhan Ratu",
        "Hobi": "Futsal",
        "Sosial Media": "@ari_sigit17",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Kepala Divisi Kerohanian"
    },
    {
        "Nama": "Josua Panggabean",
        "NIM": "122450061",
        "Umur": 21,
        "Asal": "Sumatera Utara",
        "Alamat Sekarang": "Gerbang Barat",
        "Hobi": "Ngejokes",
        "Sosial Media": "@josuapanggabean_",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Kerohanian"
    },
    {
        "Nama": "Azizah Kusuma Putri",
        "NIM": "122450068",
        "Umur": 21,
        "Asal": "Lampung Selatan",
        "Alamat Sekarang": "Natar",
        "Hobi": "Berkebun",
        "Sosial Media": "@azizahksma15",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Kerohanian"
    },
    {
        "Nama": "Meira Listyaningrum",
        "NIM": "122450011",
        "Umur": 20,
        "Asal": "Pesawaran",
        "Alamat Sekarang": "Airan",
        "Hobi": "Nonton",
        "Sosial Media": "@meirasty_",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Kerohanian"
    },
    {
        "Nama": "Rendi Alexander Hutagalung",
        "NIM": "122450057",
        "Umur": 20,
        "Asal": "Tangerang",
        "Alamat Sekarang": "Kost Benawang",
        "Hobi": "Berenang di Laut",
        "Sosial Media": "@rexander",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Kerohanian"
    }
]
        display_images_with_data(gambar_urls, data_list)
    departemeninternal()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen SSD":
    def departemenssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #1
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #2
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #3
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #4
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #5
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #6
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #7
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #8
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #9
        ]
        data_list = [
    {
        "Nama": "Andrian Agustinus Lumbangaol",
        "NIM": "121450090",
        "Umur": 21,
        "Asal": "Panjibako",
        "Alamat Sekarang": "Jl. Bel",
        "Hobi": "Mencari Uang",
        "Sosial Media": "@andriangaol",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Kepala Departemen SSD"
    },
    {
        "Nama": "Adisty Syawaida Arianto",
        "NIM": "121450136",
        "Umur": 23,
        "Asal": "Metro",
        "Alamat Sekarang": "Sukarame",
        "Hobi": "Nonton Film",
        "Sosial Media": "@adistysa_",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Sekretaris Departemen SSD"
    },
    {
        "Nama": "Nabila Azhari",
        "NIM": "121450029",
        "Umur": 21,
        "Asal": "Simalungun",
        "Alamat Sekarang": "Airan",
        "Hobi": "Menghitung Uang",
        "Sosial Media": "@zhjung",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Kepala Divisi KWU"
    },
    {
        "Nama": "Danang Hilal Kurniawan",
        "NIM": "122450085",
        "Umur": 21,
        "Asal": "Bandar Lampung",
        "Alamat Sekarang": "Airan",
        "Hobi": "Touring",
        "Sosial Media": "@dananghk_",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff KWU"
    },
    {
        "Nama": "Farel Julio Akbar",
        "NIM": "122450110",
        "Umur": 20,
        "Asal": "Bogor",
        "Alamat Sekarang": "Lapas",
        "Hobi": "Bebas",
        "Sosial Media": "@farel_julio",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff KWU"
    },
    {
        "Nama": "Ahmad Rizqi",
        "NIM": "122450138",
        "Umur": 20,
        "Asal": "Bukittingi",
        "Alamat Sekarang": "Airan 1",
        "Hobi": "Badminton",
        "Sosial Media": "@ahmad.ris45",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff KWU"
    },
    {
        "Nama": "Tessa Kania Sagala",
        "NIM": "122450040",
        "Umur": 20,
        "Asal": "Simalungun",
        "Alamat Sekarang": "Pemda",
        "Hobi": "Menulis",
        "Sosial Media": "@tesakanias",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff KWU"
    },
    {
        "Nama": "Nabilah Andika Fitriati",
        "NIM": "121450139",
        "Umur": 20,
        "Asal": "Kedaton",
        "Alamat Sekarang": "Kedaton",
        "Hobi": "Tidur",
        "Sosial Media": "@nabilahanftr",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Kepala Divisi Sponsor"
    },
    {
        "Nama": "Elia Meylani Simanjuntak",
        "NIM": "122450026",
        "Umur": 20,
        "Asal": "Bekasi",
        "Alamat Sekarang": "Korpri",
        "Hobi": "Main Alat Musik",
        "Sosial Media": "@meylanielia",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Sponsor"
    },
    {
        "Nama": "Dhafin Razaqa Luthfi",
        "NIM": "122450133",
        "Umur": 20,
        "Asal": "Bandar Lampung",
        "Alamat Sekarang": "Jl. Nangkal",
        "Hobi": "Olahraga",
        "Sosial Media": "@dhafinrzqa13",
        "Kesan": "",
        "Pesan": "",
        "Jabatan": "Staff Sponsor"
    }
]
        display_images_with_data(gambar_urls, data_list)
    departemenssd()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen MEDKRAF":
    def departemenmedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #1
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #2
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #3
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #4
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #5
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #6
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #7
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #8
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #9
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #10
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #11
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #12
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #13
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #14
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #15
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #16
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #17
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #18
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
        "pesan": "",
        "jabatan": "Kepala Departemen"
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
        "pesan": "",
        "jabatan": "Sekretaris"
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
        "pesan": "",
        "jabatan": "Kepala Divisi Media & Konten"
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
        "pesan": "",
        "jabatan": "Kepala Divisi PDD"
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
        "pesan": "",
        "jabatan": "Kepala Divisi Visual Desain"
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
        "pesan": "",
        "jabatan": "Anggota Divisi Media & Konten"
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
        "pesan": "",
        "jabatan": "Anggota Divisi Media & Konten"
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
        "pesan": "",
        "jabatan": "Anggota Divisi Media & Konten"
    },
    {
        "nama": "Patricia Leondra Diajeng Putri",
        "nim": "122450050",
        "umur": "20",
        "asal": "Bandar Lampung",
        "alamat": "Jatimulyo",
        "hobbi": "Nonton Film",
        "sosmed": "@patriciadiajeng",
        "kesan": "",
        "pesan": "",
        "jabatan": "Anggota Divisi Media & Konten"
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
        "pesan": "",
        "jabatan": "Anggota Divisi Media & Konten"
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
        "pesan": "",
        "jabatan": "Anggota Divisi Media & Konten"
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
        "pesan": "",
        "jabatan": "Anggota Divisi PDD"
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
        "pesan": "",
        "jabatan": "Anggota Divisi PDD"
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
        "pesan": "",
        "jabatan": "Anggota Divisi PDD"
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
        "pesan": "",
        "jabatan": "Anggota Divisi PDD"
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
        "pesan": "",
        "jabatan": "Anggota Divisi Visual Desain"
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
        "pesan": "",
        "jabatan": "Anggota Divisi Visual Desain"
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
        "pesan": "",
        "jabatan": "Anggota Divisi Visual Desain"
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
        "pesan": "",
        "jabatan": "Anggota Divisi Visual Desain"
    }
]
        display_images_with_data(gambar_urls, data_list)
    departemenmedkraf()
