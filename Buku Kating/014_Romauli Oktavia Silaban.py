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
            "https://drive.google.com/uc?export=view&id=1pF0tjkPfpbPcELLrQ4Ef7c6MqDBm8Bgj",
            "https://drive.google.com/uc?export=view&id=1pMMV9oVLXJfaIbk7lYjqXzdN6CgCSJnU",
            "https://drive.google.com/uc?export=view&id=1pFn6DNTJ5Bel9lJuSzL_cbM2s1nR_i9N",#4
            "https://drive.google.com/uc?export=view&id=1pPBkaqOFBreeI6tTviG9MxwG7jjZ8dTs", #5
            
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar,Way Kandis",
                "hobi": "Dengerin Musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "bang kharisma sangat berwibawa dan memiliki wawasan yang luas",  
                "pesan":"semoga bang kharisma semakin sukses dalam himpunan maupun di luar himpunan"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Bukit Kemuning, Lampung Utara",
                "alamat": "Jl.Terusan Pulau Bawean 2 , Sukarame",
                "hobi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Bang Pandra orangnya asik dan tegas",  
                "pesan":"tutor gitarnya dong bang, semangat kuliahnya bang pandra"# 2
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam , Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobi": " Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "kak meliza orangnya baik dan asik",  
                "pesan":"semoga kak meliza punya jodoh spek aktor koreah"# 3
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
                "pesan":"semangat kuliahnya kak titi"# 4
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh , Sumatrea Barat",
                "alamat": "Nangka 4",
                "hobi": "Dengerin bang Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kak putri pembawaannya baik , ramah, dan mudah senyum",  
                "pesan":"happy smile terus ya kak putri"# 5
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
                "pesan":"sukses terus ya kak nadilla"# 6
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
            "https://drive.google.com/uc?export=view&id=1q9VBbGxFfARX0PaBx7beF3bV5ZodrK_G",
            "https://drive.google.com/uc?export=view&id=1pxO7NgXtSLLhEMlNhpoKKkFsuvJM3gET",
            "https://drive.google.com/uc?export=view&id=1pp_qr_nHz-QXnmZeyqGDOKRy0O5nJmcj", #15
            "https://drive.google.com/uc?export=view&id=1pge39OdEP_uNU1mUF4aXFdpvEgK5-j88",#11
            "https://drive.google.com/uc?export=view&id=1q7VB6D2DVZfz2iXA3qXMfp631lwFdw0i",
            "https://drive.google.com/uc?export=view&id=1pahloEKWL1Piki8l-ozribwaN8sMxNhB", #12
            "https://drive.google.com/uc?export=view&id=1piufZmfFTdwIZUmHYjgntPAEbb-zf6aU", #14
            "https://drive.google.com/uc?export=view&id=1q2O_hYNI5pAbA0t8xvmRhyMPsOMJXAxR",
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
                "pesan":"happy virus terus kak tri" #7
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "Way Huwi",
                "hobi": "Membaca",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kak cahya trendy banget dan manis",  
                "pesan":"suka banget sama style kak cahya" #8
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
                "pesan":"baik baik kuliahnya kak wulan" #9
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
                "pesan":"semoga kak dini punya pacar spek aktor cina" #10
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
                "pesan": "tahun ini jadi wl lagi dong kak, suara kak clau bagus banget" #13
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
                "pesan":"spill lukisan bang, karyanya jangan lupa dijual bang biar jadi cuan" #17
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal":"Bernung, Pesawaran",
                "alamat": "Bandar Lampung",
                "hobi": "Nonton Drakor",
                "sosmed": " @ansftynn_",
                "kesan": "kak fitri baik dan ramah bangett",  
                "pesan":"keep fighting kak kuliahnya" #11
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
                "pesan":"hobinya jangan berubah ya bang" #12
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
                "pesan":"positive vibes terus ya kak" #14
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
                "pesan":"semangat kuliahnya bang mirzan" #15
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
                "pesan":"semoga ketemu ya kak dhea sinyalnya apalagi di basement" #16
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
                "pesan":"produktif terus kak berliana" #18
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
                "pesan":"jangan bengong bengong bang, konon katanya di itera...." #19
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
                "hobi": "Dengerin bang Bintang nyanyi",
                "sosmed": "@annisalutfi_",
                "kesan": "Kak luthfi orangnya baik , ceria dan public speakingnya bagus bangeet",  
                "pesan":"makasih ya kak luthfi udah dengan keluh kesah kami, semangat kuliahnya kak" #20
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
                "pesan":"jangan lupa istirahat bang, tetap semangat" #21
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
            "https://drive.google.com/uc?export=view&id=1YHwXs_aCaXdrAZTiiJdFfpoGjU4fElPm", #31
            "https://drive.google.com/uc?export=view&id=1ZENVxN3AXdz57OTS0Xs9hSThsvJ2zGSa", #25
            "https://drive.google.com/uc?export=view&id=1YbOTchA4MqemvlugWfnjTL5QIQuINqOz", #26
            "https://drive.google.com/uc?export=view&id=1Z8i1FDXg9ot6Xi8t2SpQyaAYSnhjaDRp", #27
            "https://drive.google.com/uc?export=view&id=1Yk556WBA1XNXxMDBtG0NkWDirMYrymG8", #28
            "https://drive.google.com/uc?export=view&id=1YcRL6SS06Rh6c00UP-kOVWeO5dkia7s5", #29
            "https://drive.google.com/uc?export=view&id=1Y_JbJqFNfu4K6pT_QTdchsAjuK7Pw9jw", #30
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
                "alamat": "Kobam",
                "hobi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "bang ericson orangnya baik dan aktif di setiap kegiatan",  
                "pesan":"jaga kesehatan bang, jangan lupa istirahat" #22
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "kak sabeth orangnya baik dan tegas",  
                "pesan":"semangat kuliahnya kak sabeth" #23
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "1214500148",
                "umur": "21",
                "asal": "Duri, Riau",
                "alamat": "Pulau Damar Kobam",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "bang deyvan orangnya baik dan ramah",  
                "pesan": "semangat belajarnya bang" #31
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Marahin orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "kak fifah orangnya tegas dan manis banget kalau senyum",  
                "pesan":"jangan lupa istirahat kak, keep fighting" #24
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobi": "Main",
                "sosmed": "@allyaislami_",
                "kesan": "kak allya orangnya asik dan tegas",  
                "pesan": "baik baik kuliahnya kak allya, tetap semangat" #25
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiyati",
                "nim": "122450001",
                "umur": "20",
                "asal": "Jawa Barat",
                "alamat": "Metro",
                "hobi": "Nyopet",
                "sosmed": "@eksantyfebriana",
                "kesan": "kak eksanty orangnya tegas tapi kadang suka bercanda",  
                "pesan": "hati hati kak nyopetnya, awas ketahuann" #26
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Bengong",
                "sosmed": "@farahanumafifahh",
                "kesan": "kak hanum orangnya murah senyum dan tegas",  
                "pesan": "kurangi bengongnya ya kak dan semangat terus" #27
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Jalan Pangeran Senopati Raya 18",
                "hobi": "Baca Kitab Suci",
                "sosmed": "@ferdy_kevin",
                "kesan": "bang ferdy orangnya pendiem",  
                "pesan": "jangan berubah ya bang hobinya, selalu baca kitab suci" #28
            },
            {
                "nama":  "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Kayu Agung",
                "alamat": "Jalan Pagar Alam Kedaton",
                "hobi": "Ngukur jalan",
                "sosmed": "@dransyh_",
                "kesan": "bang deri orangnya seru dan suka bercanda",  
                "pesan": "jangan lupa catat ukuran jalannya ya bang" #29
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Travelling",
                "sosmed": "@_ oktavianrwnda _",
                "kesan": "kak okta orangnya tegas",  
                "pesan": "keep strong terus kuliahnya kak okta" #30
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobi": "Membaca",
                "sosmed": "@syalaisha.i_",
                "kesan": "kak dini orangnya baik dan asik",  
                "pesan": "spill novel aksi dong kak, semangat kuliahnya kak" #32
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "Jalan Lapas",
                "hobi": "Asprak",
                "sosmed": "@johanneskrsjnnn",
                "kesan": "bang jo orangnya tegas",  
                "pesan": "Semangat ngaspraknya bang" #34
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Golf Asri",
                "hobi": "Ngetik print hello dunia",
                "sosmed": "@kemasverii",
                "kesan": "bang kemas orangnya berilmu banget dan tentunya baik",  
                "pesan": "jangan lelah ngodingnya bang, semangatt" #35
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobi": "Dengerin The Adams",
                "sosmed": "@presilliamg",
                "kesan": "kak presilia orangnya pendiem",  
                "pesan": "Semangat terus kak kuliahnya" #37
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450122",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "kak rafa orangnya cantik cantik kalem gitu",  
                "pesan": "saya rekomendasikan beauty in a click kak" #38
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Kota Depok, Jawa Barat",
                "alamat": "Jalan Airan Raya",
                "hobi": "Dengerin juicy luicy",
                "sosmed": "@sahid_maul19",
                "kesan": "bang sahid orangnya ramah",  
                "pesan": "semoga bisa jadi anggota juicy luicy ya bang, hehe" #39
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Perum Korpri",
                "hobi": "Minum kopi, belajar, bikin Deyvan senang",
                "sosmed": "@roselivness__",
                "kesan": "kak vanes orangnya baik dan ramah",  
                "pesan": "nama kakaknya cantik banget, jangan sering sering minum kopi ya kak" #40
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Kota Baru",
                "hobi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "bang ateng orangnya santai dan baik",  
                "pesan": "semangat kuliahnya bang ateng" #41
            },
            {
                "nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "bang moena orangnya asik",  
                "pesan": "Semangat terus bang kuliahnya , pinjem komik dong bang" #42
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv",
                "kesan": "kak jaclin orangnya baik banget dan cantikk",  
                "pesan": "tutor berenangnya dong kak, keep fighting kak" #43
            },
            {
                "nama":  "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "bang rafly orangnya asik dan santai",  
                "pesan": "Semangat terus bang kuliahnya" #44
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
                "asal": "Lubuk Linggau, Sumatera Selatan",
                "alamat": "Jl. Nangka 4",
                "hobi": "Olahraga",
                "sosmed": "@rafadhlillahh13",
                "kesan": "pemikiran bang rafi luas banget",  
                "pesan": "semangat olahraganya bang , jangan lupa mewing wkwk" #45
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi,Sukarame",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "kak tika orangnya baik",  
                "pesan": "bagi resep masakan dong kak, semangat kuliahnya kak" #46
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "bang ahmad orangnya baik bangett",  
                "pesan": "Semangat terus bang olahraga dan kuliahnya" #47
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi",
                "hobi": "Ngasprak ADS",
                "sosmed": "@mregiiii_",
                "kesan": "bang regi orangnya asik , vibes penyanyi",  
                "pesan": "semangat ngasprak dan ngodingnya bang" #48
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg. Yudistira",
                "hobi": "Review jurnal Bu Mika",
                "sosmed": "@dkselsd_31",
                "kesan": "kak dina orangnya baik",  
                "pesan": "semangat ngeriviewnya kak" #49
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "bang anwar orangnya ramah",  
                "pesan": "Semangat terus kuliahnya bang" #50
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobi": "Resume Webinar",
                "sosmed": "@anjaniiidev",
                "kesan": "kak deva orangnya asik",  
                "pesan": "jangan lupa bagi bagi resume kak" #51
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobi": "Membaca jurnal Bu Mika",
                "sosmed": "@dindanababan",
                "kesan": "kak dinda orangnya baik banget",  
                "pesan": "Semangat baca jurnalnya kak, spill simpulan jurnalnya dong kak ,hehe" #55
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Gg. Nangka 3",
                "hobi": "Review jurnal Bu Mika",
                "sosmed": "@marletacornelia",
                "kesan": "kak marleta super baik dan happy virus banget",  
                "pesan": "happy virus terus ya kak, semangat kuliahnya" #56
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Kepuluan Riau",
                "alamat": "Gg.Nangka 3",
                "hobi": "menghitung akurasi",
                "sosmed": "@jaclinaclcv",
                "kesan": "kak rut orangnya baik dan asik",  
                "pesan": "jangan sampai salah hitung ya kak ,semangat terus kuliahnya kak" #57
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450074",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobi": "Membangkitkan bilangan",
                "sosmed": "@jaclinaclcv",
                "kesan": "kak puspa orangnya baik",  
                "pesan": "Semangat terus kuliahnya kak, hwaiting !!" #58
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobi": "Ngoding wisata",
                "sosmed": "@rahm.adityaa",
                "kesan": "bang adit orangnya pendiem",  
                "pesan": "semangat ngodingnya bang, semangat terus bang" #60
            },
            {
                "nama": "Eggi satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobi": "Ngoding wisata",
                "sosmed": "@_egistr",
                "kesan": "bang eggi orangnya ramah dan murah senyum",  
                "pesan": "positive vibes terus ya bang, semangat terus" #61
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Tulang bawang",
                "alamat": "Jl.Kelengkeng Raya",
                "hobi": "Review jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "kak febiya orangnya baik",  
                "pesan":"Semangat terus kuliahnya kak" #62
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main game",
                "sosmed": "@sudo.syahrulramadhan",
                "kesan": "bang syahrul orangnya pendiem",  
                "pesan":"tetap semangat kuliahnya bang dan jangan lupa istirahat" #63
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Bang randa orangnya asik , baik, dan pinter matematika",  
                "pesan":"jangan lupa tidur bang, tetap aktif didalam dan luar organisasi" #64
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
                "kesan": "bang yogy orangnya tegas dan produktif",  
                "pesan":"semangat kuliahnya bang yogy jangan lupa istirahat" #66
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450031",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "TVRI",
                "hobi": "Jalan-jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "kak dhita orangnya baik dan senyumnya manis",  
                "pesan":"tetap semangat kak" #67
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Way Kandis",
                "hobi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "kak nazwa orangnya baik",  
                "pesan": "semangat belajarnya kak " #68
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam",
                "alamat": "Belwis",
                "hobi": "Main Game",
                "sosmed": "@bastiansilaban_",
                "kesan": "bang bastian orangnya baik dan mirip sama abang saya",  
                "pesan": "semangat kuliahnya ito, kita semarga bang" #69
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobi": "Dengerin musik",
                "sosmed": "@deaarsn",
                "kesan": "kak dea orangnya murah senyum",  
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
                "kesan": "kak ester orangnya ramah",  
                "pesan": "Semangat kirim bc-annya kak , jangan lupa istirahat" #71
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "20",
                "asal": "Saburai",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "kak novelia definisi cantik kalem",  
                "pesan": "udah tidur belum kak, hari ini? semangat kuliahnya ya kak" #72
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobi": "Jadi Humas",
                "sosmed": "@natee__15",
                "kesan": "kak natasya orangnya humble",  
                "pesan": "Semangat ngurus surat suratnya kak" #73
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
                "pesan": "semangat berkebunnya bang" #75
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
                "pesan": "semangat kuliahnya kak, hwaiting !!" #76
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
                "pesan": "semangat bikin portofolionya bang" #79
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Way Huwi",
                "hobi": "Imam TVRI",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "bang arifi orangnya asik",
                "pesan": "stay positive vibes bang"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara enim",
                "alamat": "Korpri",
                "hobi": "Nyuci baju",
                "sosmed": "@u_yippy",
                "kesan": "kak asa orangnya super duper ramah dan baikk",  
                "pesan": "stay humble dan semangat kuliahnya kak asaa" #80
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
                "pesan": "tetap semangat dan sukses selalu kak" #81
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobi": "nonton youtube , main game",
                "sosmed": "@alfaritziirvan",
                "kesan": "bang irvan orangnya baik",  
                "pesan": "stay healthy dan semangat kuliahnya bang" #82
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
                "pesan": "suka sama kakak yang ekstrovert banget, stay positive vibes terus kak" #83
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "jadi daplok kelompok 1",
                "sosmed": "@alyaavanefi",
                "kesan": "Kak Alyaa itu baikk, murah senyum, the best daplok",  
                "pesan": "jangan jenuh jadi daplok kami kak , we love you kak alyaa" #84
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "telat",
                "sosmed": "@rayths_",
                "kesan": "Bang Raid orangnya lucu dan ramah",
                "pesan": "jangan lupa bangun pagi dan pasang 10 alarm bang" #85
            },
            {     
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way kanan",
                "alamat": "Sukarame",
                "hobi": "membaca chat",
                "sosmed": "@tria_y062",
                "kesan": "Kak Tria itu baik dan ramah",
                "pesan": "suka banget sama senyum kakak,, semangat kuliahnya kak" #86
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
                "asal"     : "Pamulang  , Tangerang Selatan",
                "alamat"   : "Way Kandis , Kobam",
                "hobi"    : "Manjat tower sutet",
                "sosmed"   : "@dimzrky",
                "kesan"    : "bang dimas orangnya humble dan asik",  
                "pesan"    : "hati hati manjat towernya bang, awas jatuh"
            },
            {
                "nama"     : "Catherine Firdhasari Maulina Sinaga",
                "nim"      : "121450071",
                "umur"     : "20",
                "asal"     : "Sumatera Utara",
                "alamat"   : "Airan",
                "hobi"    : "Baca novel",
                "sosmed"   : "@Catherine.sinaga",
                "kesan"    : "kak catherine orangnya ramah",  
                "pesan"    : "Semangat selalu kuliahnya kak, btw rekomendasi novel romance dong kak"
            },
            {
                "nama"     : "M.Akbar Resdika",
                "nim"      : "121450066",
                "umur"     : "20",
                "asal"     : "Lampung Barat",
                "alamat"   : "Labuhan Dalam",
                "hobi"    : "Memelihara Dino",
                "sosmed"   : "@akbar_resdika",
                "kesan"    : "bang akbar orangnya asik",  
                "pesan"    : "awas dinonya lari bang, abangnya mirip abe"
            },
            {
                "nama"     : "Renta Siahaan",
                "nim"      : "122450070",
                "umur"     : "21",
                "asal"     : "Sumatera Utara",
                "alamat"   : "Gerbang Barat",
                "hobi"     : "Mancing",
                "sosmed"   : "@renta.shn",
                "kesan"    : "Kakak ini orangnya baik",  
                "pesan"    : "semoga dapat ikan ya kak , bukan dapat hikmahnya"
            },
            {
                "nama"     : "Salwa Farhanatussaidah",
                "nim"      : "122450055",
                "umur"     : "20",
                "asal"     : "Pesawaran",
                "alamat"   : "Airan raya",
                "hobi"    : "Ngeliat cogan",
                "sosmed"   : "@slwfn_694",
                "kesan"    : "kak salwa orangnya asik",  
                "pesan"    : "semangat kuliahnya kak"
            },
            {
                "nama"     : "Rendra Eka Prayoga",
                "nim"      : "122450112",
                "umur"     : "21",
                "asal"     : "Bekasi",
                "alamat"   : "Jl. Lapas Raya",
                "hobi"    : "Nulis lagu",
                "sosmed"   : "@rendaepr",
                "kesan"    : "bang rendra asik dan aktif banget",  
                "pesan"    : "ditunggu lagunya rilis di spotify bang"
            },
            {
                "nama"     : "Yosia Letare Banurea",
                "nim"      : "121450149",
                "umur"     : "20",
                "asal"     : "Dairi, Sumatera Utara",
                "alamat"   : "Perum Griya Indah",
                "hobi"    : "Nungguin ayam betina berkokok",
                "sosmed"   : "@yosiabanurea",
                "kesan"    : "bang yosia orangnya baik, asik, dan humoris",  
                "pesan"    : "semangat main futsalnya bang, jangan lupa pulkam"
            },
            {
                "nama"     : "Ari Sigit",
                "nim"      : "121450069",
                "umur"     : "23",
                "asal"     : "Lampung Barat",
                "alamat"   : "Labuhan Ratu",
                "hobi"    : "Futsal",
                "sosmed"   : "@ari_sigit17",
                "kesan"    : "bang ari orangnya baik",  
                "pesan"    : "semangat latihan futsalnya bang"
            },
            {
                "nama"     : "Rani Puspita sari",
                "nim"      : "122450030",
                "umur"     : "21",
                "asal"     : "Metro",
                "alamat"   : "Rajabasa",
                "hobi"    : "Mengaji",
                "sosmed"   : "@rannipu",
                "kesan"    : "kak rani orangnya tegas",  
                "pesan"    : "Sjangan lupa ngajinya kak"
            },
            {
                "nama"     : "Azizah Kusumah Putri",
                "nim"      : "122450068",
                "umur"     : "21",
                "asal"     : "Lampung Selatan",
                "alamat"   : "Jati Mulyo",
                "hobi"    : "Bangun Pagi",
                "sosmed"   : "@azizahksmh15",
                "kesan"    : "hak azizah orangnya ramah",  
                "pesan"    : "tetap semangat kuliahnya kak"
            },
            {
                "nama"     : "Meira Listyaningrum",
                "nim"      : "122450011",
                "umur"     : "20",
                "asal"     : "Pesawaran",
                "alamat"   : "Airan Raya",
                "hobi"    : "nonton",
                "sosmed"   : "@meiralsty",
                "kesan"    : "kak meira orangnya asik",  
                "pesan"    : "semangat kuliahnya kak, keep strong"
            },
            {
                "nama"     : "Rendi Alexander Hutagalung",
                "nim"      : "122450057",
                "umur"     : "20",
                "asal"     : "Tangerang",
                "alamat"   : "Kost Gunawan",
                "hobi"    : "menyanyi",
                "sosmed"   : "@rexanderr",
                "kesan"    : "Abang ini keliatan kalem tapi ternyata asik",  
                "pesan"    : "jangan lupa gaya rock n rollnya bang",
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
                "hobi": "Mencari Uang",
                "sosmed": "@andriangaol",
                "kesan": "bang andrian orangnya pekerja keras sekali",  
                "pesan": "cuan cuan, jangan lupa pulkam bang"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "kak adisty orangnya baik dan asik",  
                "pesan": "Semangat terus kuliahnya kak, hwaiting !!"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun, Sumut",
                "alamat": "Airan",
                "hobi": "Hitung uang",
                "sosmed": "@zhjung_",
                "kesan": "kak nabila orangnya asik",  
                "pesan": "tutor cepat hitung uang kak, semangat kuliahnya kak"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukittinggi",
                "alamat": "Airan 1",
                "hobi": "Badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "bang ahmad orangnya baik",  
                "pesan": "Semangat latihan badmintonnya bang"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Airan",
                "hobi": "Nyuruh-nyuruh",
                "sosmed": "@dananghk_",
                "kesan": "bang danang orangnya baik , ekstrovert parah , dan tentunya our best daplok",  
                "pesan": "jangan lupa jualan dan promosi bang, semangat kuliahnya"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Lapas",
                "hobi": "Apa aja",
                "sosmed": "@farrel_julio",
                "kesan": "bang farrel orangnya baik",  
                "pesan": "tetap semangat bang"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun, Sumut",
                "alamat": "Pemda",
                "hobi": "Suka nulis",
                "sosmed": "@tesakanias",
                "kesan": "kak tessa orangnya humble",  
                "pesan": "semoga kakaknya bisa terbitin tulisannya"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "kak nabilah orangnya baik",  
                "pesan": "keep strong dan semangat kuliahnya kak"
            },
            {
                "nama": "Alvia Asrinda Br.Ginting",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobi": "Nonton windah",
                "sosmed": "@alviagnting",
                "kesan": "Kak alvia baik",  
                "pesan": "stay positive dan jangan lupa istirahat kak"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Balam",
                "alamat": "Jalan Nangka 1",
                "hobi": "Tidur",
                "sosmed": "@dhafinrzqa",
                "kesan": "bang dhafin orangnya baik",  
                "pesan": "Semangat terus kuliahnya bang"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobi": "Badminton",
                "sosmed": "@meylanielia",
                "kesan": "kak elia orangnya humble dan welcome banget",  
                "pesan": "semangat main badmintonnya kak, semangat juga kuliahnyaa"
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
                "hobi": "Nonton",
                "sosmed": "@wayyulaja",
                "kesan": "bang wahyu orangnya baik dan asik",  
                "pesan": "Semangat terus kuliahnya bang, fighting !"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "kak elok orangnya baik",  
                "pesan": "semangat ngedit ngeditnya kak"
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobi": "Nugas",
                "sosmed": "@arsyiah._",
                "kesan": "kak arsy orangnya lucu dan ekstrovert banget",  
                "pesan": "salam dari romskiw kak"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar",
                "hobi": "Lagi Nyari",
                "sosmed": "@dino_kiper",
                "kesan": "bang firdaus orangnya asik",  
                "pesan": "Semangat nyari hobinya bang, semoga dapet yaa"
            },
            {
                "nama": "Muhammad Arsal Ranjana Putra",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 4",
                "hobi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "bang arsal orangnya baik",  
                "pesan": "Semangat ngodingnya bang, tetap semangat"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "kak bella orangnya baik dan asikk",  
                "pesan": "Semangat ngegym dan kulianya kak"
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": "122450045",
                "umur": "20",
                "asal": "Natar, Lampung Selatan",
                "alamat": "Natar, Lampung Selatan",
                "hobi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "kak eka orangnya asikk",  
                "pesan": "jangan lupa istirahat kak walaupun sibuk"
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Airan",
                "hobi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "kak najla kelihatan judes tapi ternyata baik",  
                "pesan": "hobi kita sama kak, bagian fangirling,hehe"
            },
            {
                "nama": "Patricia Leondra Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobi": "Nonton Film",
                "sosmed": "@patriciadiajeng",
                "kesan": "kak cia orangnya ekstrovert parah dan kayaknya banyak teman",  
                "pesan": "semangat kuliahnya kak cia , God Bless"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobi": "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan": "kak neli orangnya baik dan welcome",  
                "pesan": "semangat baca codingnya kak"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "kak try orangnya baik",  
                "pesan": "semoga bisa jadi penyanyi ya kak , semangat kuliahnya"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobi": "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan": "kak dwi orangnya baik",  
                "pesan": "tetap semangat kuliahnya kak , hwaiting !"
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "bang gym orangnya asik",  
                "pesan": "sebenarnya bulatan hitam tu buat apa bang..."
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobi": "Nonton Drakor",
                "sosmed": "@nsywanaf",
                "kesan": "kak nasywa orangnya baik dan ramah",  
                "pesan": "Semangat terus kuliahnya kak, sudah kah kakak nonton drakor hari ini?"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobi": "Baca Novel yang Bikin Nangis",
                "sosmed": "@prskslv",
                "kesan": "kak priska orangnya baik banget",  
                "pesan": "jangan lupa baca au juga kak yang mcnya dead"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa, Labuhan Dalam",
                "hobi": "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan": "bang abit orangnya super baikk dan ngehargain kreasi orang lain bangett",  
                "pesan": "Semangat terus kuliah , ngoding, dan revisian desainnya bang"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobi": "Main HP",
                "sosmed": "_akmal.faiz",
                "kesan": "bang akmal orangnya baik dan asikk",  
                "pesan": "Semangat terus kuliahnya bang, jangan lupa revisian desain"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani)",
                "hobi": "Bengong/Membaca Buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "bang herma orangnya asik , humoris , ++usil banget",  
                "pesan": "tetap semangat kuliah dan ngedesainnya bang"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Belwis",
                "hobi": "Mengerjakan Tugas",
                "sosmed": "@khusnun_nisa335",
               "kesan": "Kkak khusnun orangnya berpengalaman dan ngerti banget soal desain,baik jugaa",  
                "pesan": "keep fighting kak ngerjain tugas dan ngedesainnya"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenmedkraf()
       
             



             
        
        
            
