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

elif menu == "Departemen PSDA":
    def departemenpsda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kxKOuBdBcNLPnHrzKeliGCvQz3ZltV8V",
            "https://drive.google.com/uc?export=view&id=1lGu70rWDDpkVRpa9cRGLZRMzrmBNKdGK",
            "https://drive.google.com/uc?export=view&id=1kjp3ld_lqrneYkR5uBaZuBrcaLypSQEQ",
            "https://drive.google.com/uc?export=view&id=1kk8O_bT_Qn1kUW3ePNXZyVR0EY0AtzrT",
            "https://drive.google.com/uc?export=view&id=1l68HV_2dJCE_fzMxiQj3kPGtUZbKYqOr",
            "https://drive.google.com/uc?export=view&id=1kl4fosqOdBaMur1DMlnnSy2WTqaORx83",
            "https://drive.google.com/uc?export=view&id=1k_N0NWKTlAgW_0eU5BPOB48XsQBcK5IM",
            "https://drive.google.com/uc?export=view&id=1km_WYwb3yOBevAqdP0xNV5d33myvM8Ff",
            "https://drive.google.com/uc?export=view&id=1l8lXiNTNVrbjGlNS-LTksZNcBCuNFWVe",
            "https://drive.google.com/uc?export=view&id=1kcQIhguidw01Is36N7mXwUqK_as2C95y",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1kdrU2AwCeOUjikTsoQmTMB50u1eQVuIt",
            "https://drive.google.com/uc?export=view&id=1knKy2B1gBMnkfx6Zd3sC2lWDD-gyu-Zg",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1kkjGxzjnaG5gznpCjpGFBECACuz8iZMz",
            "https://drive.google.com/uc?export=view&id=1l94wpBW5tRsqikDVwd04dYL7MZaoDWkQ",
            "https://drive.google.com/uc?export=view&id=1lE75AV0F5SM4BHS3IK_-5jpH61c98sVJ",
            "https://drive.google.com/uc?export=view&id=1lDqzBgknljRlHeJsjUTMP2TpK4NZvIwl",
            "https://drive.google.com/uc?export=view&id=1kU6qJ8wzb4N1REuRYXHefmJn6y_bET90",
            "https://drive.google.com/uc?export=view&id=1kVYbs2E6394NaYZBZJ78Z2losM3Bg7bC",
            "https://drive.google.com/uc?export=view&id=1lGnY5-IftXz9HH3X_5rDfS8eruEeis7o",
            "https://drive.google.com/uc?export=view&id=1kWg5hvU0j95IXgyqVxU1-VwvFxH5nIU8",
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sinaga",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abangnya kritiss, wawasan nya luas",  
                "pesan":"semangat terus kuliahnya bang!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@eelisabeth",
                "kesan": "Kakaknya ekspresif banget",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Marahin orang",
                "sosmed": "@afifahnsrn",
                "kesan": "Cantikk bangettt",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg.sakum",
                "hobbi": "Gg. Perwira Belwis",
                "sosmed": "@allyaislami_",
                "kesan": "",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 4
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiyati",
                "nim": "122450001",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Metro",
                "hobbi": "Nyopet",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Bengong",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "19",
                "asal":"Medan",
                "alamat": " Jalan Pangeran Senopati Raya 18",
                "hobbi": "Baca Kitab Suci",
                "sosmed": "@ferdy_kevin",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jalan Pagar Alam Kedaton",
                "hobbi": "Ngukur Jalan",
                "sosmed": "@dransyah_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Travelling",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 9
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Duri, Riau",
                "alamat": "Pulau damar, Kobam",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "abangnya seruu",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 10
            },
            {
                "nama": "Ibnu Farhan Al-Ghifari",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 11
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Asprak",
                "sosmed": "@johanneskrsjnnn",
                "kesan": "Bang jo asik, tapi kadang segen juga",  
                "pesan":"semangat terus kuliahnya bang!"# 12
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Golf Asri",
                "hobbi": "Ngetik print hello dunia",
                "sosmed": "@kemasverii",
                "kesan": "Bang kemas asikk, vibesnya pinter ternyata beneran pinter",  
                "pesan":"semangat terus kuliahnya bang!"# 13
            },
            {
                "nama": " Leonard Andreas Napitupulu",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 14
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Kota baru",
                "hobbi": "Dengerin the adams",
                "sosmed": "@presilliamg",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 15
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450122",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Baca webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 16
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Depok, Jawa barat",
                "alamat": "Jalan airan raya",
                "hobbi": "Dengerin juicy luicy",
                "sosmed": "@sahid_maul19",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 17
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Minum kopi, belajar, bikin deyvan senang",
                "sosmed": "@roselivness",
                "kesan": "kakanya baik",  
                "pesan":"semangat terus kuliahnya kak!!"# 18
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "pembawaan nya santai, friendly jugaa",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 19
            },
            {
                "nama": "Gede Moana",
                "nim": "122450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri raya",
                "hobbi": "Belajar, game, baca komik",
                "sosmed": "@gedemoeanaa",
                "kesan": "abangnya baik",  
                "pesan":"semangat kuliahnya bang!"# 20
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv",
                "kesan": "kakanya asik lucuuu",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 21
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main game",
                "sosmed": "@raflyy_pd",
                "kesan": "abangnya asik, baik juga",  
                "pesan":"semangat kuliah bang!!"# 22
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@syalaisha.i_",
                "kesan": "kaget ternyata kakanya kembar, kirain double job",  
                "pesan":"semangat kuliah kak!!"# 23
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenpsda()

elif menu == "Departemen MIKFES":
    def departemen_mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kDkY9KTNHjG4e5fFM7mCMN0kPkOIX4__", #45
            "https://drive.google.com/uc?export=view&id=1jy-PYDPUWvNDz1R7uQtrtEnyirhZA5Lo", #46
            "https://drive.google.com/uc?export=view&id=1jpkeQR7ysuQKABd3BAejFpTYWB_YoU7B", #47
            "https://drive.google.com/uc?export=view&id=1kMksdNEBMa6Ki7Fw2TxiG4p4o3cevwvW", #48
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #49
            "https://drive.google.com/uc?export=view&id=1kMksdNEBMa6Ki7Fw2TxiG4p4o3cevwvW", #50
            "https://drive.google.com/uc?export=view&id=1jrm1F_aGBULyebm19gl4iDD-De8Q0S8b", #51
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #52
            "https://drive.google.com/uc?export=view&id=1k7GsUHnJIwihWt83AgqrBy-O06Go1E4o", #53
            "https://drive.google.com/uc?export=view&id=1jvRa8gTYCLP40RlvJzfMFeZxXeBDfE-d", #54
            "https://drive.google.com/uc?export=view&id=1kF2DjhSt4IpK27adCZTeWGTc5tW2MxyI", #55
            "https://drive.google.com/uc?export=view&id=1kMmENXi1NueCKsmbGrR-YgCJndoItKO1", #56
            "https://drive.google.com/uc?export=view&id=1jql44JWq3VGxSJV6bI5TbPqv27kVnqVT", #57
            "https://drive.google.com/uc?export=view&id=1kKdsobmYmJOUQS1RxV7lzwvWMF_DwvJg", #58
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #59
            "https://drive.google.com/uc?export=view&id=1kH8BeroSMTXItrDSlVTf9B64mIdDtI5r", #60
            "https://drive.google.com/uc?export=view&id=1kRS4LToSnbO7YKnglQ9rwYjwzgCn75Ja", #61
            "https://drive.google.com/uc?export=view&id=1k8zAp2zMGyNZi8ttDxrqB8-k_LJsiLrD", #62
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #63
            "https://drive.google.com/uc?export=view&id=1kAEH8NC_fM6HxUgF-IVjDuyI4asbc5m3", #64
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
                "kesan": "abangnya asikk",  
                "pesan":"Semangat terus bang" #50
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Gg. Yudistira",
                "hobi": "Review jurnal Bu Mika",
                "sosmed": "@",
                "kesan": "kakanya kalem pendiem",  
                "pesan":"Semangat terus kak" #51
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": "",
                "sosmed": "@natanaelokt",
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
                "kesan": "baikk",  
                "pesan":"Semangat terus kak" #53
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobi": "Resume Webinar",
                "sosmed": "@anjaniiidev",
                "kesan": "kakanya kalem gitu, asik baik jugaa",  
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
                "nim": "122450103",
                "umur": "19",
                "asal":"Kepulauan riau",
                "alamat": "Gg. Nangka 3",
                "hobi": "Menghitung akurasi",
                "sosmed": "@junitaa_0406",
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
                "sosmed": "@puspadr",
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
                "sosmed": "@rhmn_abdr",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #59
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "19",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobi": "Ngoding wisata",
                "sosmed": "@rahm_adityaa",
                "kesan": "abangnya pendiem kalem",  
                "pesan":"Semangat terus kak" #60
            },
            {
                "nama": "Eggi satria",
                "nim": "122450032",
                "umur": "19",
                "asal":"Sukabumi",
                "alamat": "Korpri",
                "hobi": "Ngoding wisata",
                "sosmed": "@_egistr",
                "kesan": "bang egi public speakingnya jago, kerennn",  
                "pesan":"Semangat kuliahnya bang" #61
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "19",
                "asal":"Tulang bawang",
                "alamat": "Jl. Kelengkeng Raya",
                "hobi": "Review jurnal",
                "sosmed": "@pratiwifebiya",
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
                "sosmed": "@sudo.syahrulramadhann",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #63
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
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
                "sosmed": "@vita.annn",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #65
            },
         ]
        display_images_with_data(gambar_urls, data_list)
    departemen_mikfes()
