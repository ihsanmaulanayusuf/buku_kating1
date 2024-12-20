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
            st.write(f"Hobi         : {data_list[i]['hobi']}")
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
            "https://drive.google.com/uc?export=view&id=1iBcQqzBHPBeyy-MSHQrEL_g8aE8GCRLG", 
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
                "hobi": "Dengerin musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "bang kharisma sangat berwibawa dan memiliki wawasan yang luas.",  
                "pesan":"semoga bang kharisma semakin sukses dalam himpunan maupun di luar himpunan"
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450077",
                "umur": "21",
                "asal":"Bukit Kemuning",
                "alamat": "Pawen 2 Sukarame",
                "hobi": "Main gitar",
                "sosmed": "@pndrinsni21",
                "kesan": "Bang Pandra orangnya asik dan tegas.",  
                "pesan":"semoga bang pandra cepat lulus dan mendapatkan kesempatan yang layak"
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kotabaru",
                "hobi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "kak meliza orangnya baik dan asik.",  
                "pesan":"semoga kak meliza semakin sukses dan lulus tepat waktu."
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "kak hartiti ramah dan mudah senyum.",  
                "pesan":"semoga kak meliza tetap sukacita ya"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "Nangka 4",
                "hobi": "Dengerin  bang Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "kakak orangnya moodbooster bangett.",  
                "pesan":"semoga kak meliza hidupnya dipermudah"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kotabaru",
                "hobi": "Dengerin  bang Pandra Gitaran",
                "sosmed": "@nadillaadr26",
                "kesan": "kakak orangnya penyebar virus smiling hihi.",  
                "pesan":"semoga kak nadilla semakin berjaya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1j1dbuhKO1DDddvS0LrVQFGr5kEXA1XLz", #7
            "https://drive.google.com/uc?export=view&id=1ix9lS6OVoYy62uUm-6HaObrlhSVPf00i", #8
            "https://drive.google.com/uc?export=view&id=1j387p89NCpLsQCUUWFVYz04VymT10g_v", #9
            "https://drive.google.com/uc?export=view&id=1jNfGQTfxSZ-uqbiypxTbCI6SPIcvvhGr", #10
            "https://drive.google.com/uc?export=view&id=1Lq7-KRSpQ2kXzcYoVlgot814uWt6-gXp",#11
            "https://drive.google.com/uc?export=view&id=1jIYpTFj9zFjtpz3P_9YTMzPxSPkReb_o",#12
            "https://drive.google.com/uc?export=view&id=1j387p89NCpLsQCUUWFVYz04VymT10g_v",#13
            "https://drive.google.com/uc?export=view&id=1M4ULGBnCrzTQYk8Ncq2YGI344TYF-ZMa",#14
            "https://drive.google.com/uc?export=view&id=1M5U5jnGVXPWyigOkXdKfHM9uXONA92KI", #15
            "https://drive.google.com/uc?export=view&id=1j2QCFl7UOO6fvtwL_JsqS6eyTiwDH-Ol", #16
            "https://drive.google.com/uc?export=view&id=1jACVmlpSH9gdP0vwNc6GdN_URxlRADSQ", #17
            "https://drive.google.com/uc?export=view&id=1j4n8hfFMMMdq3ADU2VtW6BhpKN2ewBuZ", #18
            "https://drive.google.com/uc?export=view&id=1iyUaPMN9Z4dXVWQod3tLT3upASlIwMEJ", #19
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
                "kesan": "Kakak punya wawasan yang luas dan muudah diajak berdiskusi",  
                "pesan":"Semoga kakak terus sukses dalam kuliahnya dan selalu semangat menggapai impian!" #7
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450124",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Way Hui",
                "hobi": " Membaca",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak ini baik dan murah senyum",  
                "pesan":"Teruslah semangat belajar, kak! Masa depan cerah menanti!"# 8
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Menonton Film",
                "sosmed": "@wlsbn0",
                "kesan": "Kakak punya sikap positif yang bikin suasana jadi lebih santai tapi tetap produktif.",  
                "pesan":"Tetap semangat ya kakak! Jangan lupa istirahat di tengah kesibukan kuliah!"#9
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "Sangat suportif dan selalu memberi dorongan, kakak ini bikin kita jadi lebih termotivasi.",  
                "pesan":"Sukses selalu untuk kuliahnya! Tetap semangat dan jangan pernah berhenti belajar."#10
            },{
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bernung, Pesawaran",
                "alamat": "Bandar Lampung",
                "hobi": "Nonton Drakor",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 11
            },{
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Belwis",
                "hobi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak selalu memberi energi positif",  
                "pesan":"Semoga kakak selalu diberi kelancaran dalam segala urusan. Tetap semangat!"# 12
            },{
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobi": "Baca Al-qur'an",
                "sosmed": "@fleurnsh",
                "kesan": "Kakak ini selalu ramah dan gampang diajak ngobrol, suasana jadi lebih hidup",  
                "pesan":"Semangat terus, Kak! Jangan menyerah dan teruslah berjuang sampai garis akhir!"# 13
            },{
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak punya sikap yang tenang, wawasannya luas, dan keren banget",  
                "pesan":"Semoga sukses di setiap langkah ke depannya, Kak. Teruslah bersinar!"# 14
            },{
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Kakaknya punya aura yang positif dan pendiam.",  
                "pesan":"Jaga kesehatan dan semoga selalu diberi kemudahan dalam setiap perjalanan hidup, Kak!"# 15
            },{
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Ogan Ilir",
                "alamat": "Natar",
                "hobi": "Nyari Sinyal di Gedung F",
                "sosmed": "@_.dheamelia",
                "kesan": "Kkakaknya sangat ramah, lucu dan suka mengajak brainstorming",  
                "pesan":"Teruslah jadi inspirasi untuk orang-orang di sekitar kakak! Sukses selalu!"# 16
            },{
                "nama": "Muhammad Fahrul Aditya",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@fhrul.pdf",
                "kesan": "Kakak orangnya baik dan sangat peka terhadap rekan kerjanya.",  
                "pesan":"Semoga kakak semakin sukses dan terus semangat mengejar impian!"# 17
            },{
                "nama": "Berliana enda putri",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini sosok yang humble dan asik diajak bicara tentang apa saja",  
                "pesan":"Semoga kakak selalu diberkahi kemudahan dalam segala urusan. Tetap semangat menjalani hari-hari ke depan!"# 18
            },{
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Billabong, Gedong Air",
                "hobi": "Suka Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "Kakak selalu membawa aura positif, jadi nyaman kalau ngobrol lama-lama.",  
                "pesan":"Semoga kakak selalu diberi kebahagiaan dan sukses di setiap langkahnya! Dikurangi bengongnya kak"# 19
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11Y585mcfw-CSLvL2-QFHUPqOF02dZ9gm", #20
            "https://drive.google.com/uc?export=view&id=11cwTK4RA1KxLIDnbTEJV2u4fUdYQ9suz", #21
        ]
        data_list = [
            {
                "nama": "Anissa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal":"Lampung Tengah",
                "alamat": "Kos Putri Rahayu",
                "hobi": "Bernyanyi",
                "sosmed": "@annisalutfia_",
                "kesan": "Kakak ini cantik, friendly, public speakingnya keren, tegas, dan memiliki pemahaman yang luas",  
                "pesan":"Semangat terus kuliahnya kak, jangan lupa untuk terus tersenyum" #20
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abang ini tegas, ramah, dan suka menolong",  
                "pesan":"Semangat terus bang, jaga kesehatanny bang" #21
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def departemenpsda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12DR_dg_2mM-kDrhwDu5W8WLWDGXkIqD3", #22
            "https://drive.google.com/uc?export=view&id=1QlM5gWNxjxzZ4huYCUCsFbC33vdLv85I", #23
            "https://drive.google.com/uc?export=view&id=12-1hzITghxAwGXky4-jVAMhDvjRddCfC", #24
            "https://drive.google.com/uc?export=view&id=12ZItbgfB15rVVGwNvxH8eGRWDUQ_l9Tm", #25
            "https://drive.google.com/uc?export=view&id=11nihuxl1n31eT5U5U0CVjgv9UEm_sgwz", #26
            "https://drive.google.com/uc?export=view&id=13VFjEmtL9lND3H62lKrE2zW6vLn5DyK1", #27
            "https://drive.google.com/uc?export=view&id=13XeQrSBrMQN-4SIlC9wvsjPGID9EHmrQ", #28
            "https://drive.google.com/uc?export=view&id=12GNW4ankD2sCBJ07FwKpUIQpazJR_rYO", #29
            "https://drive.google.com/uc?export=view&id=12e3jA6-g2ByGUuP5xqGrSz5TKjBIAYGT", #30
            "https://drive.google.com/uc?export=view&id=13YAmaeZ1SiE-hRvZxhmFAfHdBnSoPocq", #31
            "https://drive.google.com/uc?export=view&id=13QDZjx2crzqwV47kl-ZGekjV8KOLD3TM", #32
            "https://drive.google.com/uc?export=view&id=1292qKSlAoSLRtT58XNabDkAUbos-Is9k", #34
            "https://drive.google.com/uc?export=view&id=11lbYNMPblRqKb0nqxeCw1bSw7jdavgG-", #35
            "https://drive.google.com/uc?export=view&id=13_7VKIVKIHNasuKWUvPS96BbYpJilZ2p", #37
            "https://drive.google.com/uc?export=view&id=11ruLvDdh-3iK_DZq3NkT2lqflU8lnOcH", #38
            "https://drive.google.com/uc?export=view&id=12exExmwWTwNcTEqjquCe_1K0s-G2vPK3", #39
            "https://drive.google.com/uc?export=view&id=137vgC2uraecHnVyNb3OkvZjIirCwo3DY", #40
            "https://drive.google.com/uc?export=view&id=11pr6xsR6jMECZsGY9mClyMK7Yu_lWTAx", #41
            "https://drive.google.com/uc?export=view&id=12mTM4EAJRq6SMnVv4GTCOGn7H0X9aEuv", #42
            "https://drive.google.com/uc?export=view&id=12RVVpJZf6DO0PxX7KllxBfUyxAL2kS5p", #43
            "https://drive.google.com/uc?export=view&id=12XU8n_eQHbYoi1pU9OyyjN-phh2nehIb", #44
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
                "kesan": "Abang punya pemikiran yang luas dan problem solving yang baikk",  
                "pesan":"Semangat terus kuliahnya bang" #22
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
                "sosmed": "@celisabeth",
                "kesan": "Kakak ini orangnya cantik, tegas, dan ramah",  
                "pesan":"Semangat terus kak, jangan lupa tersenyum, dijaga kesehatannya kak" #23
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Marahin orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak ini cantik dan wawasannya luas",  
                "pesan":"Semangat terus kak kuliahnya, semoga yang disemogakan akan tersemogakan segera kak!" #24
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobi": "Main",
                "sosmed": "@allyaislami_",
                "kesan": "Kakak ini orangnya tegas, seru diajak berdiskusi dan berwibawa",  
                "pesan":"Semangat terus kak kuliahnya, jangan lupa bahagia dan tersenyum, serta apa yang diinginkan akan segera tercapai!" #25
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiyati",
                "nim": "122450001",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Metro",
                "hobi": "Nyopet",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini asik dan tegas",  
                "pesan":"Semangat terus kak, jangan lupa untuk tersenyum dan dijaga kesehatannya kak" #26
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobi": "Bengong",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini murah senyum dan manis",  
                "pesan":"Semangat kuliahnya kakak, jangan lupa tersenyum" #27
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Jalan Pangeran Senopati Raya 18",
                "hobi": "Baca Kitab Suci",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abang ini asik, baik, dan murah senyum, seru diajak ngobrol dan berdiskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga hasil yang didapat bagus dan memuaskan" #28
            },
            {
                "nama":  "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jalan Pagar Alam Kedaton",
                "hobi": "Ngukur jalan",
                "sosmed": "@dransyh_",
                "kesan": "Abang ini asik, baik, dan murah senyum, seru diajak ngobrol, terutama menyampaikan materi sangat mudah dipahami",  
                "pesan":"Semangat terus bang, semoga ilmunya terus bermanfaat, dijaga kesehatannya serta mental" #29
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Travelling",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakak ini asik, baik, dan cantik",  
                "pesan":"Semangat terus kuliahnya kak, semoga berjaya" #30
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
                "kesan": "Kakak ini manis, asik, baik dan ramah",  
                "pesan":"Semangat terus kak kuliahnya, semoga apa yang dicita-citakan akan tercapai" #32
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobi": "Asprak",
                "sosmed": "@johanneskrsjnnn",
                "kesan": "Abang ini tegas, berwibawa, asik, murah senyum, dan friendly",  
                "pesan":"Jaga kesehatannya bang, semangat ngaspraknya, semoga apa yang diinginkakan segera tercapai bang" #34
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Golf Asri",
                "hobi": "Ngetik print hello dunia",
                "sosmed": "@kemasverii",
                "kesan": "Abang ini wawasannya llluas, baik, asik juga, seru diajak ngobrol dan diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga apa yang di cita-citakan bisa terwujud" #35
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobi": "Dengerin The Adams",
                "sosmed": "@presilliamg",
                "kesan": "Kakak ini cantik, asik, baik, dan murah senyum",  
                "pesan":"Semangat terus kak kuliahnya, semoga hasil matkulnya A semua" #37
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450122",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak ini memiliki pikiran serta public speaking yang bagus, dan murah senyum",  
                "pesan":"Semangat terus kuliahnya kakak, apapun yang didoakan semoga segera tercapai" #38
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
                "pesan":"Semangat terus bang, jaga kesehatan, semoga setiap usaha sesuai dengan hasilnya" #39
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Perum Korpri",
                "hobi": "Minum kopi, belajar, bikin Deyvan senang",
                "sosmed": "@roselivness__",
                "kesan": "Kakak ini keren serta murah senyum",  
                "pesan":"Semangat terus kuliahnya kak, dijaga kesehatannya kak, semoga semuanya dalam lindungan Tuhan" #40
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Abang ini, asik, suka menolong dan mempunyai pikiran serta public speaking yang bagus",  
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
            "https://drive.google.com/uc?export=view&id=144d_GMivPfTDdTSWa-65Jaa_nmkYndSZ", #45
            "https://drive.google.com/uc?export=view&id=14TiG3kI5XDL5vWRa9Mxm0qUJvOWNGDRn", #46
            "https://drive.google.com/uc?export=view&id=14GQGStkvtbVLWPPnrB9YFmPDrIj-OQhA", #48
            "https://drive.google.com/uc?export=view&id=13rMvVgBney8i_yWG6ZFDPsaYJWNbnvl2", #50
            "https://drive.google.com/uc?export=view&id=142S0xhuXJ19moD7DZsPnVqzEV5i2YiKh", #51
            "https://drive.google.com/uc?export=view&id=13rwBxaLHxMFPPYIcaWKmYtAZv8CFVQS0", #53
            "https://drive.google.com/uc?export=view&id=142FesM97x-My7qX5qLtlsZJ8Tb8kXXy7", #54
            "https://drive.google.com/uc?export=view&id=14aeUPWkdiwcKB45iOscqPP2mEhq8Uz0G", #55
            "https://drive.google.com/uc?export=view&id=13quf-EUDI25qAWoLrOaNjPWlaqSpxzgw", #56
            "https://drive.google.com/uc?export=view&id=1496IITjFmrvOybyGvGZ8G0ZnpNVddUAl", #57
            "https://drive.google.com/uc?export=view&id=13huD1qwgD53vAyoYDlbjNOC2-vHkUmN0", #58
            "https://drive.google.com/uc?export=view&id=14LuMQ6Xp40l7pHjKFDBX7aaRMeRGpDYO", #60
            "https://drive.google.com/uc?export=view&id=13igYSg7i7PU8xL8zPqlvkOrYbNqZ8lah", #61
            "https://drive.google.com/uc?export=view&id=14OoDd5PLEPPPEXAPy4xoHrF_nUs8jVGT", #62
            "https://drive.google.com/uc?export=view&id=13z_RGrlAsN_nApdIaL-cM2igEiTDnniZ", #63
            "https://drive.google.com/uc?export=view&id=13w8N8V9u1QWeu5EXOUGZsxtM6CfIrubR", #64

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
         ]
        display_images_with_data(gambar_urls, data_list)
    departemen_mikfes()

elif menu == "Departemen Eksternal":
    def departemeneksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1CtjuxIYioCD2MS0rzhWwz9Bnww_vSk1v", #66
            "https://drive.google.com/uc?export=view&id=1CIs4jrifujPvtkqFaXDuVlMvYHq2gWa6", #68
            "https://drive.google.com/uc?export=view&id=1C_A_cgagzLT_mS_nYu0T-nHxCnIUIRHt", #69
            "https://drive.google.com/uc?export=view&id=1CTKUN1i9zIxRTCTj-P79vamim12Dt6SG", #70
            "https://drive.google.com/uc?export=view&id=1CfZWO4O8e_goSTKBk58JuSYtLU8S7yz0", #71
            "https://drive.google.com/uc?export=view&id=1CTEuhBZrSiS-rvnWle3nU4X3nQbFyH86", #72
            "https://drive.google.com/uc?export=view&id=1CAeqj31dMUojBLHZr5j4nV0tOs4tu3VY", #73
            "https://drive.google.com/uc?export=view&id=1CUdq0tR4WRssddR8eGCYg7-ZzzX8htvb", #74
            "https://drive.google.com/uc?export=view&id=1CaVR4Wr6saRldP9zWcTI0-2UNDrSdEPN", #75
            "https://drive.google.com/uc?export=view&id=1CV6G8lrhkB4w6bz2hsOkBxMbFc9XsDxQ", #76
            "https://drive.google.com/uc?export=view&id=1D8dchv6uRN04PosxIQ52IZ5vF4m60kmF", #77
            "https://drive.google.com/uc?export=view&id=1D8U0xgjsM7xg3Ygo44KBMhtJ09hK_Tyt", #80
            "https://drive.google.com/uc?export=view&id=1D6sbL8OS538FH5x1CUwaD7SMdLW2KEiE", #81
            "https://drive.google.com/uc?export=view&id=1D2dWmzsappCR5cfRjXaRV-EFnyFJzeIN", #82
            "https://drive.google.com/uc?export=view&id=1D8bZ-ndKHZE1wQjQo_w9DLMdalRlb8mv", #83
            "https://drive.google.com/uc?export=view&id=1Cu0mB6MirjMQqnrcCldJWTXBFm7ar2MJ", #84
            "https://drive.google.com/uc?export=view&id=1CmDY0Ge6ISQ_ZLIvSm2Lgv0ycT3Uru7x", #85
            "https://drive.google.com/uc?export=view&id=1C9XLogXClYGANj8hQv5e10UA81_yaiPh", #86
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
                "nim": "122450126",
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
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "Bikin portofollio",
                "sosmed": "@rzkdrnnn",
                "kesan": "Abang ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #77
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
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan": "Kakak ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #81
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abang ini asik, baik, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya" #82
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobi": "Masak",
                "sosmed": "@izzalutfia",
                "kesan": "Kakak ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
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
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Ngeresume Seminar",
                "sosmed": "@rayths_",
                "kesan": "Penuh perhatian dan selalu mendengarkan dengan baik",  
                "pesan":"Semangat terus kak kuliahnya" #85
            },
            {
                "nama": "Tria Yunanni",
                "nim": "121450062",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Way Kanan",
                "hobi": "Baca",
                "sosmed": "tria_y062",
                "kesan": "Kakak ini memiliki bikin suasana jadi ceria",  
                "pesan":"Semangat terus kak kuliahnya" #86
            },
         ]
        display_images_with_data(gambar_urls, data_list)
    departemeneksternal()

