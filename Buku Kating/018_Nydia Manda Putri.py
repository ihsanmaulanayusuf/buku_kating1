
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
            "https://drive.google.com/uc?export=view&id=1XmU6aZqXxzS4aF3w-S__lDoyyWdIBrDH",
            "https://drive.google.com/uc?export=view&id=1Y4zMdGrTnJjXCPct5hXVM5_Z4ESq0bJX",
            "https://drive.google.com/uc?export=view&id=1XoiAEW7RicB3VABx2LH_bZdATZS5xkHC",
            "https://drive.google.com/uc?export=view&id=1Xms1vAF6QsdE4Q2GHRkST6WV8ga-ji1F",
            "https://drive.google.com/uc?export=view&id=1z9XKGkCWLRKX8WDCDfOOjb0vvMQR-WI0",
            "https://drive.google.com/uc?export=view&id=1z5dDetD_xD7tiyxr54WRlD02LmdCNQ5m",
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
                "kesan": "Abang nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya bang agar bisa lulus tepat waktu dan jangan lupa jaga kesehatan!"
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal": "Bukit Kemuning",
                "alamat": "Pawen 2 Sukarame",
                "hobbi": "Main Gitar",
                "sosmed": "@pndrinsni21",
                "kesan": "Abang nya asik dan seru pada saat cerita pengalamannya",  
                "pesan":"Semangat kuliahnya bang, sukses selalu!"
            },
            {
               "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal": "Pagar Alam",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak nya baik banget, seru, dan banyak memberi ilmu baru",  
                "pesan": "Semoga kuliahnya lancar ya kak dan tetap jaga kesehatan ya!"
            },
             {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal": "Payakumbuh",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Bang Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak nya asik, selalu memberi ilmu dan banyak cerita pengalamannya",  
                "pesan": "Sukses selalu kak semoga lulus kuliah tepat waktu ya kak!"
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak nya seru dan ramah",  
                "pesan":"Semangat terus ya kak, sukses buat ke depannya!"
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin Bang Pandra Gitaran",
                "sosmed": "@nadillaadr26",
                "kesan": "Kakak asik dan banyak cerita tentang pengalamannya selama menjadi bendahara 1",  
                "pesan": "Semangat mengejar cita-cita nya ya kak dan jaga selalu kesehatan!"
            }, 
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_XZ8lZH9gpp9wu4PTFPdC2qPJRFZYu1S",
            "https://drive.google.com/uc?export=view&id=1_Hk4Atl-RyiIiqIKB-wht1f35lJR7dWZ",
            "https://drive.google.com/uc?export=view&id=1_Di_li9QcSKFF85iZ_lnQbifB2xjga_B",
            "https://drive.google.com/uc?export=view&id=1_Qwv83dGmFIo06EyAk9EiSc80M6jtORR",
            "https://drive.google.com/uc?export=view&id=1DPQ7WDdGPhr8luyv3CF3eJt39NYJ2Gv9",
            "https://drive.google.com/uc?export=view&id=1ZyEnzEqaiQ-V-7G3_lnOtHLOQcXVlm7W",
            "https://drive.google.com/uc?export=view&id=1DLiUE4D6ivWAhdY1IzrTmErr0LRBm65g",
            "https://drive.google.com/uc?export=view&id=1ppa97a5LevilJVp6LMD9ngaUXApY3zff",
            "https://drive.google.com/uc?export=view&id=1pep2AGFpJib65LohK19x6VJ90KOqiFb8",
            "https://drive.google.com/uc?export=view&id=1_BQe9hTTF8l491BiRW4w3P7wMsyrovwn",
            "https://drive.google.com/uc?export=view&id=1ZwqgPkuC3flXEZbZYBgjiIMrKaSBrYGm",
            "https://drive.google.com/uc?export=view&id=1HUOvAdj0r3j1YB6IS16LqVocfntilfxf",
            "https://drive.google.com/uc?export=view&id=1_6mOZDW4Aa-3bKkWQBukpYPel8lR3uUo",
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
                "kesan": "Kakak nya sangat asik dan baik banget ",  
                "pesan": "Semangat terus kak dan sukses untuk ke depannya!"
            },
           
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450124",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "Way Hui",
                "hobbi": "Membaca",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak nya baik dan ramah",  
                "pesan": "Semoga lulus kuliah tepat waktu ya kak!"
            },
           
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton Film",
                "sosmed": "@wlsbn0",
                "kesan": "Kakak nya seru dan menyenangkan",  
                "pesan": "Sukses terus ya kak!"
            },
           
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "Kakak nya baik banget dan ramah juga",  
                "pesan": "Semangat mengejar cita-cita kak!"
            },
           
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal": "Bernung, Pesawaran",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@ansftynn_",
                "kesan": "Kakaknya ramah dan juga asik saat menceritakan pengalamannya",  
                "pesan": "Tetap semangat dan jaga kesehatan ya kak!"
            },
           
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Abang nya baik dan asik",  
                "pesan": "Semangat terus kuliahnya bang dan jangan lupa jaga kesehatan!"
            },
           
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Baca Al-quran",
                "sosmed": "@fleurnsh",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat dan sukses selalu ya kak!"
            },
           
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal": "Lampung Timurr",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak nya baik dan kalem",  
                "pesan": "Jangan lupa jaga kesehatan kak dan sukses selalu ya!"
            },
             {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abang nya seru dan banyak berbagi ilmu pengalamannya",  
                "pesan": "Semangat terus kuliahnya bang dan jaga kesehatan nya bang!"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal": "Ogan Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari Sinyal di Gedung F",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak nya sangat baik dan seru banget",  
                "pesan": "Semangat menggapai cita-cita nya ya kak!"
            },
           
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450126",
                "umur": "22",
                "asal": "Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Melukis",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abang nya ramah dan baik",  
                "pesan": "Semangat terus kuliahnya bang!"
            },
           
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal": "Sumatra Barat",
                "alamat": "Way Huwi",
                "hobbi": "Baca Buku, Ngoding, Ibadah",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Sukses selalu ya kak!"
            },

            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Billabong, Gedong Air",
                "hobbi": "Suka Bengong",
                "sosmed": "@jeremia_s",
                "kesan": "Abang nya sangat asik dan seru saat cerita",  
                "pesan": "Semangat dan sukses ya bang untuk ke depannya!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1GlCneruH_gGV8ojJ06uwDr56Ejd59DxC",
            "https://drive.google.com/uc?export=view&id=1Gi5gS9LdgHRh0OAFXGkyFGY40sjBKq0i",
        ]
        data_list = [
            {
                "nama": "Anissa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal": "Lampung Tengah",
                "alamat": "Kos Putri Rahayu",
                "hobbi": "Bernyanyi",
                "sosmed": "@annisalutfia_",
                "kesan": "Kakak nya ramah dan baik banget",  
                "pesan": "Semangat terus kuliahnya kak dan semangat mengejar cita-citanya!"
            },
           
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abang nya asik dan banyak cerita pengalamannya",  
                "pesan": "Sukses selalu ya bang dan jangan lupa jaga kesehatan!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()
    
elif menu == "Departemen PSDA":
    def departemenpsda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EKGPM1bj7a7KW_hQMxmIGVNu096PdJu0",
            "https://drive.google.com/uc?export=view&id=1DEq3m3j_mreF9Ssp_1MRKNx_gNwCCjM7",
            "https://drive.google.com/uc?export=view&id=1DT8d6LybqmSytmJGM4cNdD-xsuJmRK23",
            "https://drive.google.com/uc?export=view&id=1E5-jUdeQIeFSlvmYRMSvdY3GPQAaEA4d",
            "https://drive.google.com/uc?export=view&id=1DQEZNGNzhDUa24Df4LGD8ij4ESaNHhje",
            "https://drive.google.com/uc?export=view&id=1FB6nWOGF0ZOyJOrSvbUa0TF4qGbU3HO6",
            "https://drive.google.com/uc?export=view&id=1EqNUar5oYAIa5GKoop5Tz932lAwh62ru",
            "https://drive.google.com/uc?export=view&id=1DQrzI-Fhpxv1SJcHCSNDwumK2s9vx4Zk",
            "https://drive.google.com/uc?export=view&id=1DWHG_-1F9graeG88TSqJWkrwMBUliLIO",
            "https://drive.google.com/uc?export=view&id=1EKnhicNU_DzJtuuNyKLrooRzY8OuO-xI",
            "https://drive.google.com/uc?export=view&id=1F2YIqJadC8v2dYl1O_P7-IkciVtoR8Y-",
            "https://drive.google.com/uc?export=view&id=1DZ8vCVYuJvNUioUe4M9Wchl4L2cwiP_k",
            "https://drive.google.com/uc?export=view&id=1DoPclreLnjiPMwEHEDxTB5oDA92aIoOH",
            "https://drive.google.com/uc?export=view&id=1EJeF_natjo-zIVqgy4hW9yUYiapcrxrw",
            "https://drive.google.com/uc?export=view&id=1EVq3n0PRYYxibOM_bHPjKWBXHIwyB_Ct",
            "https://drive.google.com/uc?export=view&id=1DwFaWQMc5mfuhH1arySwiA6YH2AB92KI",
            "https://drive.google.com/uc?export=view&id=1DyLqfcNRMe_FKJnEqMeLpJx49HTgfK1U",
            "https://drive.google.com/uc?export=view&id=1EboxN_dnK6EPoeKrHX5egzJzSBRoAVLm",
            "https://drive.google.com/uc?export=view&id=1Db3b0-cmQi-wD2uaD2UHEld89w7xw_8D",
            "https://drive.google.com/uc?export=view&id=1zA94z8wxiv8CUqxKCHsHd7kSdOL5wicj",
            "https://drive.google.com/uc?export=view&id=1zB22CbWiIh9Ic69QhlZFQNW0CXqjS0lE",
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
                "kesan": "Abang nya asik dan banyak berbagi ilmu serta cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya bang dan sukses selalu ya!"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Kakak nya baik banget dan seru sekali",  
                "pesan": "Jangan lupa jaga kesehatan ya kak dan tetap semangat semangat!"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal": "Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Marahin Orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak nya murah senyum dan baik banget",  
                "pesan": "Semangat mengejar mimpi nya ya kak sukses selalu!"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyaislami_",
                "kesan": "Kakak nya baik banget, tegas, dan ramah ",  
                "pesan": "Jaga kesehatan ya kak dan tetap semangat kuliahnya!"
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiyati",
                "nim": "122450001",
                "umur": "20",
                "asal": "Jawa Barat",
                "alamat": "Metro",
                "hobbi": "Nyopet",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak nya asik dan murah senyum",  
                "pesan": "Semangat terus kuliahnya kak agar bisa lulus tepat waktu!"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Bengong",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak nya baik dan juga ramah",  
                "pesan": "Semangat mengejar cita-cita nya ya kak!"
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Jalan Pangeran Senopati Raya 18",
                "hobbi": "Baca Kitab Suci",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abang nya asik dan baik",  
                "pesan": "Sukses selalu ya bang ke depannya!"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Kayu Agung",
                "alamat": "Jalan Pagar Alam Kedaton",
                "hobbi": "Ngukur Jalan",
                "sosmed": "@dransyh_",
                "kesan": "Abang nya seru saat menceritakan pengalamannya dan juga baik",  
                "pesan": "Semangat terus kuliahnya bang dan sukses terus!"
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Travelling",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakak nya asik dan juga baik",  
                "pesan": "Jangan lupa jaga kesehatan kak semangat!"
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "1214500148",
                "umur": "21",
                "asal": "Duri, Riau",
                "alamat": "Pulau Damar Kobam",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abang nya seru, ramah, dan juga murah senyum",  
                "pesan": "Semoga lulus kuliah tepat waktu ya bang sukses terus!"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Asprak",
                "sosmed": "@johanneskrsjnnn",
                "kesan": "Abang nya seru, tegas, dan juga murah senyum",  
                "pesan": "Jaga kesehatan ya bang sukses selalu untuk ke depannya!"
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Golf Asri",
                "hobbi": "Ngetik Print Hello Dunia",
                "sosmed": "@kemasverii",
                "kesan": "Abang nya baik banget dan banyak memberikan ilmu serta pengalamannya",  
                "pesan": "Semangat terus kuliahnya bang agar bisa lulus tepat waktu dan jangan lupa jaga kesehatan!"
            },
            {
                "nama": "Presillia",
                "nim": "122450081",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin The Adams",
                "sosmed": "@presilliamg",
                "kesan": "Kakak nya baik dan juga asik",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450122",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak nya seru dan murah senyum",  
                "pesan": "Semangat mengejar mimpinya ya kak!"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Kota Depok, Jabar",
                "alamat": "Jalan Airan Raya",
                "hobbi": "Dengerin juicy luicy",
                "sosmed": "@sahid_maul19",
                "kesan": "Abang nya seru dan juga asik",  
                "pesan": "Semangat dan sukses selalu bang!"
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Minum Kopi, Belajar, Bikin Deyvan Senang",
                "sosmed": "@roselivness__",
                "kesan": "Kakak nya seru banget dan murah senyum",  
                "pesan": "Jaga kesehatan dan semangat terus kak!"
            },
           {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Abang nya baik banget dan juga ramah",  
                "pesan": "Sukses terus bang!"
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "Abang nya baik dan juga seru",  
                "pesan": "Semangat terus kuliahnya bang!"
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv",
                "kesan": "Kakak nya asik dan baik banget",  
                "pesan": "Semangat terus kuliahnya kak agar bisa lulus tepat waktu!"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Abang nya seru dan baik",  
                "pesan": "Semangat terus belajar nya bang!"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@syalaisha.i_",
                "kesan": "Kakak nya baik dan juga murah senyum",  
                "pesan": "Semangat terus kuliahnya kak dan jangan lupa jaga kesehatan!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenpsda()
        
elif menu == "Departemen MIKFES":
    def departemenmikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ZG842FNxvXawVwQLjjwGvA8VflI0XYtQ",
            "https://drive.google.com/uc?export=view&id=1YyJcPovQqlK0pTJVFGz1IBtdPbsh7lNF",
            "https://drive.google.com/uc?export=view&id=1Z5zgN5xL54UHBvrnkx-B0_1vOrbzFTaA",
            "https://drive.google.com/uc?export=view&id=1Z6RvKc-Q5vG-uJ8Bjjl-Ko9_r5zm14is",
            "https://drive.google.com/uc?export=view&id=1ZDzBFM3vYNB9-2nUgpE9FQuEKQ1xrZhX",
            "https://drive.google.com/uc?export=view&id=1ZAowlmHqiemTlVD7kuCiT-j7qUoxOrL5",
            "https://drive.google.com/uc?export=view&id=1ZAqYi59fucEPHrzWmxrlXwIf1A-7KxYH",
            "https://drive.google.com/uc?export=view&id=1YvgOr-NcxQLXvgA1RdOX2zmjip5zCqyo",
            "https://drive.google.com/uc?export=view&id=1Z-30xbp2wj9SVhhrjwAd9SNEfXmqB-B8",
            "https://drive.google.com/uc?export=view&id=1ZOSWJeMOSjX-NGfrItfyzm9ZPMsmlZ8Q",
            "https://drive.google.com/uc?export=view&id=1ZM3IRx6W-LIEImcc4LasAoSk7EMKhmiC",
            "https://drive.google.com/uc?export=view&id=1Yr_OC2EGRL2PMrcEeHa4zC0yLz042cSb",
            "https://drive.google.com/uc?export=view&id=1ZXMWvyIpCRJrqW-7UpgBftyggn2-8Wsn",
            "https://drive.google.com/uc?export=view&id=1ZBbVjpccNuA0ZeAQjaoVkJx_a9-VBZfe",
            "https://drive.google.com/uc?export=view&id=1Z09sf--OfOLYkjWqK50G1RcNXJPYi_tq",
            "https://drive.google.com/uc?export=view&id=1Z3AUwc5VpBI4BDZockB8brgXUG5NsRuu",
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
                "kesan": "Abang nya ramah dan juga banyak memberi ilmu baru",  
                "pesan": "Semangat terus kuliahnya bang!"
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona ",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat belajar nya kak!"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Abang nya baik dan ramah",  
                "pesan": "Jaga kesehatan terus ya bang semangat!"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame ",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "Abang nya ramah dan murah senyum",  
                "pesan": "Sukses selalu bang ke depannya!"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakak nya baik banget dan juga ramah",  
                "pesan": "Semangat terus ya kak!"
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "Abang nya seru dan banyak cerita pengalamannya",  
                "pesan": "Semangat mengejar mimpi nya bang!"
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "Kakak nya baik banget dan murah senyum",  
                "pesan": "Sukses selalu kak!"
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Membaca Jurnal dari Bu Mika",
                "sosmed": "@dindanababan_",
                "kesan": "Kakak nya asik dan ramah",  
                "pesan": "Jaga kesehatan terus ya kak!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak nya seru baget dan banyak memberikan ilmu baru",  
                "pesan": "Semoga kuliahnya lancar terus ya kak!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak nya baik banget dan juga asik",  
                "pesan": "Semangat dan terus belajar ya kak!"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak nya baik banget dan juga ramah serta murah senyum",  
                "pesan": "Semangat terus kuliahnya kak agar bisa lulus tepat waktu dan jangan lupa jaga kesehatan!"
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "Abang nya ramah dan baik",  
                "pesan": "Jaga kesehatan dan lancar ya bang kuliah nya!"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "Abang nya baik dan memberi ilmu serta pengalaman baru",  
                "pesan": "Semangat terus kuliahnya bang!"
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakak nya seru dan baik",  
                "pesan": "Semangat terus kak belajarnya!"
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Abang nya asik dan ramah",  
                "pesan": "Jangan lupa jaga kesehatan bang sukses terus!"
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Abang nya baik banget dan juga murah senyum",  
                "pesan": "Semangat terus kuliahnya bang semangat mengejar cita-cita!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenmikfes()

elif menu == "Departemen Eksternal":
    def departemeneksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bdfTXEZ631GALQlQQNP6qtPENA0vxmrn", 
            "https://drive.google.com/uc?export=view&id=1byIXcxp2GV9YjYd4ln9f9kTq1x19Hhst", 
            "https://drive.google.com/uc?export=view&id=1dS3UcbXaTiKLCDmd4lTamJip6f6vwU7t", 
            "https://drive.google.com/uc?export=view&id=1bewhQ2qX6bI2GZ3pKRX9N6R_1CnWVxc4", 
            "https://drive.google.com/uc?export=view&id=1bslvvI9MGDF5feznwJEJ5uoDdnWUKwAp", 
            "https://drive.google.com/uc?export=view&id=1dNS6DHIyLoF9iA6VCF0lM_S4hfZtktTA", 
            "https://drive.google.com/uc?export=view&id=1cHXHi2UFshSp4HB6qIm6iWbh4IZ33zU_", 
            "https://drive.google.com/uc?export=view&id=1dOzX7C8oWn6sYnBZSMEX-Bk-fa7IiBYG", 
            "https://drive.google.com/uc?export=view&id=1d1JSYXMi17W-FpNbOPJUdiFPp95XsQyK", 
            "https://drive.google.com/uc?export=view&id=1bk9g3iY9HsGLl0DaCLjNqUcr-B3qK8IO", 
            "https://drive.google.com/uc?export=view&id=1cFijrVWSQm6MLmV2Sy_ty7S6_os4PxCN", 
            "https://drive.google.com/uc?export=view&id=1KM63MIs1eIt8khcebWT6M1XX-CiCX-W9", 
            "https://drive.google.com/uc?export=view&id=1c9XQwLIx35zrnr_9YjO3jgG5qVmalyS_", 
            "https://drive.google.com/uc?export=view&id=1KGTbuBI7Jg3FS2KlkDMY8J5JmF5cel4Q", 
            "https://drive.google.com/uc?export=view&id=1KH0VG9srGGqRf6kOIpq7O5B39PP9hIpZ", 
            "https://drive.google.com/uc?export=view&id=1c0gInacqJ0xce0slgvLxR1pySb2lqYxI", 
            "https://drive.google.com/uc?export=view&id=1dEiRR7Y3yfNUS6ndASrGbGEBZY42ne-N", 
            "https://drive.google.com/uc?export=view&id=1KDb8e_Q0xyMQOF2M8xE1hxMuifzuv5q4",     
            "https://drive.google.com/uc?export=view&id=1cBbxt3zMlOZ12zLq0EQS3nb2VVazbeCF",     
            "https://drive.google.com/uc?export=view&id=1bznZYxQbYhF7K0fONyRgrk39DgagTCSF",
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
                "kesan": "Abang nya asik dan banyak memberikan pengalamannya serta ilmu",  
                "pesan": "Sukses terus ke depannya bang!"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "Kakak nya seru dan murah senyum",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Nazwa Nabila",
                "nim": "21450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Korpri",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakak nya baik banget dan juga ramah",  
                "pesan": "Jangan lupa jaga kesehatan kak!"
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "Abang nya seru dan baik",  
                "pesan": "Semoga lulus tepat waktu bang!"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Berkebun",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak nya asik juga banyak memberi ilmu",  
                "pesan": "Sukses terus kak!"
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan": "Kakak nya baik banget dan ramah",  
                "pesan": "Semoga di perlancar kuliah nya kak!"
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Surfing",
                "sosmed": "@nateee__15",
                "kesan": "Kakak nya murah senyum dan juga baik banget",  
                "pesan": "Jangan lupa jaga kesehatan dan tetap semangat ya kak!"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kakak baik banget dan banyak menceritakan pengalama dan memberi pengetahuan baru",  
                "pesan": "Semangat terus kuliahnya kak dan semoga lulus tepat waktu!"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan": "Kakak nya asik dan juga ramah",  
                "pesan": "Jangan lupa jaga kesehatan kak!"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan": "Abang nya baik dan banyak menceritakan pengalamannya",  
                "pesan": "Semangat terus mengejar mimpi nya bang!"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "Kakak nya asik dan juga seru",  
                "pesan": "Semangat terus kuliahnya kak semoga di perlancar ya!"
            },
            {
                "nama": "Rizky Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "Abang nya baik dan banyak memberikan ilmu baru",  
                "pesan": "Semoga lulus tepat waktu dan tercapai mimpi nya ya bang!"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "Abang nya baik dan juga seru",  
                "pesan": "Sukses buat ke depannya bang!"
            },
            {
                "nama": "Asa Do’a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "Kakak nya baik banget dan juga murah senyum",  
                "pesan": "Semangat terus kuliahnya kak jaga kesehatannya!"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan": "Kakak nya ramah dan baik juga",  
                "pesan": "Semangat terus kuliahnya kak agar bisa lulus tepat waktu!"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton Youtube, Main Game",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abang nya seru dan baik",  
                "pesan": "Semangat mengejar mimpi nya bang!"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan": "Kakak nya baik banget dan juga menyenangkan",  
                "pesan": "Semangat belajar dan kuliah nya kak!"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "Kakak nya baik banget, murah senyum, dan juga seru",  
                "pesan": "Semangat terus kuliahnya kak sukses selalu ya kak!"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Nemenin Tobias lari",
                "sosmed": "@rayths_",
                "kesan": "Abang nya asik dan juga ramah",  
                "pesan": "Jaga kesehatan dan sukses terus ya bang!"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450127",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Way Dadi",
                "hobbi": "Olahraga",
                "sosmed": "@triayunanni",
                "kesan": "Kakak nya seru banget dan juga baik",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemeneksternal()

elif menu == "Departemen Internal":
    def departemeninternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1aiiKoXNNYUuS39atUiZdlYJlfW_87fsR", 
            "https://drive.google.com/uc?export=view&id=1ah62ZqZdD23VvzSjEzGFYwBmtI6rHsDW", 
            "https://drive.google.com/uc?export=view&id=1avdDpRGjxQVjuIg-IsfEx2vUAzF93Kfs", 
            "https://drive.google.com/uc?export=view&id=1an4jFRqzD3b72Kb7KFRrVEOYs3cF604E", 
            "https://drive.google.com/uc?export=view&id=1atHmqqZ1sU0M_XdZmgbsIssNQe8DAhFU", 
            "https://drive.google.com/uc?export=view&id=1atUpRuQl1De6AvMDs-2sHmJYSfX8uBXK", 
            "https://drive.google.com/uc?export=view&id=1ahkwUg1yoc3LZ7yTtFw5Z5IOV_a5a8U1", 
            "https://drive.google.com/uc?export=view&id=1bKAeTkIgx7yf8c_tfPbDFqNCoYsaOysG", 
            "https://drive.google.com/uc?export=view&id=1aoYYkEcvLLRPt8nurGaaG5Hdcok0gPk_", 
            "https://drive.google.com/uc?export=view&id=1bGqSJ9aduolUPygf54FMn_x7Q-5FGcdb", 
            "https://drive.google.com/uc?export=view&id=1bLPpfDmLf0wW_x4NgjUlKKljHQu-MLTe", 
            "https://drive.google.com/uc?export=view&id=1aqOeDkRcvzO7CI4w_zZkeqoXd17byqAm", 
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
                "kesan": "Abang nya asik dan juga banyak cerita pengalamannya serta memberikan ilmu baru",  
                "pesan": "Semoga di perlancar ya bang kuliahnya dan jaga kesehatan selalu!"
            },
            {
                "nama": "Chatrine Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "Kakak nya asik dan juga murah senyum",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Pasaruntung",
                "hobbi": "Mengoleksi Dino",
                "sosmed": "@akbar_restika",
                "kesan": "Abang nya seru dan ramah",  
                "pesan": "Semangat terus kuliahnya bang agar bisa lulus tepat waktu dan jangan lupa jaga kesehatan!"
            },
            {
                "nama": "Renita Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Membaca dan Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakak nya baik banget dan ramah juga",  
                "pesan": "Sukses ke depannya kak!"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "Kakak nya seru dan juga murah senyum",  
                "pesan": "Semangat mengejar mimpi nya kak!"
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "Abang nya asik dan juga ramah",  
                "pesan": "Sukses selalu dan tetap semangat bang!"
            },
            {
                "nama": "Yosia Retare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi": "Nungguin ayam betina berkokok",
                "sosmed": "@yosiabanurea",
                "kesan": "Abang nya baik dan asik",  
                "pesan": "Semangat belajar nya bang!"
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "Abang nya baik dan juga banyak cerita pengalamannya",  
                "pesan": "Jangan lupa jaga kesehatan ya bang dan tetap semangat!"
            },
            {
                "nama": "Rani Puspita sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Kakak nya seru dan juga baik",  
                "pesan": "Sukses terus ya kak semangat belajar nya!"
            },
            {
                "nama": "Azizah Kusuma Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "Kakak nya baik dan ramah juga",  
                "pesan": "Semangat terus kuliahnya kak agar bisa lulus tepat waktu!"
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@meirasty_",
                "kesan": "Kakak nya seru dan asik",  
                "pesan": "Semangat terus untuk menggapai mimpi nya kak!"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Berenang di Laut",
                "sosmed": "@rexander",
                "kesan": "Abang nya asik dan juga baik",  
                "pesan": "Sukses selalu ya bang semangat!!"
            },
        ]

        display_images_with_data(gambar_urls, data_list)
    departemeninternal()

