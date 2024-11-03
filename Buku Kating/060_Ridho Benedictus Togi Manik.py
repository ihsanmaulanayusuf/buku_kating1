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
            "https://drive.google.com/uc?export=view&id=1MUoy48hnTDmw862b__HBv84KzvsB1P2E",
            "https://drive.google.com/uc?export=view&id=1UE8koIJO0QFZiw1syIXW8x0VIgR6AAS5",
            "https://drive.google.com/uc?export=view&id=1j93CZAzBcWfl1BOvknA_QznVyDe9437X",
            "https://drive.google.com/uc?export=view&id=1aq38Xj9nTdSZL8XgBGOLAN3oREyxtdhK",
            "https://drive.google.com/uc?export=view&id=1uVuhFJ8APh-2bpfdEXbSty7_KQPq5tya",
            "https://drive.google.com/uc?export=view&id=1IjcK89ecGINA--F6IDLnHrOf5mi-KH-p",
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
                "kesan": "Abang ini punya kharisma yang keren seperti namanya, dan punya pengetahuan yang luas",  
                "pesan":"sukses terus bang, semoga mendapatkan apa yang abang mau kedepannya, dan sukses selalu dimanapun abang berada"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Bukit Kemuning",
                "alamat": "Pawen 2 Sukarame",
                "hobbi": "Main Gitar",
                "sosmed": "@pndrinsni21",
                "kesan": "Abang ini asik banget, keren jugaa",  
                "pesan":"semangat terus bang pandra, sukses selalu dimanapun abang berada"#2
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kotabaru",
                "hobbi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak ini asik, lucu, dan mudah diajak diskusi",  
                "pesan":"semangat terus kak"#3
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin  bang Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak ini asik, pintar",  
                "pesan":"semangat terus kak kuliahnya" #4
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak ini asik, mau diajak diskusi, dan murah senyum",
                "pesan":"semangat terus kuliahnya kak" #5
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Kotabaru",
                "hobbi": "Dengerin bang Pandra Gitaran",
                "sosmed": "@nadillaadr26",
                "kesan": "Kakak ini baik, asik, dan punya pemikiran yang luas",
                "pesan":"sukses terus kakk" #6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=138unPpPfnex4eHeQS5OFRzE00rI_BLEz",
            "https://drive.google.com/uc?export=view&id=1i-G72_aSknAR5YCzswphhMcuPeRIzudv",
            "https://drive.google.com/uc?export=view&id=18FvIi-_-goWdCgZL3WBwFErgJDCmHc1Q",
            "https://drive.google.com/uc?export=view&id=1CBWB3k63m74FfMVXluOhzlCCsXZrITlU",
            "https://drive.google.com/uc?export=view&id=1N5fBKp4w0pPnpkpZfb2Ia_Qj6GlehRhj",
            "https://drive.google.com/uc?export=view&id=1-x4vdxyRLFjxE7VXfoGjvhnEq8N1Jzt_",
            "https://drive.google.com/uc?export=view&id=1kE-Vf2bXzTWuegDkJGRJqwKrM4MJrjj4",
            "https://drive.google.com/uc?export=view&id=1dvjCPjDmPRq4wHJgZHReNEDT8tMRomhH",
            "https://drive.google.com/uc?export=view&id=1uO0agW2O9BVa7qyP-PuqKVxpVc9UyMRa",
            "https://drive.google.com/uc?export=view&id=1cGyjJd87QdI2aaMp1uEXTDhs7dFEPICg",
            "https://drive.google.com/uc?export=view&id=1u_iSPSN5hDhrc3Oryx_--UsgJbTXd6Od",
            "https://drive.google.com/uc?export=view&id=1aoK6kfwuExdrSPGJG6YdaNcVCEQ8kGQc",
            "https://drive.google.com/uc?export=view&id=17zZ9IYQ3pVDKIUagZlkENjRXOY7-Lic2",
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
                "kesan": "Kakak ini menyenangkan banget, murah senyum, dan punya pemikiran yang luas",  
                "pesan":"semangat terus kuliahnya, jaga kesehatan, dan bahagia selalu!" #7
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "122450000",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Way Hui",
                "hobbi": "Membaca",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak ini baik dan ramah banget",  
                "pesan":"semangat terus kuliahnya kak, bahagia selalu!"#8
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton Film",
                "sosmed": "@wlsbn0",
                "kesan": "Kakak ini asik, baik, punya pemikiran yang luas",  
                "pesan":"semangat terus kuliahnya dan menjalani kehidupan ini kak !"#9
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "Kakak ini asik, ramah, mau membagikan pengalaman dan pemikirannya",  
                "pesan":"sukses terus kak!" #10
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal": "Bernung, Pesawaran",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak ini baik, ramah, dan keren",
                "pesan": "semangat dan sukses terus kak, bahagia selalu!" #11
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Abang ini baik, ramah, dan jago alpro",
                "pesan": "Sukses terus bang dan semangat menjalani hidup ini!" #12
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Baca Al-Qur’an",
                "sosmed": "@fleurnsh",
                "kesan": "Kakak ini baik dan ramah",
                "pesan": "Semangat terus kuliahnya kak!" #13
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak baik, ramah, murah senyum, dan open minded",
                "pesan": "Semangat terus kak dan jangan lupa unutk bahagia" #14
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abang ini baik, ramah, mau juga ngobrol-ngobrol santai",
                "pesan": "Semangat terus bang, semoga apa yang abang mau terkabulkan" #15
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal": "Ogan Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari Sinyal di Gedung F",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak ini menyenangkan banget, asik, dan suka ngejokes",
                "pesan": "Semangat kuliahnya dan bahagia selalu ya kak" #16
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450126",
                "umur": "22",
                "asal": "Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Melukis",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abang ini ramah banget, baik, dan santaii",
                "pesan": "Semangat terus bang kuliahnya" #17
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal": "Sumatra Barat",
                "alamat": "Way Huwi",
                "hobbi": "Baca Buku, Ngoding, Ibadah",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini baik dan ramah",
                "pesan": "Semangat kuliahnya kak" #18
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Billabong, Gedong Air",
                "hobbi": "Suka Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang ini baik, ramah, suka ngejokes",
                "pesan": "Semangat terus kuliahnya bang dan sukses selalu apa yang abang lakukan" #19
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1TnU0arNMv-kXSeD5AHsim59_Zb1_kA0_", #20
            "https://drive.google.com/uc?export=view&id=16RTv-L8lgwPqYnXnezYiMyrNVydRwouU", #21
        ]
        data_list = [
            {
                "nama": "Anissa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal":"Lampung Tengah",
                "alamat": "Kos Putri Rahayu",
                "hobbi": "Bernyanyi",
                "sosmed": "@annisalutfia_",
                "kesan": "Kakak ini asik sekali, friendly, public speakingnya juga bagus, tegas, dan memiliki pemahaman yang luas",  
                "pesan":"Semangat terus kuliahnya kak, dan jangan lupa untuk terus tersenyum" #20
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abang ini tegas, asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus bang, sukses selalu dengan apa yang abang lakukan" #21
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def departemenpsda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1NcUcdC7OnzBewdFTtjDBA2FxV8DBYc9I", #22
            "https://drive.google.com/uc?export=view&id=1QYSTOlwJ7f5ZP-bjMry3YUQS2oIiKaWP", #23
            "https://drive.google.com/uc?export=view&id=1ROwkaQx-TdIHgkImMAY68glWMEkC2YC_", #24
            "https://drive.google.com/uc?export=view&id=1oi7ksKS4VX3NiWAPJV4hGXox1E3Pv5if", #25
            "https://drive.google.com/uc?export=view&id=1kc3L4WDz_rU2I4w64hWPmS3ahHAo019J", #26
            "https://drive.google.com/uc?export=view&id=1tpp3oW03lcDf1Ja3cYctAFJBk1DsRuEL", #27
            "https://drive.google.com/uc?export=view&id=1QzbbWQGFO3d8J3nhTqiTY2YKXStYe2Pi", #28
            "https://drive.google.com/uc?export=view&id=1-Jwk4QD73N-eqgVHThxcCBKcYiqbnviM", #29
            "https://drive.google.com/uc?export=view&id=14h1CfeEZ_0l0USQ29LO3pIViBTZNTn3S", #30
            "https://drive.google.com/uc?export=view&id=1SLaMwTobBogriMe3C9D4DbzT8f-0XtE_", #31
            "https://drive.google.com/uc?export=view&id=1UT1n8axPkDBFHWWRkEVmCwS0zndCDmWR", #32
            "https://drive.google.com/uc?export=view&id=1nrs4kPPxWNyrYyrPvfFMPTwsO_Jt4ZuF", #33
            "https://drive.google.com/uc?export=view&id=1HNmT_UIDwKfNlIOQop1bFlTrvDzvjuDL", #34
            "https://drive.google.com/uc?export=view&id=13RbHt4K3B-NkwX0UNufDgE2BqtaSAO4f", #35
            "https://drive.google.com/uc?export=view&id=1nrs4kPPxWNyrYyrPvfFMPTwsO_Jt4ZuF", #36
            "https://drive.google.com/uc?export=view&id=1uZZi5rcn8rWELyr3csaBfnQhUW7R1kjZ", #37
            "https://drive.google.com/uc?export=view&id=13f7Eyk-JBHphIKwhl8-WH1AtLrYjOy_R", #38
            "https://drive.google.com/uc?export=view&id=1tWcHQoYtStLAC3R1ggsWL1gXrlcfl0Ic", #39
            "https://drive.google.com/uc?export=view&id=1YTEVLJr4KAbeEMNYQRgw5oxOFue9KZ4L", #40
            "https://drive.google.com/uc?export=view&id=1YLe6a7Bkh9-oS4Li-xa6o9uG7YH3zIt3", #41
            "https://drive.google.com/uc?export=view&id=1F4GDJcmrpVzVQDsyny3x7iJchBC4jF9o", #42
            "https://drive.google.com/uc?export=view&id=1GAVpQHt2dE1uhoB5Z4hN8_s3UhOJ71d6", #43
            "https://drive.google.com/uc?export=view&id=1zgTjoEa7VLpz-8CZbz8aoNn31QJMbIvF", #44
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Khobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abang ini asik sekali, tegas, punya pemikiran yang luas, dan seru untuk diajak diskusi",  
                "pesan":"Semangat terus kuliahnya bang, semoga bisa cepat lulus dengan hasil yang memuaskan, dan sukses selalu dimanapun abang berada" #22
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabeth",
                "kesan": "Kakak ini asik, ramah, dan tegas",  
                "pesan":"Semangat terus kak kuliahnya, semoga mendapat hasil yang terbaik" #23
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Marahin orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak ini asik, baik, friendly, murah senyum, dan tegas",  
                "pesan":"Semangat terus kak kuliahnya, sukses selalu" #24
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyaislami_",
                "kesan": "Kakak ini tegas, murah senyum, dan punya public speaking yang bagus",  
                "pesan":"Semangat terus kak kuliahnya" #25
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiyati",
                "nim": "122450001",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Metro",
                "hobbi": "Nyopet",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini asik, tegas, pintar, lucu, friendly, dan jago ads",  
                "pesan":"Semangat terus kak, semoga sukses dalam perkuliahan dan lainnya" #26
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Bengong",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini murah senyum, baik, tegas, dan friendly",  
                "pesan":"Semangat kuliahnya kakak, semoga mendapat hasil yang baik" #27
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Jalan Pangeran Senopati Raya 18",
                "hobbi": "Baca Kitab Suci",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abang ini asik, baik, seru diajak ngobrol-ngobrol santai",  
                "pesan":"Semangat terus bang kuliahnya, semoga hasil yang didapat sesuai dengan apa yang abang inginkan" #28
            },
            {
                "nama":  "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jalan Pagar Alam Kedaton",
                "hobbi": "Ngukur jalan",
                "sosmed": "@dransyh_",
                "kesan": "Abang ini asik, baik, ramah, seru diajak ngobrol-ngobrol santai",  
                "pesan":"Semangat terus bang kuliahnya dan semangat menjalani hidup ini bang" #29
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Travelling",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakak ini baik, tegas, punya pemikiran yang luas dan murah senyum ",  
                "pesan":"Semangat terus kuliahnya kak jangan lupa untuk selalu tersenyum" #30
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "1214500148",
                "umur": "21",
                "asal":"Duri, Riau",
                "alamat": "Pulau Damar Kobam",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abang ini asik, baik, friendly, seru diajak ngobrol, dan suka ngelawak",  
                "pesan":"Semangat terus bang kuliahnya, sukses dimanapun abang berada" #31
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
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
                "hobbi": " ",
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
                "hobbi": "Asprak",
                "sosmed": "@johanneskrsjnnn",
                "kesan": "Abang ini tegas, asik, friendly, dan enak diajak ngobrol",  
                "pesan":"Semangat terus bang kuliahnya, semoga yang abang inginkan terkabulkan" #34
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Golf Asri",
                "hobbi": "Ngetik print hello dunia",
                "sosmed": "@kemasverii",
                "kesan": "Abang ini pinter, baik, asik, seru diajak ngobrol santai dan diskusi tentang perkuliahan",  
                "pesan":"Semangat terus bang kuliahnya, sukses terus di semua bidang yang abang tekuni" #35
            },
            {
                "nama": "Leonard Andreas Napitupulu",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@-",
                "kesan": "Abang ini baik, asik, dan ramah",  
                "pesan":"Semangat terus bang" #36
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin The Adams",
                "sosmed": "@presilliamg",
                "kesan": "Kakak ini asik, baik, ramah, dan murah senyum",  
                "pesan":"Semangat terus kak kuliahnya dan bahagia teruss" #37
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450122",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak ini asik, mempunyai pemikiran yang luas, dan murah senyum",  
                "pesan":"Semangat terus kuliahnya kakak, bahagia selalu ya" #38
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok, Jawa Barat",
                "alamat": "Jalan Airan Raya",
                "hobbi": "Dengerin juicy luicy",
                "sosmed": "@sahid_maul19",
                "kesan": "Abang ini asik, baik, mempunyai public speaking yang bagus, dan enak diajak diskusi ataupun ngobrol",  
                "pesan":"Semangat terus bang kuliahnya, semoga mendapat apa yang abang inginkan" #39
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Minum kopi, belajar, bikin Deyvan senang",
                "sosmed": "@roselivness__",
                "kesan": "Kakak ini tegas, asik, mempunyai public speaking yang bagus, jago banget main basket",  
                "pesan":"Semangat terus kuliahnya kak, tetap jadi diri kakak sendiri ya" #40
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Abang ini, asik, orangnya santai diajak ngobrol, friendly, suka menolong public speaking yang bagus",  
                "pesan":"Semangat terus bang kuliahnya, sukses terus dimanapun abang berada" #41
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "Abang ini asik, baik, enak diajak ngobrol santai",  
                "pesan":"Semangat terus bang kuliahnya semoga cepat lulus dengan nilai yang bagus" #42
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv",
                "kesan": "Kakak ini asik, baik, ramah banget",  
                "pesan":"Semangat terus kak, bahagia selalu" #43
            },
            {
                "nama":  "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Abang ini asik, baik, ramah, dan murah senyum",  
                "pesan":"Sukses terus bang di setiap bidang yang ditekuni" #44
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenpsda()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen MIKFES":
    def departemenmikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1w_ogFe6bp60To3vLDleVq4zrUqeH4n3G", #45
            "https://drive.google.com/uc?export=view&id=1gjiDzQKCZ7hQPG2qb-8Ci49wd-YJr1TH", #46
            "https://drive.google.com/uc?export=view&id=1OpsF_PKNM4wlY6P5awadUWjkTVEhUXo-", #47
            "https://drive.google.com/uc?export=view&id=1C3GndP8m7d8elj9Xu51m90_bd2ux_cYY", #48
            "https://drive.google.com/uc?export=view&id=1iZUzG-FSPOi6ecwgVzilS-1UY8pxX70Y", #49
            "https://drive.google.com/uc?export=view&id=1M05VMSY7hihbJLbYuXxc32uB79yctQL7", #50
            "https://drive.google.com/uc?export=view&id=1C3GndP8m7d8elj9Xu51m90_bd2ux_cYY", #51
            "https://drive.google.com/uc?export=view&id=1zCdJDHO5Yh1SxVK5xw3bSn8WGJ7K_cGF", #52
            "https://drive.google.com/uc?export=view&id=1zyou9ktaAe8Nvz0ABmCaF7_FxL9ZqHlj", #53
            "https://drive.google.com/uc?export=view&id=1AdEViTbD-tVJpcnWsSwNb_Evqd2_bVUJ", #54
            "https://drive.google.com/uc?export=view&id=1TWjDxx49_nL4GstRGbqqHBOJ1jDrhW2J", #55
            "https://drive.google.com/uc?export=view&id=1szWMaZU88kfA-Mokv_-WX7KJhQoAERHf", #56
            "https://drive.google.com/uc?export=view&id=12EeQSYzSjmuzZe4HNpYtG0o-hVOZaEFK", #57
            "https://drive.google.com/uc?export=view&id=1C3GndP8m7d8elj9Xu51m90_bd2ux_cYY", #58
            "https://drive.google.com/uc?export=view&id=1coETCqT6tRkRtXK-rrhWCGidnsCzhEA-", #59
            "https://drive.google.com/uc?export=view&id=1LMOYShXKYJHCha0buWPWyd3jiKNLUcBq", #60
            "https://drive.google.com/uc?export=view&id=1hZoUSyLfj0Wt5M48NhXs4w17PHTgxwLW", #61
            "https://drive.google.com/uc?export=view&id=1C3GndP8m7d8elj9Xu51m90_bd2ux_cYY", #62
            "https://drive.google.com/uc?export=view&id=1PHc4EOHS1M6Hz-48j_sdCiQu9U6TM08E", #63
            "https://drive.google.com/uc?export=view&id=1wven5EYxejrmPRoMatEwDqcS6ND3olsH", #64
            
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
                "kesan": "Abang ini pintar, baik, punya publik speaking yang bagus, dan pemikiran yang luas",
                "pesan": "Semangat terus bang kuliahnya, dan sukses terus baik di perkuliahan maupun di luar perkuliahan", #45
                
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Kakak ini baik, ramah, pintar, dan murah senyum",
                "pesan": "Semangat terus kuliahnya kak, semoga apa yang kakak ingini dapat terkabulkan!", #46
                
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Abang ini pintar, asik diajak ngobrol, baik, dan murah senyum",
                "pesan": "Semangat terus bang dan selalu jadi diri sendiri ya bang", #47
                
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Abang ini pintar, baik, punya pemikiran yang luas",
                "pesan": "Semangat terus kuliahnya bang, semoga dapat hasil yang memuaskan!", #48
                
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "Abang ini asik, baik, punya publik speaking yang bagus, dan friendly",
                "pesan": "Semangat terus bang dan sukses selalu dimanapun abang berada", #49
                
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakak ini pintar, asik, baik dan murah senyum",
                "pesan": "Semangat terus kuliahnya kak, bahagia selalu ya kak!", #50
                
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "121450107",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kemiling",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": "@natanaeloks",
                "kesan": "Abang ini asik, ramah, punya pemikiran yang luas, dan murah senyum",
                "pesan": "Sukses terus bang baik di perkuliahan maupun diluar perkuliahan", #51
                
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "Abang ini pintar, baik, jago strukdat, dan enak diajak ngobrol",
                "pesan": "Semangat terus kuliahnya bang, semoga mendapat hasil yang abang ingikan!", #52
               
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "Kakak ini asik, baik, ramah, enak diajak diskusi",
                "pesan": "Semangat terus kuliahnya kak dan jangan lupa untuk bahagia ya kak!", #53
                
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "",
                "sosmed": "@dindanababan_",
                "kesan": "Kakak ini baik, pintar, dan murah senyum",
                "pesan": "Semangat terus kuliahnya kak, bahagia selalu!", #54
                
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak ini pintar, asprak matdas waktu TPB, dan murah senyum",
                "pesan": "Semangat terus ya kuliahnya kak dan selalu menjadi diri kakak yang seperti ini ya kak", #55
               
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak ini pintar, baik, dan murah senyum",
                "pesan": "Semangat terus kuliahnya kak, sukses selalu di bidang yang kakak tekuni!", #56
                
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini baik dan ramah",
                "pesan": "Semangat kuliahnya kak, semoga apa yang kakak inginikan, bisa didapatkan", #57
               
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": "121450128",
                "umur": "23",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "Abang ini baik, pintar, dan punya pemikiran yang luas",
                "pesan": "Semangat terus bang kuliahnya, semoga mendapatkan apa yang abang inginkan", #58
               
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "Abang ini apintar, baik, dan murah senyum",
                "pesan": "Semangat terus kuliahnya bang, sukses selalu dimanapun abang berada!", #59
               
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "Abang ini pintar, baik, asik, dan ramah banget",
                "pesan": "Semangat terus kuliahnya bang, semoga segala hal yang abang impikan dan terkabulkan!", #60
                
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakak ini pintar, asik dan ramah",
                "pesan": "Semangat terus kuliahnya kak, bahagia selalu kak!", #61
               
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Kakak ini baik dan ramah",
                "pesan": "Semangat terus kuliahnya kak dan happy terus kak seperti namanya!", #62
                
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Jl Nangka 3",
                "hobbi": "Berolahraga",
                "sosmed": "@randardn",
                "kesan": "Abang ini pintar, baik, ramah, dan enak diajak diskusi",
                "pesan": "Semangat terus bang dan tetaplah menjadi diri sendiri ya bang", #63
                
            },
                        {
                "nama": "Mujadid Choirus Surya",
                "nim": "122450113",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "rahm_adityaa",
                "kesan": "Abang ini pintar, baik",  
                "pesan":"Semangat terus bang, dan sukses selalu" #64
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenmikfes()

elif menu == "Departemen Eksternal":
    def departemeneksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_La1rCOob_6mJ0O0MrBO2S_52lG3ol7M", #66
            "https://drive.google.com/uc?export=view&id=1VoCTJbveQ2gVEnBtLmBm4W3-2E3R6kWd", #67
            "https://drive.google.com/uc?export=view&id=1CAUTqi5ye2377WgwbQocDX4KaCAX7GhE", #68
            "https://drive.google.com/uc?export=view&id=1Zt9-df-4g2GFJdLN9K9dyY3VwDj62Ol7", #69
            "https://drive.google.com/uc?export=view&id=1NzMPD3aKx6vJUIRDCfiymbBUTSsh5LCU", #70
            "https://drive.google.com/uc?export=view&id=1-9R9ZlKdLYUoJUTsufwNFs4tZkTpaQq8", #71
            "https://drive.google.com/uc?export=view&id=1WHZ0BzKhuBXQolW-H8jIkuzoRIc9jtBa", #72
            "https://drive.google.com/uc?export=view&id=1_bL8OeY6UOvozBZivFwRpiQLP7wIdQAK", #73
            "https://drive.google.com/uc?export=view&id=11hYUxBsPrDIR_k6H5TvTyOSSHYkB4xNlN", #74
            "https://drive.google.com/uc?export=view&id=1aOGjqUYogxyGnprVl8QJSg-DviNIQNiJ", #75
            "https://drive.google.com/uc?export=view&id=1_JM_IIWJrRCk2LlhHZJ18wHHKzU-b58H", #76
            "https://drive.google.com/uc?export=view&id=1FfiS1nxEHqbqs_PAaTxV3_H0kD-aAj46", #77
            "https://drive.google.com/uc?export=view&id=1VoCTJbveQ2gVEnBtLmBm4W3-2E3R6kWd", #78
            "https://drive.google.com/uc?export=view&id=10enipp2wDa4DPCz7t971xWaCCGyQyLpD", #79
            "https://drive.google.com/uc?export=view&id=1VoCTJbveQ2gVEnBtLmBm4W3-2E3R6kWd", #80
            "https://drive.google.com/uc?export=view&id=1zkUq94B5VWG0Xi1XkKEmszsbxHf6c7Rl", #81
            "https://drive.google.com/uc?export=view&id=1g2G9RIkJE3b13ofpLOtkY8zqp2An5IYX", #82
            "https://drive.google.com/uc?export=view&id=1LAKxwdzF49f81xhTzDfJmpGFJIn5wJg3", #83
            "https://drive.google.com/uc?export=view&id=1izDuAyvGkG6zT-ZdBbIoyZ0vGoD5CwjY", #84
            "https://drive.google.com/uc?export=view&id=1tsG9hxsxOfFUJEsyX5Bzwb1hpKclXnXu", #85
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Jati Mulyo",
                "hobbi": "Bangun Pagi",
                "sosmed": "@yogyyy",
                "kesan": "Abang ini asik, tegas, baik, pemikirannya luas, dan bagus dalam komunikasi",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #66
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450031",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "TVRI",
                "hobbi": "Jalan-jalan",
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
                "hobbi": "Belajar",
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
                "hobbi": "Main Game",
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
                "hobbi": "Dengerin musik",
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
                "hobbi": "Kirim BC-an",
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
                "hobbi": "Olahraga",
                "sosmed": "Tidur",
                "kesan": "Kakak ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus kakak kuliahnya" #72
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jadi Humas",
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
                "hobbi": "Pulang malam",
                "sosmed": "@jasminednva",
                "kesan": "Kakak ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus kakak kuliahnya" #74
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Berkebun",
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
                "hobbi": "Menimba ilmu",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak ini asik, baik, murah senyum, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus kak kuliahnya, semoga setiap hasil ujiannya memuaskan" #76
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin Portofolio",
                "sosmed": "@rzkdrnnn ",
                "kesan": "Abang ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya" #77
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "121450143",
                "umur": "21",
                "asal":"Lubuk Linggau, Sumatera Selatan",
                "alamat": "Jl. Nangka 4",
                "hobbi": "Olahraga",
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
                "hobbi": "Nyuci baju",
                "sosmed": "@-",
                "kesan": "Kakak ini asik, baik dan murah senyum",  
                "pesan":"Semangat terus kak kuliahnya" #79
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": " ",
                "sosmed": " ",
                "kesan": "Kakak ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #80
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abang ini asik, baik",  
                "pesan":"Semangat terus bang kuliahnya" #81
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Masak",
                "sosmed": "@izzalutfia",
                "kesan": "Kakak ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi",  
                "pesan":"Semangat terus bang kuliahnya" #82
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "daplok kelompok 1",
                "sosmed": "@alyaavanefi",
                "kesan": "Kakak ini cantik, baik banget, murah senyum, the best lah",  
                "pesan":"Semangat terus kak kuliahnya" #83
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Telat",
                "sosmed": "@rayths_",
                "kesan": "Abang ini baik dan ramah",  
                "pesan":"Semangat terus bang kuliahnya" #84
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Membaca chat",
                "sosmed": "@triayunanni",
                "kesan": "Kakak ini asik dan baik",  
                "pesan":"Semangat terus kak kuliahnya" #85
            },
         ]
        display_images_with_data(gambar_urls, data_list)
    departemeneksternal()

