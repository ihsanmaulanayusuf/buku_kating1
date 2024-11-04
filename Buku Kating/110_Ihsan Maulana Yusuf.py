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
            st.write(f"Nama            : {data_list[i]['nama']}")
            st.write(f"NIM             : {data_list[i]['nim']}")
            st.write(f"Umur            : {data_list[i]['umur']}")
            st.write(f"Asal            : {data_list[i]['asal']}")
            st.write(f"Alamat          : {data_list[i]['alamat']}")
            st.write(f"Hobi            : {data_list[i]['hobi']}")
            st.write(f"Sosial Media    : {data_list[i]['sosmed']}")
            st.write(f"Kesan           : {data_list[i]['kesan']}")
            st.write(f"Pesan           : {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HRMWlnpO7I6uRbOrA5W-6FTlL1QNGApo", #1
            "https://drive.google.com/uc?export=view&id=11DHbdehlmCHNVylAyxcAdwGiaTpEZ8cr", #2
            "https://drive.google.com/uc?export=view&id=14IiwH93_xiBo8ATZfRYGQZrH_oyFJv4O", #3
            "https://drive.google.com/uc?export=view&id=1UFtt-GnC6E9Izs0fEI_mMWWtjxGQs-CO", #4
            "https://drive.google.com/uc?export=view&id=1qR6dlQM82i1rqyTk1WYrYy09ntAJwfm5", #5
            "https://drive.google.com/uc?export=view&id=1cZRCIVdAeq9zGGEdtXClKf2FnZtx-Vsr", #6
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar",
                "hobi": "Dengerin Musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Abang ini keren, berwibawa, dan mempunyai public speaking yang bagus",  
                "pesan":"Semoga memiliki karir yang bagus dan diterima di perusahaan yang diinginkan"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Bukit Kemuning",
                "alamat": "Pawen 2 Sukarame",
                "hobi": "Main gitar",
                "sosmed": "@pndrinsni21",
                "kesan": "Abang ini asik, humoris",  
                "pesan":"Semoga selalu sehat, dan memiliki karir yang sukses, serta bisa lulus dengan cepat tapi dengan nilai yg bagus"# 2
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kotabaru",
                "hobi": " Nonton Drakorr",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak ini baik, asik, dan cantik ",  
                "pesan":"Semangat untuk kakak, semoga sehat selalu"# 3
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak ini baik, dan friendly",  
                "pesan":"Semangat untuk kakak kuliahnya, jangan lupa senyum kak, sehat selalu, semoga cepat lulus dan setelahnya mendepatkan pekerjaan yang kakak imipikan"# 4
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "Nangka 4",
                "hobi": "Dengerin  bang Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak ini baik",  
                "pesan":"Semangat untuk kakak, semoga sehat selalu, dan rezekinya di perlancar"# 5
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kotabaru",
                "hobi": "Dengerin  bang Pandra Gitaran",
                "sosmed": "@nadillaadr26",
                "kesan": "Kakak ini baik, friendly, dan ramah",  
                "pesan":"Semangat untuk kakak, semoga sehat selalu dan bisa lulus dengan hasil yang memuaskan"# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1IF5ORenld0XiGp69CGjAEIM5YfD_hdXi", #7
            "https://drive.google.com/uc?export=view&id=1toRUKq-1-5ZyO2FOmco94Xxoe1OEW9tn", #8
            "https://drive.google.com/uc?export=view&id=1x8wS0GBUGBqiChsHapJ7ktL-wDRO2Fh4", #9
            "https://drive.google.com/uc?export=view&id=13QdFXzafl5TGpCDje_o_XGWa0DmmKH3k", #10
            "https://drive.google.com/uc?export=view&id=1iZ2asxm4SFaQlLvNR2MtCN1ESssj7R0g", #11
            "https://drive.google.com/uc?export=view&id=1DO_6DjrKWV0q7aDa1qNZAEVmh6r_VfBD", #12
            "https://drive.google.com/uc?export=view&id=147zmkTqn4aa0t72aha1sW9YnlujXOs3H", #13
            "https://drive.google.com/uc?export=view&id=1mgg5MKpJvLVt8QVZKYSNFvqCYw0Xk8as", #14
            "https://drive.google.com/uc?export=view&id=1x2yDELML0SGXTB8klEKdpbjeq1YasHpa", #15
            "https://drive.google.com/uc?export=view&id=1OS908xt0ED6cVE0RJpF70SlfHQsP69T4", #16
            "https://drive.google.com/uc?export=view&id=1UKWttVReJPUcSruodBEmpE3OAYpA0Rlr", #17
            "https://drive.google.com/uc?export=view&id=1mZ2QASD_pYf9F3LZGvG47pNDCW1geWhR", #18
            "https://drive.google.com/uc?export=view&id=15x2T_WIWrE0pBHBfVx43DsjGrDDN6bpY", #19
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
                "kesan": "Kakak ini asik sekali, friendly, public speakingnya juga bagus",  
                "pesan":"Semangat terus kuliahnya kak, semoga sehat selalu, dan jangan lupa untuk terus tersenyum" #7
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450124",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Way Huwi",
                "hobi": "Membaca",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak ini asik, cantik, baik, murah senyum juga, dan kakak ini juga bawaanya kalem",  
                "pesan":"Untuk kakak, pesan dari saya semangat terus, semoga kuliahnya lancar hingga akhir, lalu lulus, serta bisa di tempatkan di pekerjaan yang kakak imipikan dari dulu" #8
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Menonton Film",
                "sosmed": "@wlsbn0",
                "kesan": "Kakak ini cantik, baik, positif vibes juga, ramah sekali",  
                "pesan":"Pesan dari saya untuk kakak semoga sehat selalu dalam lindungan Sang Maha Kuasa, dipermudah segala urusan, dan semangat terus kuliahnya hingga akhir kak" #9
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobi": "Nonton Dracin",
                "sosmed": " @anisadini10",
                "kesan": "Kesannya adalah kakak ini ramah, baik juga, pendengar yang baik",  
                "pesan":"Tetap semangat kak dalam kuliah atau apapun itu, semoga segala urusan kakak selalu diperlancar oleh-Nya" #10
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bernung, Pesawaran",
                "alamat": "Bandar Lampung",
                "hobi": "Nonton Drakor",
                "sosmed": " @ansftynn_",
                "kesan": "Kakak ini pembawaanya tenang, baik banget, ramah juga, dan pendengar yang baik",  
                "pesan":"Serumit apapun masalah yang mungkin kakak punya hadapilah dengan ketenangan dan senyum yang bisa mencairkan suasana hati, semangat terus kak" #11
            },
            {
                "nama": " Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Belwis",
                "hobi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Abang ini ramah, tampan, public speakingnya juga keren",  
                "pesan":"Semangat bang kuliahnya, semoga lelah menjadi alhamdulillah karena hasil yang didapat sesuai jerih payah" #12
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak ini baik banget, ramah juga, friendly, cantik, dan pinter juga, serta murah senyum",  
                "pesan":"Semangat terus kakak kuliahnya semoga diperlancar Tuhan dalam segala urusan yang kakak punya dan lulus dengan hasil yang memuaskan" #13
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobi": "Baca Al-qur’an",
                "sosmed": "@fleurnsh",
                "kesan": "Kakak ini asik, pengetahuannya juga luas, ramah juga, dan murah senyum, serta public speakingnya bagus",  
                "pesan":"Semangat terus ya kak, semoga segala urusan kakak diperlancar tuhan, untuk masalah yang mungkin kakak punya hadapi dengan ketenangan ya kak, sehat selalu" #14
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abang ini friendly, baik, ramah, dan abang ini orangnya kalem",  
                "pesan":"Semangat terus bang kuliahnya, sehat selalu, tetaplah jadi orang baik bang, semoga setiap nilai ujian abang di matkul apapun itu hasilnya ga jauh dari AB/A" #15
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Ogan Ilir",
                "alamat": "Natar",
                "hobi": "Nyari Sinyal di Gedung F",
                "sosmed": "@_.dheamelia",
                "kesan": "Cantik, kakak juga baik, ramah, friendly, orangnya juga santai",  
                "pesan":"Teruslah jadi orang baik kak, jangan pernah lupakan Tuhan, saya doakan sehat selalu untuk kakak dan keluarga" #16
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450126",
                "umur": "22",
                "asal":"Surakarta",
                "alamat": " Sukarame",
                "hobi": "Melukis",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abang ini murah senyum, berwibawa, orangnya santai, dan tampan",  
                "pesan":"Semangat bang kuliahnya, semoga setiap usaha yang abang lakukan sesuai dengan hasil yang didapat, sehat selalu bang" #17
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Way Huwi",
                "hobi": "Baca Buku, Ngoding, Ibadah",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini cantik, baik, friendly, ramah sekali, murah senyum, orangnya pembawaanya tenang dan pengetahuanya luas",  
                "pesan":"Untuk kakak semoga selalu dalam lindungan tuhan, jangan melupakan-Nya, semangat terus ya kak kuliahnya, semoga hasilnya setimpal dengan jerih payah kakak dalam menghadapinya" #18
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20", 
                "asal":"Bandar Lampung",
                "alamat": "Billabong, Gedong Air",
                "hobi": "Suka Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang ini asik, lucu, tampan, sepertinya gampang berbaur dengan siapa saja, public speakingnya juga bagus",  
                "pesan":"Semangat terus bang, dari saya kurangin bengong, sehat selalu bang jere" #19
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1iW3aj4RzQohpFTyHtYmyKrRBaqA__q6B", #20
            "https://drive.google.com/uc?export=view&id=1Tpq5RWr33IuAyRc6up1dniHWwQ0oUMKB", #21
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
                "kesan": "Kakak ini asik sekali, friendly, public speakingnya juga bagus, tegas, dan memiliki pemahaman yang luas",  
                "pesan":"Semangat terus kuliahnya kak, semoga sehat selalu, dan jangan lupa untuk terus tersenyum" #20
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abang ini tegas, asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus bang bintang kuliahnya, jangan lupa untuk istirahat bang soalnya kegiatan abang banyak sekali, semoga kuliahnya juga tetap bagus dengan nilai yang memuaskan juga pada setiap matkul yang ada" #21
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def departemenpsda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BK8dk83jEIciIsS5ZRWmO61VU7U5R2WT", #22
            "https://drive.google.com/uc?export=view&id=1HuvD1X9ffARDvtI0f6MhRetQdJ3echd8", #23
            "https://drive.google.com/uc?export=view&id=1y3XZcYM6BbOiXeXE1tD_UWW-AV0QvnVa", #24
            "https://drive.google.com/uc?export=view&id=12BiBN6Z-VsYHLTnPc5k5wiV2XiztZ94a", #25
            "https://drive.google.com/uc?export=view&id=1RQTLjJwk8RyCJ_iA9cBh5HglwBX8UFxT", #26
            "https://drive.google.com/uc?export=view&id=1vTeBqoeyR34IvxsBvuWLwtSrffqXyE1L", #27
            "https://drive.google.com/uc?export=view&id=1flMeVOHUJkCnmgAcgSFnsdqrnHE_sT-s", #28
            "https://drive.google.com/uc?export=view&id=1yEAkN20ZAkx1Ha0Mkduqr1CNrMFdfw7u", #29
            "https://drive.google.com/uc?export=view&id=1KX-7P3BHz1vnMDzjTNiSbYK0kCzexo-K", #30
            "https://drive.google.com/uc?export=view&id=1ixrJFfIFSnhdhLJSjnxw8c1-lT6_cO9N", #31
            "https://drive.google.com/uc?export=view&id=1IZdlioTBZ9BuYD6flw7iMwirz-I-CVHd", #32
            "https://drive.google.com/uc?export=view&id=1UlIGJaGmKRpVZsufC8x3VnMN64f68y3z", #34
            "https://drive.google.com/uc?export=view&id=1oF2ILseFnmh3Zb1Gi1EIjQ-he4h933F4", #35
            "https://drive.google.com/uc?export=view&id=1cwwLR90vieznnhcbGXyvQcQldVpU96mt", #37
            "https://drive.google.com/uc?export=view&id=1_D7mOlSQ77xuCoKbwbvWRJW7OrnieDGs", #38
            "https://drive.google.com/uc?export=view&id=1-FsbN3aYy_Q0o9vvlIdusmqovDUx-vr2", #39
            "https://drive.google.com/uc?export=view&id=1zMx6vCEyiaXhOGO1BHABM11H4BhOKkRW", #40
            "https://drive.google.com/uc?export=view&id=1ye2Y3mmSSuyE4saZWb73_E0J6P0S_Dux", #41
            "https://drive.google.com/uc?export=view&id=1Ct4HiQljB6SHDoQoaxqPP2egxClQHMSI", #42
            "https://drive.google.com/uc?export=view&id=15uLORqCIFnJ35eDP_9xc2zsIJ71La-5C", #43
            "https://drive.google.com/uc?export=view&id=1bvJxhNev2QIRxp8IkCQEjvbRygvSwdz3", #44
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
                "pesan":"Semangat terus kuliahnya bang, semoga bisa cepat lulus dengan hasil yang memuaskan, dan mendapatkan pekerjaan sesuai dengan apa yang abnag mau" #22
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
                "sosmed": "@celisabeth",
                "kesan": "Kakak ini asik, cantik, ramah, tegas dan murah senyum, ",  
                "pesan":"Semangat terus kak, jangan lupa tersenyum, iringi usaha dan doa agar sesuatu yang ingin dicapai bisa maksimal kak" #23
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
                "pesan":"Semangat terus kak kuliahnya, dari setiap usaha yang kakak lakukan semoga sesuai dengan hasil yang kakak impikan" #24
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobi": "Main",
                "sosmed": "@allyaislami_",
                "kesan": "Kakak ini asik, dan murah senyum, ramah juga, seru diajak ngobrol dan diskusi juga",  
                "pesan":"Semangat terus kak kuliahnya, semoga hasil yang didapat sesuai dengan kemauan kakak, sehat selalu ya kak, jangan lupa istirahat kak" #25
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiyati",
                "nim": "122450001",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Metro",
                "hobi": "Nyopet",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus, suka bercanda, dan gampang mencairkan suasana",  
                "pesan":"Semangat terus kak, jangan lupa untuk tersenyum, semoga capenya kakak diganti dengan hasil yang sesuai dengan rasa cape itu, sehat-sehat ya kak" #26
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
                "pesan":"Semangat kuliahnya kakak, semoga selalu dalam lindungan-Nya, jangan lupa istirahat ya kak jika kakak merasa cape, untuk nilai yang didapat ga jauh dari AB-A" #27
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
                "pesan":"Semangat terus bang kuliahnya, semoga hasil yang didapat pada setiap mata kuliah yang ada bagus" #28
            },
            {
                "nama":  "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jalan Pagar Alam Kedaton",
                "hobi": "Ngukur jalan",
                "sosmed": "@dransyh_",
                "kesan": "Abang ini asik, baik, dan murah senyum, seru diajak ngobrol, orangnya suka bercanda",  
                "pesan":"Semangat terus bang deri kuliahnya, jangan lupa istirahat bang, sehat=sehat untuk abang, semoga setiap nilai yang diapatkan memuaskan bang" #29
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Travelling",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakak ini asik, baik, dan murah senyum, ramah, kalem",  
                "pesan":"Semangat terus kuliahnya kak kuliahnya, sehat selalu ya kak, jika ada masalah yang kakak punya hadapin dengan tenang ya kak, semoga IPK kakak terus meningkat tiap semester" #30
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
                "kesan": "Kakak ini asik, baik dan ramah, murah senyum, friendly juga, dan kakak ini kalem sekali",  
                "pesan":"Semangat terus kak kuliahnya, sehat-sehat selalu ya kak" #32
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobi": "Asprak",
                "sosmed": "@johanneskrsjnnn",
                "kesan": "Abang ini tegas, asik, murah senyum, orangnya juga tegas dan friendly, serta saya suka ootd yang dipake abang ini",  
                "pesan":"Semangat terus bang jo kuliahnya, semangat juga untuk pertandingan basket yang mendatang, sehat selalu serta dalam lindungan-Nya, jangan lupa istirahat bang" #34
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
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobi": "Dengerin The Adams",
                "sosmed": "@presilliamg",
                "kesan": "Kakak ini asik, baik, dan murah senyum",  
                "pesan":"Semangat terus kak kuliahnya, semoga hasil nilai dari setiap matkul bagus kak, dan terus meningkat tiap semester, sehat selalu ya kak" #37
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
                "pesan":"Semangat terus kuliahnya kakak, semoga apa yang kakak imipikan, baik itu nilai, pekerjaan, bahkan jadi apa di masa depan bisa terwujud ya kak" #38
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok, Jawa Barat",
                "alamat": "Jalan Airan Raya",
                "hobi": "Dengerin juicy luicy",
                "sosmed": "@sahid_maul19",
                "kesan": "Abang ini asik, ramah, berwibawa mempunyai pikiran serta public speaking yang bagus, dan cocok diajak diskusi",  
                "pesan":"Semangat terus bang, sehat selalu, selalu dalam lindungan-Nya, iringi usaha dengan doa supaya hasil lebih maksimal bang, semoga setiap usaha dan doa sesuai dengan hasilnya ya bang" #39
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
                "pesan":"Semangat terus kuliahnya kak, semoga performa kakak di basket terus meningkat kak, dan untuk akademik semoga kakak bisa cepat lulus dengan hasil yang memuaskan" #40
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
                "pesan":"Semangat terus bang kuliahnya, semoga bisa cepat lulus dengan hasil yang memuaskan, jangan pernah bosen nolong orang bang, terimaksih sudah menolong saya mencari kunci di bypass bang" #41
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "Abang ini asik, baik, dan ramah, friendly, dan gampang berbaur dengan siapa saja",  
                "pesan":"Semangat terus bang kuliahnya semoga cepat lulus dengan nilai yang bagus, semangat jadi pj Mobile Legends nya bang" #42
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv",
                "kesan": "Kakak ini asik, cantik, murah senyum dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak kuliahnya, semoga dari jerih payah kakak hasil nilai ujian yang didapat setimpal ya kak, sehat selalu kak, jangan lupa senyum kak" #43
            },
            {
                "nama":  "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Abang ini asik, baik, orangnya kalem juga, dan ramah",  
                "pesan":"Semangat terus bang kuliahnya, terus berusaha dan berdoa bang, dan untuk semester selanjutnya saya doakan abang tidak ada lagi yang mengulang matkul, sehat selalu bang" #44
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenpsda()
    
elif menu == "Departemen MIKFES":
    def departemen_mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LPWD-gDJpIV_wn3_-gpvlFbwocQ1cPOH", #45
            "https://drive.google.com/uc?export=view&id=1TWpkXvYOFkIFg4d4HqvK-IXC059wWBlf", #46
            "https://drive.google.com/uc?export=view&id=1MC6kdaqg2Nlb6V0-H6SAermZ8pAa_bNL", #48
            "https://drive.google.com/uc?export=view&id=1u3ObS1xNusM40hJenMg1z7Dd6gwPi7iT", #50
            "https://drive.google.com/uc?export=view&id=1uPqY_7qlxg0J-D5nSgabEQ70-_Ko2Qck", #51
            "https://drive.google.com/uc?export=view&id=14wRDE4igCAEn46UsW8HxdBqp6iCNRZGK", #53
            "https://drive.google.com/uc?export=view&id=1SLQH-VW9FNWP29o0nVVRnkyUYRKLq56H", #54
            "https://drive.google.com/uc?export=view&id=1fbpkSmskM4wgfCcnztr9KHNi4e3i6oNS", #55
            "https://drive.google.com/uc?export=view&id=1uYGw5mc6Bb3nvAj3tNCxMCIuHbskXcVm", #56
            "https://drive.google.com/uc?export=view&id=1xsAwn3ZngdXr-cjQfSOIb50HeoaNHEg0", #57
            "https://drive.google.com/uc?export=view&id=1dzCL700jm3frrMLHeiuRVHGqg3UVinXM", #58
            "https://drive.google.com/uc?export=view&id=1VFnk7hatyzE7LQEKnkaDyH-X-1ldq4A_", #60
            "https://drive.google.com/uc?export=view&id=1N5Quim5BZzCJ37WQnKxVjuCtMogpCyFh", #61
            "https://drive.google.com/uc?export=view&id=1mVPv4BFpoiFYlmPStnc9nY1Ild96ccZr", #62
            "https://drive.google.com/uc?export=view&id=1yyIb4HueVQljI_EYzDmwOgFSiP8B_VSR", #63
            "https://drive.google.com/uc?export=view&id=1bdBEZVaGVFImxosV17agg-rIx7ZkGKdb", #64
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
                "umur": "21",
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
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Sangat percaya diri dan mampu menjawab pertanyaan dengan baik",  
                "pesan":"Terus tingkatkan kepercayaan diri bang dalam setiap kesempatan" #48
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl. Permadi",
                "hobi": "Ngasprak ADS",
                "sosmed": "@mregiiii_",
                "kesan": "Abang ini Komunikasinya jelas dan efektif, enak banget diajak ngobrol",  
                "pesan":"Semangat terus kak ngaspraknya dan semangat terus dalam membagi ilmunya, sehat selalu" #50
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Gg. Yudistira",
                "hobi": "Review jurnal Bu Mika",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakak ini berpengetahuan luas dan selalu update dengan tren terbaru",  
                "pesan":"Teruslah belajar dan mencari tahu hal-hal baru semoga di masa depan jurnal kakak bisa lebih dikenal" #51
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal":"Bukittinggi",
                "alamat": "Korpri",
                "hobi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "Abang ini sangat sabar dalam menjelaskan, bikin saya mudah paham",  
                "pesan":"Tetap semangat berbagi ilmu ya bang, semoga selalu diberi kesehatan" #53
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobi": "Resume Webinar",
                "sosmed": "@anjaniiidev",
                "kesan": "Kakak ini memiliki pemahaman yang mendalam, bikin saya kagum",  
                "pesan":"Terus tingkatkan pengetahuannya kak dan bagikan kepada orang lain, ya" #54
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobi": "Membaca jurnal Bu Mika",
                "sosmed": "@dindanababan",
                "kesan": "Kakak ini cara menjelaskan jelas dan sistematis",  
                "pesan":"Semoga sukses dalam setiap langkah, terus berkarya kak" #55
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review jurnal Bu Mika",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak ini sangat inspiratif, bisa memotivasi orang lain",  
                "pesan":"Teruslah menjadi sumber inspirasi bagi banyak orang kak" #56
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobi": "Menghitung akurasi",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak ini sikapnya yang ramah membuat suasana jadi akrab",  
                "pesan":"Semoga selalu menjaga kebaikan hati, ya kak" #57
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini memiliki kemampuan mendengarkan yang luar biasa",  
                "pesan":"Semoga selalu bisa menjadi teman & kakak yang baik bagi semua" #58
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Korpri",
                "hobi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "Abang ini sangat menghargai pendapat orang lain",  
                "pesan":"Semoga selalu menginspirasi orang lain untuk berbicara ya bang" #60
            },
            {
                "nama": "Eggi satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Korpri",
                "hobi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "Abang ini konsisten dalam menyampaikan materi, sangat profesional",  
                "pesan":"Terus pertahankan profesionalismenya bang, sukses selalu bang" #61
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakak ini penuh motivasi, membuat saya lebih bersemangat",  
                "pesan":"Teruslah memotivasi, semoga selalu diberikan keberkahan kak" #62
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Karang Anyar",
                "hobi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #63
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten",
                "alamat": "Jl Nangka 3",
                "hobi": "Berolahraga",
                "sosmed": "@randardn",
                "kesan": "Abang ini sangat antusias saat berbagi pengetahuan",  
                "pesan":"Semoga antusiasme itu terus ada, sukses untuk abang randa" #64
            },
         ]
        display_images_with_data(gambar_urls, data_list)
    departemen_mikfes()

