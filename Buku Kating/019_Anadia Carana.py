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
            st.write(f"Nama        : {data_list[i]['nama']}")
            st.write(f"NIM         : {data_list[i]['nim']}")
            st.write(f"Umur        : {data_list[i]['umur']}")
            st.write(f"Asal        : {data_list[i]['asal']}")
            st.write(f"Alamat      : {data_list[i]['alamat']}")
            st.write(f"Hobbi       : {data_list[i]['hobbi']}")
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
            "https://drive.google.com/uc?export=view&id=1mNrex_khHrnihHo5ObIpi-T-SfqHuIzs",
            "https://drive.google.com/uc?export=view&id=1sfKcCmrMeFrH7Lcwt5ksKzS0Hm9FZkp7",
            "https://drive.google.com/uc?export=view&id=1hgdzNSs0b1cncc_7GZnFX1Qj8kmTA5vE",
            "https://drive.google.com/uc?export=view&id=1LgNq02tgdwNvaPdyPZxp1l8MAKVkqr28",
            "https://drive.google.com/uc?export=view&id=10cmHseL59luvqFjTcO3yw-DcGWDL0wgC",
            "https://drive.google.com/uc?export=view&id=1_w4moRgKLCiU_t-34F5kHxTldlIq83T0",
        ]
        data_list = [
            {
                "nama"     : "Kharisma Gumilang",
                "nim"      : "121450142",
                "umur"     : "21",
                "asal"     :"Palembang",
                "alamat"   : "Pulau Damar",
                "hobbi"    : "Dengerin musik",
                "sosmed"   : "@gumilangkharisma",
                "kesan"    : "Abangnya berwibawa, humble, dan banyak pengalamannya yang membuat saya banyak belajar",  
                "pesan"    : "Terima kasih ilmunya, sukses selalu, dan semangat terus kuliahnya bang!"
            },
            {
                "nama"     : "Pandra Insani Putra Azwar",
                "nim"      : "121450137",
                "umur"     : "21",
                "asal"     : "Bukit Kemuning",
                "alamat"   : "Pawen 2 Sukarame",
                "hobbi"    : "Main gitar",
                "sosmed"   : "@pndrinsni27",
                "kesan"    : "Abangnya seru, humble banget, dan enak diajak ngobrol",  
                "pesan"    : "Semoga abang sukses selalu di segala kegiatan yang dikerjakan"
            },
            {
                "nama"     : "Meliza Wulandari",
                "nim"      : "121450065",
                "umur"     : "20",
                "asal"     : "Pagar Alam",
                "alamat"   : "Kotabaru",
                "hobbi"    : "Nonton Drakor",
                "sosmed"   : "@wulandarimeliza",
                "kesan"    : "Kakaknya baik, seru, dan ramah",  
                "pesan"    : "Seneng banget bisa ngobrol sama kakak yang seru"
            },
            {
                "nama"     : "Putri Maulida Chairani",
                "nim"      : "121450050",
                "umur"     : "21",
                "asal"     : "Payakumbuh",
                "alamat"   : "Nangka 4",
                "hobbi"    : "Dengerin bang Pandra Gitaran",
                "sosmed"   : "@ptrimaulidaaa_",
                "kesan"    : "Kakaknya baik, sangat suportif, dan terbuka",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Hartiti Fadilah",
                "nim"      : "121450031",
                "umur"     : "21",
                "asal"     : "Palembang",
                "alamat"   : "Pemda",
                "hobbi"    : "Nyanyi",
                "sosmed"   : "@hrtfdlh",
                "kesan"    : "Kakaknya ramah dan terbuka, bikin kita nyaman buat tanya-tanya",  
                "pesan"    : "Semoga kakak selalu sehat dan tetap semangat di tugas-tugasnya kak!"
            },
            {
                "nama"     : "Nadilla Andhara Putri",
                "nim"      : "121450003",
                "umur"     : "21",
                "asal"     : "Metro",
                "alamat"   : "Kotabaru",
                "hobbi"    : "Dengerin  bang Pandra Gitaran",
                "sosmed"   : "@nadillaandr26",
                "kesan"    : "Cara komunikasi kakak menjawab pertanyaan rapi dan jelas, mudah dimengerti",  
                "pesan"    : "Sukses selalu di tugas-tugas kakak, semoga kami bisa terus belajar!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Nsu9ZZFaBrTftT2vYhSyW86oNMZw9B59",
            "https://drive.google.com/uc?export=view&id=1RG93yUlOqDb3WN0hw-x8MYSygYf1aqaA",
            "https://drive.google.com/uc?export=view&id=1vBgbMN4TwNW1v8Eh3tJ_8sZ5XHiwY0_S",
            "https://drive.google.com/uc?export=view&id=105H-xR1sK2XnzvBjOz1Bn5U2knJOgmiY",
            "https://drive.google.com/uc?export=view&id=1V8BrNSBTlQslNH8aEXGGAIBtbkZrsq5a",
            "https://drive.google.com/uc?export=view&id=1jmlpKulaa5reHn2JLr4nlOgQlTnPeq4a",
            "https://drive.google.com/uc?export=view&id=1edK109nRD7bJk9Ymm0pWiZGprsSBB-mf",
            "https://drive.google.com/uc?export=view&id=1jDaf0UW8L8IqaAjtqSi3nZD64CEK0l06",
            "https://drive.google.com/uc?export=view&id=1pMh-Bw0t13Mo_qaKmGvQsdVWNGSk_HsB",
            "https://drive.google.com/uc?export=view&id=1eWbRyxh43nliGzY9AInRf6yIBLMolE5W",
            "https://drive.google.com/uc?export=view&id=16oQfW4ePnVazmsqcpCd0purBFxlYyH5l",
            "https://drive.google.com/uc?export=view&id=1GJl32SfNIwoQpFYOchIdeyARbmIclE5L",
            "https://drive.google.com/uc?export=view&id=1ymnlzK2EhAU9lRGFApqS86I1dEsKE6EM",
        ]
        data_list = [
            {
                "nama"     : "Tri Murniya Ningsih",
                "nim"      : "121450038",
                "umur"     : "21",
                "asal"     : "Bogor",
                "alamat"   : "Raden Saleh",
                "hobbi"    : "Bertanya sama GPT",
                "sosmed"   : "@trimurniaa_",
                "kesan"    : "Kakak ini asik, baik, dan public speakingnya bagus",  
                "pesan"    : "Sukses terus kak, terima kasih sudah selalu terbuka buat diskusi"
            },
            {
                "nama"     : "Annisa Cahyani Surya",
                "nim"      : "121450114",
                "umur"     : "21",
                "asal"     : "Tangerang Selatan",
                "alamat"   : "Way Hui",
                "hobbi"    : "Membaca",
                "sosmed"   : "@annisacahyanisurya",
                "kesan"    : "Kakaknya supportive, selalu mendengarkan pendapat kami dengan baik",  
                "pesan"    : "Makasih sudah selalu siap membantu dan menjawab pertanyaan kami kak!"
            },
            {
                "nama"     : "Wulan Sabina",
                "nim"      : "121450150",
                "umur"     : "21",
                "asal"     : "Medan",
                "alamat"   : "Raden Saleh",
                "hobbi"    : "Menonton Film",
                "sosmed"   : "@wlsbn0",
                "kesan"    : "Kakak ini baik, asik, serta banyak insight dan pengalaman menarik",  
                "pesan"    : "Semoga kakak selalu sehat dan sukses terus kak"
            },
            {
                "nama"     : "Anisa Dini Amalia",
                "nim"      : "121450081",
                "umur"     : "20",
                "asal"     : "Tangerang",
                "alamat"   : "Jati Agung",
                "hobbi"    : "Nonton Dracin",
                "sosmed"   : "@anisadini10",
                "kesan"    : "Suka sama energi positif kakak, bikin suasana diskusi jadi lebih hidup!",  
                "pesan"    : "Semoga kakak terus jadi inspirasi buat kita semua"
            },
            {
                "nama"     : "Anisa Fitriyani",
                "nim"      : "122450019",
                "umur"     : "19",
                "asal"     : "Bernung, Pesawaran",
                "alamat"   : "Bandar Lampung",
                "hobbi"    : "Nonton Drakor",
                "sosmed"   : "@ansftynn_",
                "kesan"    : "Kakak selalu open buat diskusi dan mendengarkan pendapat kita",  
                "pesan"    : "Senang banget bisa belajar tentang senator dari kakak"
            },
            {
                "nama"     : "Feryadi Yulius",
                "nim"      : "122450087",
                "umur"     : "20",
                "asal"     : "Padang",
                "alamat"   : "Belwis",
                "hobbi"    : "Sholat Dhuha",
                "sosmed"   : "@fer_yulius",
                "kesan"    : "Kakak selalu kasih masukan yang membangun, bikin kita lebih percaya diri!",  
                "pesan"    : "Terima kasih bang, semoga selalu sehat dan penuh semangat!"
            }, 
            {
                "nama"     : "Renisha Putri Giani",
                "nim"      : "122450079",
                "umur"     : "21",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Teluk Betung",
                "hobbi"    : "Baca Al-qur’an",
                "sosmed"   : "@fleurnsh",
                "kesan"    : "Kakak ini ramah dan membuat wawancara terasa asik serta penuh ilmu",  
                "pesan"    : "Terima kasih sudah buat diskusi jadi menyenangkan kak"
            },
            {
                "nama"     : "Claudhea Angeliani",
                "nim"      : "121450124",
                "umur"     : "21",
                "asal"     : "Lampung Timur",
                "alamat"   : "Lampung Timur",
                "hobbi"    : "Baca Jurnal",
                "sosmed"   : "@dylebee",
                "kesan"    : "Suka sama gaya kakak yang tegas tapi tetap friendly",  
                "pesan"    : "Pengen banget bisa belajar lebih banyak dari kakak"
            },
            {
                "nama"     : "Mirzan Yusuf Rabbani",
                "nim"      : "122450118",
                "umur"     : "20",
                "asal"     : "Jakarta",
                "alamat"   : "Korpri",
                "hobbi"    : "Main Kucing",
                "sosmed"   : "@myrrinn",
                "kesan"    : "Kakak sangat peduli sama kami, kita merasa diperhatikan!",  
                "pesan"    : "Semoga kakak terus jadi inspirasi bagi kita"
            },
            {
                "nama"     : "Dhea Amelia Putri",
                "nim"      : "122450004",
                "umur"     : "20",
                "asal"     : "Ogan Ilir",
                "alamat"   : "Natar",
                "hobbi"    : "Nyari Sinyal di Gedung F",
                "sosmed"   : "@_.dheamelia",
                "kesan"    : "Kakak bisa bikin topik yang serius jadi lebih menarik",  
                "pesan"    : "Senang bisa ngobrol sama kakak dan semangat selalu kak"
            },
            {
                "nama"     : "Muhammad Fahrul Aditya",
                "nim"      : "121450156",
                "umur"     : "22",
                "asal"     : "Surakarta",
                "alamat"   : "Sukarame",
                "hobbi"    : "Melukis",
                "sosmed"   : "@fhrul.pdf",
                "kesan"    : "Diskusi dengan kakak selalu bikin kita jadi lebih kritis dalam berpikir",  
                "pesan"    : "Kakak sangat inspiratif!"
            },
            {
                "nama"     : "Berliana Enda Putri",
                "nim"      : "122450065",
                "umur"     : "20",
                "asal"     : "Sumatra Barat",
                "alamat"   : "Way Huwi",
                "hobbi"    : "Baca Buku, Ngoding, Ibadah",
                "sosmed"   : "@berlyyanda",
                "kesan"    : "Kakak punya banyak pengalaman, jadi kita dapat insight yang berharga",  
                "pesan"    : "Semoga kakak terus semangat dan sehat selalu kak"
            },
            {
                "nama"     : "Jeremia Susanto",
                "nim"      : "122450022",
                "umur"     : "20",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Billabong, Gedong Air",
                "hobbi"    : "Suka Bengong",
                "sosmed"   : "@jeremia_s_",
                "kesan"    : "Abangnya ramah dan mudah diajak ngobrol, bikin kita nggak sungkan",  
                "pesan"    : "Terima kasih sudah bikin suasana jadi lebih nyaman bang, kita appreciate banget!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1WHyeA41zi0ZoHQVileQKKaLEGY-1xBHL",
            "https://drive.google.com/uc?export=view&id=1YEq-iuqGiEFd58N-ALDINq4iB52B8p0F",
        ]
        data_list = [
            {
                "nama"     : "Anissa Luthfi Alifia",
                "nim"      : "121450093",
                "umur"     : "22",
                "asal"     : "Lampung Tengah",
                "alamat"   : "Kos Putri Rahayu",
                "hobbi"    : "Bernyanyi",
                "sosmed"   : "@anissaluthfi_",
                "kesan"    : "Kakaknya ramah, mudah diajak ngobrol, saya suka sama cara kakak ngejelasin topik yang berat jadi ringan",  
                "pesan"    : "Kakak jadi role model buat kami soal keberanian menyuarakan pendapat dan semoga kakak terus sukses"
            },
            {
                "nama"     : "Rian Bintang Wijaya",
                "nim"      : "122450094",
                "umur"     : "20",
                "asal"     : "Palembang",
                "alamat"   : "Kota baru",
                "hobbi"    : "Tidur",
                "sosmed"   : "@bintangtwinkle",
                "kesan"    : "Kakak punya wawasan luas tentang senator, keren banget",  
                "pesan"    : "Senang banget bisa belajar tentang senator dari abang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def departemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mZk8AR87moMjJnO7R_shthrY2XqesBnw",
            "https://drive.google.com/uc?export=view&id=1ZCRPuYT8y2xlbLwWnm_geVy_QyhFYQrU",
            "https://drive.google.com/uc?export=view&id=1Sq18kDThGA6OFzSvkefYUVp2ffReFXfV",
            "https://drive.google.com/uc?export=view&id=1oFvBA92gpTnnNsi4U8rmsw1ZuLh6jKGG",
            "https://drive.google.com/uc?export=view&id=1S7U_xk_zae88YhaC-ToiMFbBl8z_BXZJ",
            "https://drive.google.com/uc?export=view&id=1eSjyhly9s0WGGsV6-WppyTJj6Wuh57a7",
            "https://drive.google.com/uc?export=view&id=1KvL0qwUhrn1Hx3DvsP3IfV3krX5GFdZV",
            "https://drive.google.com/uc?export=view&id=1F-LzppnygJOlkff6YWUAtxoIG6x812Wz",
            "https://drive.google.com/uc?export=view&id=18e4J0nyeYoXcR9gv6jsQArnvAu1eCwTp",
            "https://drive.google.com/uc?export=view&id=11TF5Yt9Hc3Pg6yFVqM6vl8jG-a8chH2r",
            "https://drive.google.com/uc?export=view&id=1Q8RwZS9Fr3Yib64R7aSOUT3r3k3nzHGJ",
            "https://drive.google.com/uc?export=view&id=1xDBeUZYdB1gCXlzzPXu89AAflzN2Dbbp",
            "https://drive.google.com/uc?export=view&id=1V0OC7han4V0YaKxOaMO0rirzOQNfXL21",
            "https://drive.google.com/uc?export=view&id=1Q8RwZS9Fr3Yib64R7aSOUT3r3k3nzHGJ",
            "https://drive.google.com/uc?export=view&id=1-AmWrAv-LC_aA_8RuNeD9qCsEAyIROnK",
            "https://drive.google.com/uc?export=view&id=1-OudVyuHuzWJOj7KQTeddIHfEmNjyiBH",
            "https://drive.google.com/uc?export=view&id=1nNMjPy7GFC3J-xdnKj1Q9GqXEQ2sl-Aa",
            "https://drive.google.com/uc?export=view&id=1VfMDzKgrEpn7IGJGi-I-DcY4-4w5elq9",
            "https://drive.google.com/uc?export=view&id=13cSwCdn-ItTlxVdj2DsYbXVduJrgiLnV",
            "https://drive.google.com/uc?export=view&id=1wT2iwhI5Ma69RWeh6ZsvQcdC29mwSzuv",
            "https://drive.google.com/uc?export=view&id=1c4pSo0wR2HCvCgcNu5OfI1ORZO2y-NDL",
            "https://drive.google.com/uc?export=view&id=1JskD46pQ-NG9t5zoHXbHGzBCPV_55eYB",
            "https://drive.google.com/uc?export=view&id=1oa7si9-lqdg44v-VDf1DzG-bxkIm4Kee",
        ]
        data_list = [
            {
                "nama"     : "Ericson Chandra Sihombing",
                "nim"      : "121450026",
                "umur"     : "21",
                "asal"     : "Bekasi",
                "alamat"   : "Khobam",
                "hobbi"    : "Travelling",
                "sosmed"   : "@ericsonchandra99",
                "kesan"    : "Abang ini tegas, public speakingnya bagus, selalu kasih motivasi buat kita lebih aktif dan berkembang",  
                "pesan"    : "Semangat selalu kuliahnya bang, Makasih bang sudah ngajarin pentingnya pengembangan diri!"
            },
            {
                "nama"     : "Elisabeth Claudia Simanjuntak",
                "nim"      : "122450123",
                "umur"     : "18",
                "asal"     : "Tangerang",
                "alamat"   : "Kemiling",
                "hobbi"    : "Bernafas",
                "sosmed"   : "@celisabethh_",
                "kesan"    : "Senang bisa belajar dari kakak, pembawaan kakak bikin suasana jadi lebih hidup!",  
                "pesan"    : "Semangat selalu kak, semoga kakak terus jadi inspirasi bagi kami semua"
            },
            {
                "nama"     : "Nisrina Nur Afifah",
                "nim"      : "122450052",
                "umur"     : "19",
                "asal"     : "Jawa Barat",
                "alamat"   : "Sukarame",
                "hobbi"    : "Marahin orang",
                "sosmed"   : "@afifahhnsrn",
                "kesan"    : "Kakak selalu paham cara menjelaskan, jadi kita lebih mudah paham",  
                "pesan"    : "Makasih kak, semoga kakak bisa terus membagikan pengalaman dan ilmunya!"
            },
            {
                "nama"     : "Allya Nurul Islami Pasha",
                "nim"      : "122450033",
                "umur"     : "20",
                "asal"     : "Sumatera Barat",
                "alamat"   : "Gg. Perwira Belwis",
                "hobbi"    : "Main",
                "sosmed"   : "@allyaislami_",
                "kesan"    : "Kakak ini baik, asik, serta tegas yang bikin kita semua jadi lebih disiplin",  
                "pesan"    : "Semangat selalu kuliahnya kakak dan terima kasih sudah memberikan bimbingan yang baik bagi kami"
            },
            {
                "nama"     : "Eksanty Febriana Sugma Islamiaty",
                "nim"      : "122450001",
                "umur"     : "20",
                "asal"     : "Jawa Barat",
                "alamat"   : "Metro",
                "hobbi"    : "Nyopet",
                "sosmed"   : "@eksantyfebriana",
                "kesan"    : "Kakak seru dan friendly, bikin suasana jadi asik pas ngobrol",  
                "pesan"    : "Semoga kakak terus sehat dan tetap bersemangat dalam setiap kegiatan!"
            },
            {
                "nama"     : "Farahanum Afifah Ardiansyah",
                "nim"      : "122450056",
                "umur"     : "20",
                "asal"     : "Padang",
                "alamat"   : "Sukarame",
                "hobbi"    : "Bengong",
                "sosmed"   : "@farahanumafifahh",
                "kesan"    : "Kakaknya bisa bikin sesi belajar jadi seru dan bermanfaat",  
                "pesan"    : "Terima kasih kak, sudah membuat wawancara jadi berkesan"
            },
            {
                "nama"     : "Ferdy Kevin Naibaho",
                "nim"      : "122450107",
                "umur"     : "19",
                "asal"     : "Medan",
                "alamat"   : "Jalan Pangeran Senopati Raya 18",
                "hobbi"    : "Baca Kitab Suci",
                "sosmed"   : "@ferdy_kevin",
                "kesan"    : "Abangngnya kalem dan punya cara unik dalam menjelaskan yang bikin kita tertarik!",  
                "pesan"    : "Semoga abangnya selalu semangat dan sehat"
            },
            {
                "nama"     : "M. Deriansyah Okutra",
                "nim"      : "122450101",
                "umur"     : "19",
                "asal"     : "Kayu Agung",
                "alamat"   : "Jalan Pagar Alam Kedaton",
                "hobbi"    : "Ngukur Jalan",
                "sosmed"   : "@dransyh_",
                "kesan"    : "Abangnya murah senyum, sering memberikan dukungan dan arahan!",  
                "pesan"    : "Terima kasih, bang! Semoga kita bisa terus menjalin komunikasi yang baik!"
            },
            {
                "nama"     : "Oktavia Nurwenda Puspita Sari",
                "nim"      : "122450041",
                "umur"     : "20",
                "asal"     : "Lampung Timur",
                "alamat"   : "Way Huwi",
                "hobbi"    : "Travelling",
                "sosmed"   : "@_oktavianrwnda_",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Sukses selalu kak, semoga kita bisa belajar lebih banyak lagi"
            },
            {
                "nama"     : "Deyvan Loxefal",
                "nim"      : "121450148",
                "umur"     : "21",
                "asal"     : "Duri, Riau ",
                "alamat"   : "Pulau Damar Kobam",
                "hobbi"    : "Belajar",
                "sosmed"   : "@depanloo",
                "kesan"    : "Abang ini baik, lucu, asik, dan ramah",  
                "pesan"    : "Semoga abangnya selalu sehat dan tetap semangat dalam studinya bang!"
            },
            {
                "nama"     : "Ibnu Farhan Al-Ghifari",
                "nim"      : " ",
                "umur"     : " ",
                "asal"     : " ",
                "alamat"   : " ",
                "hobbi"    : " ",
                "sosmed"   : "@-",
                "kesan"    : " ",  
                "pesan"    : " "
            },
            {
                "nama"     : "Johannes Krisjon Silitonga",
                "nim"      : "122450043",
                "umur"     : "19",
                "asal"     : "Tangerang",
                "alamat"   : "Jalan Lapas",
                "hobbi"    : "Asprak",
                "sosmed"   : "@johanneskrsjnnn",
                "kesan"    : "Abang ini baik, asik, dan tegas",  
                "pesan"    : "Makasih bang sudah support dan bantu kami buat berkembang"
            },
            {
                "nama"     : "Kemas Veriandra Ramadhan",
                "nim"      : "122450016",
                "umur"     : "19",
                "asal"     : "Bekasi",
                "alamat"   : "Golf Asri",
                "hobbi"    : "Ngetik print hello dunia",
                "sosmed"   : "@kemasverii",
                "kesan"    : "Abangnya keren, pemahamannya luas tentang codingan, dan baik",  
                "pesan"    : "Sukses selalu bang, terima kasih sudah jadi inspirasi buat kami!"
            },
            {
                "nama"     : "Leonard Andreas Napitupulu",
                "nim"      : " ",
                "umur"     : " ",
                "asal"     : " ",
                "alamat"   : " ",
                "hobbi"    : " ",
                "sosmed"   : "@-",
                "kesan"    : " ",  
                "pesan"    : " "
            },
            {
                "nama"     : "Presilia",
                "nim"      : "122450081",
                "umur"     : "20",
                "asal"     : "Bekasi",
                "alamat"   : "Kota Baru",
                "hobbi"    : "Dengerin The Adams",
                "sosmed"   : "@presiliamg",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Terima kasih atas semua saran dan penjelasannya kak, sukses selalu"
            },
            {
                "nama"     : "Rafa Aqilla Jungjunan",
                "nim"      : "122450142",
                "umur"     : "20",
                "asal"     : "Pekanbaru",
                "alamat"   : "Belwis",
                "hobbi"    : "Baca webtonn",
                "sosmed"   : "@rafaaqilla",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Harapannya kami bisa belajar lebih banyak dari kakak"
            },
            {
                "nama"     : "Sahid Maulana",
                "nim"      : "122450109",
                "umur"     : "21",
                "asal"     : "Kota Depok, Jabar",
                "alamat"   : "Jalan Airan Raya",
                "hobbi"    : "Dengerin juicy luicy",
                "sosmed"   : "@sahid_maul19",
                "kesan"    : "Abangnya baik, cara abangnya menjelaskan membuat kami lebih paham",  
                "pesan"    : "Terima kasih sudah berbagi ilmu, semangat dan sukses selalu kuliahnya bang!"
            },
            {
                "nama"     : "Vanessa Olivia Rose",
                "nim"      : "121450108",
                "umur"     : "20",
                "asal"     : "Jakarta",
                "alamat"   : "Perum Korpri",
                "hobbi"    : "Minum kopi, belajar, bikin deyvan senang",
                "sosmed"   : "@roselivnes__",
                "kesan"    : "Kakaknya asik dan keren banget main basketnya",  
                "pesan"    : "Semangat dan sukses selalu baik dalam lomba ataupun studinya kak!"
            },
            {
                "nama"     : "M. Farhan Athaulloh",
                "nim"      : "121450117",
                "umur"     : "21",
                "asal"     : "Lampung",
                "alamat"   : "Kota Baru",
                "hobbi"    : "Menolong",
                "sosmed"   : "@mfarhan.ath",
                "kesan"    : "Abangnya ramah, ngajarin kita buat selalu semangat dalam meningkatkan skill",  
                "pesan"    : "Abangnya inspiratif banget soal pentingnya skill dalam orba"
            },
            {
                "nama"     : "Gede Moena",
                "nim"      : "121450014",
                "umur"     : "21",
                "asal"     : "Bekasi",
                "alamat"   : "Korpri Raya",
                "hobbi"    : "Belajar, Game, Baca Komik",
                "sosmed"   : "@gedemoenaa",
                "kesan"    : "Abangnya sangat sabar dalam ngejelasin, bikin kita makin paham",  
                "pesan"    : "Semangat selalu dan makasih udah kasih insight yang bermanfaat bang"
            },
            {
                "nama"     : "Jaclin Alcavella",
                "nim"      : "122450015",
                "umur"     : "19",
                "asal"     : "Sumatera Selatan",
                "alamat"   : "Korpri",
                "hobbi"    : "Berenang",
                "sosmed"   : "@jaclinalcv",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Rafly Prabu Darmawan",
                "nim"      : "122450140",
                "umur"     : "20",
                "asal"     : "Bangka Belitung",
                "alamat"   : "Sukarame",
                "hobbi"    : "Main Game",
                "sosmed"   : "@raflyy_pd2684",
                "kesan"    : "Setiap kali abangnya bicara, ada banyak hal yang kami pelajari",  
                "pesan"    : "Makasih atas semua tips dan motivasinya bang, kita semua jadi lebih termotivasi!"
            },
            {
                "nama"     : "Syalaisha Andini Putriansyah",
                "nim"      : "122450111",
                "umur"     : "21",
                "asal"     : "Tangerang",
                "alamat"   : "Sukarame",
                "hobbi"    : "Membaca",
                "sosmed"   : "@syalaisha.i__",
                "kesan"    : "Kakaknya selalu memberi warna baru dalam setiap diskusi",  
                "pesan"    : "Semangat selalu kak, terima kasih sudah membuat kami belajar hal baru yang bermanfaat"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenPSDA()

elif menu == "Departemen MIKFES":
    def departemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1K3KuZNCNwDAJj1eiJX5HIbzwTZQEN5oB",
            "https://drive.google.com/uc?export=view&id=1Q6-jORSeK7FNRiFjhKq8m5xnQVt0eaOR",
            "https://drive.google.com/uc?export=view&id=1Q8RwZS9Fr3Yib64R7aSOUT3r3k3nzHGJ",
            "https://drive.google.com/uc?export=view&id=18lUZMFKCqZDsxTX7dXimkCciVZXz861v",
            "https://drive.google.com/uc?export=view&id=1Q8RwZS9Fr3Yib64R7aSOUT3r3k3nzHGJ",
            "https://drive.google.com/uc?export=view&id=1tG61x0sqWXf2yU69xoS-R27jkEGsfiDA",
            "https://drive.google.com/uc?export=view&id=1zRYsiAnvB5t0azZkDTgNwpC3n-YXJG3n",
            "https://drive.google.com/uc?export=view&id=1Q8RwZS9Fr3Yib64R7aSOUT3r3k3nzHGJ",
            "https://drive.google.com/uc?export=view&id=1eNnc_EyUA5nVclGULWGjojt7aiPht8kI",
            "https://drive.google.com/uc?export=view&id=1Fwl57uRAzz2Ar86UYBV9vpexuVyaLqRu",
            "https://drive.google.com/uc?export=view&id=14Z_fipgAzus8YtKVm_UQ_w8TWy4FthuH",
            "https://drive.google.com/uc?export=view&id=1tOHgKp16ptWT4G7aefaTt2STo6WlX5z-",
            "https://drive.google.com/uc?export=view&id=1zADuM3nfEu3XhO2ERdOP5cGF00tj0Sb7",
            "https://drive.google.com/uc?export=view&id=1RwWH6Hoelmke-g-lybUQsgKD0BATWCIb",
            "https://drive.google.com/uc?export=view&id=1Q8RwZS9Fr3Yib64R7aSOUT3r3k3nzHGJ",
            "https://drive.google.com/uc?export=view&id=1BQ4uGE-8wY-wuMurb20YYR7TGs7vjQ2l",
            "https://drive.google.com/uc?export=view&id=1J-Z6XqvSGjd0X6bZBNMa8egs3ZDKh2Xj",
            "https://drive.google.com/uc?export=view&id=1PgKtQ6NcWsx_TZC_keyMRxOKewicuYB2",
            "https://drive.google.com/uc?export=view&id=1wzs015fw4nPWe0ew5aDHPSvTQqoZm6EY",
            "https://drive.google.com/uc?export=view&id=1GEwiHh5EhHrHlG7btGr1XOiSWzkk11In",
        ]
        data_list = [
            {
                "nama"     : "Rafi Fadhlillah",
                "nim"      : "121450143",
                "umur"     : "21",
                "asal"     : "Lubuk Linggau, Sumatera Selatan",
                "alamat"   : "Jl. Nangka 4",
                "hobbi"    : "Olahraga",
                "sosmed"   : "@rafadhlillahh13",
                "kesan"    : "Abangnya pinter dan diskusi sama kakak seru banget! Banyak insight baru yang didapat",  
                "pesan"    : "Terima kasih bang! Semoga bisa terus belajar dari abangnya!"
            },
            {
                "nama"     : "Annisa Novantika",
                "nim"      : "121450005",
                "umur"     : "21",
                "asal"     : "Lampung Utara",
                "alamat"   : "Jl. Pulau Sebesi",
                "hobbi"    : "Memasak",
                "sosmed"   : "@anovavona",
                "kesan"    : "Kakak ini baik, ramah, dan penuh semangat",  
                "pesan"    : "Semoga sukses selalu dalam hal apapun kakak!"
            },
            {
                "nama"     : "Mujadid Choirus Surya",
                "nim"      : " ",
                "umur"     : " ",
                "asal"     : " ",
                "alamat"   : " ",
                "hobbi"    : " ",
                "sosmed"   : "@-",
                "kesan"    : " ",  
                "pesan"    : " "
            },
            {
                "nama"     : "Ahmad Sahidin Akbar",
                "nim"      : "122450044",
                "umur"     : "20",
                "asal"     : "Tulang Bawang",
                "alamat"   : "Sukarame",
                "hobbi"    : "Olahraga",
                "sosmed"   : "@sahid22__",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya dan jangan lupa tersenyum bang"
            },
            {
                "nama"     : "Fadhil Fitra Wijaya",
                "nim"      : " ",
                "umur"     : " ",
                "asal"     : " ",
                "alamat"   : " ",
                "hobbi"    : " ",
                "sosmed"   : "@-",
                "kesan"    : " ",  
                "pesan"    : " "
            },
            {
                "nama"     : "Muhammad Regi Abdi Putra Amanta",
                "nim"      : "122450031",
                "umur"     : "19",
                "asal"     : "Palembang",
                "alamat"   : "Jl. Permadi",
                "hobbi"    : "Ngasprak ADS",
                "sosmed"   : "@mregiiii_",
                "kesan"    : "Abang ini baik banget, ramah, dan setiap penjelasannya mudah dimengerti",  
                "pesan"    : "Semangat dan sukses selalu kuliahnya bang, harapannya bisa terus berbagi inspirasi!"
            },
            {
                "nama"     : "Syalaisha Andina Putriansyah",
                "nim"      : "122450121",
                "umur"     : "21",
                "asal"     : "Tangerang",
                "alamat"   : "Gg. Yudistira",
                "hobbi"    : "Review jurnal Bu Mika",
                "sosmed"   : "@dkselsd_31",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Tetap sehat selalu dan semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Natanael Oktavianus Partahan Sihombing",
                "nim"      : " ",
                "umur"     : " ",
                "asal"     : " ",
                "alamat"   : " ",
                "hobbi"    : " ",
                "sosmed"   : "@-",
                "kesan"    : " ",  
                "pesan"    : " "
            },
            {
                "nama"     : "Anwar Muslim",
                "nim"      : "122450117",
                "umur"     : "21",
                "asal"     : "Bukittinggi",
                "alamat"   : "Korpri",
                "hobbi"    : "ML (Machine Learning)",
                "sosmed"   : "@here.am.ai",
                "kesan"    : "Abang ini kalem, sabar, ramah, dan baik",  
                "pesan"    : "Semangat dan semoga selalu sabar ngajarin kita ya bang"
            },
            {
                "nama"     : "Deva Anjani Khayyuninafsyah",
                "nim"      : "122450014",
                "umur"     : "21",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Kemiling",
                "hobbi"    : "Resume Webinar",
                "sosmed"   : "@anjaniiidev",
                "kesan"    : "Kakak ini baik, asik banget diajak ngobrol, dan ramah",  
                "pesan"    : "Semoga bisa mendengar lebih banyak cerita yang keren dari kakak dan semangat terus kak"
            },
            {
                "nama"     : "Dinda Nababan",
                "nim"      : "122450120",
                "umur"     : "20",
                "asal"     : "Medan",
                "alamat"   : "Jl. Lapas",
                "hobbi"    : "Membaca jurnal Bu Mika",
                "sosmed"   : "@dindanababan_",
                "kesan"    : "Kakak ini asik, ramah, dan membuat diskusi di wawancara ini sangat menyenangkan",  
                "pesan"    : "Semoga bisa ngobrol lebih banyak lagi di lain kesempatan kak"
            },
            {
                "nama"     : "Marleta Cornelia Leander",
                "nim"      : "122450092",
                "umur"     : "20",
                "asal"     : "Depok",
                "alamat"   : "Gg. Nangka 3",
                "hobbi"    : "Review jurnal Bu Mika",
                "sosmed"   : "@marletacornelia",
                "kesan"    : "Kakak ini baik banget, asik, ramah, dan sangat perhatian",  
                "pesan"    : "Semangat selalu kuliahnya kakak, semoga bisa terus belajar dari pengalaman kakak"
            },
            {
                "nama"     : "Rut Junita Sari Siburian",
                "nim"      : "122450103",
                "umur"     : "20",
                "asal"     : "Kepulauan Riau",
                "alamat"   : "Gg. Nangka 3",
                "hobbi"    : "Menghitung akurasi",
                "sosmed"   : "@junitaa_0406",
                "kesan"    : "Kakaknya baik, cara kakak menjelaskan sangat menarik dan mudah dipahami!",  
                "pesan"    : "Semangat selalu kuliah dan menghitung akurasinya kakak!"
            },
            {
                "nama"     : "Syadza Puspadari Azhar",
                "nim"      : "122450072",
                "umur"     : "20",
                "asal"     : "Palembang",
                "alamat"   : "Belwis",
                "hobbi"    : "Membangkitkan bilangan",
                "sosmed"   : "@puspadrr",
                "kesan"    : "Kakak ini baik, asik, dan selalu memberikan feedback yang membangun",  
                "pesan"    : "Terima kasih kak, semangat selalu kuliahnya!"
            },
            {
                "nama"     : "Abdurrahman Al-atsary",
                "nim"      : " ",
                "umur"     : " ",
                "asal"     : " ",
                "alamat"   : " ",
                "hobbi"    : " ",
                "sosmed"   : "@-",
                "kesan"    : " ",  
                "pesan"    : " "
            },
            {
                "nama"     : "Aditya Rahman",
                "nim"      : "122450113",
                "umur"     : "20",
                "asal"     : "Metro",
                "alamat"   : "Korpri",
                "hobbi"    : "Ngoding wisata",
                "sosmed"   : "@rahm_adityaa",
                "kesan"    : "Abang ini kalem, baik, dan pengetahuannya sangat luas",  
                "pesan"    : "Tetap semangat ngoding wisata dan kuliahnya bang! sukses selalu"
            },
            {
                "nama"     : "Eggi satria",
                "nim"      : "122450032",
                "umur"     : "20",
                "asal"     : "Sukabumi",
                "alamat"   : "Korpri",
                "hobbi"    : "Ngoding wisata",
                "sosmed"   : "@_egistr",
                "kesan"    : "Abangnya asik, ramah, baik, dan pemahamannya sangat luas",  
                "pesan"    : "Semangat selalu kuliahnya bang! Semoga kita bisa berdiskusi lebih banyak di lain waktu!"
            },
            {
                "nama"     : "Febiya Jomy Pratiwi",
                "nim"      : "122450074",
                "umur"     : "20",
                "asal"     : "Tulang Bawang",
                "alamat"   : "Jl. Kelengkeng Raya",
                "hobbi"    : "Review jurnal",
                "sosmed"   : "@pratiwifebiya",
                "kesan"    : "Kakak ini baik, lucu, dan ramah",  
                "pesan"    : "Semangat dan sukses selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Happy Syahrul Ramadhan",
                "nim"      : "122450013",
                "umur"     : "20",
                "asal"     : "Lampung Timur",
                "alamat"   : "Karang Anyar",
                "hobbi"    : "Main game",
                "sosmed"   : "@sudo.syahrulramadhannn",
                "kesan"    : "Abang ini ramah dan baik",  
                "pesan"    : "Jangan lupa bahagia dan semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Randa Andriana Putra",
                "nim"      : "122450083",
                "umur"     : "21",
                "asal"     : "Banten",
                "alamat"   : "Sukarame ",
                "hobbi"    : "Tidur dan Berkembang",
                "sosmed"   : "@randaandriana_",
                "kesan"    : "Abang ini baik, asik, ramah, pengalaman abangnya sangat menginspirasi dan memotivasi",  
                "pesan"    : "Sukses selalu dan tetap sabar buat ngajarin kita ya bang"
            },
            {
                "nama"     : "Vita Anggraini",
                "nim"      : " ",
                "umur"     : " ",
                "asal"     : " ",
                "alamat"   : " ",
                "hobbi"    : " ",
                "sosmed"   : "@-",
                "kesan"    : " ",  
                "pesan"    : " "
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenMIKFES()

elif menu == "Departemen Eksternal":
    def departemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1uCAQbrKHDqzQw2mpR6lm2crKSJhQMdgV",
            "https://drive.google.com/uc?export=view&id=1aFs9pYlmCfFdUFtZ2jiG__eV-DVBJxfh",
            "https://drive.google.com/uc?export=view&id=1I2ncvNIrGT1NYlM53NuoBzMEVt-49xpQ",
            "https://drive.google.com/uc?export=view&id=1sheFq6DJSYalr25B2Q5QHdizTagqlR84",
            "https://drive.google.com/uc?export=view&id=1EKCqFpdPc8gl9Wk203HJBKmOCiODxUA9",
            "https://drive.google.com/uc?export=view&id=1Nq3Kb9ZfzLGALF6bMVj1lY9BjPuQ6kb2",
            "https://drive.google.com/uc?export=view&id=1C9FsZDQu6-5KsB1qFyYwcHJkQ-noZ8VJ",
            "https://drive.google.com/uc?export=view&id=1rwdi5SofPPIcqlLYttT2ROeIIooBQ_E3",
            "https://drive.google.com/uc?export=view&id=1eJQUXqRGdSTCdU78D64NATOVJ87HpBtv",
            "https://drive.google.com/uc?export=view&id=1a09jh1a0i5dj7A_HHt5zTTUyRN0BYPDT",
            "https://drive.google.com/uc?export=view&id=1SzTUK8E6C1eIg2I1RHVDnOcJz5y0eVqc",
            "https://drive.google.com/uc?export=view&id=1bfJu6_NLeaNonnYoVx19HTj9xrAsElQG",
            "https://drive.google.com/uc?export=view&id=1uCFWW6tC4qqxzyZvEcjERIT1N8JzUjwo",
            "https://drive.google.com/uc?export=view&id=1JytbetI76ZOLck8Xe-SIW22ag1Y0Xc1k",
            "https://drive.google.com/uc?export=view&id=1ViZRt1CMC_fabnpeFpYjIDSQEnlOSz8x",
            "https://drive.google.com/uc?export=view&id=1xZwkn2huZJrrCuyn_mzmHZEutfqezsjD",
            "https://drive.google.com/uc?export=view&id=1RjtWPEk64xHAGMdgIF5KNKNuIhKRk2zT",
            "https://drive.google.com/uc?export=view&id=1edeNIv1woILw75tqulJpEV5jc1uoF0AZ",
            "https://drive.google.com/uc?export=view&id=1n2oQxZlz39xLspcHKJ0PVDowZm9Xjre5",
            "https://drive.google.com/uc?export=view&id=19ADRvjZL_7GAVoCd3g0E_l1QZcQsBMGr",
        ]
        data_list = [
            {
                "nama"     : "Yogy Sa'e Tama",
                "nim"      : "121450041",
                "umur"     : "21",
                "asal"     : "Tangerang",
                "alamat"   : "Jatimulyo",
                "hobbi"    : "Bangun pagi",
                "sosmed"   : "@yogyyyyyyy",
                "kesan"    : "Abangnya tegas namun punya vibe yang asik banget",  
                "pesan"    : "Tetap semangat bang! Sukses selalu, semoga bisa terus berkarya dan jadi teladan!"
            },
            {
                "nama"     : "Ramadhita Atifa Hendri",
                "nim"      : "121450131",
                "umur"     : "21",
                "asal"     : "Bandar Lampung",
                "alamat"   : "TVRI",
                "hobbi"    : "Jalan-jalan",
                "sosmed"   : "@ramadhitatifa",
                "kesan"    : "Kakak ini baik, ramah yang bikin ngobrol jadi enak dan informatif",  
                "pesan"    : "Harapan terbaik buat kakak, semoga semua rencana kakak tercapai!"
            },
            {
                "nama"     : "Nazwa Nabilla",
                "nim"      : "121450122",
                "umur"     : "21",
                "asal"     : "Lampung",
                "alamat"   : "Way Kandis",
                "hobbi"    : "Belajar",
                "sosmed"   : "@nazwanbilla",
                "kesan"    : "Kakak seru banget ngejelasin, bikin wawancara jadi hidup",  
                "pesan"    : "Semangat dan semoga sukses selalu dalam belajarnya kak!"
            },
            {
                "nama"     : "Bastian Heskia Silaban",
                "nim"      : "122450130",
                "umur"     : "21",
                "asal"     : "Batam, Kep. Riau",
                "alamat"   : "Belwis",
                "hobbi"    : "Main game",
                "sosmed"   : "@bastiansilaban_",
                "kesan"    : "Abang ini baik, open-minded, dan ramah",  
                "pesan"    : "Semangat bang, semoga terus diberi kemudahan dalam perjalanan kuliah dan kegiatan lainnya!"
            },
            {
                "nama"     : "Dea Mutia Risani",
                "nim"      : "122450099",
                "umur"     : "20",
                "asal"     : "Sumatera Barat",
                "alamat"   : "Korpri",
                "hobbi"    : "Dengerin musik",
                "sosmed"   : "@deaa.rsn",
                "kesan"    : "Kakak ini asik, ramah, dan seru banget ngejelasinnya",  
                "pesan"    : "Sukses dan semangat selalu kak! Semoga bisa terus jadi inspirasi buat kita semua!"
            },
            {
                "nama"     : "Esteria Rohanauli Sidauruk",
                "nim"      : "122450025",
                "umur"     : "19",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Bandar Lampung",
                "hobbi"    : "Kirim BC-an",
                "sosmed"   : "@esteriars",
                "kesan"    : "Kakak ini baik, asik, dan  selalu ramah",  
                "pesan"    : "Terima kasih atas waktunya kak, semoga kakak bisa makin sukses dan bahagia!"
            },
            {
                "nama"     : "Natasya Ega Lina Marbun",
                "nim"      : "122450024",
                "umur"     : "19",
                "asal"     : "Sumatera Utara",
                "alamat"   : "Pemda",
                "hobbi"    : "Jadi humas",
                "sosmed"   : "@nateee__15",
                "kesan"    : "Kakak ini kalem, ramah, dan baik",  
                "pesan"    : "Tetap semangat kak! sukses selalu, semoga bisa terus berkarya"
            },
            {
                "nama"     : "Novelia Adinda",
                "nim"      : "122450104",
                "umur"     : "20",
                "asal"     : "Saburai",
                "alamat"   : "Belwis",
                "hobbi"    : "Tidur",
                "sosmed"   : "@nvliaadinda",
                "kesan"    : "Kakak ini baik, ramah, dan soft spoken yang bikin ngobrol jadi nyaman",  
                "pesan"    : "Semangat terus, semoga semua rencana kedepan kakak tercapai"
            },
            {
                "nama"     : "Ratu Keisha Jasmine Deanova",
                "nim"      : "122450106",
                "umur"     : "20",
                "asal"     : "Bogor",
                "alamat"   : "Way Kandis",
                "hobbi"    : "Pulang malam",
                "sosmed"   : "@jasminednva",
                "kesan"    : "Kakak ini ramah dan positive vibes",  
                "pesan"    : "Semoga semua pengalaman berharga kakak di sini jadi bekal hebat buat ke depannya!"
            },
            {
                "nama"     : "Tobias David Manogari",
                "nim"      : "122450091",
                "umur"     : "20",
                "asal"     : "Jakarta Selatan",
                "alamat"   : "Pemda",
                "hobbi"    : "Berkebun",
                "sosmed"   : "@tobiassiagian",
                "kesan"    : "Abangnya kelihatan tegas ternyata asik dan baik",  
                "pesan"    : "Abangnya keren! Semoga terus semangat dan sukses di semua bidang bang!"
            },
            {
                "nama"     : "Yohana Manik",
                "nim"      : "122450126",
                "umur"     : "20",
                "asal"     : "Sumatera Utara",
                "alamat"   : "Belwis",
                "hobbi"    : "Menimba ilmu",
                "sosmed"   : "@yo_anamnk",
                "kesan"    : "Kakak ini keren dan punya perspektif yang luas",  
                "pesan"    : "Semangat selalu kuliahnya kakak dan makasih atas ilmu yang bermanfaatnya kak"
            },
            {
                "nama"     : "Rizki Adrian Bennovry",
                "nim"      : "121450073",
                "umur"     : "21",
                "asal"     : "Bekasi",
                "alamat"   : "TVRI",
                "hobbi"    : "Bikin portofolio",
                "sosmed"   : "@rzkdrnnn",
                "kesan"    : "Abangnya ternyata humble dan asik banget, bikin sesi wawancara jadi enjoy",  
                "pesan"    : "Sukses selalu bang! Semoga langkah apapun selalu dilancarkan bang"
            },
            {
                "nama"     : "Arafi Ramadhan Maulana",
                "nim"      : "122450002",
                "umur"     : "20",
                "asal"     : "Depok",
                "alamat"   : "Way Huwi",
                "hobbi"    : "Imam TVRI",
                "sosmed"   : "@arafiramadhanmaulana",
                "kesan"    : "Abang ini humble, ramah, dan komunikatif",  
                "pesan"    : "Semoga abangnya selalu dikelilingi hal-hal baik dan mencapai semua cita-citanya!"
            },
            {
                "nama"     : "Asa Doa Uyi",
                "nim"      : "122450005",
                "umur"     : "20",
                "asal"     : "Muara Enim",
                "alamat"   : "Korpri",
                "hobbi"    : "Nyuci baju",
                "sosmed"   : "@u_yippy",
                "kesan"    : "Kakak ini ramah, baik, humble banget bikin nyaman untuk ngobrol",  
                "pesan"    : "Semoga kakak selalu diberi kesehatan dan kekuatan buat jalani semua kesibukan!"
            },
            {
                "nama"     : "Chalifia Wananda",
                "nim"      : "122450076",
                "umur"     : "20",
                "asal"     : "Padang",
                "alamat"   : "Sukarame",
                "hobbi"    : "Q-Time",
                "sosmed"   : "@chlfawww",
                "kesan"    : "Kakak ini lucu, baik, dan ramah banget",  
                "pesan"    : "Harapan terbaik buat kakak! Semoga selalu sukses dan terus menginspirasi."
            },
            {
                "nama"     : "Irvan Alfaritzi",
                "nim"      : "122450093",
                "umur"     : "21",
                "asal"     : "Sumatera Barat",
                "alamat"   : "Sukarame",
                "hobbi"    : "Nonton Youtube, Main Game",
                "sosmed"   : "@alfaritziirvan",
                "kesan"    : "Abang ini ramah, baik, dan cara menjawabnya saat wawancara santai tapi tetap fokus.",  
                "pesan"    : "Tetap jadi inspirasi bang! Semoga ilmu yang abang bagi makin luas manfaatnya."
            },
            {
                "nama"     : "Izza Lutfia",
                "nim"      : "122450090",
                "umur"     : "20",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Teluk Betung",
                "hobbi"    : "Main Rubik",
                "sosmed"   : "@izzalutfiaa",
                "kesan"    : "Kakak ini baik, asik, ramah, dan ceria banget",  
                "pesan"    : "Bahagia selalu kak, semoga ilmu yang kakak bagi makin luas manfaatnya."
            },
            {
                "nama"     : "Khaalishah Zuhrah Alyaa Vanefi",
                "nim"      : "122450034",
                "umur"     : "20",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Rajabasa",
                "hobbi"    : "Jadi daplok kelompok 1",
                "sosmed"   : "@alyaavanefi",
                "kesan"    : "Kakaknya lucu, supportif, sabar dan baik banget",  
                "pesan"    : "Jangan cape buat ngajarin dan ngingetin kita ya kak, semangat dan bahagia selalu kakak!"
            },
            {
                "nama"     : "Raid Muhammad Naufal",
                "nim"      : "122450027",
                "umur"     : "20",
                "asal"     : "Lampung Tengah",
                "alamat"   : "Sukarame",
                "hobbi"    : "Telat",
                "sosmed"   : "@rayths_",
                "kesan"    : "Abang ini ramah, asik, bikin ngobrol jadi enak dan informatif",  
                "pesan"    : "Harapannya, kakak makin sukses dan tetap semangat berbagi ilmu ke kita"
            },
            {
                "nama"     : "Tria Yunanni",
                "nim"      : "122450062",
                "umur"     : "20",
                "asal"     : "Way Kanan",
                "alamat"   : "Sukarame",
                "hobbi"    : "Membaca chat",
                "sosmed"   : "@tria_y062",
                "kesan"    : "Kakak ini asik, ceria, dan punya energi positif yang bikin kita semangat",  
                "pesan"    : "Semoga kuliah dan kegiatan kakak lancar semua! Terima kasih sudah berbagi kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenEksternal()

elif menu == "Departemen Internal":
    def departemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1P60mNMJYzOQLBYk68cw4fXYDSAAZ-5VD",
            "https://drive.google.com/uc?export=view&id=1V8MT88FGVYA9sLDJPfFHo0KhMY6IeXCa",
            "https://drive.google.com/uc?export=view&id=1nS5SQ38kmPNO7JvY1hPOZ7GHlN03oIky",
            "https://drive.google.com/uc?export=view&id=15pw4tjh7iTKvtNj2tnTJXa-0UUw1Ohb1",
            "https://drive.google.com/uc?export=view&id=1RLDiKOoXpdRCTDWlq-4WYFst4mdaw_5k",
            "https://drive.google.com/uc?export=view&id=1xFXxf32OvypLA7THPMlKrVS4sePLUoL5",
            "https://drive.google.com/uc?export=view&id=1q9Elu-RThlPBI7Q2_0xKNyx8-k_5z6Qm",
            "https://drive.google.com/uc?export=view&id=1QmOSpuS5ryzhQaKLsrlXh3FDIY7I_D-i",
            "https://drive.google.com/uc?export=view&id=1Q8RwZS9Fr3Yib64R7aSOUT3r3k3nzHGJ",
            "https://drive.google.com/uc?export=view&id=1hjRKKs-VLe_rQ77MUHfKDYr7ljav2-5e",
            "https://drive.google.com/uc?export=view&id=1TQ06Dga7wHjB2Tnv2Bl81R5bHxPrlRhz",
            "https://drive.google.com/uc?export=view&id=1BkfiRYwIpqKfD4-NEUfj1azuRB88lftL",
            "https://drive.google.com/uc?export=view&id=1gfZn1Hk310AHRbdG-51sTg8hjYpJBXTe",
            "https://drive.google.com/uc?export=view&id=17wkrmtwO0wV-LXt3UKbre5INhb5jGt2d",
        ]
        data_list = [
            {
                "nama"     : "Dimas Rizky Ramadhani",
                "nim"      : "121450027",
                "umur"     : "20",
                "asal"     : "Pamulang, Tangerang Selatan",
                "alamat"   : "Way Kandis Kobam",
                "hobbi"    : "Manjat tower sutet",
                "sosmed"   : "@dimzrky_",
                "kesan"    : "Abang ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Catherine Firdhasari Maulina Sinaga",
                "nim"      : "121450072",
                "umur"     : "20",
                "asal"     : "Sumatera Utara",
                "alamat"   : "Airan",
                "hobbi"    : "Baca novel",
                "sosmed"   : "@catherine.sinagaa",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "M. Akbar Resdika",
                "nim"      : "121450066",
                "umur"     : "20",
                "asal"     : "Lampung Barat",
                "alamat"   : "Labuhan Dalam",
                "hobbi"    : "Memelihara Dino",
                "sosmed"   : "@akbar_resdika",
                "kesan"    : "Abang ini baik, lucu, dan banyak dapat insight baru tentang pentingnya keharmonisasian",  
                "pesan"    : "Terima kasih bang, semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Rani Puspita sari",
                "nim"      : "122450030",
                "umur"     : "21",
                "asal"     : "Metro",
                "alamat"   : "Rajabasa",
                "hobbi"    : "Mengaji",
                "sosmed"   : "@rannipu",
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
                "sosmed"   : "@rendraepr",
                "kesan"    : "Seru banget ngobrol dengan abangnya, punya banyak insight yang menginspirasi",  
                "pesan"    : "Sukses selalu bang! Semoga dapat bisa bertanya banyak lagi di lain waktu!"
            },
            {
                "nama"     : "Salwa Farhanatussaidah",
                "nim"      : "122450055",
                "umur"     : "20",
                "asal"     : "Pesawaran",
                "alamat"   : "Airan raya",
                "hobbi"    : "Ngeliat cogan",
                "sosmed"   : "@slwafhn_694",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Ari Sigit",
                "nim"      : "121450069",
                "umur"     : "23",
                "asal"     : "Lampung Barat",
                "alamat"   : "Labuhan Ratu",
                "hobbi"    : "Main Futsal",
                "sosmed"   : "@ari.sigit17",
                "kesan"    : "Abang ini kalem, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
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
                "nama"     : "Dearni Monica Br Manik",
                "nim"      : "122450075",
                "umur"     : "21",
                "asal"     : "Tangerang",
                "alamat"   : "Jati Mulyo",
                "hobbi"    : "Bangun Pagi",
                "sosmed"   : "@arnimnk",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Meira Listyaningrum",
                "nim"      : "122450011",
                "umur"     : "20",
                "asal"     : "Pesawaran",
                "alamat"   : "Airan Raya",
                "hobbi"    : "Menghalu",
                "sosmed"   : "@meiralsty_",
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
                "sosmed"   : "@rexanderr",
                "kesan"    : "Abang ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Renta Siahaan",
                "nim"      : "122450070",
                "umur"     : "21",
                "asal"     : "Sumatera Utara",
                "alamat"   : "Gerbang Barat",
                "hobbi"    : "Mancing",
                "sosmed"   : "@renta.shn",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
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
                "nama"     : "Josua Alfa Viando Panggabean",
                "nim"      : "121450061",
                "umur"     : "21",
                "asal"     : "Pematang Siantar",
                "alamat"   : "Bia Kost",
                "hobbi"    : "Ngawinin cupang",
                "sosmed"   : "@josuapanggabean16_",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenInternal()

elif menu == "Departemen SSD":
    def departemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RogDzeGNfVQNCk4d2x2c1yLes2oXAteQ",
            "https://drive.google.com/uc?export=view&id=1nNr9nqVU9NJHuA3SCS5X1HYWMV8Z5VqC",
            "https://drive.google.com/uc?export=view&id=1rRlk5sMRpaS_QapQHICdyTA0ioxTo0Ld",
            "https://drive.google.com/uc?export=view&id=1ggarDPW_kKKTY9HFbxXhoqh2WJoPoi_R",
            "https://drive.google.com/uc?export=view&id=1zvIO0u2HPGOCpJaMneB2qtW7rMpQp9no",
            "https://drive.google.com/uc?export=view&id=1M7P7TEPjzCaUc0JClwElTi70uA-ML8pn",
            "https://drive.google.com/uc?export=view&id=1B6aOjB38XAs2613lLJ6IdHW3LGTGV8xR",
            "https://drive.google.com/uc?export=view&id=11F9XyUKbPNcZUUYXy7BQbS_WzVf7qdVu",
            "https://drive.google.com/uc?export=view&id=1mQfLsCW5Bf_V5VdOJ3pXedTsDhhgKq5a",
            "https://drive.google.com/uc?export=view&id=1jNuYdZONQChIbEU6BqI3EyysKuAz2-D_",
            "https://drive.google.com/uc?export=view&id=1lBIlSd3UJj7d_cw9Xi27AQdQFV8OvAkJ",
        ]
        data_list = [
            {
                "nama"     : "Andrian Agustinus Lumban Gaol",
                "nim"      : "121450090",
                "umur"     : "21",
                "asal"     : "Panjibako",
                "alamat"   : "Jl. Bel",
                "hobbi"    : "Mencari Uang",
                "sosmed"   : "@andrianlgaol",
                "kesan"    : "Abang ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Adisty Syawalda Ariyanto",
                "nim"      : "121450136",
                "umur"     : "22",
                "asal"     : "Metro",
                "alamat"   : "Sukarame",
                "hobbi"    : "Nonton film",
                "sosmed"   : "@adistysa_",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Nabila Azhari",
                "nim"      : "121450029",
                "umur"     : "21",
                "asal"     : "Simalungun, Sumut",
                "alamat"   : "Airan",
                "hobbi"    : "Hitung uang",
                "sosmed"   : "@zhjung_",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Ahmad Rizqi",
                "nim"      : "122450138",
                "umur"     : "20",
                "asal"     : "Bukittinggi",
                "alamat"   : "Airan 1",
                "hobbi"    : "Badminton",
                "sosmed"   : "@ahmad.riz45",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Danang Hilal Kurniawan",
                "nim"      : "122450085",
                "umur"     : "21",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Airan",
                "hobbi"    : "Nyuruh-nyuruh",
                "sosmed"   : "@dananghk_",
                "kesan"    : "Abang ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Farrel Julio Akbar",
                "nim"      : "122450110",
                "umur"     : "20",
                "asal"     : "Bogor",
                "alamat"   : "Lapas",
                "hobbi"    : "Apa aja",
                "sosmed"   : "@farrel__julio",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Tessa Kania Sagala",
                "nim"      : "122450040",
                "umur"     : "20",
                "asal"     : "Simalungun, Sumut",
                "alamat"   : "Pemda",
                "hobbi"    : "Suka nulis",
                "sosmed"   : "@tesakanias",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Nabilah Andika Fitriati",
                "nim"      : "121450139",
                "umur"     : "20",
                "asal"     : "Kedaton",
                "alamat"   : "Kedaton",
                "hobbi"    : "Tidur",
                "sosmed"   : "@nabilahanftr",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Alvia Asrinda Br.Ginting",
                "nim"      : "122450077",
                "umur"     : "20",
                "asal"     : "Binjai",
                "alamat"   : "Korpri",
                "hobbi"    : "Nonton windah",
                "sosmed"   : "@alviagnting",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Dhafin Razaqa Luthfi",
                "nim"      : "122450133",
                "umur"     : "20",
                "asal"     : "Balam",
                "alamat"   : "Jalan Nangka 1",
                "hobbi"    : "Tidur",
                "sosmed"   : "@dhafinrzqa13",
                "kesan"    : "Abang ini ramah dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Elia Meylani Simanjuntak",
                "nim"      : "122450026",
                "umur"     : "20",
                "asal"     : "Bekasi",
                "alamat"   : "Korpri",
                "hobbi"    : "Badminton",
                "sosmed"   : "@meylanielia",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenSSD()

elif menu == "Departemen MEDKRAF":
    def departemenMEDKRAF():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1DioFBBswRIesm62ZPouWIwePFMudjlBQ",
            "https://drive.google.com/uc?export=view&id=11fa60-8TnU72WNvKoIybbzBbzQrR6z6H",
            "https://drive.google.com/uc?export=view&id=1GEwdI1288EDUx8kWyqrvrG3icNSfxP6A",
            "https://drive.google.com/uc?export=view&id=1NyQ27NXYOQ9x6MZpcs8d88S9NRQ6nxK6",
            "https://drive.google.com/uc?export=view&id=1MPLF73_Rf-1gTmza_FBAhIFYT1Y0QgNs",
            "https://drive.google.com/uc?export=view&id=1m7yedA2BjPuZxBQBQd7jwpErhOgNbGcl",
            "https://drive.google.com/uc?export=view&id=1z_EnvdMI6TmEdQyo31LG_lZTrT31k4b5",
            "https://drive.google.com/uc?export=view&id=1eY2n2K11X39EYrLf0-xacYGrrY0XIR6c",
            "https://drive.google.com/uc?export=view&id=1vfVMcS22rbhLB_9IlPRd-vZacpvGBhSU",
            "https://drive.google.com/uc?export=view&id=16TObeVb3-BP7ob9zRBGTJsluOShl8wEj",
            "https://drive.google.com/uc?export=view&id=14Xuo-y5X7IkD_xFfloeLbBQOkDEwCXY5",
            "https://drive.google.com/uc?export=view&id=1lA2MzVQL_lluhnHZp-EzMa9IbYfZnhU7",
            "https://drive.google.com/uc?export=view&id=1hg8dyTwTz2h5jTIGiW7eNxteJNS6njhs",
            "https://drive.google.com/uc?export=view&id=1no9ehwXhm9FOjcJvQuCZ6IJOKDFLeMQm",
            "https://drive.google.com/uc?export=view&id=119jMZIRNePbh6bezOZVvcPvshfF-RHmJ",
            "https://drive.google.com/uc?export=view&id=1Z7YjIEugC3FU6ZAYb8607kfUZhdiLP6c",
            "https://drive.google.com/uc?export=view&id=13Kb0SR-PcyN9XIUkeGBU26jkJQXHDIMW",
            "https://drive.google.com/uc?export=view&id=10UC9fbCEBpPUXT-DNx-xajWz5WXd9jZh",
            "https://drive.google.com/uc?export=view&id=18xDAWE1lapN1R4IKKVWduJkyc0HE6WWW",
        ]
        data_list = [
            {
                "nama"     : "Wahyudiyanto",
                "nim"      : "121450040",
                "umur"     : "22",
                "asal"     : "Makassar, Sulsel",
                "alamat"   : "Sukarame",
                "hobbi"    : "Nonton",
                "sosmed"   : "@-",
                "kesan"    : "Abang ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Elok Fiola",
                "nim"      : "122450051",
                "umur"     : "19",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Bandar Lampung",
                "hobbi"    : "Editing",
                "sosmed"   : "@elokfiola",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Arsyiah Azahra",
                "nim"      : "121450035",
                "umur"     : "21",
                "asal"     : "Balam",
                "alamat"   : "Tanjung Senang",
                "hobbi"    : "Nugas",
                "sosmed"   : "@arsyiah._",
                "kesan"    : "Kakak ini asik, ramah, dan public speakingnya bagus",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Cintya Bella",
                "nim"      : "122450066",
                "umur"     : "20",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Teluk",
                "hobbi"    : "Ngegym",
                "sosmed"   : "@cintyabella28",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Eka Fidiya Putri",
                "nim"      : "122450045",
                "umur"     : "20",
                "asal"     : "Natar",
                "alamat"   : "Natar",
                "hobbi"    : "Menyibukkan diri",
                "sosmed"   : "@ekafdyaptri",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Najla Juwairia",
                "nim"      : "122450037",
                "umur"     : "19",
                "asal"     : "Sumatera Utara",
                "alamat"   : "Airan",
                "hobbi"    : "Nulis, baca, fangirling",
                "sosmed"   : "@nanana.minjoe",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Patricia Leondrea Diajeng Putri",
                "nim"      : "122450050",
                "umur"     : "20",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Jatimulyo",
                "hobbi"    : "Nonton film",
                "sosmed"   : "@patriciadiajeng",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Rahma Neliyana",
                "nim"      : "122450036",
                "umur"     : "20",
                "asal"     : "Lampung",
                "alamat"   : "Sukarame",
                "hobbi"    : "Baca Coding",
                "sosmed"   : "@rahmanellyana",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Try Yani Rizki Nur Rohmah",
                "nim"      : "122450020",
                "umur"     : "20",
                "asal"     : "Lampung Barat",
                "alamat"   : "Korpri",
                "hobbi"    : "Bernyanyi dan menonton",
                "sosmed"   : "@tryyaniciaaa",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Muhammad Kaisar Firdaus",
                "nim"      : "121450135",
                "umur"     : "21",
                "asal"     : "Pesawaran",
                "alamat"   : "Pulau Damar",
                "hobbi"    : "Lagi Nyari",
                "sosmed"   : "@dino_kiper",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Dwi Ratna Anggraeni",
                "nim"      : "122450008",
                "umur"     : "20",
                "asal"     : "Jambi",
                "alamat"   : "Jalan Durian 5 Pemda",
                "hobbi"    : "Membaca",
                "sosmed"   : "@dwiratnn_",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Gymnastiar Al Khoarizmy",
                "nim"      : "122450096",
                "umur"     : "20 ",
                "asal"     : "Serang",
                "alamat"   : "Lapangan Golf UIN",
                "hobbi"    : "Baca Komik  ",
                "sosmed"   : "@jimnn.as",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Nasywa Nur Afifah",
                "nim"      : "122450125",
                "umur"     : "20",
                "asal"     : "Bekasi",
                "alamat"   : "Jalan Durian 1 Pemda",
                "hobbi"    : "Nonton Drakor",
                "sosmed"   : "@nsywanaf",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Priska Silvia Ferantiana",
                "nim"      : "122450053",
                "umur"     : "20",
                "asal"     : "Palembang",
                "alamat"   : "Jalan Nangka 2",
                "hobbi"    : "Baca Novel yang Bikin Nangis",
                "sosmed"   : "@prskslv",
                "kesan"    : "Kakak ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
            {
                "nama"     : "Muhammad Arsal Ranjana Utama",
                "nim"      : "121450111",
                "umur"     : "21",
                "asal"     : "Depok",
                "alamat"   : "Nangka 3",
                "hobbi"    : "Ngoding",
                "sosmed"   : "@arsal.utama",
                "kesan"    : "Abang ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Abit Ahmad Oktarian",
                "nim"      : "122450042",
                "umur"     : "19",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Rajabasa Labuhan dalam",
                "hobbi"    : "Ngoding, gaming",
                "sosmed"   : "@abitahmad",
                "kesan"    : "Abangnya lucu, baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Akmal Faiz Abdillah",
                "nim"      : "122450114",
                "umur"     : "20",
                "asal"     : "Bandar Lampung",
                "alamat"   : "Perumahan Griya Sukarame",
                "hobbi"    : "Main HP",
                "sosmed"   : "@_akmal.faiz",
                "kesan"    : "Abang ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Hermawan Manurung",
                "nim"      : "122450069",
                "umur"     : "20",
                "asal"     : "Bogor",
                "alamat"   : "Wisma Hana Hani",
                "hobbi"    : "Bengong/ Membaca buku",
                "sosmed"   : "@hermawan.mnrng",
                "kesan"    : "Abang ini baik, asik, dan ramah",  
                "pesan"    : "Semangat selalu kuliahnya bang!"
            },
            {
                "nama"     : "Khusnun Nisa",
                "nim"      : "122450078",
                "umur"     : "20",
                "asal"     : "Lampung Selatan",
                "alamat"   : "Belwis",
                "hobbi"    : "Mengerjakan tugas",
                "sosmed"   : "@khusnun_nisa335",
                "kesan"    : "Kakak ini asik, ramah, dan baik",  
                "pesan"    : "Semangat selalu kuliahnya kakak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenMEDKRAF()
# Tambahkan menu lainnya sesuai kebutuhan
