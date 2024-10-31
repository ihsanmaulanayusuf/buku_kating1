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
            "https://drive.google.com/uc?export=view&id=1pHCPurAGtHLG8hhf8JlAEnxT7i_8oYqY",
            "https://drive.google.com/uc?export=view&id=1pQkb6oMl8MsJlHwcBfSrjPH4Fvw0uABs",
            "https://drive.google.com/uc?export=view&id=1pF0tjkPfpbPcELLrQ4Ef7c6MqDBm8Bgj",
            "https://drive.google.com/uc?export=view&id=1pMMV9oVLXJfaIbk7lYjqXzdN6CgCSJnU",
            "https://drive.google.com/uc?export=view&id=1pFn6DNTJ5Bel9lJuSzL_cbM2s1nR_i9N",
            "https://drive.google.com/uc?export=view&id=1pPBkaqOFBreeI6tTviG9MxwG7jjZ8dTs",

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
                "kesan": "bang kharisma sangat berwibawa dan memiliki wawasan yang luas.",  
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
                "kesan": "Bang Pandra orangnya asik dan tegas.",  
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
            "https://drive.google.com/uc?export=view&id=1pk-ejc5BroWimNrIqzy7vHc32x3AZo4z",
            "https://drive.google.com/uc?export=view&id=1pnQwBdI8d_KBpxDdj36iO5Bf3akZ1zuJ",
            "https://drive.google.com/uc?export=view&id=1q--U4G4GczFrHDe_VuSfSg3c84aSdV_K",
            "https://drive.google.com/uc?export=view&id=1pxO7NgXtSLLhEMlNhpoKKkFsuvJM3gET",
            "https://drive.google.com/uc?export=view&id=1q9VBbGxFfARX0PaBx7beF3bV5ZodrK_G",
            "https://drive.google.com/uc?export=view&id=1q7VB6D2DVZfz2iXA3qXMfp631lwFdw0i",
            "https://drive.google.com/uc?export=view&id=1pge39OdEP_uNU1mUF4aXFdpvEgK5-j88",
            "https://drive.google.com/uc?export=view&id=1q2O_hYNI5pAbA0t8xvmRhyMPsOMJXAxR",
            "https://drive.google.com/uc?export=view&id=1pp_qr_nHz-QXnmZeyqGDOKRy0O5nJmcj",
            "https://drive.google.com/uc?export=view&id=1q6pfhMRjcGUD59unfidgr6FrdcPLN1kf",
            "https://drive.google.com/uc?export=view&id=1q5cyhlZqkME5FjCB8p-87US5LXti-qvU",        
            
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
                "kesan": "kak tri humoris, mudah bergaul, dan perhatian.",  
                "pesan":"semoga kak semakin sukses dalam himpunan maupun di luar himpunan"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450124",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Way Hui",
                "hobbi": " Membaca",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kak cahya trendy banget dan manis.",  
                "pesan":"semoga kak semakin sukses dalam himpunan maupun di luar himpunan"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton Film",
                "sosmed": "@wlsbn0",
                "kesan": "kak wulan baik dan positif vibes.",  
                "pesan":"semoga kak wulan semakin sukses dalam himpunan maupun di luar himpunan"# 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "kak dini baik dan mudah senyum.",  
                "pesan":"semoga kak dini semakin sukses dalam himpunan maupun di luar himpunan."# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bernung, Pesawaran",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@ansftynn_",
                "kesan": "kak fitri baik dan ramah bangett",  
                "pesan":"semoga kak fitri semakin sukses dalam himpunan maupun di luar himpunan"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Belwis",
                "hobbi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "bang feryadi mudah senyum dan baik",  
                "pesan":"semoga bang feryadi semakin sukses dalam himpunan maupun di luar himpunan"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Baca Al-qur'an",
                "sosmed": "@fleurnsh",
                "kesan": "Kak renisha asikk dan pembawaannya alim ",  
                "pesan":"semoga kak renisha semakin sukses dalam himpunan maupun di luar himpunan"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Ogan Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari Sinyal di Gedung F",
                "sosmed": "@_.dheamelia",
                "kesan": "kak dhea kece dan asik.",  
                "pesan":"semoga kak dhea  semakin sukses dalam himpunan maupun di luar himpunan"# 1
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "bang Fahrul asik dan mudah bergaul.",  
                "pesan":"semoga bang fahrul semakin sukses dalam himpunan maupun di luar himpunan!"# 1
            },
            {
                "nama": "Berliana enda putri",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "kakak berliana baik dan keren",  
                "pesan":"semoga kak Berliana semakin sukses dalam himpunan maupun di luar himpunan"# 1
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Billabong, Gedong Air",
                "hobbi": "Suka Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "bang jeremy baik dan humoris.",  
                "pesan":"semoga bang jeremy semakin sukses dalam himpunan maupun di luar himpunan"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18nzsh3oRtT970-n4rFcpiB5mzFcdwJEG", #1
            "https://drive.google.com/uc?export=view&id=18_vPbYy-748Rmxg9ZHJV2jhVqWqfLEyr", #2
        ]
        data_list = [
            {
                "nama": "Annisa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal": "Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi": "Dengerin bang Bintang nyanyi",
                "sosmed": "@annisalutfi_",
                "kesan": "Kak luthfi orangnya baik , ceria dan public speakingnya bagus bangeet",
                "pesan": "Semoga Kak luthfi semakin sukses baik didalam maupun luar himpunan" #1
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kotabaru",
                "hobbi": "Menyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "bang bintang orang yang sangat aktif dan disiplin",
                "pesan": "Semoga bang bintang semakin sukses di dalam maupun luar himpunan" #2
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen PSDA":
    def departemenpsda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YUj1rA1R7eR5HuLwEeBlO8rq1f8IYlC0", #1
            "https://drive.google.com/uc?export=view&id=1ZEmkMLtffVrIXwJPEvgcQacmxlx9PLsA", #2
            "https://drive.google.com/uc?export=view&id=1YHwXs_aCaXdrAZTiiJdFfpoGjU4fElPm", #3
            "https://drive.google.com/uc?export=view&id=1ZAMZw3n5FMl7Fm8lD0n55lE3uKA1E-EA", #4
            "https://drive.google.com/uc?export=view&id=1YppUQUdQCSTGVdiXAgHnt2HR7Knd6wf4", #5
            "https://drive.google.com/uc?export=view&id=1YOZPBx5QQFUGj_zFaBlP_UHLwl4BA01C", #6
            "https://drive.google.com/uc?export=view&id=1YPn8zJFRcp9PfTQ_Zkl8qme_YTLSG_hh", #7
            "https://drive.google.com/uc?export=view&id=1YIYeQuZ6RPJuVR2_mlgg8dSbzL6fl-5P", #8
            "https://drive.google.com/uc?export=view&id=1YTjz2bNXWmwoClQS4vyJuQgOdeuYuNqh", #9
            "https://drive.google.com/uc?export=view&id=1XzSUlEDikqjsIDRWAtOfygAl6gPeMpG2", #10
            "https://drive.google.com/uc?export=view&id=1Y2yj3_Ap8G95MeiEYkCwA1clq3mZXMdv", #11
            "https://drive.google.com/uc?export=view&id=1ZENVxN3AXdz57OTS0Xs9hSThsvJ2zGSa", #12
            "https://drive.google.com/uc?export=view&id=1Z8i1FDXg9ot6Xi8t2SpQyaAYSnhjaDRp" ,#13
            "https://drive.google.com/uc?export=view&id=1Yk556WBA1XNXxMDBtG0NkWDirMYrymG8" , #14
            "https://drive.google.com/uc?export=view&id=1YbOTchA4MqemvlugWfnjTL5QIQuINqOz", #15
            "https://drive.google.com/uc?export=view&id=1YcRL6SS06Rh6c00UP-kOVWeO5dkia7s5", #16
            "https://drive.google.com/uc?export=view&id=1Y_JbJqFNfu4K6pT_QTdchsAjuK7Pw9jw", #17
            "https://drive.google.com/uc?export=view&id=1YkXeFZz3l_nQrK2IpQ6R8UWglDFwynr8", #18
            "https://drive.google.com/uc?export=view&id=1Z4xI2Bn4C3kppnRzRF7cFStyOUcO6hMB", #19
            "https://drive.google.com/uc?export=view&id=1YsfJXTvkEyQ-IeVeRYq-wUh7x6dOymmN" , #20
            "https://drive.google.com/uc?export=view&id=1YySgWmaeu7bwY-Rg30Gz2JLdsRaVRn19", #21
            
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
                "kesan": "bang ericson orangnya baikk",
                "pesan": "semoga bang ericson semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "kak sabeth orangnya tegas",
                "pesan": "semoga kak sabeth semakin sukses didalam maupun diluar himpunan)",
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal": "Riau",
                "alamat": "Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "bang deyvan orangnya seru",
                "pesan": "semoga bang deyvan semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450033",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Sukarame",
                "hobbi": "Muter - Muter",
                "sosmed": "@afifahhnsrn",
                "kesan": "kak fifah orangnya baik dan cantik",
                "pesan": "semoga kak fifah semakin sukses didalam maupun diluar himpunan)",
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "bang ateng orangnya santai dan seru",
                "pesan": "semoga bang ateng semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "Jl. Lapas",
                "hobbi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "bang Johannes orangnya tegas ",
                "pesan": "semoga bang Johannes semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo",
                "hobbi": "Main Game",
                "sosmed": "@kemasverii",
                "kesan": "bang kemas orangnya baik dan humoris",
                "pesan": "semoga bang kemas semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin Lomba Sihir",
                "sosmed": "@presiliamg",
                "kesan": "kak presilia orangnya baik dan ramah",
                "pesan": "semoga kak presilia semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "kak rafa orangnya pendiam dan pembawaannya alim",
                "pesan": "semoga kak rafa semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobbi": "Nonton Jagad review",
                "sosmed": "@sahid_maulana",
                "kesan": "bang sahid orangnya baik",
                "pesan": "semoga bang sahid semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Belajar",
                "sosmed": "@roselivnes__",
                "kesan": "kak vanessa orangnya kece dan namanya cantik banget",
                "pesan": "semoga kak vanessa semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobbi": "Nongs",
                "sosmed": "@allyaislami_",
                "kesan": "kak alya orangnya tegas bangett",
                "pesan": "semoga kak alya semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Natar",
                "hobbi": "Nyari sinyal di gedung F",
                "sosmed": "@eksantyfebriana",
                "kesan": "kak eksanty orangnya tegas dan suka buat lucu lucuan",
                "pesan": "semoga kak eksanty semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": " Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Bengong",
                "sosmed": "@farahanumafifahh",
                "kesan": "kak hanum orangnya baik",
                "pesan": "semoga kak hanum semakin sukses didalam maupun diluar himpunan)",
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Jalan Pangeran Senopati Raya 18",
                "hobbi": "Baca Kitab Suci",
                "sosmed": "@ferdy_kevin",
                "kesan": "bang ferdy orangnya baik",
                "pesan": "semoga bang ferdy semakin sukses didalam maupun diluar himpunan)",
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450051",
                "umur": "19",
                "asal": "Kayu Agung",
                "alamat": "Kedaton",
                "hobbi": "Nongki - nongki",
                "sosmed": "@dransyah_",
                "kesan": "bang deri murah senyum",
                "pesan": "semoga bang deri semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Oktavia Nurwendah Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@oktavianrwnda",
                "kesan": "kak okta orangnya baik",
                "pesan": "semoga kak okta semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "bang moana orangnya bik dan seruu",
                "pesan": "semoga bang moana semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "kak jaclin cantik dan super baik",
                "pesan": "semoga kak jaclin semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "bang rafly orangnya seru",
                "pesan": "semoga bang rafly semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i_",
                "kesan": "kak dini orangnya baik ",
                "pesan": "semoga kak dini semakin sukses didalam maupun diluar himpunan",
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenpsda()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen MIKFES":
    def departemenmikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_nXi6BLo_F-PDUWNl6WaFzmJcONSEeAg", #1
            "https://drive.google.com/uc?export=view&id=1_oDM_DIDsW4osl783LtfMvZc0aNzgTEl", #2
            "https://drive.google.com/uc?export=view&id=1_RUbegWS-6E82FtNbMZPVcu9fNYz-SDA", #3
            "https://drive.google.com/uc?export=view&id=1_MPrJrodvQr3BOXGkf-lrufTwZLHae2q", #4
            "https://drive.google.com/uc?export=view&id=1_CSi-vrp7TnIR0-2ICwAsdIRsNRC7X8g", #5
            "https://drive.google.com/uc?export=view&id=1_i5dPKfljdAfx76A1ES5j1fpYfB0sZ3g", #6
            "https://drive.google.com/uc?export=view&id=1_ppt2dX6Ig7adPduH6usX4OhconXEs-o", #7
            "https://drive.google.com/uc?export=view&id=1_n3s4EI1eDuuBJH5470-kXwMQ3sr1bdu", #8
            "https://drive.google.com/uc?export=view&id=1_VIsuuFA9NvZNf9AgmfLlXZ7fzENggXJ", #9
            "https://drive.google.com/uc?export=view&id=1_b76Q9revbSnipwpuaQf8jdAwq_10nDP", #10
            "https://drive.google.com/uc?export=view&id=_QOMZnEl-CKwGel5HSKhtc357onaOPAV", #11
            "https://drive.google.com/uc?export=view&id=1_Pfy_4qXxnuRpEjJ0MwT9WckK_XfWA", #12
            "https://drive.google.com/uc?export=view&id=1aL3DZMQo3Ef9B_b6Oau0PAWVUbsW6n6b", #13
            "https://drive.google.com/uc?export=view&id=1_Rfo6qAK4QQ4wnhdLxrqKvMFdc_EJo9a", #14
            "https://drive.google.com/uc?export=view&id=1_GtAtjHLcDWEJqtTj1YsHRJF8wSupg3S", #15
            "https://drive.google.com/uc?export=view&id=1a-5JTSaOj2up2JcHXLLmHhw2N4tTF7r8", #16
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
                "kesan": "bang rafi orangnya baik",
                "pesan": "semoga bang rafi semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "kak anissa orangnya baik",
                "pesan": "semoga kak anissa semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "bang sahit orangnya baik dan ramah ",
                "pesan": "semoga bang sahid semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "bang regi orangnya seru",
                "pesan": "semoga bang regi semakin sukses didalam maupun diluar himpunan*",
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "kak syalaisha orangnya ramah",
                "pesan": "semoga kak syalaisha semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "bang anwar orangnya baik",
                "pesan": "semoga bang anwar semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "kak deva orangnya baik",
                "pesan": "semoga kak deva semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "",
                "sosmed": "@dindanababan_",
                "kesan": "kak dinda orangnya ramah",
                "pesan": "semoga kak dinda semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "kak marleta orangnya baik bangett",
                "pesan": "semoga kak marleta semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "kak junita orangnya ramah",
                "pesan": "semoga kak junita semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "kak puspa orangnya ramah",
                "pesan": "semoga kak puspa semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": "121450128",
                "umur": "23",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "bang Rahman orangnya baik dan asik",
                "pesan": "semoga bang Rahman semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "bang adit orangnya baik",
                "pesan": "semoga bang adit semakin sukses didalam maupun diluar himpunan",
                "jabatan": "Staff Divisi Survei dan Riset"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "bang eggi orangnya baik dan ramah",
                "pesan": "semoga bang eggi semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "kak febiya orangnya ramah",
                "pesan": "semoga kak febiya semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "bang syahrul orangnya asik",
                "pesan": "semoga bang syahrul semakin sukses didalam maupun diluar himpunan",
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Jl Nangka 3",
                "hobbi": "Berolahraga",
                "sosmed": "@randardn",
                "kesan": "bang randa orangnya baik",
                "pesan": "semoga bang randa semakin sukses didalam maupun diluar himpunan",
            }
        ]

        display_images_with_data(gambar_urls, data_list)
    departemenmikfes()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen Eksternal":
    def departemeneksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kBeaDPyYw0hKKRsEyVkF9VrwDZP2pekB", #1
            "https://drive.google.com/uc?export=view&id=1kO9vC-CUy_wmyzAH22FUi1VD9wwU1yhn", #2
            "https://drive.google.com/uc?export=view&id=1or7T6Yzu4TqpdnWLASzrkSiL84eWecyY", #3
            "https://drive.google.com/uc?export=view&id=1kgcdRD2hWxpWEfIq0Og6Cbvr0zOmJdkH", #4
            "https://drive.google.com/uc?export=view&id=1kUk9fvP3EX4Q4PxSfdpj1XemtSEF8aDy", #5
            "https://drive.google.com/uc?export=view&id=1p1bpgh3ROKQ7bwFKgt_FF69FOyH7lHmg", #6
            "https://drive.google.com/uc?export=view&id=1kP0GPQqy48_6Lx0KZPZkRVMzfsMxXtXJ", #7
            "https://drive.google.com/uc?export=view&id=1kOMbN1njo9FEhiXC4i5gGKw8vrDR3FpM", #8
            "https://drive.google.com/uc?export=view&id=1keJrC4cQw6HGl8MKhog04e_Goc0NdFv4", #9
            "https://drive.google.com/uc?export=view&id=1ki-CgbhrS6naCUhMB2Klk5F7ESEDPqTY", #10
            "https://drive.google.com/uc?export=view&id=1k0mHylrGYhdtr1kLixJRl13Tx6VVuULC", #11
            "https://drive.google.com/uc?export=view&id=1kc_t438Gz5SyzTLECBq8wN9XljBw3T7i", #12
            "https://drive.google.com/uc?export=view&id=1k6916iEK7N_b5OVq2HKAXq3BPL1yDC-z", #13
            "https://drive.google.com/uc?export=view&id=1k6MqnXb0WmpY3OoTWliklc_cgFdoGpJ6", #14
            "https://drive.google.com/uc?export=view&id=1jwSoG-C93ikkvyH4j5GmopTUAYdkMRfW", #15
            "https://drive.google.com/uc?export=view&id=1k7s5BpqVi7pDvoz3mPY8bJegkjWHxux0", #16
            "https://drive.google.com/uc?export=view&id=1kanrsBPhT62OLIstUpJwjRFS76axNvBK", #17
            "https://drive.google.com/uc?export=view&id=1kiFC-LTGwH66RRSQMhBJG9ZIUDHGf8sJ", #18
            "https://drive.google.com/uc?export=view&id=1kkY_L2MwyFVhC2TNsb3eRHQadA7NLK_O", #19
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21",
                "asal": "Tangerang",
                "alamat sekarang": "Jatimulyo",
                "hobbi": "BAB setiap jam 7 pagi",
                "sosial media": "@yogyst",
                "kesan": "bang yogy orangnya humoris",
                "pesan": "semoga bang yogy semakin sukses didalam maupun diluar himpunan",
            
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat sekarang": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosial media": "@ramadhitaatifa",
                "kesan": "kak dhita orangnya berwawasan luas",
                "pesan": "semoga kak dhita semakin sukses didalam maupun diluar himpunan",
                
            },
            {
                "nama": "Nazwa Nabila",
                "nim": "121450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat sekarang": "Kochpri",
                "hobbi": "Main Golf",
                "sosial media": "@nazwanbilla",
                "kesan": "kak nazwa orangnya ramah",
                "pesan": "semoga kak nazwa semakin sukses didalam maupun diluar himpunan",
               
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam, Kep. Riau",
                "alamat sekarang": "Belwis",
                "hobbi": "Menggambar",
                "sosial media": "@bastiansilaban_",
                "kesan": "bang bastian orangnya baik",
                "pesan": "semoga bang bastian semakin sukses didalam maupun diluar himpunan",
                
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat sekarang": "Korpri",
                "hobbi": "Berkebun",
                "sosial media": "@deaa.rsn",
                "kesan": "kak dea orangnya ramah",
                "pesan": "semoga kak dea semakin sukses didalam maupun diluar himpunan",
               "
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat sekarang": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosial media": "@esteriars",
                "kesan": "kak ester orangnya baik dan ramah",
                "pesan": "semoga kak ester semakin sukses didalam maupun diluar himpunan",
               
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat sekarang": "Belwais",
                "hobbi": "Surfing",
                "sosial media": "@nateee__15",
                "kesan": "kak natasya orangnya baik",
                "pesan": "semoga kak natasya semakin sukses didalam maupun diluar himpunan",
                
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat sekarang": "Belwis",
                "hobbi": "Tidur",
                "sosial media": "@nvliaadinda",
                "kesan": "kak lia orangnya ramah dan baik",
                "pesan": "semoga kak lia semakin sukses didalam maupun diluar himpunan",
                
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat sekarang": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosial media": "@jasminednva",
                "kesan": "kak ratu orangnya baik",
                "pesan": "semoga kak ratu semakin sukses didalam maupun diluar himpunan",
               
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat sekarang": "Pemda",
                "hobbi": "Jogging",
                "sosial media": "@tobiassiagian",
                "kesan": "bang tobias orangnya baik dan ramah",
                "pesan": "semoga bang tobias semakin sukses didalam maupun diluar himpunan",
               
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat sekarang": "Belwais",
                "hobbi": "Main Bowling",
                "sosial media": "@yo_annamnk",
                "kesan": "kak yohana orangnya tegas",
                "pesan": "semoga kak yohana semakin sukses didalam maupun diluar himpunan",
               
            },
            {
                "nama": "Rizky Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat sekarang": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosial media": "@rzkdrnnn",
                "kesan": "bang riky orangnya baik",
                "pesan": "semoga bang rizky semakin sukses didalam maupun diluar himpunan",
                
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat sekarang": "Way Huwi",
                "hobbi": "Bertani",
                "sosial media": "@rafiramadhanmaulana",
                "kesan": "bang arafi orangnya ramah",
                "pesan": "semoga bang arafi semakin sukses didalam maupun diluar himpunan",
               
            },
            {
                "nama": "Asa Do’a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat sekarang": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosial media": "@u_yippy",
                "kesan": "kak asa orangnya super duper baikk dan ramah juga",
                "pesan": "semoga kak asa semakin sukses didalam maupun diluar himpunan",
                
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat sekarang": "Sukarame",
                "hobbi": "Q Time",
                "sosial media": "@chlfawww",
                "kesan": "kak chalifia orangnya asik",
                "pesan": "semoga kak chalifia semakin sukses didalam maupun diluar himpunan",
                
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat sekarang": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosial media": "@alfaritziirvan",
                "kesan": "bang irvan orangnya ramah dan baik benget",
                "pesan": "semoga bang irvan semakin sukses didalam maupun diluar himpunan",
               
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat sekarang": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosial media": "@izzalutfia",
                "kesan": "kak izza orangnya ekstrovert banget dan asik",
                "pesan": "semoga kak izza semakin sukses didalam maupun diluar himpunan",
                
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat sekarang": "Rajabasa",
                "hobbi": "Mengaji",
                "sosial media": "@alyaavanevi",
                "kesan": "kak alyaa cantik, baik ,the best daplok",
                "pesan": "semoga kak alyaa semakin sukses didalam maupun diluar himpunan",
                
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat sekarang": "Sukarame",
                "hobbi": "Nemenin Tobias lari",
                "sosial media": "@rayths_",
                "kesan": "bang raid orangnya baik",
                "pesan": "semoga bang raid semakin sukses didalam maupun diluar himpunan",
               
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450127",
                "umur": "20",
                "asal": "Palembang",
                "alamat sekarang": "Way Dadi",
                "hobbi": "Olahraga",
                "sosial media": "@triayunanni",
                "kesan": "kak tria orangnya ramah",
                "pesan": "semoga kak tria semakin sukses didalam maupun diluar himpunan",
            }
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



