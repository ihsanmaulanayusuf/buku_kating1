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
            "https://drive.google.com/uc?export=view&id=1pHCPurAGtHLG8hhf8JlAEnxT7i_8oYqY", #1
            "https://drive.google.com/uc?export=view&id=1pQkb6oMl8MsJlHwcBfSrjPH4Fvw0uABs", #2
            "https://drive.google.com/uc?export=view&id=1pF0tjkPfpbPcELLrQ4Ef7c6MqDBm8Bgj", #3
            "https://drive.google.com/uc?export=view&id=1pMMV9oVLXJfaIbk7lYjqXzdN6CgCSJnU", #4
            "https://drive.google.com/uc?export=view&id=1pFn6DNTJ5Bel9lJuSzL_cbM2s1nR_i9N", #5
            "https://drive.google.com/uc?export=view&id=1pPBkaqOFBreeI6tTviG9MxwG7jjZ8dTs", #6
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
                "kesan": "bang kharisma sangat berwibawa dan memiliki wawasan yang luas",  
                "pesan":"semoga bang kharisma semakin sukses dalam himpunan maupun di luar himpunan"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Bukit Kemuning",
                "alamat": "Pawen 2 Sukarame",
                "hobi": "Main gitar",
                "sosmed": "@pndrinsni21",
                "kesan": "Bang Pandra orangnya asik dan tegas",  
                "pesan":"semoga bang pandra semakin sukses dalam himpunan maupun di luar himpunan"# 2
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kotabaru",
                "hobi": " Nonton Drakorr",
                "sosmed": "@wulandarimeliza",
                "kesan": "kak meliza orangnya baik dan asik",  
                "pesan":"semoga kak meliza semakin sukses dalam himpunan maupun di luar himpunan"# 3
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "kak hartiti ramah dan mudah senyum",  
                "pesan":"semoga kak meliza semakin sukses dalam himpunan maupun di luar himpunan"# 4
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "Nangka 4",
                "hobi": "Dengerin  bang Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kak putri pembawaannya baik , ramah, dan mudah senyum",  
                "pesan":"Ssemoga kak putri semakin sukses dalam himpunan maupun di luar himpunan"# 5
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kotabaru",
                "hobi": "Dengerin  bang Pandra Gitaran",
                "sosmed": "@nadillaadr26",
                "kesan": "Kak nadilla mudah senyum dan baik",  
                "pesan":"semoga kak nadilla semakin sukses dalam himpunan maupun di luar himpunan"# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1pk-ejc5BroWimNrIqzy7vHc32x3AZo4z", #7
            "https://drive.google.com/uc?export=view&id=1pnQwBdI8d_KBpxDdj36iO5Bf3akZ1zuJ", #8
            "https://drive.google.com/uc?export=view&id=1q--U4G4GczFrHDe_VuSfSg3c84aSdV_K", #9
            "https://drive.google.com/uc?export=view&id=1pxO7NgXtSLLhEMlNhpoKKkFsuvJM3gET", #10
            "https://drive.google.com/uc?export=view&id=1q9VBbGxFfARX0PaBx7beF3bV5ZodrK_G", #11
            "https://drive.google.com/uc?export=view&id=1q7VB6D2DVZfz2iXA3qXMfp631lwFdw0i", #12
            "https://drive.google.com/uc?export=view&id=1pahloEKWL1Piki8l-ozribwaN8sMxNhB",
            "https://drive.google.com/uc?export=view&id=1pge39OdEP_uNU1mUF4aXFdpvEgK5-j88", #13
            "https://drive.google.com/uc?export=view&id=1q2O_hYNI5pAbA0t8xvmRhyMPsOMJXAxR", #14
            "https://drive.google.com/uc?export=view&id=1piufZmfFTdwIZUmHYjgntPAEbb-zf6aU",
            "https://drive.google.com/uc?export=view&id=1pp_qr_nHz-QXnmZeyqGDOKRy0O5nJmcj", #15
            "https://drive.google.com/uc?export=view&id=1q6pfhMRjcGUD59unfidgr6FrdcPLN1kf", #16
            "https://drive.google.com/uc?export=view&id=1q5cyhlZqkME5FjCB8p-87US5LXti-qvU", #17
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
                "kesan": "kak tri humoris, mudah bergaul, dan perhatian",  
                "pesan":"semoga kak tri semakin sukses dalam himpunan maupun di luar himpunan" #7
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450124",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Way Huwi",
                "hobi": "Membaca",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kak cahya trendy banget dan manis",  
                "pesan":"semoga kak cahya semakin sukses dalam himpunan maupun di luar himpunan" #8
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Menonton Film",
                "sosmed": "@wlsbn0",
                "kesan": "kak wulan baik dan positif vibes",  
                "pesan":"semoga kak wulan semakin sukses dalam himpunan maupun di luar himpunan" #9
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobi": "Nonton Dracin",
                "sosmed": " @anisadini10",
                "kesan": "kak dini baik dan mudah senyum",  
                "pesan":"semoga kak dini semakin sukses dalam himpunan maupun di luar himpunan" #10
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bernung, Pesawaran",
                "alamat": "Bandar Lampung",
                "hobi": "Nonton Drakor",
                "sosmed": " @ansftynn_",
                "kesan": "kak fitri baik dan ramah bangett",  
                "pesan":"semoga kak fitri semakin sukses dalam himpunan maupun di luar himpunan" #11
            },
            {
                "nama": " Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Belwis",
                "hobi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "bang feryadi mudah senyum dan baik",  
                "pesan":"semoga bang feryadi semakin sukses dalam himpunan maupun di luar himpunan" #12
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "kak clau orangnya baik, my singer team",  
                "pesan":"semoga kak clau semakin sukses dalam himpunan maupun di luar himpunan" #13
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobi": "Baca Al-qur’an",
                "sosmed": "@fleurnsh",
                "kesan": "Kak renisha asikk dan pembawaannya alim",  
                "pesan":"semoga kak renisha semakin sukses dalam himpunan maupun di luar himpunan" #14
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Bang Mirzan orangnya baik",  
                "pesan":"semoga bang mirzan semakin sukses dalam himpunan maupun di luar himpunan" #15
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Ogan Ilir",
                "alamat": "Natar",
                "hobi": "Nyari Sinyal di Gedung F",
                "sosmed": "@_.dheamelia",
                "kesan": "kak dhea kece dan asik",  
                "pesan":"semoga kak dhea  semakin sukses dalam himpunan maupun di luar himpunan" #16
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450126",
                "umur": "22",
                "asal":"Surakarta",
                "alamat": " Sukarame",
                "hobi": "Melukis",
                "sosmed": "@fhrul.pdf",
                "kesan": "Bang Fahrul asik dan mudah bergaul",  
                "pesan":"emoga bang fahrul semakin sukses dalam himpunan maupun di luar himpunan" #17
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Way Huwi",
                "hobi": "Baca Buku, Ngoding, Ibadah",
                "sosmed": "@berlyyanda",
                "kesan": "kakak berliana baik dan keren",  
                "pesan":"semoga kak Berliana semakin sukses dalam himpunan maupun di luar himpunan" #18
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20", 
                "asal":"Bandar Lampung",
                "alamat": "Billabong, Gedong Air",
                "hobi": "Suka Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "bang jeremy baik dan humoris",  
                "pesan":"semoga bang jeremy semakin sukses dalam himpunan maupun di luar himpunan" #19
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18nzsh3oRtT970-n4rFcpiB5mzFcdwJEG", #20
            "https://drive.google.com/uc?export=view&id=18_vPbYy-748Rmxg9ZHJV2jhVqWqfLEyr", #21
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
                "kesan": "Kak luthfi orangnya baik , ceria dan public speakingnya bagus bangeet",  
                "pesan":"Semoga Kak luthfi semakin sukses baik didalam maupun luar himpunan" #20
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "bang bintang orang yang sangat aktif dan disiplin",  
                "pesan":"Semoga bang bintang semakin sukses di dalam maupun luar himpunan" #21
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def departemenpsda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YUj1rA1R7eR5HuLwEeBlO8rq1f8IYlC0", #22
            "https://drive.google.com/uc?export=view&id=1ZEmkMLtffVrIXwJPEvgcQacmxlx9PLsA", #23
            "https://drive.google.com/uc?export=view&id=1ZAMZw3n5FMl7Fm8lD0n55lE3uKA1E-EA", #24
            "https://drive.google.com/uc?export=view&id=1ZENVxN3AXdz57OTS0Xs9hSThsvJ2zGSa", #25
            "https://drive.google.com/uc?export=view&id=1YbOTchA4MqemvlugWfnjTL5QIQuINqOz", #26
            "https://drive.google.com/uc?export=view&id=1Z8i1FDXg9ot6Xi8t2SpQyaAYSnhjaDRp", #27
            "https://drive.google.com/uc?export=view&id=1Yk556WBA1XNXxMDBtG0NkWDirMYrymG8", #28
            "https://drive.google.com/uc?export=view&id=1YcRL6SS06Rh6c00UP-kOVWeO5dkia7s5", #29
            "https://drive.google.com/uc?export=view&id=1Y_JbJqFNfu4K6pT_QTdchsAjuK7Pw9jw", #30
            "https://drive.google.com/uc?export=view&id=1YHwXs_aCaXdrAZTiiJdFfpoGjU4fElPm", #31
            "https://drive.google.com/uc?export=view&id=1YySgWmaeu7bwY-Rg30Gz2JLdsRaVRn19", #32
            "https://drive.google.com/uc?export=view&id=1YOZPBx5QQFUGj_zFaBlP_UHLwl4BA01C", #33
            "https://drive.google.com/uc?export=view&id=1YPn8zJFRcp9PfTQ_Zkl8qme_YTLSG_hh", #34
            "https://drive.google.com/uc?export=view&id=1YIYeQuZ6RPJuVR2_mlgg8dSbzL6fl-5P", #35
            "https://drive.google.com/uc?export=view&id=1YTjz2bNXWmwoClQS4vyJuQgOdeuYuNqh", #36
            "https://drive.google.com/uc?export=view&id=1XzSUlEDikqjsIDRWAtOfygAl6gPeMpG2", #37
            "https://drive.google.com/uc?export=view&id=1Y2yj3_Ap8G95MeiEYkCwA1clq3mZXMdv", #38
            "https://drive.google.com/uc?export=view&id=1YppUQUdQCSTGVdiXAgHnt2HR7Knd6wf4", #39
            "https://drive.google.com/uc?export=view&id=1YkXeFZz3l_nQrK2IpQ6R8UWglDFwynr8", #40
            "https://drive.google.com/uc?export=view&id=1Z4xI2Bn4C3kppnRzRF7cFStyOUcO6hMB", #41
            "https://drive.google.com/uc?export=view&id=1YsfJXTvkEyQ-IeVeRYq-wUh7x6dOymmN", #42
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
                "pesan":"Semangat terus kuliahnya bang, semoga bisa cepat lulus dengan hasil yang memuaskan" #22
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
                "sosmed": "@celisabeth",
                "kesan": "Kakak ini asik, dan murah senyum",  
                "pesan":"Semangat terus kak, jangan lupa tersenyum" #23
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
                "pesan":"Semangat terus kak kuliahnya" #24
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobi": "Main",
                "sosmed": "@allyaislami_",
                "kesan": "Kakak ini asik, dan murah senyum",  
                "pesan":"Semangat terus kak kuliahnya, semoga hasil yang didapat sesuai dengan kemauan kakak" #25
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiyati",
                "nim": "122450001",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Metro",
                "hobi": "Nyopet",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak, jangan lupa untuk tersenyum" #26
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
                "pesan":"Semangat kuliahnya kakak" #27
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
                "pesan":"Semangat terus bang kuliahnya, semoga hasil yang didapat bagus" #28
            },
            {
                "nama":  "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jalan Pagar Alam Kedaton",
                "hobi": "Ngukur jalan",
                "sosmed": "@dransyh_",
                "kesan": "Abang ini asik, baik, dan murah senyum, seru diajak ngobrol",  
                "pesan":"Semangat terus bang" #29
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Travelling",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakak ini asik, baik, dan murah senyum",  
                "pesan":"Semangat terus kuliahnya kak" #30
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
                "kesan": "Kakak ini asik, baik dan ramah",  
                "pesan":"Semangat terus kak kuliahnya" #32
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobi": "Asprak",
                "sosmed": "@johanneskrsjnnn",
                "kesan": "Abang ini tegas, asik, murah senyum, dan friendly",  
                "pesan":"Semangat terus bang kuliahnya" #34
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
                "pesan":"Semangat terus kak kuliahnya" #37
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
                "pesan":"Semangat terus kuliahnya kakak" #38
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
                "pesan":"Semangat terus bang" #39
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
                "pesan":"Semangat terus kuliahnya kak" #40
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
            "https://drive.google.com/uc?export=view&id=1_nXi6BLo_F-PDUWNl6WaFzmJcONSEeAg", #45
            "https://drive.google.com/uc?export=view&id=1_oDM_DIDsW4osl783LtfMvZc0aNzgTEl", #46
            "https://drive.google.com/uc?export=view&id=1_RUbegWS-6E82FtNbMZPVcu9fNYz-SDA", #47
            "https://drive.google.com/uc?export=view&id=1_MPrJrodvQr3BOXGkf-lrufTwZLHae2q", #48
            "https://drive.google.com/uc?export=view&id=1_CSi-vrp7TnIR0-2ICwAsdIRsNRC7X8g", #49
            "https://drive.google.com/uc?export=view&id=1_i5dPKfljdAfx76A1ES5j1fpYfB0sZ3g", #50
            "https://drive.google.com/uc?export=view&id=1_ppt2dX6Ig7adPduH6usX4OhconXEs-o",
            "https://drive.google.com/uc?export=view&id=1_n3s4EI1eDuuBJH5470-kXwMQ3sr1bdu", #52
            "https://drive.google.com/uc?export=view&id=1_VIsuuFA9NvZNf9AgmfLlXZ7fzENggXJ", #53
            "https://drive.google.com/uc?export=view&id=1_b76Q9revbSnipwpuaQf8jdAwq_10nDP", #54
            "https://drive.google.com/uc?export=view&id=1_QOMZnEl-CKwGel5HSKhtc357onaOPAV", #55
            "https://drive.google.com/uc?export=view&id=1__Pfy_4qXxnuRpEjJ0MwT9WckK_XfWA_",
            "https://drive.google.com/uc?export=view&id=1aL3DZMQo3Ef9B_b6Oau0PAWVUbsW6n6b", #57
            "https://drive.google.com/uc?export=view&id=1_Rfo6qAK4QQ4wnhdLxrqKvMFdc_EJo9a", #58
            "https://drive.google.com/uc?export=view&id=1_GtAtjHLcDWEJqtTj1YsHRJF8wSupg3S", #59
            "https://drive.google.com/uc?export=view&id=1a-5JTSaOj2up2JcHXLLmHhw2N4tTF7r8", #60
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
                "pesan":"Semangat terus kak" #47
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
                "pesan":"Semangat terus kak" #48
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
                "pesan":"Semangat terus kak" #49
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
                "pesan":"Semangat terus kak" #50
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
                "pesan":"Semangat terus kak" #51
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
            "https://drive.google.com/uc?export=view&id=1kBeaDPyYw0hKKRsEyVkF9VrwDZP2pekB", #66
            "https://drive.google.com/uc?export=view&id=1kO9vC-CUy_wmyzAH22FUi1VD9wwU1yhn", #67
            "https://drive.google.com/uc?export=view&id=1or7T6Yzu4TqpdnWLASzrkSiL84eWecyY", #68
            "https://drive.google.com/uc?export=view&id=1kgcdRD2hWxpWEfIq0Og6Cbvr0zOmJdkH", #69
            "https://drive.google.com/uc?export=view&id=1kUk9fvP3EX4Q4PxSfdpj1XemtSEF8aDy", #70
            "https://drive.google.com/uc?export=view&id=1p1bpgh3ROKQ7bwFKgt_FF69FOyH7lHmg", #71
            "https://drive.google.com/uc?export=view&id=1kOMbN1njo9FEhiXC4i5gGKw8vrDR3FpM",
            "https://drive.google.com/uc?export=view&id=1kP0GPQqy48_6Lx0KZPZkRVMzfsMxXtXJ", #72
            "https://drive.google.com/uc?export=view&id=1keJrC4cQw6HGl8MKhog04e_Goc0NdFv4", #74
            "https://drive.google.com/uc?export=view&id=1ki-CgbhrS6naCUhMB2Klk5F7ESEDPqTY", #75
            "https://drive.google.com/uc?export=view&id=1k0mHylrGYhdtr1kLixJRl13Tx6VVuULC", #76
            "https://drive.google.com/uc?export=view&id=1kc_t438Gz5SyzTLECBq8wN9XljBw3T7i", #77
            "https://drive.google.com/uc?export=view&id=1k6916iEK7N_b5OVq2HKAXq3BPL1yDC-z", #78
            "https://drive.google.com/uc?export=view&id=1k6MqnXb0WmpY3OoTWliklc_cgFdoGpJ6", #79
            "https://drive.google.com/uc?export=view&id=1jwSoG-C93ikkvyH4j5GmopTUAYdkMRfW", #80
            "https://drive.google.com/uc?export=view&id=1k7s5BpqVi7pDvoz3mPY8bJegkjWHxux0", #81
            "https://drive.google.com/uc?export=view&id=1kanrsBPhT62OLIstUpJwjRFS76axNvBK", #82
            "https://drive.google.com/uc?export=view&id=1kiFC-LTGwH66RRSQMhBJG9ZIUDHGf8sJ", #83
            "https://drive.google.com/uc?export=view&id=1kkY_L2MwyFVhC2TNsb3eRHQadA7NLK_O", #84
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
                "kesan": "Abang ini asik, tegas, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #66
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450031",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "TVRI",
                "hobi": "Jalan-jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "Kakak ini asik, baik, pemikirannya luas, dan publik speakingnya bagus",  
                "pesan":"Semangat terus kak kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #67
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Way Kandis",
                "hobi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakak ini asik, baik, dan ramah",  
                "pesan": "Semangat terus kak kuliahnya, semoga semua nilai matkulnya diatas B" #68
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam",
                "alamat": "Belwis",
                "hobi": "Main Game",
                "sosmed": "@",
                "kesan": "Abang ini asik, baik, dan sepertinya seru diajak diskusi",  
                "pesan": "Semangat terus bang kuliahnya" #69
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
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
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Kirim BC-an",
                "sosmed": "@esteriars",
                "kesan": "Kakak ini asik, baik, ramah, dan murah senyum",  
                "pesan": "Semangat terus kak kuliahnya" #71
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450",
                "umur": "20",
                "asal": "Saburai",
                "alamat": "Belwis",
                "hobi": "Olahraga",
                "sosmed": "Tidur",
                "kesan": "Kakak ini asik, baik, ramah, dan murah senyum",  
                "pesan": "Semangat terus kakak kuliahnya" #72
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobi": "Jadi Humas",
                "sosmed": "@natee__15",
                "kesan": "Kakak ini asik, baik, ramah, dan murah senyum",  
                "pesan": "Semangat terus Kakak kuliahnya" #73
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobi": "Berkebun",
                "sosmed": "@tobiassiagian",
                "kesan": "bang tobias orangnya baik, santai tapi tegas",  
                "pesan": "Semoga bang tobias selalu sukses di luar dan di dalam himpunan" #75
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Main Bowling",
                "sosmed": "@yo_anamnk",
                "kesan": "kak yohana orangnya tegas",  
                "pesan": "Semoga kak yohana selalu sukses di luar dan di dalam himpunan" #76
            },
            {
                "nama": "Rizky Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "bang rizky orangnya baik",  
                "pesan": "Semoga bang rizky selalu sukses di luar dan di dalam himpunan" #79
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "bang arifi orangnya asik",
                "pesan": "Semoga bang arifi selalu sukses di luar dan di dalam himpunan"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara enim",
                "alamat": "Korpri",
                "hobi": "Nyuci baju",
                "sosmed": "@-",
                "kesan": "kak asa orangnya super duper ramah dan baikk",  
                "pesan": "Semoga kak asa selalu sukses di luar dan di dalam himpunan" #80
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan": "kak chalifia orangnya ramah",  
                "pesan": "Semoga kak chalifia selalu sukses di luar dan di dalam himpunan" #81
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobi": " ",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abang irvan orangnya baik",  
                "pesan": "Semoga bang irvan selalu sukses di luar dan di dalam himpunan" #82
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan": "kak izza orangnya ekstrovert banget dan seruu",  
                "pesan": "Semoga kak izza selalu sukses di luar dan di dalam himpunan" #83
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "daplok kelompok 1",
                "sosmed": "@alyaavanefi",
                "kesan": "Kak Alyaa itu baikk, murah senyum, the best daplok",  
                "pesan": "Semoga kak alyaa selalu sukses di luar dan di dalam himpunan" #84
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nIM": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Nemenin Tobias lari",
                "sosmed": "@rayths_",
                "kesan": "Bang Raid orangnya lucu, keren, dan ramah",
                "pesan": "Semoga bang raid selalu sukses di luar dan di dalam himpunan" #85
            },
            {     
                "nama": "Tria Yunanni",
                "nim": "122450127",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Way Dadi",
                "hobi": "Olahraga",
                "sosmed": "@triayunanni",
                "kesan": "Kak Tria itu baik dan ramah",
                "pesan": "Semoga kak tria selalu sukses di luar dan di dalam himpunan" #86
            },
         ]
        display_images_with_data(gambar_urls, data_list)
    departemeneksternal()

