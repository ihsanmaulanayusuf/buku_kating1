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
                "hobbi": "Dengerin musik",
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
                "hobbi": "Main gitar",
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
                "hobbi": "Nyanyi",
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
                "hobbi": "Dengerin  bang Pandra Gitaran",
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
                "hobbi": "Dengerin  bang Pandra Gitaran",
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #14
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #15
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
                "hobbi": "Bertanya sama GPT",
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
                "hobbi": " Membaca",
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
                "hobbi": "Menonton Film",
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
                "hobbi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "Sangat suportif dan selalu memberi motivasi.",  
                "pesan": "Sukses selalu untuk kuliahnya kak!"#10
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal": "Bernung, Pesawaran",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak ini asik banget.",  
                "pesan": "Semangat terus kuliahnya kakak!"#11
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Punya energi positif tersendiri nih",  
                "pesan": "Semoga abang selalu diberi kelancaran dalam segala urusan."#12
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Baca Al-qur'an",
                "sosmed": "@fleurnsh",
                "kesan": "Ramah dan mudah diajak ngobrol",  
                "pesan": "Semangat terus, Kak!"#13
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak punya sikap yang menyenangkan hehe.",  
                "pesan": "Semoga sukses di setiap langkah ke depannya, Kak. Teruslah bersinar!"#14
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Kakak yang selalu ceria dan bisa bikin orang lain moodnya naik juga nih.",  
                "pesan": "Jaga kesehatan dan semoga selalu diberi kemudahan ya Kak!"#15
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal": "Ogan Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari Sinyal di Gedung F",
                "sosmed": "@_.dheamelia",
                "kesan": "Mudah bergaul dan selalu membawa suasana jadi nyaman.",  
                "pesan": "Sukses selalu kakak!"#16
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "122450000",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini selalu bisa diandalkan, baik dalam situasi santai maupun serius.",  
                "pesan": "Sukses terus dan semangat mengejar impiannya kak!"#17
            },
            {
                "nama": "Berliana enda putri",
                "nim": "122450000",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini sosok yang humble dan asik diajak bicara.",  
                "pesan": "Semoga kakak selalu diberkahi kemudahan dalam segala urusan!"#18
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Billabong, Gedong Air",
                "hobbi": "Suka Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "Kakak selalu membawa aura positif dan humoris juga.",  
                "pesan": "Semoga kakak selalu diberi kemudahan dalam segala urusan!"#19
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
