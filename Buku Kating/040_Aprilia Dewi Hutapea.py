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
            st.write(f"Nama          : {data_list[i]['nama']}")
            st.write(f"NIM           : {data_list[i]['nim']}")
            st.write(f"Umur          : {data_list[i]['umur']}")
            st.write(f"Asal          : {data_list[i]['asal']}")
            st.write(f"Alamat        : {data_list[i]['alamat']}")
            st.write(f"Hobbi         : {data_list[i]['hobbi']}")
            st.write(f"Sosial Media  : {data_list[i]['sosmed']}")
            st.write(f"Kesan         : {data_list[i]['kesan']}")
            st.write(f"Pesan         : {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1iBcQqzBHPBeyy-MSHQrEL_g8aE8GCRLG", #1
            "https://drive.google.com/uc?export=view&id=1hu_tp1DTE8J4kFvC2mm__w6_8tUQIyFe",
            "https://drive.google.com/uc?export=view&id=1i503ZA6rRdAiiCm7Y2bQkYubUgbrP5BD",
            "https://drive.google.com/uc?export=view&id=1i7cNmyKKEbWtgfpdsWgt6mrwfKY6kr1f",
            "https://drive.google.com/uc?export=view&id=1i0lsr-cPF4Ux39g7EB_VaG7TA7fx-qkO",
            "https://drive.google.com/uc?export=view&id=1iIvcxiMucUzuw2_CNEkQrsFXN5S0lZdl",
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
                "kesan": "bang kharisma memiliki karisma yang kuat dan berwawasan sangat luas.",  
                "pesan":"semoga bang kharisma semakin sukses dalam himpunan maupun di luar himpunan"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450077",
                "umur": "21",
                "asal":"Bukit Kemuning",
                "alamat": "Pawen 2 Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni21",
                "kesan": "Bang Pandra wawasannya luas dan asikk.",  
                "pesan":"semoga bang pandra semakin sukses dalam himpunan maupun di luar himpunan"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kotabaru",
                "hobbi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "kak meliza orangnya baik dan asik.",  
                "pesan":"semoga kak meliza semakin sukses dalam himpunan maupun di luar himpunan"# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "kak hartiti ramah dan mudah senyum.",  
                "pesan":"semoga kak meliza semakin sukses dalam himpunan maupun di luar himpunan"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin  bang Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kak putri pembawaannya baik , ramah, dan mudah senyum.",  
                "pesan":"semoga kak meliza semakin sukses dalam himpunan maupun di luar himpunan"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kotabaru",
                "hobbi": "Dengerin  bang Pandra Gitaran",
                "sosmed": "@nadillaadr26",
                "kesan": "Kak nadilla mudah senyum dan baik.",  
                "pesan":"semoga kak nadilla semakin sukses dalam himpunan maupun di luar himpunan"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Kakak ini asik diajak tukar pikiran, selalu ada solusi buat setiap masalah.",  
                "pesan":"Teruslah semangat belajar, kak! Masa depan cerah menanti!"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton Film",
                "sosmed": "@wlsbn0",
                "kesan": "Kakak punya sikap positif yang bikin suasana jadi lebih santai tapi tetap produktif.",  
                "pesan":"Tetap semangat ya kakak! Jangan lupa istirahat di tengah kesibukan kuliah!"# 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "Sangat suportif dan selalu memberi dorongan, kakak ini bikin kita jadi lebih termotivasi.",  
                "pesan":"Sukses selalu untuk kuliahnya! Tetap semangat dan jangan pernah berhenti belajar."# 1
            },{
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bernung, Pesawaran",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },{
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Belwis",
                "hobbi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak selalu memberi energi positif",  
                "pesan":"Semoga kakak selalu diberi kelancaran dalam segala urusan. Tetap semangat!"# 1
            },{
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Baca Al-qur'an",
                "sosmed": "@fleurnsh",
                "kesan": "Kakak ini selalu ramah dan gampang diajak ngobrol, suasana jadi lebih hidup",  
                "pesan":"Semangat terus, Kak! Jangan menyerah dan teruslah berjuang sampai garis akhir!"# 1
            },{
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak punya sikap yang menyenangkan, setiap obrolan jadi asik dan nggak pernah membosankan.",  
                "pesan":"Semoga sukses di setiap langkah ke depannya, Kak. Teruslah bersinar!"# 1
            },{
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Kakaknya selalu ceria dan bisa bikin orang lain ikut merasa positif.",  
                "pesan":"Jaga kesehatan dan semoga selalu diberi kemudahan dalam setiap perjalanan hidup, Kak!"# 1
            },{
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Ogan Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari Sinyal di Gedung F",
                "sosmed": "@_.dheamelia",
                "kesan": "Sangat mudah bergaul dan selalu membawa suasana jadi nyaman.",  
                "pesan":"Teruslah jadi inspirasi untuk orang-orang di sekitar kakak! Sukses selalu!"# 1
            },{
                "nama": "Muhammad Fahrul Aditya",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini selalu bisa diandalkan, baik dalam situasi santai maupun serius.",  
                "pesan":"Semoga kakak semakin sukses dan terus semangat mengejar impian!"# 1
            },{
                "nama": "Berliana enda putri",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini sosok yang humble dan asik diajak bicara tentang apa saja",  
                "pesan":"Semoga kakak selalu diberkahi kemudahan dalam segala urusan. Tetap semangat menjalani hari-hari ke depan!"# 1
            },{
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Billabong, Gedong Air",
                "hobbi": "Suka Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "Kakak selalu membawa aura positif, jadi nyaman kalau ngobrol lama-lama.",  
                "pesan":"Semoga kakak selalu diberi kebahagiaan dan sukses di setiap langkahnya!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
# Tambahkan menu lainnya sesuai kebutuhan