elif menu == "Departemen Internal":
    def departemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lmBVUiyPKb_D-jGTY9kTEhhwcO7SMQAx",
            "https://drive.google.com/uc?export=view&id=1mVotpn2OhP3rXRhsE68w7VIivkGUMg2l",
            "https://drive.google.com/uc?export=view&id=1m11u7MGMUzjrr9Qg0nFhZDRT5k19MHjC",
            "https://drive.google.com/uc?export=view&id=1lzaw-b8eYnRNnpwv8mQ6GoIoZCzTa73q",
            "https://drive.google.com/uc?export=view&id=1lmvQY79ciwDk9vmGgvgfelrdjr8K5VJS",
            "https://drive.google.com/uc?export=view&id=1m1yOkgOXRvw-LwJ4JVCrvjz44RWX2uN_",
            "https://drive.google.com/uc?export=view&id=1mVcfk8zJAME-dpKJyNwT9n65ssFHl7G4",
            "https://drive.google.com/uc?export=view&id=1mSZe7tmGjKKjMCogRHnUWg-ZybieQPf4",
            "https://drive.google.com/uc?export=view&id=1lo-d0C5CkgEzYC4_52vGrqN8BvVnU_Lw",
            "https://drive.google.com/uc?export=view&id=1m3tpyBTBQbvWq-HXfEQ8OtagwKW5xz01",
            "https://drive.google.com/uc?export=view&id=1mEr_1HVyWrmbGxlieNOzhAq3U8uJHl4q",
            "https://drive.google.com/uc?export=view&id=1mLuQaeBhDAABmO6oxSIe6opT5lgryMOF",
        ]
        data_list = [
            {
                "nama"     : "Dimas Rizky Ramadhani",
                "nim"      : "121450027",
                "umur"     : "20",
                "asal"     : "Pamulang, Tangerang Selatan",
                "alamat"   : "Way Kandis Kobam",
                "hobbi"    : "Manjat tower sutet",
                "sosmed"   : "@dimzrky",
                "kesan"    : "Abang ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Catherine Firdhasari Maulina Sinaga",
                "nim"      : "121450071",
                "umur"     : "20",
                "asal"     : "Sumatera Utara",
                "alamat"   : "Airan",
                "hobbi"    : "Baca novel",
                "sosmed"   : "@Catherine.sinaga",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "M.Akbar Resdika",
                "nim"      : "121450066",
                "umur"     : "20",
                "asal"     : "Lampung Barat",
                "alamat"   : "Labuhan Dalam",
                "hobbi"    : "Memelihara Dino",
                "sosmed"   : "@akbar_resdika",
                "kesan"    : "Abang ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Renita Siahaan",
                "nim"      : "122450112",
                "umur"     : "21",
                "asal"     : "Sumatera Utara",
                "alamat"   : "Gerbang Barat",
                "hobi"     : "Mancing",
                "sosmed"   : "@renta.shn",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Salwa Farhanatussaidah",
                "nim"      : "122450055",
                "umur"     : "20",
                "asal"     : "Pesawaran",
                "alamat"   : "Airan raya",
                "hobbi"    : "Ngeliat cogan",
                "sosmed"   : "@slwfn_694",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Rendra Eka Prayoga",
                "nim"      : "122450112",
                "umur"     : "21",
                "asal"     : "Bekasi",
                "alamat"   : "Jl. Lapas Raya",
                "hobbi"    : "Nulis lagu",
                "sosmed"   : "@rendaepr",
                "kesan"    : "Abang ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Yosia Letare Banurea",
                "nim"      : "121450149",
                "umur"     : "20",
                "asal"     : "Dairi, Sumatera Utara",
                "alamat"   : "Perum Griya Indah",
                "hobbi"    : "Bawa motor pake kaki",
                "sosmed"   : "@yosiabanurea",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Ari Sigit",
                "nim"      : "121450069",
                "umur"     : "23",
                "asal"     : "Lampung Barat",
                "alamat"   : "Labuhan Ratut",
                "hobbi"    : "Futsal",
                "sosmed"   : "@ari_sigit17",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Rani Puspita sari",
                "nim"      : "122450030",
                "umur"     : "21",
                "asal"     : "Metro",
                "alamat"   : "Labuhan Ratu",
                "hobbi"    : "Mengaji",
                "sosmed"   : "@rannipu",
                "kesan"    : "kak rani orangnya tegas",  
                "pesan"    : "Semoga kak rani semakin sukses baik di dalam maupun luar himpunan"
            },
            {
                "nama"     : "Azizah Kusumah Putri",
                "nim"      : "122450068",
                "umur"     : "21",
                "asal"     : "Lampung Selatan",
                "alamat"   : "Jati Mulyo",
                "hobbi"    : "Bangun Pagi",
                "sosmed"   : "@azizahksmh15",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Meira Listyaningrum",
                "nim"      : "122450011",
                "umur"     : "20",
                "asal"     : "Pesawaran",
                "alamat"   : "Airan Raya",
                "hobbi"    : "Menghalu",
                "sosmed"   : "@meiraln",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Rendi Alexander Hutagalung",
                "nim"      : "122450057",
                "umur"     : "20",
                "asal"     : "Tangerang",
                "alamat"   : "Kost Gunawan",
                "hobbi"    : "menyanyi",
                "sosmed"   : "@alexanderr",
                "kesan"    : "Abang ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya bang!",
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    departemenInternal()

elif menu == "Departemen SSD":
    def departemenssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lbKJNhAJ89fYEXXAS3Z_UV0d-lMCzwoV", 
            "https://drive.google.com/uc?export=view&id=1lM5hiyYRfWL36tq1zh3i6ISPYAhtptwT", 
            "https://drive.google.com/uc?export=view&id=1lSJB1k3YV4JYp-1UJkkrNihm4xcPaheW", 
            "https://drive.google.com/uc?export=view&id=1krnTELzBG20AmRIoVycnCTSzst0aEV3c", 
            "https://drive.google.com/uc?export=view&id=1l060QZO07tctiWE6xIA-0YAuF7yjNxVM", 
            "https://drive.google.com/uc?export=view&id=1lJGu4d7mIRJ_xzvLplYwSnnfutdwKWyf", 
            "https://drive.google.com/uc?export=view&id=1lOpC5_n3xJFKomtThgWojAvvtlHiHWHa", 
            "https://drive.google.com/uc?export=view&id=1lW26EsEKrK03gCB8DKgF9STTWBQWCwp9", 
            "https://drive.google.com/uc?export=view&id=1lW1Seqe2f4k_K8bzz2IbhVpAS_lcnNHG", 
            "https://drive.google.com/uc?export=view&id=1l1cj3yyYg6uVQkUL4uBFi5ergdBhCisb", 
            "https://drive.google.com/uc?export=view&id=1lMMK4CI27EgHY0AVs3UHuu1J4gcdYMcd", 

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
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal":"Simalungun, Sumut",
                "alamat": "Airan",
                "hobbi": "Hitung uang",
                "sosmed": "@zhjung_",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Bukittinggi",
                "alamat": "Airan",
                "hobbi": "Badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Nyuruh-nyuruh",
                "sosmed": "@dananghk_",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Lapas",
                "hobbi": "Apa aja",
                "sosmed": "@farrel_julio",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Simalungun, Sumut",
                "alamat": "Pemda",
                "hobbi": "Suka nulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal":"Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "Nonton windah",
                "sosmed": "@alviagnting",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
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
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Badminton",
                "sosmed": "@meylanielia",
                "kesan": "Kakak nya asik dan banyak cerita pengalamannya",  
                "pesan": "Semangat terus kuliahnya kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenssd()

elif menu == "Departemen MEDKRAF":
    def departemenmedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mnlBkJoiqp5XVBOUm9iR1DusvjbnltEZ", 
            "https://drive.google.com/uc?export=view&id=1n0Use5qiJ_bT2tgUH0FnT9m9YS71h0ss", 
            "https://drive.google.com/uc?export=view&id=1mon7Gt-5UsyJCNQ2LG3Wy68_QoM5iVrC", 
            "https://drive.google.com/uc?export=view&id=1nyBb_rKDWwLV3dAObP13iJ3Sq8aBc75r", 
            "https://drive.google.com/uc?export=view&id=1oDkQ316bMwn_-s8C-kyXBDef0P7IXjzh", 
            "https://drive.google.com/uc?export=view&id=1n4gIeOLFeEcc_KKCep2uOYFTOEZ3U8zb", 
            "https://drive.google.com/uc?export=view&id=1nNg-uZYmxcHXuM4lBHeNlOBQUaYH62OC", 
            "https://drive.google.com/uc?export=view&id=1mq9Hf5VvDhJ_h--O7v_eCBqaNjN-lYda", 
            "https://drive.google.com/uc?export=view&id=1mcEpza1_yIRn0bqcCxbzbOiefNsh9IL7", 
            "https://drive.google.com/uc?export=view&id=1nDtnjN6nLVi1eoP3EulnBLcCXnN5ucKP", 
            "https://drive.google.com/uc?export=view&id=1mqxLGVc_FH6cDmEIJtcgfC6gkx5Pgc2E", 
            "https://drive.google.com/uc?export=view&id=1nXSMSoyRJLORXnKk0y0Dd-BMTfiwRTwy", 
            "https://drive.google.com/uc?export=view&id=1ngvJTuybYVXrSpqpl0URLTwtHToWxVET", 
            "https://drive.google.com/uc?export=view&id=1o53bPRgkdh3ANmKLsJEO9QQIlO3b_ihG", 
            "https://drive.google.com/uc?export=view&id=1oB48ztCBXzga-WX7IFO7bNee866qKzVA", 
            "https://drive.google.com/uc?export=view&id=1nX0uwN6VHr3_grOrdjVRQ-oFKDv3FlN-", 
            "https://drive.google.com/uc?export=view&id=1o4H7VtGZQbUltjFPFIuvt5eQMuRI9uOx", 
            "https://drive.google.com/uc?export=view&id=1nHkmreLMN-drKpCYeef9FIMVBy2JaBOF", 
            "https://drive.google.com/uc?export=view&id=1nF6Wpcli93sd2cHO0a5Z8kihHDFbBwQU", 
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
                "pesan": "Semangat terus kuliahnya kak!"
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
                "pesan": "Semangat terus kuliahnya kak!"
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
                "pesan": "Semangat terus kuliahnya kak!"
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
                "pesan": "Semangat terus kuliahnya kak!"
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
                "pesan": "Semangat terus kuliahnya kak!"
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
                "pesan": "Semangat terus kuliahnya kak!"
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
                "pesan": "Semangat terus kuliahnya kak!"
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
                "pesan": "Semangat terus kuliahnya kak!"
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
                "pesan": "Semangat terus kuliahnya kak!"
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
                "pesan": "Semangat terus kuliahnya kak!"
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
                "pesan": "Semangat terus kuliahnya kak!"
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
                "pesan": "Semangat terus kuliahnya kak!"
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
                "pesan": "Semangat terus kuliahnya kak!"
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
                "pesan": "Semangat terus kuliahnya kak!"
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
                "pesan": "Semangat terus kuliahnya kak!"
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
                "pesan": "Semangat terus kuliahnya kak!"
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
                "pesan": "Semangat terus kuliahnya kak!"
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
                "pesan": "Semangat terus kuliahnya kak!"
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
                "pesan": "Semangat terus kuliahnya kak!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenmedkraf()
       
             



             
        
        
            
