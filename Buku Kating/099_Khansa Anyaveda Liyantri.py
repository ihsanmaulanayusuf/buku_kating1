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
            "https://drive.google.com/uc?export=view&id=151iYJpuIdkm-bU_5rX1Puw_12bub9AXf",# 1kahim
            "https://drive.google.com/uc?export=view&id=151UwaScsvKhi30bJ2hLeh0oH4c8Kyjmj",# 2sekjen
            "https://drive.google.com/uc?export=view&id=1540ux8D6-fGiU0iDbpuyN9vdHN7QZL-I",# 3sekum
            "https://drive.google.com/uc?export=view&id=151sC0kOm2X20V6lWxf9yLyBoH9v8Uxem",# 4bendum
            "https://drive.google.com/uc?export=view&id=152sV2D_Oo4wdZdKG175Oo32yxGidokQt",# 5sekre1
            "https://drive.google.com/uc?export=view&id=152QQBffwirZqfZIIWzSg6ISc1-X3ZHPn",# 6bend1
            
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar",
                "hobbi": "Dengerin musik",
                "sosmed": "@amsirahk",
                "kesan": "Abang ini mirip bang Pandra",  
                "pesan":"Sukses teruss bang Kahim !!!"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450077",
                "umur": "21",
                "asal":"Bukit Kemuning, Lampung Utara",
                "alamat": "Bawean 2",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Abang ini mirip bang Gumi",  
                "pesan":"Semangat terus kuliahnya bang Sekjen"# 2
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimelinza",
                "kesan": "kakaknya imut banget",  
                "pesan":"Tetaplah rendah hati dan jangan berhenti belajar. Masa depanmu pasti cerah kakak sekre cantikk!!! "# 3
            },
            {
                "nama": "Hartiti Fadhilah",
                "nim": "12145031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "kakak ini baik dan sedikit pendiam",  
                "pesan":"Tetaplah percaya diri dan jangan takut bermimpi besar BUNDAhara!!!"# 4
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "kakaknya baik dan sedikit pendiam seperti kak Hartiti",  
                "pesan":"Jangan pernah berhenti berjuang dan selalu berikan yang terbaik kakak sekre 1!!!"# 5
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin Bang Pandra gitaran kaya kak Putri",
                "sosmed": "@nadillaandr26",
                "kesan": "kakaknya keren dan tegas bangett",  
                "pesan":"Jangan berhenti belajar dan teruslah menginspirasi orang-orang di sekitar kakak bendahara 1!!!"# 6
            }, 
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15BLGseVaYlVEfi7beBYG6Y6d9ofR4T3u",# 1
            "https://drive.google.com/uc?export=view&id=158mbC7-s_hbg2-NUrhWyshll0bSVL8gw",# 2
            "https://drive.google.com/uc?export=view&id=158k_5TL_FMFYfe1D5M4wB5orr6LvScCz",# 3
            "https://drive.google.com/uc?export=view&id=15CfgkXCIRPy5iXV4yKSSwqILtLTyuTY2",# 4.
            "https://drive.google.com/uc?export=view&id=15Cv8mLfxLkglsdKQnO6stXTxT7rNEltV",# 12
            "https://drive.google.com/uc?export=view&id=157-PqUArCiusclvdIi6LbTzR3ONUhUFq",# 6
            "https://drive.google.com/uc?export=view&id=15A43GmlG9j4TXi9hqajZ18nJfCMSlIGY",# 7
            "https://drive.google.com/uc?export=view&id=1HQ3eLyEdnan3O0d8vjn-CmvddPzzVOAV",# 5
            "https://drive.google.com/uc?export=view&id=1HQ_d0TJCofwMY0rDZHpwUNKJ29lCASIX",# 13
            "https://drive.google.com/uc?export=view&id=15C73VM9UVl6ByrthN56L57k5NQDRFOlx",# 11
            "https://drive.google.com/uc?export=view&id=159VkYNPiYdWkev85LGCmr2iDkAIdQllP",# 8
            "https://drive.google.com/uc?export=view&id=156Lb-l2AdrdyQv8nJdY9fpqwG-nITJHi",# 9
            "https://drive.google.com/uc?export=view&id=156y5bWZYw2J76E9mH9exYZJJz0MQk9hv",#10
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Nanya ke GPT",
                "sosmed": "@trimurniaa_",
                "kesan": "selalu sigap kalau ditanya tentang organisasi",  
                "pesan":"Makasih banyak udah jadi panutan, Kak! Semoga Kak Tri makin sukses dan bisa cepet lulus IPK besar."# 1kadep
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Way Huwi",
                "hobbi": "Membaca, menonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak ini ramah dan baik hati",  
                "pesan":"Teruslah berkembang dan jangan takut sama tantangan baru. Masa depan cerah nungguin kakak!!!"# 2sekre
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Belajar, nonton film, tidur",
                "sosmed": "@wlsbn0",
                "kesan": "Kakak ini cantik banget!!!",  
                "pesan":"Kakak pasti bisa capai semua yang apa yang dicita-citakan!!"# 3bend
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Drachin",
                "sosmed": "@anisadini10",
                "kesan": "Kakak ini imut", 
                "pesan":"semangat terus kuliahnya kakak imut !!!"# 4kk1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bernung, Pesawaran",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton drakor",
                "sosmed": "@ansftynn_",
                "kesan": "kakak ini baik dan sedikit pendiam",  
                "pesan":"super sabar dan nggak pernah marah walaupun kita banyak nanya."# 12anggotakk1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "ramah dan nggak segan ngajarin kami",  
                "pesan":"Semoga semua yang terbaik ada di masa depan abang"# 6anggotakk1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Jualan pancing",
                "sosmed": "@fleurnsh",
                "kesan": "Manis bangettttt!!!",  
                "pesan":"Jangan pernah ragu buat terus maju dan cari pengalaman baru. Kakak pasti bakal sukses!!!"# 7anggotakk1
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "122450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak ini vibesnya positif, bikin semangat kita ikut naik",  
                "pesan":"sehat selalu kakakk!!"# 5kk2
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main kucing",
                "sosmed": "@myrriinn",
                "kesan": "Abang ini baik dan tinggi!!",  
                "pesan":""# 13anggotakk2
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Ogan Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari Sinyal di gedung F",
                "sosmed": "@_.dheamelia",
                "kesan": "gemas dan random",  
                "pesan":"Kak Dhea selalu bawa energi positif ke tim. Bikin suasana jadi semangat"# 11anggotakk2
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Melukis, olahraga",
                "sosmed": "@fhrul.pdf",
                "kesan": "baik",  
                "pesan":"Terima kasih banyak, bang Fahrul! Semoga sukses dan sehat selalu Bang"# 8kk3
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang ini aktif menjawab pertanyaan",  
                "pesan":"Makasih banyak ya, Bang! Semoga Abang dapet semua yang diimpikan. Tetap semangat."# 9anggotakk3
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi": "Duduk di tepi pantai sambil galauin bintang ynag tinggal satu",
                "sosmed": "@berlyyanda",
                "kesan": "lucu dan seru",  
                "pesan":"Tetap semangat terus ya, Kak! Aku doain kesuksesan selalu bersama Kakak"# 10anggotakk3
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=176h671cwnUjLgn9O2m1FQFXQ9oK7po8M",# 1
            "https://drive.google.com/uc?export=view&id=176cdKNA6b6ztCyMX2xLcvJ3Z6UqJqxXz",# 2
        ]
        data_list = [
            {
                "nama": "Anissa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal":"Lampung Tengah",
                "alamat": "Kos Putri Rahayu",
                "hobbi": "Bernyanyi",
                "sosmed": "@anissaluthfi_",
                "kesan": "Kakak ini tegas tapi baik hati, bikin kita lebih disiplin tapi tetep santai juga",  
                "pesan":"Semangat mengemban jabatannya kakak kerenn!!!"# 1
            },
            {
                "nama": "Ryan Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abang ini kece abiezz",  
                "pesan": "Terus maju ya, Kak! Jangan berhenti berbagi ilmu sama yang lain!!!"
# 2
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()
# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen PSDA":
    def departemenpsda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13BpftEyugi_nRv8CIDEIsW1yQdpIp71u", #1
            "https://drive.google.com/uc?export=view&id=13BpmwuKnTQjMnD4ryi2uLsogzD1B-K4L", #2
            "https://drive.google.com/uc?export=view&id=12yUZvSEV9aUowxiQ9pN-2HQA7_5S5svZ", #3
            "https://drive.google.com/uc?export=view&id=136UJRINLiEB7RrXEMOrT4rzxhI4ibRbv", #4
            "https://drive.google.com/uc?export=view&id=135mjT7mM2uvxU0S5AUkxJ3qA8tB5pzlv", #5
            "https://drive.google.com/uc?export=view&id=12zOPuMl59yIcZIeqiCk46GRqu-Ensv3e", #6
            "https://drive.google.com/uc?export=view&id=12u2MFwJLQERa_onjNE426p6Z9KHqOR_q", #7
            "https://drive.google.com/uc?export=view&id=13-rqDTBmm4KOyZq4ecg-vAHZfIhTjqaS", #8
            "https://drive.google.com/uc?export=view&id=130b-gVC38gd_sl81U1nGK7jdAnn2bnfS", #9
            "https://drive.google.com/uc?export=view&id=12u5ntP021raozEk9bDZL1SwuF6ibvll_", #10
            "https://drive.google.com/uc?export=view&id=13-Xhcgkd23VSAccFUaWK1FZOWtXlao7b", #11
            "https://drive.google.com/uc?export=view&id=1370U9MU4g5ZeOQM0J7YsWHdqUtC8b-bE", #12
            "https://drive.google.com/uc?export=view&id=13BPlGIxGQoyXtolPHAGKG4qbAWsQ2uNd", #13
            "https://drive.google.com/uc?export=view&id=136eCdtwSL3NfGUMj8n0Bth7qxQj8O3Xk", #14
            "https://drive.google.com/uc?export=view&id=13ApcRlYZNxfwZmk0-2y6JTPDXZ7OMsTy", #15
            "https://drive.google.com/uc?export=view&id=135LuXCkCfiuzhaq4OLCB0NM5KZgYIDK2", #16
            "https://drive.google.com/uc?export=view&id=133oPZTYCLFkxGaW_xiTI4sANtMlHHr2i", #17
            "https://drive.google.com/uc?export=view&id=132tMDBhaqRMGJDbj5ihVFVTxaUn_5B8m", #18
            "https://drive.google.com/uc?export=view&id=132jT5V3scf-mcU4lpFBWMvhCQIydj-iS", #19
            "https://drive.google.com/uc?export=view&id=137HxddapiW0_cSOCrDlXuJfc7KMqHX3_", #20
            "https://drive.google.com/uc?export=view&id=136hwJD2xkkVClv4dHAwhf8QhJ_OG-TkY", #21
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
                "kesan": "Abang ini jago banget dalam organisasi, sangat menginspirasi.",
                "pesan": "Semoga sukses terus, baik di akademik maupun di organisasi. Makin keren lagi ya, Bang!"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "orangnya penuh semangat, bikin kami jadi lebih termotivasi.",
                "pesan": "Terus semangat ya, Kak Abet! Semoga ilmu dan kerja keras kakak bisa jadi inspirasi buat banyak orang."
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal": "Riau",
                "alamat": "Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "selalu sabar ngadepin kami yang sering nanya-nanya. Baik banget!",
                "pesan": "Semangat terus, Kak! Kami yakin bang Ericson bakal sukses di mana pun nanti"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450033",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Sukarame",
                "hobbi": "Muter - Muter",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak  hadir dengan aura positifnya. Bikin kami ngerasa nyaman belajar bareng kakak",
                "pesan": "Semangat ya, Kak!! Semoga apa yang kakak cita-citakan segera tercapai"
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Abang ini humble dan selalu senyum. Nyaman banget ngobrol sama bang Ateng, semua pertanyaan dijawab",
                "pesan": "Abang ini keren banget bisa jawab pertanyaan yang kami tanyakan"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "Jl. Lapas",
                "hobbi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Abang ini tegas, apalagi waktu supporteran",
                "pesan": "Semangat menjabat sebagai Capo utama Damaskus Bang!!!"
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo",
                "hobbi": "Main Game",
                "sosmed": "@kemasverii",
                "kesan": "Abang ini selalu punya jawaban untuk pertanyaan Kelompok 1. PJ tugas paling Top!",
                "pesan": "Semoga bang Kemas bisa terus berkembang dan jadi orang sukses di masa depan"
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin Lomba Sihir",
                "sosmed": "@presiliamg",
                "kesan": "Kakak ini ramah banget, selalu senyum",
                "pesan": "Tetap baik dan ramah ya Kak, sukses selalu"
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak ini orangnya tenang",
                "pesan": "Semoga Kakak selalu diberi kelancaran dalam segala hal"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobbi": "Nonton Jagad review",
                "sosmed": "@sahid_maulana",
                "kesan": "Abang ini tegas dan perhatian, bikin kita ngerasa diperhatikan",
                "pesan": "Semoga makin sukses dan tetap jadi inspirasi buat adik-adik di organisasi"
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Belajar",
                "sosmed": "@roselivnes__",
                "kesan": "Kakak ini cool bangett, jago basket jugaaa!!",
                "pesan": "Kami doakan semoga makin sukses buat Kak Vaness biar aku bisa nyanyi 'Dataku menang lagi'"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobbi": "Nongs",
                "sosmed": "@allyaislami_",
                "kesan": "Kakak ini tegas dan diplin banget, bikin kita lebih termotivasi untuk jadi lebih baik",
                "pesan": "Terima kasih banyak, Kak! Semoga sukses selalu menyertai Kak Allya"
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Natar",
                "hobbi": "Nyari sinyal di gedung F",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini kreatif dan selalu kasih ide-ide brilian",
                "pesan": "Terus berkarya dan sukses ya, Kak! Semoga semua rencana Kak Eksanty berjalan lancar"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450051",
                "umur": "19",
                "asal": "Kayu Agung",
                "alamat": "Kedaton",
                "hobbi": "Nongki - nongki",
                "sosmed": "@dransyah_",
                "kesan": "Abang ini selalu bikin suasana jadi cair, santai dan seru banget orangnya",
                "pesan": "Tetap jadi sosok yang asik ya, Bang! Semoga Bang Deri selalu dilancarkan dalam segala hal"
            },
            {
                "nama": "Oktavia Nurwendah Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@oktavianrwnda",
                "kesan": "Kakak ini membawa suasana yang positif dan hangat",
                "pesan": "Semoga kak Okta selalu bahagia dan sukses di masa depan"
            },
            {
                "nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "Abang ini ramah dan nggak pelit ilmu, selalu bantu jawab pertanyaan kalau kita bertanya",
                "pesan": "Tetap humble ya, Kak. Aku doakan semoga Abang selalu mendapatkan yang terbaik"
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "Kak Jaclin positive vibes dan kreatif bangett",
                "pesan": "Terima kasih atas semua bantuan Kak! Semoga sukses selalu kakak MC."
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Abang ini selalu mendengarkan pertanyaan kita dengan baik",
                "pesan": "Semoga abang selalu dikelilingi oleh orang-orang baik "
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i_",
                "kesan": "sangat ramah dan selalu siap berbagi ilmu",
                "pesan": "Terima kasih, Kak! Semoga Kakak selalu dipermudah di semua urusan"
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Pangeran Senopati Raya 18",
                "hobbi": "Baca Kitab Suci",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abang ini selalu bisa mengatasi setiap masalah dengan tenang",
                "pesan": "Tetap jadi jadi panutan bagi kita semua ya Bang"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Bengong",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini murah senyum dan cantik bangett",
                "pesan": "Jangan pernah berubah, ya Kak! Semoga sukses dalam setiap langkah"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenpsda()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen MIKFES":
    def departemenmikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18hdAAefK2KsGzJGN6odfUSq5yfYMY5x7", #1
            "https://drive.google.com/uc?export=view&id=18dbSe8ThfxW3lLP9CCsEeREUrJ2iGAkx", #2
            "https://drive.google.com/uc?export=view&id=18ipTbf_DDUSaUd-TbDd4hi8phsh-BcSX", #3
            "https://drive.google.com/uc?export=view&id=18XUho29DrUdfkOLBkSQhXBPEXcPW02ec", #4
            "https://drive.google.com/uc?export=view&id=18bDO8Moyg9fyjofbajYru52t7IhxDlTS", #5
            "https://drive.google.com/uc?export=view&id=18dim6vnJ7OsPDynkX9GIgTME4wotaB-6", #6
            "https://drive.google.com/uc?export=view&id=18dVqqfDTu7lrzMZQyv6k7Lm489rvk4eG", #7
            "https://drive.google.com/uc?export=view&id=18i4FowhU0Sy3oA-f2Olyeecf3AU81Lm4", #8
            "https://drive.google.com/uc?export=view&id=18jgiR8wz-HHy6VhegAzzHfO1ltOsXGBG", #9
            "https://drive.google.com/uc?export=view&id=18XYc_AkAU7woyh9mFgx92Qr61PuBCxIt", #10
            "https://drive.google.com/uc?export=view&id=18i8dB_yuuo-xBbepuLkb_z7G9Vkq2oXg", #11
            "https://drive.google.com/uc?export=view&id=18_2SM5InLDP_vrmbqjU0bWugGhIzO4qv", #12
            "https://drive.google.com/uc?export=view&id=18etF4JagxrQNX7PpstseHVOmdBY61AiY", #13
            "https://drive.google.com/uc?export=view&id=18cIjC8VowFdcA0fONDGIbZs0rDCwegHH", #14
            "https://drive.google.com/uc?export=view&id=18_2SM5InLDP_vrmbqjU0bWugGhIzO4qv", #15
            "https://drive.google.com/uc?export=view&id=18gI8jrSZFJWeAJYbluyTs6AFXB1VuEm5", #16
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
                "kesan": "sangat berdedikasi, selalu memberikan yang terbaik dan selalu berbagi ilmu dengan senang hati",
                "pesan": "Makasih banyak Bang, semoga usaha abang memberikan kesuksesan untuk abang"
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Kakak ini ceria dan membawa suasana positif",
                "pesan": "Tetap ceria ya, Kak! Semoga semua impian Kakak bisa cepat terwujud"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "Abang ini punya ide-ide yang kreatif",
                "pesan": "Teruslah berpikir kreatif, ya Bang! Semoga semua cita-cita Kakak tercapai"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakak ini baik, ramah, dan murah senyum",
                "pesan": "Semoga Kakkak selalu diberikan kesehatan dan kebahagiaan"
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "Abang ini selalu punya solusi kreatif untuk setiap masalah",
                "pesan": "Tetap jadi pendengar yang baik ya, Bang! Semoga semua cita-cita Abang bisa tercapai"
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "Kakak ini positif vibes dan gemoyyyy bangettt",
                "pesan": "Tetap jadi sosok yang inspiratif ya, Kak!"
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Membaca jurnal Bu Mika",
                "sosmed": "@dindanababan_",
                "kesan": "Kakak ini sangat sabar",
                "pesan": "Tetaplah berpikir positif, ya Kak! Semoga sukses selalu menyertai Kakak"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak ini super manisss dan positif vibes banget",
                "pesan": "Semoga kakak terus menjadi sumber keceriaan bagi banyak orang"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Menghitung akurasi",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak ini baikkk, ramah dan gemess bgt",
                "pesan": "Terus berinovasi dan semoga kakak sukses di masa depan"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membangkitkan bilangan",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini sangat inspiratif",
                "pesan": "Semoga Kak Syadza terus jadi penyemangat bagi orang-orang di sekitar"
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "Abang ini selalu mau membantu dan tidak pernah mengeluh",
                "pesan": "Terima kasih atas semua bantuannya bang!"
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Kelengkeng Raya",
                "hobbi": "Review jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakak ini cantikk dan ramah bangett",
                "pesan": "Semoga Kakak bisa menginspirasi orang-orang di sekitar"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "Murah senyum dan suka membantu",
                "pesan": "Terimakasih banyak atas bantuannya Bang!!!"
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Abang ini baik dan sedikit pendiam",
                "pesan": "Terus tersenyum ya bang, Semoga abang selalu sukses"
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Jl Nangka 3",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randardn",
                "kesan": "Abang ini Pintar dan ramah",
                "pesan": "Semoga Abang selalu dikelilingi oleh orang-orang baik dan terus bahagia"
            }
        ]

        display_images_with_data(gambar_urls, data_list)
    departemenmikfes()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen Eksternal":
    def departemeneksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=171mQQpwb7IoOIR5o_TQ7tCB1BVrDE5bW", #1
            "https://drive.google.com/uc?export=view&id=170WZsJFSml2fV1fCWaihDL4ULNMbi9Aq", #2
            "https://drive.google.com/uc?export=view&id=16yfMV2F6tar9OL9C15d1JwW2IsrgpSU-", #3
            "https://drive.google.com/uc?export=view&id=16x5LaMCyRgS59vaBHYnWD9K-CfUJB4AS", #4
            "https://drive.google.com/uc?export=view&id=1724JRRZbPcXQyTWvcggr-RDnlMkhwQuV", #5
            "https://drive.google.com/uc?export=view&id=16xoOb4pR-Eym-VzwQQ4m2VO7QhlCgGD4", #6
            "https://drive.google.com/uc?export=view&id=16xjhTuM36dYNRbN_0_-McoMH-dYU_sIJ", #7
            "https://drive.google.com/uc?export=view&id=16wLHcz4Tbz5NPksr9uA009t0YBDNIEOw", #8
            "https://drive.google.com/uc?export=view&id=16zRhVbuU7HHg4S9Ls-qLR7_Ug7_fLX6q", #9
            "https://drive.google.com/uc?export=view&id=16w2N2czv2hmMS_ziH2UmoPaHRAjknxgp", #10
            "https://drive.google.com/uc?export=view&id=17--ma6mxF93yX3T5jnIxKusd7VIdj6vY", #11
            "https://drive.google.com/uc?export=view&id=172dMOOgCcWaMYWtUFqWkAU-FC0PVqqKU", #12
            "https://drive.google.com/uc?export=view&id=16z6YysQT3QKbZdiJRANUiFT6dWsmMc9B", #13
            "https://drive.google.com/uc?export=view&id=173ftfirDYW7VXUylMFQdciVFa7w7y0lT", #14
            "https://drive.google.com/uc?export=view&id=17560N2Gq68yOjokvq0pnhGeNXLzx02xZ", #15
            "https://drive.google.com/uc?export=view&id=16v-cMRRvnIF4KZtsUrVpXnwYrNotn3jZ", #16
            "https://drive.google.com/uc?export=view&id=16vxFGqr1cemW2II87Bwe5HEm6pL82_K1", #17
            "https://drive.google.com/uc?export=view&id=175ne3zzTkkhKm9nx6YXWYXirqJbdMIuz", #18
            "https://drive.google.com/uc?export=view&id=16tWn7qwW2HU0osxsenNjqE16vMgcasHl", #19
            "https://drive.google.com/uc?export=view&id=16rEQ_YdCUC-jlG1KH0O6ljIaXHHeAkKo", #20
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
                "kesan": "Abangnya asik, selalu bikin suasana jadi lebih seru!",
                "pesan": "Makasih banyak, Bang! Semoga Abang selalu mendapatkan yang terbaik."
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan-Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "Kakak ini ramah dan siap diajak berdiskusi",
                "pesan": "Makasih atas semua bantuannya, Kak. Semoga selalu sukses dalam setiap langkah"
            },
            {
                "nama": "Nazwa Nabila",
                "nim": "121450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Kochpri",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakak ini ramah, mampu menciptakan suasana positif",
                "pesan": "Semoga Kak Lala selalu menemukan kebahagiaan dalam setiap hal yang dilakukan"
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "Abang ini bijak dan selalu memberi motivasi yang tepat",
                "pesan": "Semoga abang, selalu beruntung dan mencapai semua tujuannya"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Berkebun",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak ini gemas, ramah, positif vibes",
                "pesan": "semua yang Kak Dea ajarkan menjadi bermanfaat bagi banyak orang"
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan": "Kakak ini selalu ceria dan membuat suasana menjadi lebih hidup",
                "pesan": "Terima kasih atas semua bantuannya, Kak! Semoga sukses selalu"
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Surfing",
                "sosmed": "@nateee__15",
                "kesan": "Kakak ini humble dan selalu senyum",
                "pesan": "Semangat terus kuliahnya kakak cantikk!!"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "cantik, baik, dan soft spoken bangettt??!!",
                "pesan": "Semangat terus kakakkk, semoga kakak selalu dipermudah dalam segala hal, dan jangan lupa jaga kesehatan!!"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan": "Ramah banget, terus namanya bagus bangett (salfok)",
                "pesan": "Semangat kuliahnya kak, semoga bisa lulus cumlaude!!"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan": "Tegas tapi baik dan ramah bangett waktu disapa",
                "pesan": "Jangan lupa jaga kesehatan bang, biar ga gampang sakit"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "Kakak ini keren banget",
                "pesan": "Semangat terus kuliahnya, doa terbaik untuk kakak"
            },
            {
                "nama": "Rizky Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "Abang ini keren dan tinggi sekali",
                "pesan": "Tetap semangat dan selalu jaga kesehatan ya bang!"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "Abang ini ramah dan humble",
                "pesan": "Semoga sukses besar menanti bang Arafi di masa depan. Tetap rendah hati ya, Bang!"
            },
            {
                "nama": "Asa Do’a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "Kakak ini gemess bangett kaya karakter cerpen anak di majalah/koran gituu",
                "pesan": "Tetap berbagi ilmu ya, Kak! Semoga Kakak selalu dimudahkan dalam segala hal"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan": "Kakak ini cantik, baik dan ramahhh bangettt",
                "pesan": "Makasih ya, Kak, buat semua sharing-nya! Semoga rezeki Kakak lancar terus!"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abang ini murah senyum dan perhatian sekalii",
                "pesan": "Terimakasih bang Irvan, Jangan pernah berubah ya Bang!"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan": "Kakak ini ekstrovert dan ceria banget",
                "pesan": "Tetap humble ya, Kak. Semoga ke depan makin sukses dan bahagia!"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "Kak Alyaa orangnya bisa diandalkan waktu dibutuhkan, selalu ngingetin kami buat terus semangat. Support kakak luar biasa. Best daplok dari segala daplok",
                "pesan": "Makasih banyak kak, Tetap jadi pendengar yang baik ya!!! Semoga Kakak dapet semua yang diimpikan. Tetap semangat selalu."
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Nemenin Tobias lari",
                "sosmed": "@rayths_",
                "kesan": "Abang ini pintar, ramah, dan sedikit pendiam",
                "pesan": "Semangat terus ngaspraknya bang Raid, jangan cape-cape ngajarin kita yaaa!!"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450127",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Way Dadi",
                "hobbi": "Olahraga",
                "sosmed": "@triayunanni",
                "kesan": "Kakak ini lucu dan imut banget pliss",
                "pesan": "Semangat terus kuliahnya kak Yuna, semoga bisa cepat lulus dengan IPK sesuai harapan"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemeneksternal()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen Internal":
    def departemeninternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18IUGYN8XDj_PKjhQqZLqibK5QJfAAym2", #1
            "https://drive.google.com/uc?export=view&id=18VZ9-3hbux0V4b4j57QNv2L4msGfzVEV", #2
            "https://drive.google.com/uc?export=view&id=18Q41oCyPwUxpvwtR2o95ibckDX6D07AC", #3
            "https://drive.google.com/uc?export=view&id=18NwLy52otdSjr6RL_gbxNuqv2UO3xxCq", #4
            "https://drive.google.com/uc?export=view&id=18JHDOUofaz1PExraec8nlInXAXPwbdOr", #5
            "https://drive.google.com/uc?export=view&id=18OU0J4feGJUeYRcszqnAywdomNjXUt4r", #6
            "https://drive.google.com/uc?export=view&id=18VF810Sfhco5E9qbWq3lAJBtr-C9m28a", #7
            "https://drive.google.com/uc?export=view&id=18UMOSA-CcetN80Q4S6xDb82kSO0fBcEA", #8
            "https://drive.google.com/uc?export=view&id=18UFzb-S0K1ikKR3cJsq8F7HqbAUpiLPH", #9
            "https://drive.google.com/uc?export=view&id=18SMexfGUyfYH9PsWQ6DVI_IBpr6mZOVg", #10
            "https://drive.google.com/uc?export=view&id=18Sex_0--fg65Z4uXGUgY_3btgvDwl97X", #11
            "https://drive.google.com/uc?export=view&id=18TBDbisdE3UsgNxlpCTBhk9YU7oa3DG4", #12
            "https://drive.google.com/uc?export=view&id=18MGYNe15NMfU0oPUjqEye-bMolY3HnyY", #13
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
                "kesan": "Abang ini ramah, keren, dan asik juga orangnya",
                "pesan": "Semoga Bang Dimas bisa terus berkembang dan sukses di mana pun berada. tetap jadi orang keren ya bang!!!"
            },
            {
                "nama": "Chatrine Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "Kakak ini selalu tenang dan sabar",
                "pesan": "Makasih banyak, Kak Catherine. Semoga ke depannya tambah lancar kariernya!"
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Pasaruntung",
                "hobbi": "Mengoleksi Dino",
                "sosmed": "@akbar_restika",
                "kesan": "Abang ini aktif dan suka menjawab pertanyaan dengan baik",
                "pesan": "Makasih sharingnya bang, semoga abang selalu dimudahkan dalam segala hal"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Membaca dan Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakak ini aktif menjawab dan suka memberi support berdasarkan pengalamannya",
                "pesan": "Pertahankan ya kak, kakak keren banget!!"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "Kakak ini baik, humble, positif vibes",
                "pesan": "Tetap jadi kakak yang hebat ya, Kak. Semoga semua usahanya berbuah manis!"
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "Abang ini aktif dan keren banget, aura calon orang sukses",
                "pesan": "Semangat terus kuliahnya Bang, semoga diberi jalan yang terbaik dalam setiap langkah menuju sukses"
            },
            {
                "nama": "Yosia Retare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi": "Nungguin ayam betina berkokok",
                "sosmed": "@yosiabanurea",
                "kesan": "Abang ini asik, murah senyum dan ramah",
                "pesan": "Tetap humble ya, Bang! Semoga apa pun yang dicita-citakan segera tercapai"
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "Abang ini baik dan sedikit pendiam",
                "pesan": "Semangat terus Bang, Jangan lupa senyummm!!"
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Ngejokes",
                "sosmed": "@josuapanggabean_",
                "kesan": "Abang ini tinggi, ramah, dan keren",
                "pesan": "Semangat terus kuliahnya Bang, semoga mendapat hasil akhir sesuai yang diharapkan"
            },
            {
                "nama": "Azizah Kusuma Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@meirasty_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Berenang di Laut",
                "sosmed": "@rexander",
                "kesan": "Abang ini baik, pintar, dan terlihat sedikit pendiam",
                "pesan": "Terimakasih Bang, Semoga kebaikan Abang dibalas dengan kesuksesan"
            },
            {
                "nama": "Rani Puspita Ningrum",
                "nim": "122450022",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@rannipu",
                "kesan": "Kakak ini cantik, baik, dan cool banget",
                "pesan": "Semangat terus kuliahnya kak, semoga bisa lulus tepat waktu dengan IPK yang diharapkan"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemeninternal()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen SSD":
    def departemenssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18WbGDT-i8p0aG119TgklWr-qTP5jBNRj", #1
            "https://drive.google.com/uc?export=view&id=16hJ1w-9SzPGI6jcRX7nXJ95lqhYnMVzn", #2
            "https://drive.google.com/uc?export=view&id=16dXaRl0csTDe3Z0IDXtjTOjKTX7bC7Cd", #3
            "https://drive.google.com/uc?export=view&id=16kqKF46BdO21zJyecQwfOvL0zmhMt7MW", #4
            "https://drive.google.com/uc?export=view&id=16k53TAgwZMRG6zmc4LiEADiU1lwH_sZ3", #5
            "https://drive.google.com/uc?export=view&id=16kz9jzGGCJ238H33-h-D_9xM9_AManGK", #6
            "https://drive.google.com/uc?export=view&id=16hZ5Scpq-buqEIdNytVQ83GjA8yqsvhE", #7
            "https://drive.google.com/uc?export=view&id=18W973aUG5X6dTNKvgbIpF1FTp4XMd5a-", #8
            "https://drive.google.com/uc?export=view&id=16j5ko3jbYtSdlZPVdyAQnQZOA6OQkA1l", #9
            "https://drive.google.com/uc?export=view&id=16jRZRMIiUTbW_wnpRyyYxsJ0vea9iGmw", #10
            "https://drive.google.com/uc?export=view&id=16gtgAjlS4mq5BbV-nvTiBCUafb22x06b", #11
        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumbangaol",
                "nim": "121450090",
                "umur": "21",
                "asal": "Panjibako",
                "alamat": "Jl. Bel",
                "hobbi": "Mencari Uang",
                "sosmed": "@andriangaol",
                "kesan": "Abang ini keren, dan terlihat seperti bisa diandalkan",
                "pesan": "Semangat terus Bang Kadep, semoga urusannya selalu dipermudah"
            },
            {
                "nama": "Adisty Syawaida Arianto",
                "nim": "121450136",
                "umur": "23",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan": "Kakak ini cantik dan positif vibes bangetttt",
                "pesan": "Semoga kakak selalu dikelilingi keberuntungan."
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "Kakak ini orangnya ceria",
                "pesan": "Terimakasih banyak kak, Semoga lancar terus kuliahnya"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Touring",
                "sosmed": "@dananghk_",
                "kesan": "Bang Danang selalu excited berbagi ilmu dan pengalaman. Kita jadi lebih termotivasi belajar. Best daplok pokoknya!!!",
                "pesan": "Makasih atas supportnya Bang daplok 01!!! Kami doakan semua yang terbaik untuk karier bang Danang (calon orang sukses)"
            },
            {
                "nama": "Farel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "Abang ini punya pandangan yang luas dan bijak, Kita jadi lebih terbuka pikiran",
                "pesan": "Selalu bang Capo 1 diberikan kelancaran dan sukses di masa depan."
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukittingi",
                "alamat": "Airan 1",
                "hobbi": "Badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "Abang ini ramah dan selalu sabar",
                "pesan": "Tetap sabar dan baik ya, Bang! Kami doakan semoga Abang bisa cepat merealisasikan cita-cita"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakak ini aktif di sharing session, ramah dan murah senyum juga!!",
                "pesan": "Terimaksih sharingnya kak, jangan lupa selalu jaga kesehatan"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Kakak ini sedikit pendiam, tapi baik dan ramah",
                "pesan": "Semoga sukses terus dan selalu tercapai semua keinginan Kakak"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobbi": "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan": "Kakak ini ga pelit ilmu, aktif waktu wawancara, terlihat punya banyak koneksi",
                "pesan": "Semangat terus kakak sponsorship"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangkal",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abang ini keren dan selalu mau mendengar pertanyaan kita",
                "pesan": "Semangat terus Bang, semoga abang selalu diberi kesehatan"
            },
            {
                "nama": "Alvia Asrinda Br. Ginting",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobbi": "Nonton",
                "sosmed": "@Alifiagntg",
                "kesan": "Kakak ini baik dan mau berbagi ilmu",
                "pesan": "Stay positif ya Kak!!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenssd()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen MEDKRAF":
    def departemenmedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12JJW-fJm4yI7KmO3GvFZQ_7Tr9Pm8sHB", #1
            "https://drive.google.com/uc?export=view&id=12H49bczxog2EbLOoi1XETVs3uyEbewnm", #2
            "https://drive.google.com/uc?export=view&id=12I5ISPKSeCRufaqtCQY-DljrkuXssDvM", #3
            "https://drive.google.com/uc?export=view&id=12AxtsPIp-3SUaw2P_b8UsWFrhmG-Ly1f", #4
            "https://drive.google.com/uc?export=view&id=12J8pkMR0xlCtpvwy78YliERP7Jbhibxb", #5
            "https://drive.google.com/uc?export=view&id=12GlEr2UCpWYwRNi-XXsh7DNnMX__-R5W", #6
            "https://drive.google.com/uc?export=view&id=12DGhMPNdXdyvv1mOeDxeNO6l-aCmqX1j", #7
            "https://drive.google.com/uc?export=view&id=12If52dX9Gs4o677y-Gu04RrP0jto_VWR", #8
            "https://drive.google.com/uc?export=view&id=1265h-HwFutH6CYTZZW_sOTVGDRtBaz9U", #9
            "https://drive.google.com/uc?export=view&id=12GP7_192beNbzo72eO3IXQVfDVD1CMX_", #10
            "https://drive.google.com/uc?export=view&id=12IU7LU8qMkVmV3xPgZejiNoOp5trIkvG", #11
            "https://drive.google.com/uc?export=view&id=12Cy1pX1IAAHC5BhmFV1Rum1GsmsiTCyO", #12
            "https://drive.google.com/uc?export=view&id=12Bfn3FwhoPfSgPSmbO0YxxNuMx0Cgd3S", #13
            "https://drive.google.com/uc?export=view&id=1285Z3YCQUgdBPTgo_N28HKQP1IAavdGf", #14
            "https://drive.google.com/uc?export=view&id=128fHeAjsCpSDpmCtDHWMbYkx0z1dY7zT", #15
            "https://drive.google.com/uc?export=view&id=12DFQbstMEpTD1KIqDCZI7__8LkPatpsE", #16
            "https://drive.google.com/uc?export=view&id=12Ezv2515m1Ad0feKw2ddJqem2aLhGB5e", #17
            "https://drive.google.com/uc?export=view&id=127wFwJZ6woPYmnEHxU0ayRvb4H1qO2E5", #18
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
                "kesan": "Abang ini keren, ramah dan ga pelit ilmu, bikin kita merasa dihargai",
                "pesan": "Semoga Abang selalu diberi kebahagiaan dan tercapai semua yang diinginkan"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "Kakak ini cantik banget, dan terilaht disiplin",
                "pesan": "Semangat terus kuliah dan ngaspraknya kak Elok, jangan bosen ngajarin kita ya!!"
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Nugas",
                "sosmed": "@arsyiah._",
                "kesan": "Kakak ini keren dan seru banget orangnya",
                "pesan": "Semoga ke depannya selalu sukses ya kak!!"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Lagi Nyari",
                "sosmed": "@dino_kiper",
                "kesan": "Abang ini keren, tegas, dan menghargai orang lain",
                "pesan": "Terimakasih Bang!!, semoga Abang lancar selalu dalam karier dan hidup"
            },
            {
                "nama": "Muhammad Arsal Ranjana Putra",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 4",
                "hobbi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "Abang ini baik dan ramah, suka membantu kalau ada yang kesulitan",
                "pesan": "Terimakasih ilmunya bang,  Semoga sukses dan jadi inspirasi!"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Kakak ini cantik, murah senyum, dan tinggi bangettttt!!!",
                "pesan": "Semangat terus kak, semoga selalu diberi kesehatan biar bisa ngegym teruss!!"
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": "122450045",
                "umur": "20",
                "asal": "Natar, Lampung Selatan",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "Kakak ini ceria dan Ekstrovert banget bikin jadi semangat tiap materi",
                "pesan": "Semangat terus kak, soalnya kakak bikin semangat yang lain jugaaa"
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "Kakak ini cantik dan terlihat sedikit pendiam",
                "pesan": "Semoga hari-hari kakak selalu dipermudahh yaa!!"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton Film",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakak ini cantik, imut, ramah, baik, positive vibes... duh apa lagi ya, semua yang bagus-bagus diborong soalnya",
                "pesan": "Semangat terus kuliahnya ya kak!!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan": "Kakak ini cantik, asik, gemasss, dan lucuuu bangetttt",
                "pesan": "Semangat terus ngontennya kak Neli!!!"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakak ini cantikk, baik, dan ramah banget",
                "pesan": "Semangat terus ya kak, semoga sehat dan sukses selalu"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi": "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan": "Kakak ini gemess dan Humble bangetttttt!!!!",
                "pesan": "Semangat terus ya kak, tapi jangan lupa istirahat biar ga kecapean!!"
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "Abang ini asik dan humoris bangettt",
                "pesan": "Semoga pejalanan hidup bang Gym selalu di perlancar biar cepet sukses yaa!!!!"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi": "Nonton Drakor",
                "sosmed": "@nsywanaf",
                "kesan": "Kakak ini keren, baik, dan jago bangett main UNO!!!!",
                "pesan": "Makasi sharingnya kak, semoga kakak "
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Baca Novel yang Bikin Nangis",
                "sosmed": "@prskslv",
                "kesan": "Kakak ini orangnya seru, ceria, dan terlihat sabar",
                "pesan": "Semangat terus kak, jangan sering-sering nangis dong walaupun hobi:("
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa, Labuhan Dalam",
                "hobbi": "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan": "Abang ini humble dan suka memberi pendapat saat sharing session",
                "pesan": "Terimakasih bang, semoga ilmu yang abang beri bisa membuahkan hasil yang baik juga"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "_akmal.faiz",
                "kesan": "Abang ini keliatannya perhatian dan pintar bangett",
                "pesan": "Semangat terus bang, pertahanin perhatian ke anak anaknyaa!!"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani)",
                "hobbi": "Bengong/Membaca Buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Abang ini humoris, perhatian jugaa",
                "pesan": "Makasih ya bang!! Semoga kebaikan yang abang sampaikan berbalik kembali ke abang"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi": "Mengerjakan Tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Kakak ini Polos, imut, dan baik sekali",
                "pesan": "Semangat terus kak bikin design nyaaa!!!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenmedkraf()