elif menu == "Departemen Internal":
    def departemeninternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1AtzC355zQJhjiqE_Aa14W7Db5UgpsdYq", #87
            "https://drive.google.com/uc?export=view&id=1Q0TgY65se4vjePd2NiLQjRDDlhWh-XoJ", #88
            "https://drive.google.com/uc?export=view&id=1F4gHOKavOOX9tB5ekYso4JZvOr1otn02", #89
            "https://drive.google.com/uc?export=view&id=1eoee80_-wAOc-zn0H85rrpOrqYF4-Syu", #90
            "https://drive.google.com/uc?export=view&id=1Y99GRWat2hJNFWRjeQG6C8hw-BHSIGll", #91
            "https://drive.google.com/uc?export=view&id=1aHJknp_hHy0DSXa6Oz4wL_45-qrSywMh", #92
            "https://drive.google.com/uc?export=view&id=1AagB0Zmw0hNztNTN039BYsawRXwlSFMB", #93
            "https://drive.google.com/uc?export=view&id=13e5LckINMz5_3IdV7i17CrgUh3DqihEt", #94
            "https://drive.google.com/uc?export=view&id=1nrs4kPPxWNyrYyrPvfFMPTwsO_Jt4ZuF", #95
            "https://drive.google.com/uc?export=view&id=1WbQbz-v2bx_uegPypYjnktjgLXlTGbbf", #96
            "https://drive.google.com/uc?export=view&id=1NSVQKrEF07caOr34ZfrbPRpcKRF2-g03", #97
            "https://drive.google.com/uc?export=view&id=1r53UP5JXaomLOpvDVNLDl-6IOj03Ueha", #98
            "https://drive.google.com/uc?export=view&id=1gaKRAlT4pLz0EmXS49h0gdPVWf7EcmZb", #99
            "https://drive.google.com/uc?export=view&id=1jN_T8nL_qJoOYIyBOb6CXznlcid2b7Pr", #100

        ]
        data_list = [
            {
                "nama": "Dimas Rizky Ramadhani",
                "nim": "121450027",
                "umur": "20",
                "asal":"Pamulang, Tangerang Selatan",
                "alamat": "Way Kandis Kobam",
                "hobbi": "Manjat tower sutet",
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
                "hobbi": "Baca novel",
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
                "hobbi": "Memelihara Dino",
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
                "hobbi": "Mengaji",
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
                "hobbi": "Nulis lagu",
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
                "hobbi": "Ngeliat cogan",
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
                "hobbi": "Main Futsal",
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
                "hobbi": "Bangun Pagi",
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
                "hobbi": "Bangun Pagi",
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
                "hobbi": "Menghalu",
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
                "hobbi": "menyanyi",
                "sosmed": "@alexanderr",
                "kesan": "Abang ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya" #97
            },
            {
                "nama": "Renita Siahaan",
                "nim": "122450112",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Mancing",
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
                "hobbi": "Bawa motor pake kaki",
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
                "hobbi": "Ngawinin cupang",
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
            "https://drive.google.com/uc?export=view&id=1lF3zMJuyO-OnjLz2ORq4rPgyqP5QQASl", #101
            "https://drive.google.com/uc?export=view&id=1MDT3RJwqsi3AVdcEu0H6AEuoo-evW5KX", #102
            "https://drive.google.com/uc?export=view&id=1Z_v7IAO_eSk4P1vPxC1In49N_NQEfsZB", #103
            "https://drive.google.com/uc?export=view&id=12NrsADCpTdP0qivRYElzxynVVglb3cdA", #104
            "https://drive.google.com/uc?export=view&id=1xIA0wTAs0mWwBbLKj2rDDNcCqTTCzFR0", #105
            "https://drive.google.com/uc?export=view&id=1VN3_HigIrsmkWJ87ZTWXzPTz8xJdxmZ_", #106
            "https://drive.google.com/uc?export=view&id=1ahlGq58hSym5h3NnyuRYxhlzJwyFU-6r", #107
            "https://drive.google.com/uc?export=view&id=1l5UZi5LbiP3nH0JtY3Sn8I6s-fzWkFwK", #108
            "https://drive.google.com/uc?export=view&id=1RHPuK3jT2-8G54-qe-zMKNROx4IaA_QJ", #109
            "https://drive.google.com/uc?export=view&id=1i1NNxUD7B40FcdbVT82QaATr0LNq5qA5", #110
            "https://drive.google.com/uc?export=view&id=1ejNhTi21zBrOFMaHm3S09rqBJXa9q--g", #111

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
                "kesan": "Abang ini asik, tegas, baik",  
                "pesan":"Semangat terus bang kuliahnya" #101
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Kakak ini asik, baik, dan seru ",  
                "pesan":"Semangat terus Kakak kuliahnya" #102
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal":"Simalungun, Sumut",
                "alamat": "Airan",
                "hobbi": "Hitung uang",
                "sosmed": "@zhjung_",
                "kesan": "Kakak ini asik, baik, dan seru",  
                "pesan":"Semangat terus kak kuliahnya" #103
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Bukittinggi",
                "alamat": "Airan",
                "hobbi": "Badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "Abang ini asik, baik",  
                "pesan":"Semangat terus bang kuliahnya" #104
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Nyuruh-nyuruh",
                "sosmed": "@dananghk_",
                "kesan": "Abang ini asik banget, baik, punya pemikiran yang luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya" #105
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Lapas",
                "hobbi": "Apa aja",
                "sosmed": "@farrel_julio",
                "kesan": "Abang ini asik, baik , dan seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya" #106
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Simalungun, Sumut",
                "alamat": "Pemda",
                "hobbi": "Suka nulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakak ini asik, baik",  
                "pesan":"Semangat terus kak kuliahnya" #107
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal":"Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Kakak ini asik, baik",  
                "pesan":"Semangat terus kak kuliahnya" #108
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "Nonton windah",
                "sosmed": "@alviagnting",
                "kesan": "Kakak ini asik, baik, dan ramah",  
                "pesan":"Semangat terus kak kuliahnya" #109
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Balam",
                "alamat": "Jalan Nangka 1",
                "hobbi": "Tidur",
                "sosmed": "@dhafinrzqa",
                "kesan": "Abang ini asik, baik",  
                "pesan":"Semangat terus bang kuliahnya" #110
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Badminton",
                "sosmed": "@meylanielia",
                "kesan": "Kakak ini asik, baik, dan bagus dalam komunikasi",  
                "pesan":"Semangat terus kakak kuliahnya" #111
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenssd()

elif menu == "Departemen MEDKRAF":
    def departemenmedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RBsMdwxVR-TpstcNVHSSXyCGoODIhXPc", #112
            "https://drive.google.com/uc?export=view&id=17xfXkWheASsparVgJapcdQ1lOzku8WYu", #113
            "https://drive.google.com/uc?export=view&id=1n9Ar9n0-DbpIOxw-qFb1W77ZoN1PnUaB", #114
            "https://drive.google.com/uc?export=view&id=1Vu4Fp6dWJHQdiAMtaumw5-wElDkHWNpD", #115
            "https://drive.google.com/uc?export=view&id=1JOc2zuM73Mv3YKrHTgyQP0mrP4_qTifW", #116
            "https://drive.google.com/uc?export=view&id=1nA6fBWkwYOO0AKUOAi66oNO_qoouk2U8", #117
            "https://drive.google.com/uc?export=view&id=10DcgQftUvcFqMA7lApH1OD-2TIhAph-E", #118
            "https://drive.google.com/uc?export=view&id=1kO06Y0BaFuOUoybm__2ydGp0VOFSUiuD", #119
            "https://drive.google.com/uc?export=view&id=1y66j79o1wvuvsM96QjFvpe-ko5AyovL9", #120
            "https://drive.google.com/uc?export=view&id=1EX2OweuMISOhCf9aLy1v4NfF0afKiGnW", #121
            "https://drive.google.com/uc?export=view&id=16-_tE2iW0_DUYVYgmIsZlDuKwPsCOJQx", #122
            "https://drive.google.com/uc?export=view&id=1diWd_DyYdarS0SdjqhFzYmUPGzIkGT8C", #123
            "https://drive.google.com/uc?export=view&id=1n0npaUZD8us82HMNmjvov-QDRZHeqWoY", #124
            "https://drive.google.com/uc?export=view&id=1v6Iqq5mzHXgO_aoVQ5X2KH8lD4MacppC", #125
            "https://drive.google.com/uc?export=view&id=1gby1IVMDhGm1SIICSiod89890GnwYCHd", #126
            "https://drive.google.com/uc?export=view&id=1RQk85zrMFPcQx6EQ8yt_OAPsMvS6naZp", #127
            "https://drive.google.com/uc?export=view&id=1Zp1sHuW2QaZm36nD5I7zt0PnQpBL8yUt", #128
            "https://drive.google.com/uc?export=view&id=1uebVBst2QCK3us1gYL-2L9r8r7h6zrba", #129
            "https://drive.google.com/uc?export=view&id=1X7XB3jmNzGVZDHRu5cgUv92eXWAtI5OF", #130
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
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!" #112
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!" #113
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Nugas",
                "sosmed": "@arsyiah._",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!" #114
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Lagi Nyari",
                "sosmed": "@dino_kiper",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!" #115
            },
            {
                "nama": "Muhammad Arsal Ranjana Putra",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 4",
                "hobbi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!" #116
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!" #117
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": "122450045",
                "umur": "20",
                "asal": "Natar, Lampung Selatan",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!" #118
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!" #119
            },
            {
                "nama": "Patricia Leondra Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton Film",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!" #120
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!" #121
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!" #122
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi": "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!" #123
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!" #124
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi": "Nonton Drakor",
                "sosmed": "@nsywanaf",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!" #125
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Baca Novel yang Bikin Nangis",
                "sosmed": "@prskslv",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!" #126
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa, Labuhan Dalam",
                "hobbi": "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!" #127
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "_akmal.faiz",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!" #128
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani)",
                "hobbi": "Bengong/Membaca Buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!" #129
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi": "Mengerjakan Tugas",
                "sosmed": "@khusnun_nisa335",
               "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!" #130
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenmedkraf()