elif menu == "Departemen Internal":
    def departemeninternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EMZiaC_0KVItV3sLogYqrwDdsxAtcgpZ", #87
            "https://drive.google.com/uc?export=view&id=1DbafEdgJO5QBJsKp_nxj_XdQTOPHovNS", #88
            "https://drive.google.com/uc?export=view&id=1DoG2dnSwnVuLUGnod1QoZB9EK1UdpTqw", #89
            "https://drive.google.com/uc?export=view&id=1DfnrlaZ0DXzG0O_WPtJiVMHH3EVesMlq", #91
            "https://drive.google.com/uc?export=view&id=1QlM5gWNxjxzZ4huYCUCsFbC33vdLv85I", #92
            "https://drive.google.com/uc?export=view&id=1DlCoJvEbMTgR8nsBdg7FLdCC1d_QhaKL", #93
            "https://drive.google.com/uc?export=view&id=1DwOFZb1fzti7M-r9puHq9JERrq9t9Zda", #94
            "https://drive.google.com/uc?export=view&id=1DWAm_ahoX2x5-pzP8POzVF1L24O6krQl", #96
            "https://drive.google.com/uc?export=view&id=1Dx5PHhRCh3m9Cad_YuCAQI6eSarBd8Vm", #97
            "https://drive.google.com/uc?export=view&id=1EB5U_Z292evWyYDo-eqs20oF7ZY8zkfY", #98
            "https://drive.google.com/uc?export=view&id=1DpTyjbpjYCG-sxHEzqnxEtTLMXBfAQaI", #99
            "https://drive.google.com/uc?export=view&id=1DuqkUdEnc5GD2U66bTRfiLVgc-w7SqX5", #100

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
                "nim": "121450069",
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
            "https://drive.google.com/uc?export=view&id=1AIgF3oKQ7TCsAZumxvSwFH-YR4_1yM7b", #101
            "https://drive.google.com/uc?export=view&id=1ApKGs-ymbNzEVnVX3tSElTt6u_aUIbkF", #102
            "https://drive.google.com/uc?export=view&id=1B4XDYLey_5WOAWWXBkkokV1-3_BaEf4Y", #103
            "https://drive.google.com/uc?export=view&id=1AczpfQsyThu9waAbk4IlHrQUT3WhnVUf", #104
            "https://drive.google.com/uc?export=view&id=1Ak_eiRvhetFmWmYhYjr5skxpD1jt6_ak", #105
            "https://drive.google.com/uc?export=view&id=1QlM5gWNxjxzZ4huYCUCsFbC33vdLv85I", #106
            "https://drive.google.com/uc?export=view&id=1AxVOTx2DdAPu7P2zn1E8soNd07PKU9lX", #107
            "https://drive.google.com/uc?export=view&id=1AbRV_kPoXY_0nf0LV4QWf_WVHzAYyqQX", #108
            "https://drive.google.com/uc?export=view&id=1AkHVWn8rZKrVgb1p-ILO7s0bURiMJPqs", #109
            "https://drive.google.com/uc?export=view&id=1B0jZISee0JuvNTAXiJkeYpkbv_oTzqge", #110
            "https://drive.google.com/uc?export=view&id=1B5_IrbyaP-u710PvGXCVguJ9h1OCA3fA", #111

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
            "https://drive.google.com/uc?export=view&id=1F9ziutV3lrVErMlyjPHvjk6RG7d205qT", #112
            "https://drive.google.com/uc?export=view&id=1G5hFLH5R-EbeCAJsTS9QPHw9y289Djtq", #113
            "https://drive.google.com/uc?export=view&id=1Frum6jGCSb-S5Vkz_RR6EyE3P6cwNlWo", #114
            "https://drive.google.com/uc?export=view&id=1GOG2mnJLBb7S2D6CLK5ToYvQysjuJS32", #115
            "https://drive.google.com/uc?export=view&id=1GUifWNL_mHFBqjBzU5RMHVO5xFg7NKC_", #116
            "https://drive.google.com/uc?export=view&id=1GXv6vRcKv-fkvQnS6p-DdDPHQhhZhFwu", #117
            "https://drive.google.com/uc?export=view&id=1FWmhaoWgB6AeFDNJ_KbzL161nNEr_pLL", #118
            "https://drive.google.com/uc?export=view&id=1Fb3VmWVlpqb-NpZMxQNvOriyXLHPetIN", #119
            "https://drive.google.com/uc?export=view&id=1F491jzV2RXq7xfoixxK0rIGGugpuYxW2", #120
            "https://drive.google.com/uc?export=view&id=1FZ4XCt6zLKwaaQdt2VggaTPBl-OaGJa_", #121
            "https://drive.google.com/uc?export=view&id=1FZQSkaPc6ll5bYpu-qXsyIOlBhJ7rl2_", #122
            "https://drive.google.com/uc?export=view&id=1GPuzuCbkA6IHs_48sv_NHDdAt2frviBN", #123
            "https://drive.google.com/uc?export=view&id=1FOIPOcAz3orMb0e5GVfRSSPzR0uoZXzP", #124
            "https://drive.google.com/uc?export=view&id=1FCJAq2Ra8uN801b40qmQGwOvQpTUt5rx", #125
            "https://drive.google.com/uc?export=view&id=1FAxzx0ybr6USaqH3zgftvRFZ_2PV_nV_", #126
            "https://drive.google.com/uc?export=view&id=1FNGXjLIXViscr34GEVj-QtvNJXe4r5Jv", #127
            "https://drive.google.com/uc?export=view&id=1GAn2a5J1ooX7yC9VYaKxZQiqvjYFEfx_", #128
            "https://drive.google.com/uc?export=view&id=1FICRib3kPdPaouFd3kLPWIYJhB6IhjH7", #129
            "https://drive.google.com/uc?export=view&id=1G6xAkUGntDi8VETUgl9yRMvzoyq1Gc97", #130
            
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
                "nim": "121450045",
                "umur": "20",
                "asal":"Natar",
                "alamat": "Natar",
                "hobi": "Menyibukkan diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "Kakak ini bisa mencairkan suasana",  
                "pesan":"Semangat terus kak kuliahnya, tetap konsisten dalam menyebarkan energi positif ya kak" #116
            },
            {
                "nama": "Najla Juwairia",
                "nim": "121450037",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Nulis, baca, fangirling",
                "sosmed": "@nanana.minjoo",
                "kesan": "Sangat kreatif dan kakaknya cantik",  
                "pesan":"Semangat terus kak kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #117
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobi": "Nonton film",
                "sosmed": "@patriciadiajeng",
                "kesan": "kakaknya ramah dan murah senyum",  
                "pesan":"Semangat terus kak kuliahnya, selalu tersenyum yaa" #118
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Sukarame",
                "hobi": "Baca coding",
                "sosmed": "@rahmanellyana",
                "kesan": "Kakkaknya baik, ramah, public speakingnya keren, suka tersenyum",  
                "pesan":"Sehat selalu ya kak, semoga mimpinya terwujud!" #119
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobi": "Bernyanyi dan menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakanya kreatif banget dan seruu",  
                "pesan":"Semangat menghadapi semester selanjutnya kak, jangan lupa bahagia" #120
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "1214500135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar",
                "hobi": "Lagi nyari",
                "sosmed": "@dino_kiper",
                "kesan": "Abangnya pendiem tapi wawasannya seluas samudera",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan, dan dipermudahkan segala sesuatunya" #121
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobi": "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan": "Komunikasi kakaknya baik dan kreatif",  
                "pesan":"Semoga bakat kakak dapat membantu orang dan semoga dipermudah jalannya" #122
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf UIN",
                "hobi": "Mencari Uang",
                "sosmed": "@jimnn.as",
                "kesan": "Abang ini asik, tegas, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #123
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "1224500125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jalan Durian 1 Pembda",
                "hobi": "Nonton Drakor",
                "sosmed": "@nsywanaf",
                "kesan": "Kakak ini asik, tegas, baik, dan pemikirannya luas",  
                "pesan":"Semangat terus kak kuliahnya, semoga bisa lulus dengan hasil yang memuaskan dan membanggakan" #124
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. Nangka 2",
                "hobi": "Baca Novel yang Bikin Nangis",
                "sosmed": "@prskslv",
                "kesan": "Kakak ini ramah, tegas, dan baik",  
                "pesan":"Semangat kak kuliahnya semoga keinginannya tercapai dalam waktu dekat" #125
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "Abang ini baik, tampan, dan pemikirannya luas",  
                "pesan":"Semangat dan sehat selalu bang, semoga ilmunya bermanfaat bagi semua orang" #126
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "210",
                "asal":"Lampung Selatan",
                "alamat": "Belwis",
                "hobi": "Mengerjakan tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Kakaknya baik, cantik, dan positive vibes",  
                "pesan":"Semangat terus kak kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #127
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa Labuhan Dalam",
                "hobi": "Ngoding, gaming",
                "sosmed": "@abitahmad",
                "kesan": "Abang ini asik, tegas, baik, dan friendly",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa yang disemogakan tersemogakan" #128
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Panjibako",
                "alamat": "Bandar Lampung",
                "hobi": "Main Hp",
                "sosmed": "@_akmal.faizl",
                "kesan": "Abang ini asik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, selalu berikan hasil yang terbaik bang" #129
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Wisma Hana Hani",
                "hobi": "Bengong/Membaca buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Abang ini asik, pemikirannya luas, jepretannya bagus, dan berwibawa",  
                "pesan":"Semangat terus bang kuliahnya, kurangi bengong perbanyak membaca bukunya bang" #130
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenmedkraf()