elif menu == "Departemen Eksternal":
    def departemeneksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bPLIPW1A5KkyEmXsLsoU8os_uGKiVvRY", #66
            "https://drive.google.com/uc?export=view&id=1nkBWzEDdFTh2pySvmLUeE-DhLnHDrXeF", #68
            "https://drive.google.com/uc?export=view&id=1666oWCFY0ZVObrEvIldvX99Mjv-GkQBk", #69
            "https://drive.google.com/uc?export=view&id=1i5MIiPXwvTcanmp4vWOxFn3WXeMBqNPx", #70
            "https://drive.google.com/uc?export=view&id=1pFyetHn-y6l0B2tF0jNDtabrS7nzhhDI", #71
            "https://drive.google.com/uc?export=view&id=1-zK-h9nDknOjmUjxUY9EEOzme3JJYQNh", #72
            "https://drive.google.com/uc?export=view&id=1rtFVxvMVu5tPo4i2iHbragC-_gl6anYW", #73
            "https://drive.google.com/uc?export=view&id=10acMfFkqrpUvYlYRf5cnDyvlFL6HqzDa", #74
            "https://drive.google.com/uc?export=view&id=1I25ugGkPs-fLLJJa7GLi7zvvEVWRjNR0", #75
            "https://drive.google.com/uc?export=view&id=1hh-XuS2CU8uc06vnnClK2mYWKyFCrnla", #76
            "https://drive.google.com/uc?export=view&id=1-V3XCObKO7vVPxoB01JD-yV6ZjLWEJI-", #77
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
                "nim": "121450041",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Jati Mulyo",
                "hobi": "Bangun Pagi",
                "sosmed": "@yogyyy",
                "kesan": "Abang ini asik, tegas, baik, penuh rasa empati, membuat orang merasa diperhatika",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan, dan semoga selalu bisa merasakan dan memahami perasaan orang lain" #66
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
                "sosmed": "@bastiansilaban_",
                "kesan": "Abang ini Mampu menjawab pertanyaan dengan jelas dan tepat sasaran",  
                "pesan":"Semoga selalu sabar dan bersemangat dalam menjawab pertanyaan bang" #69
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobi": "Dengerin musik",
                "sosmed": "@deaarsn",
                "kesan": "Kakak ini sangat empati dan peka terhadap perasaan orang lain",  
                "pesan":"Semoga selalu bisa memahami dan mendukung teman-teman bahkan lingkungan di sekitar kakak" #70
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450005",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Kirim BC-an",
                "sosmed": "@esteriars",
                "kesan": "Kakak ini Kehadirannya selalu membawa energi positif ",  
                "pesan":"Semoga terus bisa menyebarkan kebaikan di mana pun berada ya kak" #71
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal":"Jakarta Timur",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kakak ini sikapnya rendah hati, open minded, positif vibes, dan friendly",  
                "pesan":"Semangat terus kakak kuliahnya, selalu menebarkan energi-energi positif yang kakak punya ya" #72
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobi": "Jadi Humas",
                "sosmed": "@natee__15",
                "kesan": "Kakak ini membawa suasana yang ceria dan menyenangkan",  
                "pesan":"Semoga selalu bisa membawa keceriaan di sekitar ya kak" #73
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobi": "Pulang malam",
                "sosmed": "@jasminednva",
                "kesan": "Kakak ini sangat analitis, membuat diskusi menjadi lebih mendalam",  
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
                "pesan":"Teruslah berpikir kritis dan berbagi analisis yang cerdas ya kak" #75
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
                "asal":"Bekasi",
                "alamat": "TVRI",
                "hobi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "Penuh dengan ide-ide segar yang membuat semua terinspirasi",  
                "pesan":"Teruslah berpikir kreatif dan berbagi ide-ide hebat bang" #77
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal":"Muara enim",
                "alamat": "Korpri",
                "hobi": "Nyuci baju",
                "sosmed": "@u_yippy",
                "kesan": "Kakak ini sangat inspiratif dan penuh motivasi, selalu mendorong orang lain",  
                "pesan":"Semoga terus menginspirasi banyak orang dengan semangat kakak" #80
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan": "Abang ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
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
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobi": "Masak",
                "sosmed": "@izzalutfia",
                "kesan": "Kakak ini Ccra bicaranya tenang dan meyakinkan, membuat semua orang merasa nyaman",  
                "pesan":"Semangat terus kak kuliahnya, terus jaga ketenangan itu ya kak dengan hobi memasak semoga kakak bisa menjadi chef" #83
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "daplok kelompok 1",
                "sosmed": "@alyaavanefi",
                "kesan": "Kakak ini cantik, asik, baik, murah senyum, best lah, this is daplok kelompok 1",  
                "pesan":"Semangat terus kak kuliahnya, semoga hasil selalu bagus setiap ujian dengan matkul apapun itu" #84
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Ngeresume Seminar",
                "sosmed": "@rayths_",
                "kesan": "Penuh perhatian dan selalu mendengarkan dengan baik",  
                "pesan":"Semoga sikap abang yang penuh perhatian itu tetap ada, yaa bang" #85
            },
            {
                "nama": "Tria Yunanni",
                "nim": "121450062",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Way Kanan",
                "hobi": "Baca",
                "sosmed": "@tria_y062",
                "kesan": "Kakak ini memiliki humor yang segar, bikin suasana jadi ceria",  
                "pesan":"Teruslah menghibur orang dengan humor dan keceriaan kakak, semoga dengan hobi membaca suatu saat nanti kakak bisa membuat sebuah buku hasil karya kakak" #86
            },
         ]
        display_images_with_data(gambar_urls, data_list)
    departemeneksternal()