elif menu == "Departemen SSD":
    def departemenssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YGtrSqVeXHSYt6y5CnZNR-At3sDSpPdU", 
            "https://drive.google.com/uc?export=view&id=1NUMbNM0x4scCVeGvzbdYlqxnlriOK5am", 
            "https://drive.google.com/uc?export=view&id=1NrWZ0JnVCK10RjtSY98m3mMq1MKcIAxU", 
            "https://drive.google.com/uc?export=view&id=1Nrw2F3emgRluFg1FfFcgnucqn8-SLJcm", 
            "https://drive.google.com/uc?export=view&id=1Nh-ooYUjYBV2cgufiEOFNuXFs9Y0tbWd", 
            "https://drive.google.com/uc?export=view&id=1NkOS1pjsdB48C1OSA7ZO4fvIhGDDpWX4", 
            "https://drive.google.com/uc?export=view&id=1NQOAsf2-SXdAkuJtOH7huwpV35yJDugu", 
            "https://drive.google.com/uc?export=view&id=1YCV8LstdIWwFiGFD2Emh1a8tcIYhywnm", 
            "https://drive.google.com/uc?export=view&id=1NNEjok47rj_wchS5G98HRY27-RStvh0k", 
            "https://drive.google.com/uc?export=view&id=1Nw7rve1lnUYLL7orasIMaJGvyD-neGuV", 
            "https://drive.google.com/uc?export=view&id=1Nn9SP9YQm5-cgcYScTZnsO57h-hzYJZi", 

        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "21",
                "asal":"Panjibako",
                "alamat": "Jl. Bel",
                "hobbi": "Mencari Uang",
                "sosmed": "@andriangaol",
                "kesan": "Abang nya baik dan banyak memberikan ilmu serta pengalamannya",  
                "pesan": "Semangat terus kuliahnya bang sukses terus!"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Kakak nya asik dan juga ramah",  
                "pesan": "Semangat terus kuliahnya kak agar bisa lulus tepat waktu!"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal":"Simalungun, Sumut",
                "alamat": "Airan",
                "hobbi": "Hitung uang",
                "sosmed": "@zhjung_",
                "kesan": "Kakak nya baik dan murah senyum",  
                "pesan": "Semangat terus belajar nya kak!"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Bukittinggi",
                "alamat": "Airan",
                "hobbi": "Badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "Abang nya asik dan juga baik",  
                "pesan": "Semoga lulus tepat waktu ya bang kuliah nya semangat!"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Nyuruh-nyuruh",
                "sosmed": "@dananghk_",
                "kesan": "Abang nya baik banget, seru, dan juga banyak memberikan ilmu dan pengalamannya",  
                "pesan": "Semangat terus kuliahnya bang agar bisa lulus tepat waktu dan sukses terus untuk ke depannya!"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Lapas",
                "hobbi": "Apa aja",
                "sosmed": "@farrel_julio",
                "kesan": "Abang nya asik dan banyak memberi ilmu baru",  
                "pesan": "Sukses terus dan tetap semangat bang!"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Simalungun, Sumut",
                "alamat": "Pemda",
                "hobbi": "Suka nulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakak nya baik banget dan juga ramah",  
                "pesan": "Jaga kesehatan selalu ya kak semangat!"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal":"Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Kakak nya asik dan juga seru",  
                "pesan": "Semangat terus kuliahnya kak dan jangan lupa jaga kesehatan!"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "Nonton windah",
                "sosmed": "@alviagnting",
                "kesan": "Kakak nya murah senyum dan juga ramah",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Balam",
                "alamat": "Jalan Nangka 1",
                "hobbi": "Tidur",
                "sosmed": "@dhafinrzqa",
                "kesan": "Abang nya baik dan juga seru",  
                "pesan": "Semoga di perlancar kuliah nya ya bang!"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Badminton",
                "sosmed": "@meylanielia",
                "kesan": "Kakak nya seru dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus untuk mengejar mimpi nya ya kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenssd()

