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
            "https://drive.google.com/uc?export=view&id=1iMCqW9bXwE4KSx5QmklmzlpcRKk7-QjX",
            "https://drive.google.com/uc?export=view&id=1iJceiXU0E5BI6lKFlHeMCJ47nl4EKJ9b",
            "https://drive.google.com/uc?export=view&id=1iNot2bz55FPfcV2OYlzeRG_LIQSa5E_e",
            "https://drive.google.com/uc?export=view&id=1i6q-6USMexKlprmqHNseMH7MzVPbgO4f",
            "https://drive.google.com/uc?export=view&id=1i5Kg191Sp7sGeTWAtx8BvvI3swdx8lWb",
            "https://drive.google.com/uc?export=view&id=1iN_zu1Jt_6KkXLK96qIY73G9otzhuBjc",
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
                "kesan": "Charming person",  
                "pesan":"Semangat dan sukses selalu bang gumi"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Bukit kemuning",
                "alamat": "Pawen 2 Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni21",
                "kesan": "Charismatic dan Sociable, ngobrol sampe pagi pun ga akan keabisan topik",  
                "pesan":"semangat terus kuliahnya bang pandra!"# 2
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar alam",
                "alamat": "Kotabaru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakanya inspiring, jadi waktu ngobrol bikin kita termotivasi dan berpikir lebih jauh",  
                "pesan":"terimakasi sesi sharing session nya ka sehat selalu"# 3
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "kakanya keliatan tegas dan percaya diri",  
                "pesan":"semangat terus kuliahnya kakak!"# 4 
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "kakanya serene alias kepribadian nya kaya kalem tenang gitu",  
                "pesan":"semangat kak semoga sukses!"# 5
            },
            {
                "nama": "Nadila Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kotabaru",
                "hobbi": "Dengerin bang pandra giatara",
                "sosmed": "@nadillaadr26",
                "kesan": "Fun-loving dan ceria",  
                "pesan":"sehat selalu dan semangat kuliahnya ka nadila!"# 1 
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fgWqssmUziuaHQFIhr_DGWdhbn4q529v",
            "https://drive.google.com/uc?export=view&id=1fyaC5ll6cdrFiObneJq1_ZiHe16DpQY6",
            "https://drive.google.com/uc?export=view&id=1g6XAp6EaGDT4VRU_P_ZzZy9YV2OjQlso",
            "https://drive.google.com/uc?export=view&id=1gKwnARsd07N3GCM8X465ikdrD-DEPHUW",
            "https://drive.google.com/uc?export=view&id=1gQ9B0HT3YhoWyrbNB3RZJVVmMdiz4GkG",
            "https://drive.google.com/uc?export=view&id=1gFk42bc_4efBRkvym4etYFX6WXIMPjzp",
            "https://drive.google.com/uc?export=view&id=1fpA9i32p1kBNW_5oaJ5F3ONVhH2y5LWK",
            "https://drive.google.com/uc?export=view&id=14qk7upfYCxCRKkfyquWu9qCIpRgWUbOn",
            "https://drive.google.com/uc?export=view&id=14qbyVX3Ecvd7NjVC6K9fDRv6_PH17rIY",
            "https://drive.google.com/uc?export=view&id=1fjhLldMZX79mtV2naj7MXNd5BBQaDo3-",
            "https://drive.google.com/uc?export=view&id=1fvDgdR0Wfk9_Kmg84MCOsO7TdHhSuDU5",
            "https://drive.google.com/uc?export=view&id=1gJhtp3YxE2T4LAIQlwFHTY2RGsX3rJz-",
            "https://drive.google.com/uc?export=view&id=1gITGp2A-lpgSSNxPzgDuXCh4J6i79QYS",
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden saleh",
                "hobbi": "Bertanya sama GPT",
                "sosmed": "@trimurniaa_",
                "kesan": "Engaging sama friendly banget, cara ngomongnya bikin orang betah dengerin dan wawasannya luas jadi seru",  
                "pesan":"every small step takes you closer to your goal, semoga terus menginspirasi kak!"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tangerang selatan",
                "alamat": "way hui",
                "hobbi": "Membaca",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Vibes kakanya Maternal authority, kaya kalem yang lemah lembut",  
                "pesan":"Stay focused, your hard work will pay off! semangat kuliah ka!!"# 2
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton film",
                "sosmed": "@wlsbn0",
                "kesan": "definisi beauty with brains, kak kamu menginspirasi bgt!",  
                "pesan":"semangat kuliah ka, sukses selalu, stay positive, work hard, and make it happen"# 3
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jati agung",
                "hobbi": "Nonton Drachin",
                "sosmed": "@anisadini10",
                "kesan": "",  
                "pesan":"!"# 4
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bernug Pesawaran",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakot",
                "sosmed": "@ansftynn_",
                "kesan": "",  
                "pesan":""# 5
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Belwis",
                "hobbi": "Sholat duha",
                "sosmed": "@fer_yulius",
                "kesan": "!",  
                "pesan":""# 6
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar lampung",
                "alamat": "Teluk betung",
                "hobbi": "Baca al-qur'an",
                "sosmed": "@fleurnsh",
                "kesan": "",  
                "pesan":""# 7
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung timur",
                "alamat": "Lampung timur",
                "hobbi": "Baca jurnal",
                "sosmed": "@dylebee",
                "kesan": "",  
                "pesan":"!"# 8
            },
            {
               "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main kucing",
                "sosmed": "@myrriinn",
                "kesan": "",  
                "pesan":"!"# 9
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Ogan Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari sinyal di gedung f",
                "sosmed": "@_.dheamelia",
                "kesan": "",  
                "pesan":""# 10
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450126",
                "umur": "22",
                "asal":"Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Melukis",
                "sosmed": "@fhrul.pdf",
                "kesan": "",  
                "pesan":"!"# 11
            },
            {
               "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatra Barat",
                "alamat": "Way Huwi",
                "hobbi": "Baca buku, ngoding, ibadah",
                "sosmed": "@berlyyanda",
                "kesan": "",  
                "pesan":"!"# 12
            },
            {
               "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Billabong, Gedong air",
                "hobbi": "Suka bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "bang jere baik banget asik jugaa",  
                "pesan":"Semangat kuliahnya bang!"# 13
            },
            
            
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator ():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mM9apWiLnliAJIgdKSU09bpdO3qNW-v8",
            "https://drive.google.com/uc?export=view&id=1mO-iRiFk11rX_qJHnp8x5iKXQJU0-RdS",
        ]
        data_list = [
            {
                "nama": "Anissa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal":"Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi": "Bernyanyi",
                "sosmed": "@annisalutfia_",
                "kesan": "Kakanya baik asik jugaa",  
                "pesan":"semangat terus kuliahnya kak!" #1

            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kota baru",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "abangnya baik dan tegas",  
                "pesan":"semangat terus kuliahnya bang" #2

            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()


