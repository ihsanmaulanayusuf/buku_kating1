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
            st.write(f"Nama        : {data_list[i]['nama']}")
            st.write(f"NIM         : {data_list[i]['nim']}")
            st.write(f"Umur        : {data_list[i]['umur']}")
            st.write(f"Asal        : {data_list[i]['asal']}")
            st.write(f"Alamat      : {data_list[i]['alamat']}")
            st.write(f"Hobi       : {data_list[i]['hobi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan       : {data_list[i]['kesan']}")
            st.write(f"Pesan       : {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=10JMTzZp346Jpvx4S7PRfMG7XXTYHmDXc",#1
            "https://drive.google.com/uc?export=view&id=1V00ajYtfybobCZxx3BtGLgxfgfgxMYvA",#2
            "https://drive.google.com/uc?export=view&id=1Tazku1SaObGy6LaXIviIlggP0FEWfPEy",#3
            "https://drive.google.com/uc?export=view&id=1bb-7cSuTgkoRezMkbdLUo-faMPZIdRMN",#4
            "https://drive.google.com/uc?export=view&id=1fC9Nho0n_A6sacyRUQzdPZ_Nt3q2W7ct",#5
            "https://drive.google.com/uc?export=view&id=1zp4MVBN-LEZdb5gvcFhf6zYmqlsC5ei2",#6
       
        ]
        data_list = [
            {
                "nama"  : "Kharisma Gumilang",
                "nim"   : "121450142",
                "umur"  : "21",
                "asal"  :"Palembang",
                "alamat": "Pulau Damar",
                "hobi" : "Dengerin musik",
                "sosmed": "@amsirahk",
                "kesan" : "Baik dan Keren banget",  
                "pesan" :"semangat terus kuliahnya bang"#1

            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450077",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobi": "Main gitar",
                "sosmed": "@pndrinsnptr2",
                "kesan": "Abangnya asik",  
                "pesan":"semangat terus kuliahnya bang"#2

            },
            {
               "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobi": "Nonton drakor",
                "sosmed": "@azilem",
                "kesan": "Kakaknya lucu",  
                "pesan":"semangat terus kuliahnya kakak!"#3

            },
            {
                "nama": "Hartiti Fadhilaj",
                "nim": "12145031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakaknya baik dan keren",  
                "pesan":"semangat terus kuliahnya kakak!" #4

            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Nangka 4",
                "hobi": "Dengerin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "kakaknya baik dan keren",  
                "pesan":"semangat terus kuliahnya kakak!"#5

            },
            {
               "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobi": "Dengerin bang Pandra Gitaran",
                "sosmed": "@azilem",
                "kesan": "kakaknya baik dan keren",  
                "pesan":"semangat terus kuliahnya kakak!" #6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ljb9SvoosMi5KmnZeK4zVxS7voKFkgcU",#1
            "https://drive.google.com/uc?export=view&id=1NjhtffCc82MtBFUSA2fzTAVC5_imxkkg",#2
            "https://drive.google.com/uc?export=view&id=10HlLY9RZ2J11NaAI-lcOv_6u1Ku6nBvh",#3
            "https://drive.google.com/uc?export=view&id=1Dp07vXIkUG2iC04B3wIEpvQCNVvxq4Z1",#4
            "https://drive.google.com/uc?export=view&id=1Ffk9SXS1tLeogQlM8nqmscilaqXUXQSE",#5
            "https://drive.google.com/uc?export=view&id=1gqKqs1xSchDmHs-yV6Hvbe2j_t7wNO3G",#6
            "https://drive.google.com/uc?export=view&id=1aHSlA8xzCqpjE3uVzhRNStT0zyX5POUo",#7
            "https://drive.google.com/uc?export=view&id=1mcaAXEfl3s1SelPYauHeh7YucCyRvxJn",#8
            "https://drive.google.com/uc?export=view&id=1XLwRMp-nUeR7mkaMEHv4Thx8NQKygWUg",#9
            "https://drive.google.com/uc?export=view&id=1hUiGkZy3YhqCfERBH08wPtevcIY9vPbM",#10
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#11
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobi": "Bertanya sama GPT",
                "sosmed": "@trimurniaa_",
                "kesan": "Kakaknya asik banget dan cara berkomunikasinya enak didengar",  
                "pesan":"semangat kak terus menginspirasi dan semangat kuliahnya!" #1

            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Way Hui",
                "hobi": "Membaca",
                "sosmed": "@annisacahyanisurya",
                "kesan": "kakaknya lucu dan asik",  
                "pesan":"semangat terus kuliahnya kak!" #2

            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Menonton Film",
                "sosmed": "@wlsbn0",
                "kesan": "kakaknya baik banget dan mukanya adem",  
                "pesan":"sukses terus kuliahnya kak!" #3

            },
            {
               "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jati Agung",
                "hobi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "cantik dan asik",  
                "pesan":"semangat terus kuliahnya kak!" #4

            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "abangnya baik",  
                "pesan":"semangat terus kuliahnya bang!" #5

            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobi": "Baca Al-qur’an",
                "sosmed": "@fleurnsh",
                "kesan": "Kakaknya baik dan lucu",  
                "pesan":"semangat terus kuliahnya kak!" #6

            },
            {
               "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "kakanya baik banget",  
                "pesan":"semangat terus kuliahnya kak!" #7

            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450110",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "tinggi banget",  
                "pesan":"jangan lupa kasih makan kucing bang" #8

            },
            {
                "nama": "Muhammad fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta",
                "alamat": "Sukarame",
                "hobi": "Melukis",
                "sosmed": "@fhrul.pdf",
                "kesan": "abangnya baik banget",  
                "pesan":"semangat terus kuliahnya bang!" #9

            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Suka Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "Abangnya keren dan baik ",  
                "pesan":"semangat terus kuliahnya bang" #10

            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Way Huwi",
                "hobi": "Baca Buku, Ngoding, Ibadah",
                "sosmed": "@berlyyanda",
                "kesan": "kakaknya baik dan seru",  
                "pesan":"semangat terus kuliahnya kak!" #11
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator ():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1W416RWlfUso17VcEJ7JOF6mZk4U62WWo",#1
            "https://drive.google.com/uc?export=view&id=1Uo7U9JXLSgCoj6eCVV1gj8O3Z00JLEaJ",#2
        ]
        data_list = [
            {
                "nama": "Anissa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal":"Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobi": "Bernyanyi",
                "sosmed": "@annisalutfia_",
                "kesan": "Kakaknya baik dan cara berkomunikasinya enak didengar",  
                "pesan":"semangat terus kuliahnya kak!" #1

            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kota baru",
                "hobi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "abangnya baik dan tegas",  
                "pesan":"semangat terus kuliahnya bang!" #2

            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()
    
elif menu == "Departemen PSDA":
    def departemenpsda ():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bGrtJvqxyagI71zr0yOgCYOATjcdjnSv",#1
            "https://drive.google.com/uc?export=view&id=1hd_ZBV8YXCjifW3POxChGh5B9432VlOo",#2
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#3
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#4
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#5
            "https://drive.google.com/uc?export=view&id=15O1wFRBBL-6CnyHdG03sZiObWNUIpNOf",#6
            "https://drive.google.com/uc?export=view&id=1SJBR8830ArwIeedJJ5rpBZu4-uVP1jPZ",#7
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#8
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#9
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#10
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#11
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#12
            "https://drive.google.com/uc?export=view&id=16F3MzhLyOCkVOO-pNG9HHMH-PB6JtD2F",#13
            "https://drive.google.com/uc?export=view&id=1sl7-pT9eJMwmv7jsw5-EbKl0don5CW-t",#14
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#15
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#16
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#17
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#18
            "https://drive.google.com/uc?export=view&id=12kIyMuSNELwUt6GZk_lPGgBsY6I9Y2CB",#19
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#20
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#21
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#22
            
        ]
        data_list = [
            {
                "nama"  : "Ericson Chandra Sihombing",
                "nim"   : "121450026",
                "umur"  : "21",
                "asal"  :"Bekasi",
                "alamat": "Kobam",
                "hobi" : "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan" : "abangnya keren dan tegas",  
                "pesan" :"semangat terus kuliahnya bang" #1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
                "sosmed": "@celisabeth",
                "kesan": "kakaknya lucu dan asik",  
                "pesan": "semangat terus kuliahnya kak!" #2
            },
            {
               "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Marahin orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya lucu dan asik",  
                "pesan":"semangat terus kuliahnya kak!" #3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobi": "Main",
                "sosmed": "@allyaislami_",
                "kesan": "Kakaknya keren dan ramah",  
                "pesan":"semangat terus kuliahnya kak!" #4
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiyati",
                "nim": "122450001",
                "umur": "20",
                "asal": "Jawa Barat",
                "alamat": "Metro",
                "hobi": "Nyopet",
                "sosmed": "@eksantyfebriana",
                "kesan": "kakaknya keren dan baik",  
                "pesan":"semangat terus kuliahnya kak!" #5
            },
            {
               "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Bengong",
                "sosmed": "@farahanumafifahh",
                "kesan": "kakaknya baik dan asik",  
                "pesan":"semangat terus kuliahnya kak!" #6
            },
             {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Jalan Pangeran Senopati Raya 18",
                "hobi": "Baca Kitab Suci",
                "sosmed": "@ferdy_kevin",
                "kesan": "abangnya baik dan seru",  
                "pesan": "semangat kuliahnya bang!" #7

            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Kayu Agung",
                "alamat": "Jalan Pagar Alam Kedaton",
                "hobi": "Ngukur Jalan",
                "sosmed": "@dransyh_",
                "kesan": "abangnya lucu dan asik",  
                "pesan": "semangat terus kuliahnya bang!" #8

            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Travelling",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "kakanya baik dan keren",  
                "pesan":"semangat terus kuliahnya kak" #9
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Duri, Riau",
                "alamat": "Pulau Damar Kobam",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "abangnya lucu dan seru",  
                "pesan": "semangat terus kuliahnya bang!" #10

            },
            {
               "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobi": "Dengerin The Adams",
                "sosmed": "@presilliamg",
                "kesan": "Kakaknya baik dan asik",  
                "pesan": "Semangat terus kuliahnya kak!" #11

            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "Jalan Lapas",
                "hobi": "Asprak",
                "sosmed": "@johanneskrsjnnn",
                "kesan": "Abangnya baik dan seru",  
                "pesan": "Semangat terus kuliahnya bang!" #12

            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Golf Asri",
                "hobi": "Ngetik print hello dunia",
                "sosmed": "@kemasverii",
                "kesan": "Abangnya seru banget, sepuh kodingan, dan baik banget",  
                "pesan": "Semangat terus kuliahnya bang!" #13

            },
            {
               "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok, Jabar",
                "alamat": "Jalan Airan Raya",
                "hobi": "Dengerin juicy luicy",
                "sosmed": "@sahid_maul19",
                "kesan": "Abangnya baik banget dan seru",  
                "pesan": "Semangat terus kuliahnya bang!" #14

            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450122",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobi": "Baca webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakaknya baik dan asik",  
                "pesan":"Semangat terus kuliahnya kak!" #15

            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Perum Korpri",
                "hobi": "Minum kopi, belajar, bikin deyvan senang",
                "sosmed": "@roselivness__",
                "kesan": "Kakaknya lucu dan asik",  
                "pesan": "Semangat terus kuliahnya kak!" #16

            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Abangnya baik dan cara berkomunikasinya enak didengar",  
                "pesan": "Semangat terus kuliahnya bang!" #17

            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobi": "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan": "Abangnya baik dan seru",  
                "pesan":"Semangat terus kuliahnya bang!" #18
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "121450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "Kakaknya baik dan asik",  
                "pesan":"Semangat terus kuliahnya kak!" #19

            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "Abangnya baik dan seru",  
                "pesan": "Semangat terus kuliahnya bang!" #20

            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobi": "Baca",
                "sosmed": "@syalaisha.i__",
                "kesan": "Kakaknya baik dan asik",  
                "pesan":"Semangat terus kuliahnya kak!" #21
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenpsda()

elif menu == "MIKFES":
    def mikfes ():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17PkJXwqPqa4lyeBMno1iCsnvqGy1ytYd",#1
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#2
            "https://drive.google.com/uc?export=view&id=1oUGYdedJx1FzdRBEunbriW7v8wqgjJNq",#3
            "https://drive.google.com/uc?export=view&id=1SH5Ep3AglNZL-k1rkBGSmzKBD25iFGx0",#4
            "https://drive.google.com/uc?export=view&id=1U7d0QQNQjA7SZuPS49q-lezyfmJv9by7",#5
            "https://drive.google.com/uc?export=view&id=1h00eL-OCFb9fgoTX6BRQSKVqKjFirDJw",#6
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#7
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#8
            "https://drive.google.com/uc?export=view&id=1ufAiRZrrKLPFSdZtEMviJAeGhqrLgfbE",#9
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#10
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#11
            "https://drive.google.com/uc?export=view&id=1CXYxfH77XFnJ4ZbMXCjSwyVxxTcPopdc",#12
            "https://drive.google.com/uc?export=view&id=10HtMXzV8oBASuu8L7UKsruQ_O3NmxmhB",#13
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#14
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#15
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#16
        ]
        data_list = [
            {
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21",
                "asal":"Lubuk Linggau, Sumsel",
                "alamat": "Jl. Nangka 4",
                "hobi": "Olahraga",
                "sosmed": "@rafadhlillahh13",
                "kesan": "Abangnya baik dan seru",  
                "pesan":"Semangat terus kuliahnya bang!" #1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Sebesi",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Kakaknya baik dan asik",  
                "pesan": "Semangat terus kuliahnya kak!" #2
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Abangnya baik dan asik",  
                "pesan":"Sukses terus kuliahnya bang!" #3

            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl. Permadi",
                "hobi": "Ngasprak ADS",
                "sosmed": "@mregiiii_",
                "kesan": "Abangnya baik dan seru banget",  
                "pesan":"Semangat terus kuliahnya bang!" #4

            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Gg. Yudistira",
                "hobi": "Review jurnal bu mika",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakaknya baik dan lucu",  
                "pesan":"Semangat terus kuliahnya kak!" #5

            },
            {
               "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal":"Bukit tinggi",
                "alamat": "Korpri",
                "hobi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "Abangnya baik dan seru",  
                "pesan":"Semangat terus kuliahnya bang!" #6
            },  
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobi": "Resume Webinar",
                "sosmed": "@anjaniiidev",
                "kesan": "Kakanya baik dan keren",  
                "pesan":"Semangat terus kuliahnya kak" #7
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobi": "Membaca jurnal bu mika",
                "sosmed": "@dindanababan",
                "kesan": "NIM ujung dan marga kita sama kak",  
                "pesan": "Semangat terus kuliahnya ya kak!" #8
 
            },
            {
               "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review jurnal bu mika",
                "sosmed": "@marletacornelia",
                "kesan": "Kakaknya baik banget dan asik",  
                "pesan": "Semangat terus kuliahnya kak!" #9

            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Kepulauan Riau",
                "alamat": "Gg. Nangka 3",
                "hobi": "Menghitung akurasi",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakaknya baik dan seru",  
                "pesan": "Semangat terus kuliahnya kak!" #10

            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450074",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobi": "Membangkitkan bilangan",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakaknya baik dan asik",  
                "pesan": "Semangat terus kuliahnya kak!" #11

            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobi": "Ngoding wisata",
                "sosmed": "@rahm.adityaa",
                "kesan": "Abangnya baik dan asik",  
                "pesan":"Semangat terus kuliahnya bang!" #12

            },
            {
                "nama": "Eggi satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobi": "Ngoding wisata",
                "sosmed": "@_egistr",
                "kesan": "Abangnya baik dan keren",  
                "pesan": "Semangat terus kuliahnya bang!" #13

            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl. Kelengkeng Raya",
                "hobi": "Review jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakaknya baik dan asik",  
                "pesan": "Semangat terus kuliahnya kak!" #14

            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": " ",
                "asal":"Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main game",
                "sosmed": "@sudo.syahrulramadhan",
                "kesan": "Abangnya baik dan asik",  
                "pesan":"Semangat terus kuliahnya bang!" #15
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Abangnya baik dan asik",  
                "pesan":"Semangat terus kuliahnya bang!" #16
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def departemen_eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "12145",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Jati Mulyo",
                "hobi": "Bangun Pagi",
                "sosmed": "@yogyyy",
                "kesan": "Abangnya baik dan seru",  
                "pesan":"Semangat terus kuliahnya bang!" #1

            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "TVRI",
                "hobi": "Jalan-jalan",
                "sosmed": "@ramadhitatifa",
                "kesan": "Kakaknya baik dan asik",  
                "pesan":"Semangat terus kuliahnya kak!" #2

            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Way Kandis",
                "hobi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakaknya baik dan asik",  
                "pesan":"sukses terus kuliahnya kak!" #3

            },
            {
               "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Belwis",
                "hobi": "Main Game",
                "sosmed": "@bastiansilaban_",
                "kesan": "Abangnya baik dan seru",  
                "pesan":"Semangat terus kuliahnya bang!" #4

            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakaknya baik dan seru",  
                "pesan":"Semangat terus kuliahnya kak!" #5

            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450005",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Kirim BC-an",
                "sosmed": "@esteriars",
                "kesan": "Kakaknya baik asik",  
                "pesan":"Semangat terus kuliahnya kak!" #6

            },
            {
               "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobi": "Jadi Humas",
                "sosmed": "@natee__15",
                "kesan": "Kakaknya baik dan seru",  
                "pesan":"Semangat terus kuliahnya kak!" #7

            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "20",
                "asal":"Saburai",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kakaknya baik dan seru",  
                "pesan":"Semangat terus kuliahnya kak!" #8

            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobi": "Pulang malam",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya baik dan seru",  
                "pesan":"emangat terus kuliahnya kak!" #9

            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_eksternal()

