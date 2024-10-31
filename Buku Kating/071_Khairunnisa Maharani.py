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
            "https://drive.google.com/uc?export=view&id=14DhRtvnb5UcEIAGqFe-d7fLat_5u1H-r",
            "https://drive.google.com/uc?export=view&id=14GrbyWyqXY1wS4rDB6QBGc98TbGVxcoR",
            "https://drive.google.com/uc?export=view&id=14MrjnZDcKJFstNX6oGblGcXWopC1KiiE",
            "https://drive.google.com/uc?export=view&id=14MJotgMAMP03E1UsfWdPLudVSmQ98d-V",
            "https://drive.google.com/uc?export=view&id=14JAB81cih6GiA3HHeqffIAWZEzdpfhev",
            "https://drive.google.com/uc?export=view&id=1mOdDVDcEBgXuLXBc8LKnCpfzYvlyXWhm",
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
                "kesan": "Kakak ini enak diajak diskusi, selalu terbuka kalau saya butuh bantuan.",  
                "pesan":"Semoga kakak semakin berprestasi dan sukses di masa depan. Semangat kuliahnya!"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450077",
                "umur": "21",
                "asal":"Bukit Kemuning",
                "alamat": "Pawen 2 Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni21",
                "kesan": "Sangat ramah dan selalu siap membantu, kakak ini nggak pelit ilmu.",  
                "pesan":"Terus semangat ya, Kak! Semoga kuliahnya lancar dan sukses selalu!"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kotabaru",
                "hobbi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakaknya baik banget dan selalu memberikan penjelasan yang mudah dimengerti.",  
                "pesan":"Semoga kakak bisa mencapai semua cita-citanya! Tetap semangat dan jangan menyerah!"# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak ini menyenangkan, selalu bisa diajak ngobrol santai tapi ilmunya banyak.",  
                "pesan":"Semangat terus, Kak! Semoga sukses dalam setiap langkahmu di kampus dan di luar!"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin  bang Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Sikap kakak yang selalu sabar dan perhatian bikin saya nyaman bertanya.",  
                "pesan":"Jaga kesehatan dan semangat terus ya, Kak! Semoga sukses dalam studinya!"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kotabaru",
                "hobbi": "Dengerin  bang Pandra Gitaran",
                "sosmed": "@nadillaadr26",
                "kesan": "Kakak ini sangat pengertian, selalu mendengarkan dan memberikan masukan yang bijak.",  
                "pesan":"Semoga kuliahnya lancar, kakak! Terus berjuang dan gapai mimpimu!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=105brwiz2HlVf_5oztIM3rGZs3-StaAar", #1
            "https://drive.google.com/uc?export=view&id=1-mji1Sn-u6vll__yhV3uWOVsameUh3v3", #2
            "https://drive.google.com/uc?export=view&id=1-m--bsigFmXuCQNr6jJ373W_HUHeLYnf", #3
            "https://drive.google.com/uc?export=view&id=106mAjV6vabED1EhNMdBBlQbUZwpTeQ6y", #4
            "https://drive.google.com/uc?export=view&id=1-hCdTwCzWXqS_YQ-3NYHoUWKzoou8H1F", #5
            "https://drive.google.com/uc?export=view&id=103w9a1gtY8F2vQ9SrMxuXxFTFsc7y0-b", #6 
            "https://drive.google.com/uc?export=view&id=1-l6jgcfnmF1Yh5yXd48qZtdy-_wcRKhZ", #7
            "https://drive.google.com/uc?export=view&id=1_VgaxKZE7607r1MhUJvbL8704B57zYYv", #8
            "https://drive.google.com/uc?export=view&id=1e7uGwfW8aCgJbl5ZjgMRCxRay4qgVtim", #9
            "https://drive.google.com/uc?export=view&id=1-l6jgcfnmF1Yh5yXd48qZtdy-_wcRKhZ", #10
            "https://drive.google.com/uc?export=view&id=1-tzj7nR8eFe4L1FO-fuIDNC993Hejxqh", #11
            "https://drive.google.com/uc?export=view&id=1056mKidCjkNitjQAGh7lbsI9BzHTOPvm", #12
            "https://drive.google.com/uc?export=view&id=1-lzvM0otdkRW025tM-oahYKLInd0cSCg", #13
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
                "kesan": "Kakak selalu ramah dan mudah diajak ngobrol, suasananya jadi nyaman.",  
                "pesan":"Semoga kakak terus sukses dalam kuliahnya dan selalu semangat menggapai impian!" #1
            },{
                "nama": "Annisa Cahyani Surya",
                "nim": "121450124",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Way Hui",
                "hobbi": " Membaca",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak ini asik diajak tukar pikiran, selalu ada solusi buat setiap masalah.",  
                "pesan":"Teruslah semangat belajar, kak! Masa depan cerah menanti!"# 2
            },{
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton Film",
                "sosmed": "@wlsbn0",
                "kesan": "Kakak punya sikap positif yang bikin suasana jadi lebih santai tapi tetap produktif.",  
                "pesan":"Tetap semangat ya kakak! Jangan lupa istirahat di tengah kesibukan kuliah!"# 3
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "Sangat suportif dan selalu memberi dorongan, kakak ini bikin kita jadi lebih termotivasi.",  
                "pesan":"Sukses selalu untuk kuliahnya! Tetap semangat dan jangan pernah berhenti belajar."# 4
            },{
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bernung, Pesawaran",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 5
            },{
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Belwis",
                "hobbi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak selalu memberi energi positif",  
                "pesan":"Semoga kakak selalu diberi kelancaran dalam segala urusan. Tetap semangat!"# 6
            },{
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Baca Al-qur'an",
                "sosmed": "@fleurnsh",
                "kesan": "Kakak ini selalu ramah dan gampang diajak ngobrol, suasana jadi lebih hidup",  
                "pesan":"Semangat terus, Kak! Jangan menyerah dan teruslah berjuang sampai garis akhir!"# 7
            },{
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak punya sikap yang menyenangkan, setiap obrolan jadi asik dan nggak pernah membosankan.",  
                "pesan":"Semoga sukses di setiap langkah ke depannya, Kak. Teruslah bersinar!"# 8
            },{
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Kakaknya selalu ceria dan bisa bikin orang lain ikut merasa positif.",  
                "pesan":"Jaga kesehatan dan semoga selalu diberi kemudahan dalam setiap perjalanan hidup, Kak!"# 9
            },{
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Ogan Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari Sinyal di Gedung F",
                "sosmed": "@_.dheamelia",
                "kesan": "Sangat mudah bergaul dan selalu membawa suasana jadi nyaman.",  
                "pesan":"Teruslah jadi inspirasi untuk orang-orang di sekitar kakak! Sukses selalu!"# 1
            },{
                "nama": "Muhammad Fahrul Aditya",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini selalu bisa diandalkan, baik dalam situasi santai maupun serius.",  
                "pesan":"Semoga kakak semakin sukses dan terus semangat mengejar impian!"# 1
            },{
                "nama": "Berliana enda putri",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini sosok yang humble dan asik diajak bicara tentang apa saja",  
                "pesan":"Semoga kakak selalu diberkahi kemudahan dalam segala urusan. Tetap semangat menjalani hari-hari ke depan!"# 1
            },{
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Billabong, Gedong Air",
                "hobbi": "Suka Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "Kakak selalu membawa aura positif, jadi nyaman kalau ngobrol lama-lama.",  
                "pesan":"Semoga kakak selalu diberi kebahagiaan dan sukses di setiap langkahnya!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kcWDX0ohoLplcmZam70KYYQqqaskT-Li", #1
            "https://drive.google.com/uc?export=view&id=16U0E8cI_iI_KbnNrC0jyHYsTCWMSuCQD", #2
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
                "kesan": "kakak ini baik dan suka bercerita banyak",
                "pesan": "semoga sukses terus kak jadi senator" #1
            },{
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kotabaru",
                "hobbi": "Menyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "kakak ini tegas",
                "pesan": "jangan tegas terus kak, lebih banyak bercanda coba" #2
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen PSDA":
    def departemenpsda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1z1kXp-4e8f7TLhU9Aa0hnkYtkS1YEmLt", #1
            "https://drive.google.com/uc?export=view&id=1z2NFe04zjARWZCW8rMvLiye_S1Mqj1Xy", #2
            "https://drive.google.com/uc?export=view&id=1yW6wP5r1LBXwY-UJu8IlMqn3cs695Rid", #3
            "https://drive.google.com/uc?export=view&id=1yN65qkZUK-yRL95CKesMV48haKuzYSrc", #4
            "https://drive.google.com/uc?export=view&id=1z0ZBFPy5qOE70b-sVyhkzoyNs_TB9Bj0", #5
            "https://drive.google.com/uc?export=view&id=1ybWFb6WXy9paLtoqab5hUqa2F4q-mkyX", #6
            "https://drive.google.com/uc?export=view&id=1TO4PGCXnefD5v5DuN4kjL13Oppuvm_hG", #7
            "https://drive.google.com/uc?export=view&id=1yvpaJ0HHSzCt4eg8w_yBAtIDbWT0a2tu", #8
            "https://drive.google.com/uc?export=view&id=1yc3-ZYIVe0I8XbRwZdZMPlWVKe9HtCId", #9
            "https://drive.google.com/uc?export=view&id=1qv9qqDw5HhuCAHAunZBhlJGEbWOGWKoc", #10
            "https://drive.google.com/uc?export=view&id=1dZoEOqlgV-AGmkErxUipiiaE3ESXnDQA", #11
            "https://drive.google.com/uc?export=view&id=1yTRKblZ21rzLqhdZbiN3-RFWE18mVU0_", #12
            "https://drive.google.com/uc?export=view&id=1IW5m8o4E_BlYF6Fm-_12dAga4gCvkuzL", #13
            "https://drive.google.com/uc?export=view&id=1yUjArE0Ku3vKc66Z09efsHB3sRAlpc7E", #14
            "https://drive.google.com/uc?export=view&id=1yOLhl9uLFCsM6hZPklnEM72LYst2MBhu", #15
            "https://drive.google.com/uc?export=view&id=1z-9-lOmguBymSZ0vm0NXcq5eCmxjxcvV", #16
            "https://drive.google.com/uc?export=view&id=1yx5LLG-n5Vj9Ya7iesV5gLnH6CfD7NNu", #17
            "https://drive.google.com/uc?export=view&id=1yzQ1tLYTTp4cuhBcJ3EA2DtIL_mSChlo", #18
            "https://drive.google.com/uc?export=view&id=1ywzdCOAzSAn5BTEEx0JnnJGOOHuS21lp", #19
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
                "kesan": "Kakak ini orangnya ramah dan mudah diajak bicara.",
                "pesan": "Semangat terus dalam mengejar cita-cita, kak!"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Cantik dan Fast respond.",
                "pesan": "Saya doakan kakak sukses terus dan punya keluarga bahagia!"
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal": "Riau",
                "alamat": "Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Kakak ini selalu tampil percaya diri dan positif.",
                "pesan": "Jangan pernah lelah untuk belajar dan berkembang, kak!"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450033",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Sukarame",
                "hobbi": "Muter - Muter",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak ini cantik dan baik",
                "pesan": "Saya harap kakak tetap terus menjadi baik, tersenyum dan bahagia"
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Kakak ini gayanya santai tapi tetap keren.",
                "pesan": "Jangan lupa istirahat juga, kak!"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "Jl. Lapas",
                "hobbi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Kakak ini tegas dan lucu",
                "pesan": "Semoga makin bahagia dan terus menjadi orang yang keren kak!"
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kojo",
                "hobbi": "Main Game",
                "sosmed": "@kemasverii",
                "kesan": "Kakak ini baik banget dan murah hati untuk mengajar sesuatu yang dia tahu",
                "pesan": "Semoga kakak makin sukses dengan karir kakak dan cita cita kakak!"
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin Lomba Sihir",
                "sosmed": "@presiliamg",
                "kesan": "Sering lihat kakak ini sibuk terus, kelihatan aktif",
                "pesan": "Sukses terus kuliahnya, Kak!"
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal": "Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak kayaknya enak banget kalau diajak ngobrol.",
                "pesan": "Semangat terus ngejalanin semua kesibukannya, Kak!"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Airan Raya",
                "hobbi": "Nonton Jagad review",
                "sosmed": "@sahid_maulana",
                "kesan": "Kakak kayaknya gampang akrab sama orang baru.",
                "pesan": "Semoga lancar semua urusannya, Kak!"
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Belajar",
                "sosmed": "@roselivnes__",
                "kesan": "Kakak ini cewek keren dan berwibawa soalnya jago main voli",
                "pesan": "Sukses terus kak dalam kompetisi yang kakak jalani!"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobbi": "Nongs",
                "sosmed": "@allyaislami_",
                "kesan": "Kakak ini aura kepemimpinannya kerasa dari jauh.",
                "pesan": "Jangan capek jadi contoh yang baik, Kak!"
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Natar",
                "hobbi": "Nyari sinyal di gedung F",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini senyumnya ramah, kelihatan friendly.",
                "pesan": "Tetap humble ya, Kak, biar makin keren!"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450051",
                "umur": "19",
                "asal": "Kayu Agung",
                "alamat": "Kedaton",
                "hobbi": "Nongki - nongki",
                "sosmed": "@dransyah_",
                "kesan": "Kakak ini kayaknya tenang banget, nggak gampang panik.",
                "pesan": "Jaga kesehatan ya, Kak, jangan terlalu sibuk."
            },
            {
                "nama": "Oktavia Nurwendah Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@oktavianrwnda",
                "kesan": "Kakak ini kelihatannya disiplin, sering tepat waktu.",
                "pesan": "Terus jadi panutan buat kami, Kak!"
            },
            {
                "nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "Sering lihat kakak ini sibuk terus, kelihatan aktif.",
                "pesan": "Semoga kakak selalu dapat nilai bagus ya!"
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv_",
                "kesan": "Kakak ini kelihatannya disiplin, sering tepat waktu.",
                "pesan": "Jangan lupa nikmatin masa-masa kuliah juga, Kak!"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Kakak ini gayanya asik, kayaknya seru buat diajak ngobrol.",
                "pesan": "Jangan bosen jadi inspirasi dari jauh, Kak!"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i_",
                "kesan": "Kakak ini kayaknya selalu fokus banget, serius banget.",
                "pesan": "Jangan terlalu capek ya, Kak, santaiin sedikit!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenpsda()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen MIKFES":
    def departemenmikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BSvpP6GKzs8Ub4FInJcHIAlRgH-t7w0M", #1
            "https://drive.google.com/uc?export=view&id=1BK8yv6CTmhuuyV9rE4Eesah9lU7TFmCP", #2
            "https://drive.google.com/uc?export=view&id=1BWqFCAxg3fRto87RALxg0B09CFo7goyb", #3
            "https://drive.google.com/uc?export=view&id=17QUdwvccQh0cz3_7ryKjU4t3NFaPo5v1", #4
            "https://drive.google.com/uc?export=view&id=1CWQeZb6_jP-A81vjCUusiIS6XbgUy3wq", #5
            "https://drive.google.com/uc?export=view&id=1CGx32vU5-bXUKCdhfLpzQhHhiK27hyA4", #6
            "https://drive.google.com/uc?export=view&id=1CVts_ZeNI-vCc_xOEaVpany4LapEp3F9", #7
            "https://drive.google.com/uc?export=view&id=1BKl7N_wmqDjCReqcBkI2kVqeB5wx8HSh", #8
            "https://drive.google.com/uc?export=view&id=1BK3dlTEQUfxJuE5gT8a4ZeBJQ6fd5bPD", #9
            "https://drive.google.com/uc?export=view&id=1BQ3OT-otHNhEgQusrh5SAbH0YMBI76Je", #10
            "https://drive.google.com/uc?export=view&id=1BYPhRDwxic7FkY4cbHAubFrZDamkCqsX", #11
            "https://drive.google.com/uc?export=view&id=1CaououcxDxAckmhtKd414qJPMQ2S4lhN", #12
            "https://drive.google.com/uc?export=view&id=1BUIhn53s6JhhmFL94T0BjL6t-r0EAbJF", #13
            "https://drive.google.com/uc?export=view&id=17QUdwvccQh0cz3_7ryKjU4t3NFaPo5v1", #14
            "https://drive.google.com/uc?export=view&id=1BS6GCx0E0OTKAertM8uxWgc0xlfYCIrW", #15
            "https://drive.google.com/uc?export=view&id=1DeqL45cbuFToqzP3S3VyVIe67103s1l4", #16
            "https://drive.google.com/uc?export=view&id=1BLzKF6VLfFh3QC2OQSS-ZVMnrkZYW6TJ", #17
            "https://drive.google.com/uc?export=view&id=1ChPkXwdH26fpnOTCcBBG4bMQMvVBsKOC", #18
            "https://drive.google.com/uc?export=view&id=1BNrN2XQ-O6dn_9u3blqd-mIMnWImokbf", #19
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
                "kesan": "Gayanya santai tapi tetap kelihatan smart, keren!",
                "pesan": "Sukses terus ya, Kak, semoga lancar sampai wisuda!"
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Kakak ini kayaknya selalu fokus banget, serius banget.",
                "pesan": "Semoga semua yang kakak usahakan tercapai!"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Kakak ini gayanya asik, kayaknya seru buat diajak ngobrol.",
                "pesan": "Semoga kakak makin keren di setiap hal yang dijalani!"
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Kayaknya kakak ini rapi banget, selalu tampil oke.",
                "pesan": "Selalu semangat dan terus berkarya ya, Kak!"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "Kakak ini kayaknya punya energi positif, bikin suasana jadi hidup.",
                "pesan": "Jangan lupa bahagia dan nikmatin kuliah, Kak!"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakak kayaknya bijak banget, cocok jadi role model.",
                "pesan": "Tetap humble dan jadi diri sendiri ya, Kak!"
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "121450107",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kemiling",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": "@natanaeloks",
                "kesan": "Kakak ini kayaknya selalu datang tepat waktu, patut dicontoh!",
                "pesan": "Terus jadi panutan buat yang lain juga ya, Kak!"
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "Kakak selalu kelihatan cool, kayaknya nggak gampang panik.",
                "pesan": "Jangan lupa tetap happy, Kak, walau sibuk."
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "Kakak kelihatan berwibawa, kayaknya bisa diandalkan.",
                "pesan": "Semangat terus ya, Kak, sampai jadi orang sukses!"
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "",
                "sosmed": "@dindanababan_",
                "kesan": "Kakak sering terlihat enjoy aja, nggak pernah kelihatan stres.",
                "pesan": "Semoga kakak bisa capai semua mimpi-mimpinya!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak ini kayaknya perhatian sama sekitarnya, ramah banget.",
                "pesan": "Semoga kakak selalu dikelilingi hal-hal positif!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak ini selalu terlihat serius, tapi kayaknya asik juga.",
                "pesan": "Semangat terus ya, Kak, jangan lupa senyum!"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini kelihatannya pintar banget, pasti banyak baca.",
                "pesan": "Semoga makin banyak inspirasi dari setiap buku, Kak!"
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": "121450128",
                "umur": "23",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "Kakak ini terlihat bijak, kayaknya banyak pengalaman.",
                "pesan": "Semoga selalu sukses dalam setiap langkah, Kak!"
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "Kakak ini keliatan seru dan kreatif banget saat coding.",
                "pesan": "Semoga terus bikin proyek keren, Kak!"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "Kakak ini kayaknya jago bikin konten, pasti banyak ide.",
                "pesan": "Semoga terus berkarya dan seru-seruan, Kak!"
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakak ini keliatan fun dan pasti punya banyak rekomendasi K-Drama.",
                "pesan": "Semoga terus menikmati setiap episode yang ditonton, Kak!"
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Kakak ini pasti seru dan asik, bisa jadi teman main yang keren.",
                "pesan": "Semoga selalu menemukan game yang seru, Kak!"
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal": "Banten",
                "alamat": "Jl Nangka 3",
                "hobbi": "Berolahraga",
                "sosmed": "@randardn",
                "kesan": "Kakak ini keliatan aktif, pasti sehat dan bugar.",
                "pesan": "Semoga terus semangat berolahraga dan sehat selalu, Kak!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenmikfes()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen Eksternal":
    def departemeneksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17D2FymXXK0ZMaoO8oQwp82e6CEiZB0c8", #1
            "https://drive.google.com/uc?export=view&id=17EuKg-pzfpWSod6vSOLDYtLSf7frHUjG", #2
            "https://drive.google.com/uc?export=view&id=17TKMJPxj_YvsovDXkRZZFartjNA30Kl2", #3
            "https://drive.google.com/uc?export=view&id=17aeDqFvptn3Drmm2IqXnugIo5eQaPbkF", #4
            "https://drive.google.com/uc?export=view&id=17FbblvgZ4BWHeqZ1BEGffMVcYVZwh-NN", #5
            "https://drive.google.com/uc?export=view&id=17SBkcRIXG2PTwtkxqTGMfojTNqI9SXL0", #6
            "https://drive.google.com/uc?export=view&id=17FiyBqaYWbP6zwEKhCMMC6aaXOLFXSIp", #7
            "https://drive.google.com/uc?export=view&id=17_xjrrd3Lj1hoMY3tim3N-H1QcS8qGy_", #8
            "https://drive.google.com/uc?export=view&id=17BxbUzN_DXK-lZsGjg5qYH-NKD5PFQIV", #9
            "https://drive.google.com/uc?export=view&id=17WHcV3mX8Lf8GNdZr99pnaRXFuLwOvZN", #10
            "https://drive.google.com/uc?export=view&id=17A5317wYzurBTEmeXILbOUb_YQcdKD3S", #11
            "https://drive.google.com/uc?export=view&id=17ro6YLHHOyiUjCRXKcGkafPciOeIj-d1", #12
            "https://drive.google.com/uc?export=view&id=17EKjHbCSjNshSqredGkGsV1pUTVLCZqZ", #13
            "https://drive.google.com/uc?export=view&id=17jER21HBIomBC5EwDD2BDzVLvMBJuixu", #14
            "https://drive.google.com/uc?export=view&id=17mAMrMIpGEpTUKuzI0vMJM3YR0tQUD5R", #15
            "https://drive.google.com/uc?export=view&id=17clFpLooK4hdSxU8La_DCFSRbgCGbKyA", #16
            "https://drive.google.com/uc?export=view&id=17jDscDbS4Rx6wsL9EzHcviSZ61mpecrl", #17
            "https://drive.google.com/uc?export=view&id=17jck-30bMbHh6S0D5pYwa_KcM5Rc2o9X", #18
            "https://drive.google.com/uc?export=view&id=17bzGX0XVOLsY60siyNErh82LFJZYwITO", #19
            "https://drive.google.com/uc?export=view&id=178cw49H9lFRurKILz8xjSHXd9R_wvlGO", #20
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
                "kesan": "Kak Yogy itu ramah dan selalu siap bantu.",
                "pesan": "Tetap semangat, Kak Yogy! Terus jadi inspirasi bagi kita semua!"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "Kak Ramadhita selalu membawa kebahagiaan di tim.",
                "pesan": "Jangan lupa bawa cerita seru dari jalan-jalan ya, Kak!"
            },
            {
                "nama": "Nazwa Nabila",
                "nim": "121450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Kochpri",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "Kak Nazwa selalu tampil percaya diri dan positif.",
                "pesan": "Semangat terus, Kak! Kita dukung satu sama lain!"
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "Kak Bastian selalu kreatif dan menginspirasi.",
                "pesan": "Terus berkreasi ya, Kak! Karya-karyamu luar biasa!"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Berkebun",
                "sosmed": "@deaa.rsn",
                "kesan": "Kak Dea punya hati yang besar dan suka berbagi.",
                "pesan": "Semoga selalu sukses di setiap kegiatan ya, Kak!"
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan": "Kak Esteria selalu ceria dan positif.",
                "pesan": "Terus berbagi keceriaan ya, Kak!"
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Surfing",
                "sosmed": "@nateee__15",
                "kesan": "Kak Natasya energik dan selalu bersemangat.",
                "pesan": "Semoga selalu bisa bersenang-senang ya, Kak!"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kak Novelia selalu tenang dan menyenangkan.",
                "pesan": "Semoga selalu mendapatkan istirahat yang baik ya, Kak!"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan": "Kak Ratu selalu aktif dan penuh semangat.",
                "pesan": "Semoga selalu bugar dan sehat ya, Kak!"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan": "Kak Tobias selalu berusaha keras dan disiplin.",
                "pesan": "Semoga selalu berprestasi ya, Kak!"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "Kak Yohana penuh semangat dan selalu ceria.",
                "pesan": "Semoga selalu berbahagia ya, Kak!"
            },
            {
                "nama": "Rizky Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "Kak Rizky selalu kreatif dan berinovasi.",
                "pesan": "Terus berkarya, Kak! Karya-karyamu dinanti!"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "Kak Arafi selalu peduli dan ramah.",
                "pesan": "Semoga selalu sukses dalam berkarya ya, Kak!"
            },
            {
                "nama": "Asa Do’a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "Kak Asa selalu membawa energi positif.",
                "pesan": "Terus semangat ya, Kak! Energi positifnya menular!"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan": "Kak Chalifia selalu asyik diajak ngobrol.",
                "pesan": "Semoga selalu ceria dan bahagia ya, Kak!"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan": "Kak Irvan selalu punya rekomendasi film dan game yang bagus.",
                "pesan": "Terus berbagi rekomendasinya ya, Kak!"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Masak",
                "sosmed": "@izzalutfia",
                "kesan": "Kak Izza selalu bisa masak makanan enak.",
                "pesan": "Selalu share resep enaknya ya, Kak!"
            },
            {
                "nama": "Tiara Ayu",
                "nim": "122450101",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Way Halim",
                "hobbi": "Tari",
                "sosmed": "@tiara_ayu",
                "kesan": "Kak Tiara selalu tampil anggun saat menari.",
                "pesan": "Semoga selalu berbakat di dunia tari ya, Kak!"
            },
            {
                "nama": "Sandy Shafira",
                "nim": "122450123",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Gading Rejo",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@sandyshafira",
                "kesan": "Kak Sandy selalu punya playlist musik yang bagus.",
                "pesan": "Semoga terus menemukan lagu-lagu keren ya, Kak!"
            },
            {
                "nama": "Dika Puspaningtyas",
                "nim": "121450114",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@dika_puspaningtyas",
                "kesan": "Kak Dika jago masak, pasti selalu enak.",
                "pesan": "Semoga terus berkreasi di dapur ya, Kak!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemeneksternal()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen Internal":
    def departemeninternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BZGEatbyf2qVMkBiDNLTBjIqrF3LP-0W", #1
            "https://drive.google.com/uc?export=view&id=1Bla5wCFwjRdlCrZXaAO_2yOBgmc03GIw", #2
            "https://drive.google.com/uc?export=view&id=1C0_dqsGEqVF4KAcibafo4hBEqKzZsXwr", #3
            "https://drive.google.com/uc?export=view&id=1BYrSdfQZ9ITpkx78qNxznE-eax0dHR-Q", #4
            "https://drive.google.com/uc?export=view&id=1BUYuNOTLLIYP_PprcGZcFSI-Kd_26FKD", #5
            "https://drive.google.com/uc?export=view&id=1C2W6tIQpDQcuEm8_760vD7yfNbV1oHCj", #6
            "https://drive.google.com/uc?export=view&id=1BnpXyEl6yV27lU0je518GncrIyxUDIwP", #7
            "https://drive.google.com/uc?export=view&id=1BuJTXAaIc0GmqnZTKTSjzP8HfVvK_pPC", #8
            "https://drive.google.com/uc?export=view&id=1BfG9HU9Sn2iiKTAFmD486wBN1e0yj0i3", #9
            "https://drive.google.com/uc?export=view&id=1BZHL8ckn7aCFmuyPPKqwms7-WwsmYj5u", #10
            "https://drive.google.com/uc?export=view&id=1C-wbf55_zoqyXL_GBkzusuPaz2dlRBAB", #11
            "https://drive.google.com/uc?export=view&id=1ByBETQg--n1rAIDGr4nLUwKSjd-KXIbC", #12
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
                "kesan": "Kak Dimas selalu ceria dan penuh semangat.",
                "pesan": "Terus berkarya dan jangan pernah kehilangan semangat ya, Kak!"
            },
            {
                "nama": "Chatrine Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "Kak Chatrine selalu punya rekomendasi novel yang menarik.",
                "pesan": "Semoga terus menemukan cerita yang inspiratif ya, Kak!"
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Pasaruntung",
                "hobbi": "Mengoleksi Dino",
                "sosmed": "@akbar_restika",
                "kesan": "Kak Akbar punya pengetahuan yang luas tentang dinosaurus.",
                "pesan": "Tetap eksplorasi dan bagikan pengetahuanmu ya, Kak!"
            },
            {
                "nama": "Renita Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Membaca dan Memancing",
                "sosmed": "@renita.shn",
                "kesan": "Kak Renita selalu tenang dan sabar saat memancing.",
                "pesan": "Semoga dapat banyak tangkapan di setiap sesi memancing ya, Kak!"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "Kak Salwa selalu bisa memilih film yang menarik untuk ditonton.",
                "pesan": "Tetap berbagi rekomendasi film seru ya, Kak!"
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "Kak Rendra memiliki bakat luar biasa dalam menulis lirik.",
                "pesan": "Semoga karya-karyamu selalu menginspirasi banyak orang, Kak!"
            },
            {
                "nama": "Yosia Retare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi": "Nungguin ayam betina berkokok",
                "sosmed": "@yosiabanurea",
                "kesan": "Kak Yosia punya sabar yang luar biasa.",
                "pesan": "Semoga kesabaranmu selalu terbayar dengan hal-hal baik, Kak!"
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "Kak Ari selalu antusias saat bermain futsal.",
                "pesan": "Terus semangat berolahraga dan jaga kesehatan ya, Kak!"
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Ngejokes",
                "sosmed": "@josuapanggabean_",
                "kesan": "Kak Josua selalu bisa bikin orang tertawa.",
                "pesan": "Semoga terus membawa keceriaan bagi orang-orang di sekitar ya, Kak!"
            },
            {
                "nama": "Azizah Kusuma Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "Kak Azizah selalu ramah dan suka berbagi hasil kebunnya.",
                "pesan": "Tetap semangat berkebun dan berbagi ya, Kak!"
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@meirasty_",
                "kesan": "Kak Meira selalu tahu film-film terbaru yang menarik.",
                "pesan": "Tetap berbagi info film seru ya, Kak!"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Berenang di Laut",
                "sosmed": "@rexander",
                "kesan": "Kak Rendi sangat suka tantangan saat berenang.",
                "pesan": "Semoga selalu menemukan tempat berenang yang seru, Kak!"
            }
        ]

        display_images_with_data(gambar_urls, data_list)
    departemeninternal()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen SSD":
    def departemenssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zxrH1JMqPDZXLa17sgQVQvLqFx7qYUVb", #1
            "https://drive.google.com/uc?export=view&id=19qKVsNjExplwXiY-36bupKkl08PN91pX", #2
            "https://drive.google.com/uc?export=view&id=19aoYT1W16nCm3N0INxX7mAoaKxwoH9pQ", #3
            "https://drive.google.com/uc?export=view&id=19vScNgkdMY3WBNA1-zQeP8UdLx1Y94hV", #4
            "https://drive.google.com/uc?export=view&id=19jlAHm3_j403ZjB_zdq_hCBMu7Oo_teC", #5
            "https://drive.google.com/uc?export=view&id=1A4THYDA8AQArtMVS0UHwyERJ3NMXYc2q", #6
            "https://drive.google.com/uc?export=view&id=19_S8zBjW-mWiv6cMkxe8zBnqS9zoaSqn", #7
            "https://drive.google.com/uc?export=view&id=19c8SRRN1Yf9n-KKHdmPaIhdslFRJwdmr", #8
            "https://drive.google.com/uc?export=view&id=19j0JccEW9M4rLfwCxW08F6Q0ZTvABcup", #9
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
                "kesan": "Kak Andrian itu sangat pekerja keras dan penuh semangat!",
                "pesan": "Tetap semangat dalam mencari peluang ya, Kak!"
            },
            {
                "nama": "Adisty Syawaida Arianto",
                "nim": "121450136",
                "umur": "23",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan": "Kak Adisty selalu membawa keceriaan di setiap acara.",
                "pesan": "Jangan lupa share film rekomendasi ya, Kak!"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "Kak Nabila pintar dalam mengelola keuangan.",
                "pesan": "Ajarin kita semua tips keuangan ya, Kak!"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Touring",
                "sosmed": "@dananghk_",
                "kesan": "Kak Danang selalu ceria dan siap membantu.",
                "pesan": "Semoga bisa ikut touring bareng, Kak!"
            },
            {
                "nama": "Farel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "Kak Farel memiliki semangat yang positif!",
                "pesan": "Teruslah jadi inspirasi untuk kita semua, Kak!"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukittingi",
                "alamat": "Airan 1",
                "hobbi": "Badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "Kak Rizqi sangat antusias saat bermain badminton.",
                "pesan": "Semoga bisa main bareng di lapangan, Kak!"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Kak Tessa selalu kreatif dalam berkarya.",
                "pesan": "Kirimkan karya-karyamu ya, Kak!"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Kak Nabilah selalu tahu kapan waktu istirahat.",
                "pesan": "Jangan lupa menjaga kesehatan ya, Kak!"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobbi": "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan": "Kak Elia berbakat dalam musik, suaranya merdu!",
                "pesan": "Tunjukkan bakat musikmu di acara mendatang, ya Kak!"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangkal",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Kak Dhafin sangat aktif dan energik.",
                "pesan": "Semoga bisa berolahraga bersama, Kak!"
            }
        ]

        display_images_with_data(gambar_urls, data_list)
    departemenssd()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen MEDKRAF":
    def departemenmedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1cH8o6SW2w0Bir3m1n3Xq4VALNmBfelAN", #1
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
                "kesan": "Kak Wahyu kelihatan berwibawa dan visioner. Salut sama dedikasinya di departemen.",
                "pesan": "Semangat terus, Kak! Jangan lupa istirahat di tengah kesibukan, ya."
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "Kak Elok keliatan cekatan dan teliti. Profesional banget kalau kerja!",
                "pesan": "Tetap semangat, Kak Elok! Jangan lupa sisihkan waktu buat diri sendiri juga!"
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Nugas",
                "sosmed": "@arsyiah._",
                "kesan": "Kak Arsyiah sosok yang kuat dan selalu totalitas. Kerja kerasnya bikin salut!",
                "pesan": "Jangan lupa rehat juga, Kak. Semoga makin sukses ke depannya!"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Lagi Nyari",
                "sosmed": "@dino_kiper",
                "kesan": "Kak Kaisar keliatan santai tapi tetap bisa diandalkan, keren banget!",
                "pesan": "Tetap semangat ya, Kak! Jangan lupa sisihkan waktu buat refreshing juga."
            },
            {
                "nama": "Muhammad Arsal Ranjana Putra",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 4",
                "hobbi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "Kak Arsal pasti kreatif banget, hasil desainnya keren-keren!",
                "pesan": "Lanjut terus, Kak Arsal! Semoga makin sukses dan makin kreatif ya."
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Kak Cintya kelihatan aktif dan energik. Inspirasi buat tetap produktif.",
                "pesan": "Semoga makin semangat, Kak! Jaga kesehatan juga ya."
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": "122450045",
                "umur": "20",
                "asal": "Natar, Lampung Selatan",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "Kak Eka terlihat rajin dan aktif, selalu semangat dalam segala hal.",
                "pesan": "Semangat terus, Kak! Jangan lupa nikmati waktu luang juga ya."
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "Kak Najla kelihatan kreatif dan punya banyak ide keren.",
                "pesan": "Tetap semangat ya, Kak Najla! Keep inspiring with your creativity."
            },
            {
                "nama": "Patricia Leondra Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton Film",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kak Patricia kayaknya santai tapi produktif, selalu ada ide baru.",
                "pesan": "Semoga makin sukses ya, Kak Patricia! Keep up the good work!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan": "Kak Rahma kelihatan rajin dan tekun, pasti keren dalam coding!",
                "pesan": "Semoga selalu semangat, Kak! Terus berkembang dalam coding ya!"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kak Try Yani kelihatan ceria dan suka bikin suasana jadi santai.",
                "pesan": "Tetap semangat ya, Kak! Terus berkarya dan jangan lupa have fun juga!"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi": "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan": "Kak Dwi kelihatan tenang dan selalu detail kalau mengerjakan sesuatu.",
                "pesan": "Semangat terus, Kak Dwi! Teruslah menginspirasi dengan ketelitianmu."
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "Kak Gym kelihatan santai dan suka berbagi hal-hal yang seru.",
                "pesan": "Jaga semangatmu, Kak! Terus jadilah inspirasi buat yang lain ya."
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi": "Nonton Drakor",
                "sosmed": "@nsywanaf",
                "kesan": "Kak Nasywa kelihatan aktif dan seru diajak ngobrol. Antusias banget!",
                "pesan": "Keep up the energy, Kak Nasywa! Teruslah jadi sumber keceriaan tim."
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Baca Novel yang Bikin Nangis",
                "sosmed": "@prskslv",
                "kesan": "Kak Priska kayaknya penyayang dan empati banget sama sekitar.",
                "pesan": "Jangan lupa tersenyum, Kak Priska! Terus tebar energi positifmu ya."
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa, Labuhan Dalam",
                "hobbi": "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan": "Kak Abit kelihatan fokus dan passion-nya di coding patut diacungi jempol.",
                "pesan": "Tetap semangat, Kak Abit! Semoga makin jago coding dan terus berprestasi."
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "_akmal.faiz",
                "kesan": "Kak Akmal santai tapi selalu siap kalau dibutuhkan. Orang yang bisa diandalkan!",
                "pesan": "Semangat terus, Kak! Terus produktif dan tetap keep cool ya."
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani)",
                "hobbi": "Bengong/Membaca Buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Kak Hermawan kelihatan kalem dan penuh ide. Kayaknya orangnya thoughtful banget.",
                "pesan": "Terus semangat dan inspirasi, Kak! Jangan lupa buat nikmati waktu luang juga."
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi": "Mengerjakan Tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Kak Khusnun rajin dan selalu disiplin, hebat banget!",
                "pesan": "Semangat terus ya, Kak Khusnun! Jangan lupa ambil waktu buat rileks juga."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenmedkraf()