elif menu == "Departemen MEDKRAF":
    def departemenmedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1cy6Xj2D_Mfv6ZEBGYmT7XUnhk_FPOy4t", 
            "https://drive.google.com/uc?export=view&id=1cnhdMzpSb-OAAJsH3fEfKUsPjOoD3bnV", 
            "https://drive.google.com/uc?export=view&id=1cOtl7GDJ55ORviqEIVIO9-FSSj7p3L9T", 
            "https://drive.google.com/uc?export=view&id=1cWHI43CVGTz3PKZu3FIb-SDArZ5QnsjM", 
            "https://drive.google.com/uc?export=view&id=1cWcjdy8va2gLfpgiWD8MV0tkaBXjMpxS", 
            "https://drive.google.com/uc?export=view&id=1cONgiid0sez8VLsomIS8oG8TxyMAh3tX", 
            "https://drive.google.com/uc?export=view&id=1cU0jacaLcx6EWpi9zTBRi0xzmGCmgD6V", 
            "https://drive.google.com/uc?export=view&id=1cuKKjBBgPYQDL8rD0T-gOB8NSa3un6xI", 
            "https://drive.google.com/uc?export=view&id=1cM0w7GJ3MBHZb8DEz4PKq29Y3FBageDI", 
            "https://drive.google.com/uc?export=view&id=1cqDA-fIh5sXkGLBJh_uBgHZ4t7AbrSX4", 
            "https://drive.google.com/uc?export=view&id=1d-bSXg6GtpklnGQx0atCC_xIRRVnX6BH", 
            "https://drive.google.com/uc?export=view&id=1d19buZjHK_OT4n6-RnZiYhfQTow7aRzb", 
            "https://drive.google.com/uc?export=view&id=1cdVDGZS5N1wIM-fZPu6vaCjzOpsGQh_n", 
            "https://drive.google.com/uc?export=view&id=1cqPmKF4GDsJq2QExuhcOtg1ABHb2bnoU", 
            "https://drive.google.com/uc?export=view&id=1cKGQNWnHgdQXMZMnr-je656zQyyHlqdL", 
            "https://drive.google.com/uc?export=view&id=1csYAX0fUzjbq75M9gSqGqaXXfRS0XJeH", 
            "https://drive.google.com/uc?export=view&id=1ciOszcu_x-qUGWwBAAyb9-hRuxA-xHTo", 
            "https://drive.google.com/uc?export=view&id=1cMoHHBVikSxpNBGDnTrtlqA7JCCUi3DJ", 
            "https://drive.google.com/uc?export=view&id=1cQdnlsJZ-DG2_BKerox5aagWIA3v1jK7", 
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
                "kesan": "Abang nya baik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya bang agar bisa lulus tepat waktu!"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "Kakak nya baik banget dan murah senyum juga",  
                "pesan": "Sukses terus ke depannya kak jaga kesehatan nya ya!"
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Nugas",
                "sosmed": "@arsyiah._",
                "kesan": "Kakak nya seru dan juga ramah",  
                "pesan": "Semangat kuliah nya kak!"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Lagi Nyari",
                "sosmed": "@dino_kiper",
                "kesan": "Abang nya asik dan seru",  
                "pesan": "Semangat terus bang dan sukses untuk ke depannya!"
            },
            {
                "nama": "Muhammad Arsal Ranjana Putra",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 4",
                "hobbi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "Abang nya seru dan banyak memberi ilmu",  
                "pesan": "Jangan lupa jaga kesehatan bang semangat!"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Kakak nya baik banget dan ramah",  
                "pesan": "Semangat terus kak buat ke depannya!"
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": "122450045",
                "umur": "20",
                "asal": "Natar, Lampung Selatan",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "Kakak nya asik dan murah senyum juga",  
                "pesan": "Semangat belajar nya kak dan dijaga kesehatannya!"
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "Kakak nya seru dan ramah",  
                "pesan": "Semangat menggapai cita-cita nya kak sukses terus!"
            },
            {
                "nama": "Patricia Leondra Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton Film",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakak nya baik banget dan juga seru",  
                "pesan": "Semangat kuliahnya kak semoga lulus tepat waktu ya!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan": "Kakak nya ramah dan juga murah senyum",  
                "pesan": "Jaga kesehatan selalu ya kak semangat terus ya!"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakak nya baik dan ramah",  
                "pesan": "Semangat terus kuliahnya kak agar bisa lulus tepat waktu!"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi": "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan": "Kakak nya baik dan asik",  
                "pesan": "Semangat terus dan sukses selalu kak1"
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "Abang nya seru dan juga asik",  
                "pesan": "Jaga kesehatan dan semangat terus belajar nya bang!"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi": "Nonton Drakor",
                "sosmed": "@nsywanaf",
                "kesan": "Kakak nya baik dan banyak cerita pengalamannya",  
                "pesan": "Sukses selalu ya kak!"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Baca Novel yang Bikin Nangis",
                "sosmed": "@prskslv",
                "kesan": "Kakak nya ramah dan baik juga",  
                "pesan": "Sukses terus dan semangat ya kak!"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa, Labuhan Dalam",
                "hobbi": "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan": "Abang nya asik dan juga memnceritakan pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak agar bisa lulus tepat waktu dan jangan lupa jaga kesehatan!"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "_akmal.faiz",
                "kesan": "Abang nya baik dan juga ramah",  
                "pesan": "Selalu jaga kesehatan bang dan tetap semangat ya!"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani)",
                "hobbi": "Bengong/Membaca Buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Abang nya baik dan juga seru",  
                "pesan": "Selalu semangat terus ya bang sukses ke depannya!"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi": "Mengerjakan Tugas",
                "sosmed": "@khusnun_nisa335",
               "kesan": "Kakak nya baik banget dan ramah juga",  
                "pesan": "Semangat belajar nya kak semoga lulus tepat waktu ya!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenmedkraf()