elif menu == "Departemen Internal":
    def departemeninternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1MAastkagwtGWUC9GzEdMGB0IzUsJLtqA", #87
            "https://drive.google.com/uc?export=view&id=1KiBZtdMhh0B1mksLm2GMpV3AzFEVbwHz", #88
            "https://drive.google.com/uc?export=view&id=1SNj0J7eh0fdJDX7rnHaf5pikEOAeCSUf", #89
            "https://drive.google.com/uc?export=view&id=1Pazqi3pSxG18QJc58ALRYtaFpTtn9gRM", #91
            "https://drive.google.com/uc?export=view&id=1aKOuUJrVyuANLyHE6Msc1hxLPHzRlhn8", #92
            "https://drive.google.com/uc?export=view&id=1pkitQk81ZLsrBi0Xoc-D1at3Q8N7y9bB", #93
            "https://drive.google.com/uc?export=view&id=10BLWeQKyUYfyuXaipOfVtGUdW0pepcpT", #94
            "https://drive.google.com/uc?export=view&id=1Cnea6MCIa4MzrOLIHTlkzyWCsqQ6X9uf", #96
            "https://drive.google.com/uc?export=view&id=1f9fENquXS0Joza_pOveBn1pPHjKuOYAl", #99
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
                "kesan": "Abang ini asik, tegas, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi dalam hal apapun, ramah, baik, disiplin",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa cepat lulus dengan hasil yang memuaskan dan ditempatkan di pekerjaan yang sesuai dengan apa yang abang mau" #87
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca novel",
                "sosmed": "@Catherine.sinaga",
                "kesan": "Kakak mampu menyesuaikan diri dengan berbagai situasi dengan baik",  
                "pesan":"Semangat terus kak kuliahnya, semoga bisa lulus dengan hasil yang memuaskan, semoga fleksibilitas kakak tetap menjadi kelebihan yang luar biasa" #88
            },
            {
                "nama": "Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Labuhan Dalam",
                "hobi": "Memelihara Dino",
                "sosmed": "@akbar_resdika",
                "kesan": "Abang ini sangat berpengalaman dan selalu siap berbagi pengetahuan",  
                "pesan":"Semangat terus bang kuliahnya, semoga selalu berkenan membagikan pengalaman yang berharga" #89
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobi": "Nulis lagu",
                "sosmed": "@rendaepr",
                "kesan": "Abang ini asik, baik, sangat disiplin dan teratur dalam mengelola waktu",  
                "pesan":"Semangat terus bang kuliahnya, semoga suatu saat nanti bisa merilis sebuah lagu dan didengar banyak orang" #91
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
                "pesan":"Semangat terus kak kuliahnya, semoga salah satu dari sekian cogan yang dilihat ada yang nyantol kak" #92
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal":"Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobi": "Main Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "Abang ini asik, baik, bisa membuat topik yang sulit jadi lebih mudah dimengerti",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan, dan semoga selalu berkembang dalam dunia futsal" #93
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
                "pesan":"Semangat terus kak kuliahnya, saya harap kakak selalu menjadi morning person, senantiasa konsisten" #94
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan Raya",
                "hobi": "Menghalu",
                "sosmed": "@meiraln",
                "kesan": "Kakak ini asik, baik, dan ceria",  
                "pesan":"Semangat terus kakak kuliahnya, dari saya untuk kakak adalah kurangin ngehalu ya kak" #96
            },
            {
                "nama": "Yosia Letare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal":"Dairi, Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobi": "Bawa motor pake kaki",
                "sosmed": "@yosiabanurea",
                "kesan": "Abang ini asik, baik, murah senyum, dan pembawaanya ceria sekali",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa cepat lulus, dan mendapatkan pekerjaan yang bagus, semoga keceriaan abang membawa berkah untuk abang sendiri" #99
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemeninternal()

elif menu == "Departemen SSD":
    def departemenssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11i-RffyRtIRUkj6MUqYIL9sfKMbmTG-4", #101
            "https://drive.google.com/uc?export=view&id=1-5-T_P7VFs_WbsmNy0D1e5hEm3r0jf6s", #102
            "https://drive.google.com/uc?export=view&id=1KTUmTnSQ6Trz9R61uxCAbE-G97E6UOLY", #103
            "https://drive.google.com/uc?export=view&id=10T4c7w2C2rpuxOHf1hsLWsOxRRhkDuWk", #104
            "https://drive.google.com/uc?export=view&id=19wuPXIPpdBnIwXJxiReZYeyzChyD8oCH", #105
            "https://drive.google.com/uc?export=view&id=1ymVJWI6yKzbJuYEF8_lH9T6xbq7JkEjF", #106
            "https://drive.google.com/uc?export=view&id=1HiDWVumn3aTnMjbb1nY5baAcqAjwz9rl", #107
            "https://drive.google.com/uc?export=view&id=1kZO26W5C2YmMxsgYK1Vy1RmNIowxzT0P", #108
            "https://drive.google.com/uc?export=view&id=1_n5UXf1RulNv4-X4IYfyMbU-G5WZc7js", #109
            "https://drive.google.com/uc?export=view&id=1bbHmOp9GdbCpb4pGrNtJmO0sIP-whmWE", #110
            "https://drive.google.com/uc?export=view&id=1DIb668c7lr60mltzLta7H8YFeFVoxCYO", #111

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
                "kesan": "Abang ini asik, tegas, seru diajak diskusi terutama topik bisnis",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan, dan semoga bisa punya bisnis sendiri setelah lulus dari ITERA" #101
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Kakak ini asik, baik, cantik, ramah, asik sekali mengobrol dan diskusi bareng kakak",  
                "pesan":"Semangat terus Kakak kuliahnya, semoga bisa lulus dengan hasil yang memuaskan, dan dengan hobi yang nonton film semoga di masa depan kakak bisa bikin film sendiri dan di tonton oleh banyak orang" #102
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal":"Simalungun, Sumut",
                "alamat": "Airan",
                "hobi": "Hitung uang",
                "sosmed": "@zhjung_",
                "kesan": "Kakak ini asik, baik, ramah, sangat teliti dan hati-hati dalam setiap langkah",  
                "pesan":"Semangat terus kak kuliahnya, semoga bisa lulus dengan hasil yang memuaskan, dan semoga ketelitian kakak selalu membuahkan hasil yang baik" #103
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Bukittinggi",
                "alamat": "Airan",
                "hobi": "Badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "Abang ini asik, baik, kalem, wajah abang ini juga adem untuk dilihat seperti orang yang taat beribadah",  
                "pesan":"Semangat terus bang kuliahnya, semoga suatu saat nanti bisa menjadi atlet badminton profesional" #104
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Airan",
                "hobi": "Nyuruh-nyuruh",
                "sosmed": "@dananghk_",
                "kesan": "Abang ini asik, suka bercanda juga, paling suka ngobrol dan diskusi bareng abang ini karena ngalir terus, and this is daplok kelompok 1",  
                "pesan":"Semangat terus bang kuliahnya, semoga hasil ujian selalu memuaskan, tetaplah menjadi orang yang senang berbagi soal pengalam dan ilmu bang" #105
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Lapas",
                "hobi": "Apa aja",
                "sosmed": "@farrel_julio",
                "kesan": "Abang ini asik, baik, keren, dan sepertinya bisa apa aja",  
                "pesan":"Semangat terus bang kuliahnya, tetaplah keren selalu dengan hobi abang yang apa aja itu" #106
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
                "pesan":"Semangat terus kak kuliahnya, semoga suatu saat nanti dengan hobi kakak yang suka nulis bisa menerbitkan sebuah buku hasil tulisan kakak" #107
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal":"Kedaton",
                "alamat": "Kedaton",
                "hobi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Kakak ini asik, baik, mampu memecahkan masalah dengan cara yang unik dan efektif",  
                "pesan":"Semoga kreativitas kakak dalam memecahkan masalah selalu berkembang, dan semoga bisa lulus dengan hasil yang memuaskan" #108
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
                "pesan":"Semangat terus kak kuliahnya, semoga kakak bisa di notice bang windah, sehat selalu ya kak" #109
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Balam",
                "alamat": "Jalan Nangka 1",
                "hobi": "Tidur",
                "sosmed": "@dhafinrzqa",
                "kesan": "Abang baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, tetaplah konsisten dalam membagi ilmunya bang" #110
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobi": "Badminton",
                "sosmed": "@meylanielia",
                "kesan": "Kakak ini asik, baik, sangat komunikatif dan tidak ragu untuk berbagi pengetahuan",  
                "pesan":"Semangat terus kakak kuliahnya, semoga bisa menjadi atlet profesional di badminton dan dengan pendidikan yang tinggi juga, sehat selalu ya kak" #111
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenssd()
    
elif menu == "Departemen MEDKRAF":
    def departemenmedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jkuKFGNLHwd7LOuNrcEW2fo-7KYHI6mv", #112
            "https://drive.google.com/uc?export=view&id=14-SZhAULSm8Hs8ZmW2leYoZBEVhi99Kr", #113
            "https://drive.google.com/uc?export=view&id=1XECueK5R4WevA2zr_pK053tDVxjZ4ssU", #114
            "https://drive.google.com/uc?export=view&id=1icAYmK062K8cPljwn3Zx8xzdldHjZyR9", #115
            "https://drive.google.com/uc?export=view&id=1G6FDGR-9RyPXnYLmdLsoRiiPy3cG2U1j", #116
            "https://drive.google.com/uc?export=view&id=1bpPHniXJWhhRkLKPW9zeFDBmXFzljXjR", #117
            "https://drive.google.com/uc?export=view&id=1B61syVG5AjoXi8r_J0OdcrdAFbAyxfQm", #118
            "https://drive.google.com/uc?export=view&id=12Rkf9Jm0-dJzdiZFQQB66-t8yXAGF8Ot", #119
            "https://drive.google.com/uc?export=view&id=14vSMBMMEImeocaU1IrmbAyjFS22y6Q4A", #120
            "https://drive.google.com/uc?export=view&id=10jwjo6zJ-mFw1xmWkKFNuWoUGm8eVf7Q", #121
            "https://drive.google.com/uc?export=view&id=1yz9WslVPsBRf8ulL2M66Yvv4P1bl6ERv", #122
            "https://drive.google.com/uc?export=view&id=16Q-Bgx98KZPdZfb-YGOE8iC547mAuQEu", #123
            "https://drive.google.com/uc?export=view&id=1KA5BxnM8iVeqixic0Psr_CPHk7wqkNnr", #124
            "https://drive.google.com/uc?export=view&id=1jePKimMsnCoyYoQHU10mlJAsq4S5_-HS", #125
            "https://drive.google.com/uc?export=view&id=1mT65K_RaI10jqVAbBi00-3Q8crLyxlva", #126
            "https://drive.google.com/uc?export=view&id=1txnBDiOWOdaK5z6Sk-x4BHqkGb1_3y4Z", #127
            "https://drive.google.com/uc?export=view&id=1Ui2J-IphlXapPcKKGcngKLFbzZKMQcvy", #128
            "https://drive.google.com/uc?export=view&id=1SIk2_7_YDOM99MeOEOo9NTqRjjzBWWoC", #129
            "https://drive.google.com/uc?export=view&id=19AXaGW1OOyqf-X--Qg5nY5PQUbhoI7zj", #130
            
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
                "kesan": "Abang ini tegas, baik, sangat menghargai orang lain, disiplin, serta seru untuk diajak diskusi",  
                "pesan":"Semangat bang semoga bisa cepat lulus, dan mendapatkan pekerjaan yang bagus, sesuai kemampuan dan minat abang, semoga semangat abang tidak pernah padam ya" #112
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "Kakak ini cantik, asik, baik, murah senyum, disiplin dan sedikit tegas, ",  
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
                "nim": "122450045",
                "umur": "20",
                "asal":"Natar",
                "alamat": "Natar",
                "hobi": "Menyibukkan diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "Kakak ini ceria, gampang mencairkan suasana yang rumit menjadi lebih murah, dan baik juga",  
                "pesan":"Semoga tetap konsisten dalam menebar energi positif kakak, dan selalu menebar kebahagiaan kepada orang lain" #116
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Nulis, baca, fangirling",
                "sosmed": "@nanana.minjoo",
                "kesan": "Sangat komunikatif dan tidak ragu untuk berbagi pengetahuan, cantik, baik",  
                "pesan":"Teruslah berbagi ilmu, ya kak Itu sangat berarti bagi banyak orang, semoga kakak dalam lindungan tuhan selalu dan diberikan kesehatan" #117
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobi": "Nonton film",
                "sosmed": "@patriciadiajeng",
                "kesan": "Cantik, positive vibes, baik, seru diajak ngobrol, dan ramah juga, serta murah senyum",  
                "pesan":"Semangat kak kuliahnya, jangan lupa senyum, bahagia selalu, dan mendapatkan nilai yang bagus untuk matkul apapun itu, teruslah menjadi penyemangat dan kebahagiaan kepada orang lain dan lingkungan sekitar" #118
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Sukarame",
                "hobi": "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan": "Baik, ramah, orangnya santai, suka bercanda, murah senyum, dan pembawaannya selalu ceria & happy",  
                "pesan":"Sehat selalu ya kak, semoga kakak tidak pernah bosan dalam penebar kebahagiaan bagi orang lain, semoga selalu dijaganya oleh tuhan YME " #119
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobi": "Bernyanyi dan menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": " ",  
                "pesan":" " #120
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar",
                "hobi": "Lagi Nyari",
                "sosmed": "@dino_kiper",
                "kesan": "Abang ini lucu, suka bercanda, baik, seru diajak ngobrol juga ",  
                "pesan":"Semangat bang terus bang kuliahnya, semoga bisa cepat lulus, sehat selalu, dan mendapatkan pekerjaan sesuai yang abang mau" #121
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobi": "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan": "Kakak ini sangat berempati dan penuh perhatian terhadap lingkungan",  
                "pesan":"Semoga selalu peduli terhadap orang-orang di sekitarmu, semoga bisa menerbitkan buku suatu saat nanti kak, dan semoga dengan hobi membaca pengetahuan kakak semakin bertambah" #122
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf UIN",
                "hobi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "abang ini baik, lucu, ramah, dan tampan, abang ini juga mampu menjalin hubungan yang baik dengan semua orang",  
                "pesan":"Semoga hubungan baik itu terus terjaga, ya bang, semangat terus kuliahnya bang" #123
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobi": "Nonton Drakor",
                "sosmed": "@nsywanaf",
                "kesan": " ",  
                "pesan":" " #124
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jalan Nangka 2",
                "hobi": "Baca Novel yang Bikin Nangis",
                "sosmed": "@prskslv",
                "kesan": "Kakak ini cantik dan baik",  
                "pesan":"Semangat kak kuliahnya semoga bisa pergi ke Korea Selatan suatu saat nanti" #125
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "Abang ini tampan, baik, ramah, apabila menjawab sebuah pertanyaan gampang di mengerti",  
                "pesan":"Sehat selalu bang, jangan pernah bosan dalam membagi ilmunya ya bang, apalagi yang berhubungan dengan codingan" #126
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Belwis",
                "hobi": "Mengerjakan tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "positive vibes, baik, ramah, dan friendly ",  
                "pesan":"semangat kak kuliahnya, kurangi ngeluh, dan semoga hasil nilai yang didapat selalu memuaskan " #127
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa Labuhan dalam",
                "hobi": "Ngoding, gaming",
                "sosmed": "@abitahmad",
                "kesan": "Abang ini asik, lucu, baik, friendly, pintar juga",  
                "pesan":"Semangat terus bang kuliahnya, semoga ga pernah ngulang lagi bang" #128
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Panjibako",
                "alamat": " Bandar Lampung",
                "hobi": " Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Abang ini asik, pemikirannya luas, ramah, dan abang sangat teliti dalam menyampaikan informasi, tidak ada yang terlewat",  
                "pesan":"Semangat terus bang kuliahnya, semoga ketelitianmu selalu memberikan hasil yang maksimal dan semoga abang sehat selalu supaya bisa membagikan ilmu yang dimiliki" #129
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Wisma Hana Hani",
                "hobi": "Bengong/ Membaca buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Abang ini asik, tegas, baik, berwibawa, keren, cocok menjadi inspirasi bagi semua orang",  
                "pesan":"Semangat terus bang kuliahnya, tetaplah konsisten dalam menjadi inspirasi bagi semua orang bang, dan kurangin bengongnya bang" #130
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenmedkraf()
        
       
             



             
        
        
            
