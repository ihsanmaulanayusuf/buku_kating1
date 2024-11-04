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
                "kesan": "Kakak ini enak diajak diskusi, selalu terbuka kalau saya punya pertanyaan.",  
                "pesan":"Semoga kakak semakin berprestasi dan sukses di masa depan. Semangat kuliahnya!"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
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
                "kesan": "Kakak ini baik, mau ngajarin dengan senang hati.",  
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
                "kesan": "Kakak ini enak kalau di tanya dan di ajak diskusi.",  
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
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=105brwiz2HlVf_5oztIM3rGZs3-StaAar", #tri murniya
            "https://drive.google.com/uc?export=view&id=1-mji1Sn-u6vll__yhV3uWOVsameUh3v3", #annisa cahyani
            "https://drive.google.com/uc?export=view&id=1-m--bsigFmXuCQNr6jJ373W_HUHeLYnf", #wulan sabina
            "https://drive.google.com/uc?export=view&id=106mAjV6vabED1EhNMdBBlQbUZwpTeQ6y", #anisa dini
            "https://drive.google.com/uc?export=view&id=1_VgaxKZE7607r1MhUJvbL8704B57zYYv", #claudhea
            "https://drive.google.com/uc?export=view&id=1-tzj7nR8eFe4L1FO-fuIDNC993Hejxqh", #muhammad fachrul 
            "https://drive.google.com/uc?export=view&id=1-hCdTwCzWXqS_YQ-3NYHoUWKzoou8H1F", #anisa fitriyani
            "https://drive.google.com/uc?export=view&id=103w9a1gtY8F2vQ9SrMxuXxFTFsc7y0-b", #feryadi yulius
            "https://drive.google.com/uc?export=view&id=1-l6jgcfnmF1Yh5yXd48qZtdy-_wcRKhZ", #renisha putri
            "https://drive.google.com/uc?export=view&id=1e7uGwfW8aCgJbl5ZjgMRCxRay4qgVtim", #mirzan yusuf rabani
            "https://drive.google.com/uc?export=view&id=1-nPqhkpkcHLX3XRciCdlpUKypdDr_8DT", #Dhea Amelia Putri
            "https://drive.google.com/uc?export=view&id=1056mKidCjkNitjQAGh7lbsI9BzHTOPvm", #Berliana Enda Putri
            "https://drive.google.com/uc?export=view&id=1-lzvM0otdkRW025tM-oahYKLInd0cSCg", #Jeremia Susanto
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
                "kesan": "Kakak selalu ramah dan jelas kalau menjelaskan sesuatu, suasananya jadi nyaman.",  
                "pesan":"Semoga kakak terus sukses dalam kuliahnya dan selalu semangat menggapai impian!" #1
            },{
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Way Hui",
                "hobbi": "Membaca",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak ini asik dan lucu.",  
                "pesan":"Teruslah semangat belajar, kak! Masa depan cerah menanti!"# 2
            },{
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton Film",
                "sosmed": "@wlsbn0",
                "kesan": "Kakak punya sikap positif yang bikin suasana jadi lebih santai.",  
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
                "kesan": "Sangat Muslimah dan suka berbau china.",  
                "pesan":"Sukses selalu untuk kuliahnya! Tetap semangat dan jangan pernah berhenti belajar."# 4
            },{
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak Clau punya sikap yang baik dan lembut.",  
                "pesan":"Semoga sukses di setiap langkah ke depannya, Kak. Teruslah bersinar!"# 8
            },{
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kak Fahrul keren bisa bahasa prancis",  
                "pesan":"Semoga kakak semakin sukses dan terus semangat mengejar impian!"# 1
            },{
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bernung, Pesawaran",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak ini baik dan cantik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 5
            },{
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Belwis",
                "hobbi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Kak Feriyadi kalau ngejelasin tuh jelas banget bikin ngerti",  
                "pesan":"Semoga kakak selalu diberi kelancaran dalam segala urusan. Tetap semangat!"# 6
            },{
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Baca Al-qur'an",
                "sosmed": "@fleurnsh",
                "kesan": "Kak Renisha lumayan pendiam menurut saya",  
                "pesan":"Semangat terus, Kak!"# 7
            },{
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Kakaknya selalu ceria dan kelihatan soft",  
                "pesan":"Jaga kesehatan dan semoga selalu diberi kemudahan dalam setiap perjalanan hidup, Kak!"# 9
            },{
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Ogan Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari Sinyal di Gedung F",
                "sosmed": "@_.dheamelia",
                "kesan": "Kak Dhea mudah bergaul dan selalu membawa suasana jadi nyaman.",  
                "pesan":"Teruslah jadi inspirasi untuk orang-orang di sekitar kakak! Sukses selalu!"# 1
            },{
                "nama": "Berliana Enda Putri",
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
            }
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
                "nama": "Anissa Luthfi Alifia",
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
                "kesan": "kakak ini tegas dan orangnya baik, welcoming banget",
                "pesan": "Semoga lain kali bisa main musik bareng kak" #2
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen PSDA":
    def departemenpsda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1z1kXp-4e8f7TLhU9Aa0hnkYtkS1YEmLt", #Ericson Chandra Sihombing
            "https://drive.google.com/uc?export=view&id=1z2NFe04zjARWZCW8rMvLiye_S1Mqj1Xy", #Elisabeth Claudia Simanjuntak
            "https://drive.google.com/uc?export=view&id=1yW6wP5r1LBXwY-UJu8IlMqn3cs695Rid", #Deyvan Loxefal
            "https://drive.google.com/uc?export=view&id=1yN65qkZUK-yRL95CKesMV48haKuzYSrc", #Nisrina Nur Afifah
            "https://drive.google.com/uc?export=view&id=1z0ZBFPy5qOE70b-sVyhkzoyNs_TB9Bj0", #M. Farhan Athaulloh
            "https://drive.google.com/uc?export=view&id=1ybWFb6WXy9paLtoqab5hUqa2F4q-mkyX", #Johannes Krisjon Silitonga
            "https://drive.google.com/uc?export=view&id=1TO4PGCXnefD5v5DuN4kjL13Oppuvm_hG", #Kemas Veriandra Ramadhan
            "https://drive.google.com/uc?export=view&id=1yvpaJ0HHSzCt4eg8w_yBAtIDbWT0a2tu", #Presilia
            "https://drive.google.com/uc?export=view&id=1yc3-ZYIVe0I8XbRwZdZMPlWVKe9HtCId", #Rafa Aqilla Jungjunan
            "https://drive.google.com/uc?export=view&id=1qv9qqDw5HhuCAHAunZBhlJGEbWOGWKoc", #Sahid Maulana
            "https://drive.google.com/uc?export=view&id=1dZoEOqlgV-AGmkErxUipiiaE3ESXnDQA", #Vanessa Olivia Rose
            "https://drive.google.com/uc?export=view&id=1yTRKblZ21rzLqhdZbiN3-RFWE18mVU0_", #Allya Nurul Islami Pasha
            "https://drive.google.com/uc?export=view&id=1IW5m8o4E_BlYF6Fm-_12dAga4gCvkuzL", #Eksanty Febriana Sukma Islamiaty
            "https://drive.google.com/uc?export=view&id=1yUjArE0Ku3vKc66Z09efsHB3sRAlpc7E", #M. Deriansyah Okutra
            "https://drive.google.com/uc?export=view&id=1yOLhl9uLFCsM6hZPklnEM72LYst2MBhu", #Oktavia Nurwinda Puspitasari
            "https://drive.google.com/uc?export=view&id=1z-9-lOmguBymSZ0vm0NXcq5eCmxjxcvV", #Gede Moena
            "https://drive.google.com/uc?export=view&id=1yx5LLG-n5Vj9Ya7iesV5gLnH6CfD7NNu", #Jaclin Alcavella
            "https://drive.google.com/uc?export=view&id=1yzQ1tLYTTp4cuhBcJ3EA2DtIL_mSChlo", #Rafly Prabu Darmawan
            "https://drive.google.com/uc?export=view&id=1ywzdCOAzSAn5BTEEx0JnnJGOOHuS21lp", #Syalaisha Andini Putriansyah
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
                "kesan": "Bang Ericson tuh keren banget kalo soal organisasi, pembawaannya juga bagus.",
                "pesan": "Semangat terus dalam menyelesaikan semesternya!"
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
                "kesan": "Kakak ini selalu tampil percaya diri dan positif terus lucu juga.",
                "pesan": "Jangan pernah lelah untuk belajar dan berkembang, kak!"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Sukarame",
                "hobbi": "Marahin Orang",
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
                "kesan": "Kakak enak banget kalau diajak ngobrol.",
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
                "kesan": "Bang sahid keren soalnya bisa musik jadi pengen belajar bareng.",
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
                "kesan": "Kakak ini cewek keren dan berwibawa soalnya jago main basket",
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
                "kesan": "Kakak ini senyumnya ramah, kelihatan friendly dan juga disiplin.",
                "pesan": "Tetap humble ya, Kak, biar makin keren!"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal": "Kayu Agung",
                "alamat": "Kedaton",
                "hobbi": "Nongki - nongki",
                "sosmed": "@dransyah_",
                "kesan": "Bang Deri tuh santai kalo ngajar terus lucu juga.",
                "pesan": "Jaga kesehatan ya, Kak!."
            },
            {
                "nama": "Oktavia Nurwinda Puspitasari",
                "nim": "122450041",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@oktavianrwnda",
                "kesan": "Kakak ini kelihatannya disiplin.",
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
                "kesan": "Bang Gede kelihatan seru.",
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
                "kesan": "Kak Jaclin tuh baik dan enak di ajak ngobrol.",
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
                "kesan": "Bang Rafly ini gayanya asik, kayaknya seru buat diajak ngobrol.",
                "pesan": "Jangan bosen jadi inspirasi, Kak!"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i_",
                "kesan": "Kakk Andini tuh baik hati.",
                "pesan": "Jangan terlalu capek ya, Kak, santaiin sedikit!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenpsda()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen MIKFES":
    def departemenmikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BSvpP6GKzs8Ub4FInJcHIAlRgH-t7w0M", #Rafi Fadhlillah
            "https://drive.google.com/uc?export=view&id=1BK8yv6CTmhuuyV9rE4Eesah9lU7TFmCP", #Annisa Novantika
            "https://drive.google.com/uc?export=view&id=1BWqFCAxg3fRto87RALxg0B09CFo7goyb", #Ahmad Sahidin Akbar
            "https://drive.google.com/uc?export=view&id=1CWQeZb6_jP-A81vjCUusiIS6XbgUy3wq", #Muhammad Regi Abdi Putra Amanta
            "https://drive.google.com/uc?export=view&id=1CGx32vU5-bXUKCdhfLpzQhHhiK27hyA4", #Syalaisha Andina Putriansyah
            "https://drive.google.com/uc?export=view&id=1BKl7N_wmqDjCReqcBkI2kVqeB5wx8HSh", #Anwar Muslim
            "https://drive.google.com/uc?export=view&id=1BK3dlTEQUfxJuE5gT8a4ZeBJQ6fd5bPD", #Deva Anjani Khayyuninafsyah
            "https://drive.google.com/uc?export=view&id=1BQ3OT-otHNhEgQusrh5SAbH0YMBI76Je", #Dinda Nababan
            "https://drive.google.com/uc?export=view&id=1BYPhRDwxic7FkY4cbHAubFrZDamkCqsX", #Marleta Cornelia Leander
            "https://drive.google.com/uc?export=view&id=1CaououcxDxAckmhtKd414qJPMQ2S4lhN", #Rut Junita Sari Siburian
            "https://drive.google.com/uc?export=view&id=1BUIhn53s6JhhmFL94T0BjL6t-r0EAbJF", #Syadza Puspadari Azhar
            "https://drive.google.com/uc?export=view&id=1BS6GCx0E0OTKAertM8uxWgc0xlfYCIrW", #Aditya Rahman
            "https://drive.google.com/uc?export=view&id=1DeqL45cbuFToqzP3S3VyVIe67103s1l4", #Eggi Satria
            "https://drive.google.com/uc?export=view&id=1BLzKF6VLfFh3QC2OQSS-ZVMnrkZYW6TJ", #Febiya Jomy Pratiwi
            "https://drive.google.com/uc?export=view&id=1ChPkXwdH26fpnOTCcBBG4bMQMvVBsKOC", #Happy Syahrul Ramadhan
            "https://drive.google.com/uc?export=view&id=1BNrN2XQ-O6dn_9u3blqd-mIMnWImokbf", #Randa Andriana Putra
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
                "kesan": "Kak Andina mirip banget dengan kak Andini, baik hati juga.",
                "pesan": "Tetap humble dan jadi diri sendiri ya, Kak!"
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "Bang Anwar terlihat pinter soalnya sering lihat jelasin materi.",
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
                "kesan": "Kakak kelihatan berwibawa.",
                "pesan": "Semangat terus ya, Kak, sampai jadi orang sukses!"
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Membaca jurnal Bu Mika",
                "sosmed": "@dindanababan_",
                "kesan": "Kakak sering terlihat enjoy aja.",
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
                "kesan": "Kakak ini kayaknya perhatian sama sekitarnya, ramah banget dan cantik.",
                "pesan": "Semoga kakak selalu dikelilingi hal-hal positif!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Menghitung akurasi",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak ini selalu terlihat ceria, dan kayaknya asik juga.",
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
                "kesan": "Kakak ini kelihatannya seru di ajak ngobrol",
                "pesan": "Semoga makin banyak inspirasi dari setiap buku, Kak!"
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "Kakak ini kelihatannya pintar banget, pasti banyak baca.",
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
                "kesan": "Bang Eggi tuh pinter banget dan keren sering membantu",
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
                "kesan": "Bang Syahrul tuh pinter Back End atau Front End",
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
            "https://drive.google.com/uc?export=view&id=17D2FymXXK0ZMaoO8oQwp82e6CEiZB0c8", #Yogy Sa'e Tama
            "https://drive.google.com/uc?export=view&id=17BxbUzN_DXK-lZsGjg5qYH-NKD5PFQIV", #Ramadhita Atifa Hendri
            "https://drive.google.com/uc?export=view&id=17TKMJPxj_YvsovDXkRZZFartjNA30Kl2", #Nazwa Nabilla
            "https://drive.google.com/uc?export=view&id=17aeDqFvptn3Drmm2IqXnugIo5eQaPbkF", #Bastian Heskia Silaban
            "https://drive.google.com/uc?export=view&id=17FbblvgZ4BWHeqZ1BEGffMVcYVZwh-NN", #Dea Mutia Risani
            "https://drive.google.com/uc?export=view&id=17SBkcRIXG2PTwtkxqTGMfojTNqI9SXL0", #Esteria Rohanauli Sidauruk
            "https://drive.google.com/uc?export=view&id=17FiyBqaYWbP6zwEKhCMMC6aaXOLFXSIp", #Natasya Ega Lina Marbun
            "https://drive.google.com/uc?export=view&id=17_xjrrd3Lj1hoMY3tim3N-H1QcS8qGy_", #Novelia Adinda
            "https://drive.google.com/uc?export=view&id=17EuKg-pzfpWSod6vSOLDYtLSf7frHUjG", #Ratu Keisha Jasmine Deanova
            "https://drive.google.com/uc?export=view&id=17WHcV3mX8Lf8GNdZr99pnaRXFuLwOvZN", #Tobias David Manogari
            "https://drive.google.com/uc?export=view&id=17A5317wYzurBTEmeXILbOUb_YQcdKD3S", #Yohana Manik
            "https://drive.google.com/uc?export=view&id=17ro6YLHHOyiUjCRXKcGkafPciOeIj-d1", #Rizki Adrian Bennovry
            "https://drive.google.com/uc?export=view&id=17EKjHbCSjNshSqredGkGsV1pUTVLCZqZ", #Arafi Ramadhan Maulana
            "https://drive.google.com/uc?export=view&id=17jER21HBIomBC5EwDD2BDzVLvMBJuixu", #Asa Do’a Uyi
            "https://drive.google.com/uc?export=view&id=17mAMrMIpGEpTUKuzI0vMJM3YR0tQUD5R", #Chalifia Wananda
            "https://drive.google.com/uc?export=view&id=17clFpLooK4hdSxU8La_DCFSRbgCGbKyA", #Irvan Alfaritzi
            "https://drive.google.com/uc?export=view&id=17jDscDbS4Rx6wsL9EzHcviSZ61mpecrl", #Izza Lutfia
            "https://drive.google.com/uc?export=view&id=17jck-30bMbHh6S0D5pYwa_KcM5Rc2o9X", #Khaalishah Zuhrah Alyaa Vanefi
            "https://drive.google.com/uc?export=view&id=17bzGX0XVOLsY60siyNErh82LFJZYwITO", #Raid Muhammad Naufal
            "https://drive.google.com/uc?export=view&id=178cw49H9lFRurKILz8xjSHXd9R_wvlGO", #Tria Yunanni
        ]
        data_list = [
            {
                "nama": "Yogy Sa'e Tama",
                "nim": "121450041",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Jatimulyo",
                "hobbi": "Bangun Pagi",
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
                "sosmed": "@ramadhitatifa",
                "kesan": "Kak Ramadhita tuh imuttt.",
                "pesan": "Jangan lupa bawa cerita seru dari jalan-jalan ya, Kak!"
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Kochpri",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "Kak Nazwa tuh keren soalnya main golf.",
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
                "kesan": "Kak Esteria juga keren karena main golf tuh jarang banget yang saya temui.",
                "pesan": "Terus berbagi keceriaan ya, Kak!"
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Surfing",
                "sosmed": "@nateee__15",
                "kesan": "Kak Natasya energik dan keren.",
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
                "kesan": "Kak Ratu selalu aktif dan penuh semangat juga cantik.",
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
                "kesan": "Bang Tobias keliatan disiplin dan cool.",
                "pesan": "Semoga selalu berprestasi ya, Kak!"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "Kak Yohana tuh tegas dan berwibawa",
                "pesan": "Semoga selalu berbahagia ya, Kak!"
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "Bang Rizky keliatan seperti orang yang dkv banget.",
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
                "kesan": "Kak Asa tuh vibe nya suka menolong dan main sama anak kecil.",
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
                "kesan": "Kak Chalifia kesannya seperti kutu buku yang pinter itu.",
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
                "kesan": "Kak Irvan kesannya gamers banget.",
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
                "kesan": "Kak Izza kesannya bisa masak makanan enak dan ramah.",
                "pesan": "Selalu share resep enaknya ya, Kak!"
            },{
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "Kak Alya tuh paling gemoy",
                "pesan": "Bahagia dan sukses selalu kak alyaaa!"
            },{
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Ngeresume Seminar",
                "sosmed": "@rayths_",
                "kesan": "Kak Raid kesannya suka ngoding.",
                "pesan": "Semoga terus langgeng ya, Kak!"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "121450062",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Jakarta",
                "hobbi": "Baca",
                "sosmed": "@tria_y062",
                "kesan": "Kak Tria tuh cantik dan imut terus baik hati juga sering senyum",
                "pesan": "Semangat mengerjakan tugas kuliah, Kak!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemeneksternal()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen Internal":
    def departemeninternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BZGEatbyf2qVMkBiDNLTBjIqrF3LP-0W", #Dimas Rizky Ramadhani
            "https://drive.google.com/uc?export=view&id=1Bla5wCFwjRdlCrZXaAO_2yOBgmc03GIw", #Catherine Firdhasari Maulina Sinaga
            "https://drive.google.com/uc?export=view&id=1C0_dqsGEqVF4KAcibafo4hBEqKzZsXwr", #M. Akbar Resdika
            "https://drive.google.com/uc?export=view&id=1BYrSdfQZ9ITpkx78qNxznE-eax0dHR-Q", #Renta Siahaan
            "https://drive.google.com/uc?export=view&id=1BUYuNOTLLIYP_PprcGZcFSI-Kd_26FKD", #Salwa Farhanatussaidah
            "https://drive.google.com/uc?export=view&id=1C2W6tIQpDQcuEm8_760vD7yfNbV1oHCj", #Rendra Eka Prayoga
            "https://drive.google.com/uc?export=view&id=1BnpXyEl6yV27lU0je518GncrIyxUDIwP", #Yosia Letare Banurea
            "https://drive.google.com/uc?export=view&id=1BuJTXAaIc0GmqnZTKTSjzP8HfVvK_pPC", #Ari Sigit
            "https://drive.google.com/uc?export=view&id=1BfG9HU9Sn2iiKTAFmD486wBN1e0yj0i3", #Josua Alfa Viando Panggabean
            "https://drive.google.com/uc?export=view&id=1BZHL8ckn7aCFmuyPPKqwms7-WwsmYj5u", #Azizah Kusumah Putri
            "https://drive.google.com/uc?export=view&id=1C-wbf55_zoqyXL_GBkzusuPaz2dlRBAB", #Meira Listyaningrum
            "https://drive.google.com/uc?export=view&id=1ByBETQg--n1rAIDGr4nLUwKSjd-KXIbC", #Rendi Alexander Hutagalung
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
                "kesan": "Kak Dimas selalu ceria, lucu dan penuh semangat bener bener bikin semangat juga.",
                "pesan": "Terus berkarya dan jangan pernah kehilangan semangat ya, Kak!"
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "Kak Chatrine kesannya punya rekomendasi novel yang menarik.",
                "pesan": "Semoga terus menemukan cerita yang inspiratif ya, Kak!"
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Pasaruntung",
                "hobbi": "Mengoleksi Dino",
                "sosmed": "@akbar_restika",
                "kesan": "Kak Akbar kesannya pengetahuan yang luas tentang dinosaurus.",
                "pesan": "Tetap eksplorasi dan bagikan pengetahuanmu ya, Kak!"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Membaca dan Memancing",
                "sosmed": "@renita.shn",
                "kesan": "Kak Renita kesannya tenang dan sabar.",
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
                "kesan": "Kak Salwa kesannya bisa memilih film yang menarik untuk ditonton.",
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
                "kesan": "Kak Rendra kesannya punya bakat dalam menulis lirik.",
                "pesan": "Semoga karya-karyamu selalu menginspirasi banyak orang, Kak!"
            },
            {
                "nama": "Yosia Letare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi": "Nungguin ayam betina berkokok",
                "sosmed": "@yosiabanurea",
                "kesan": "Kak Yosia tuh kesannya seru kalo jadi satu circle.",
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
                "kesan": "Kak Ari kesannya antusias kalau bermain futsal.",
                "pesan": "Terus semangat berolahraga dan jaga kesehatan ya, Kak!"
            },
            {
                "nama": "Josua Alfa Viando Panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Ngejokes",
                "sosmed": "@josuapanggabean_",
                "kesan": "Kak Josua selalu bisa bikin orang tertawa.",
                "pesan": "Semoga terus membawa keceriaan bagi orang-orang di sekitar ya, Kak!"
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "Kak Azizah kesannya ramah dan suka berbagi.",
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
                "kesan": "Kak Meira kesannya tahu film-film terbaru yang menarik.",
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
                "kesan": "Kak Rendi kesannya suka tantangan saat berenang.",
                "pesan": "Semoga selalu menemukan tempat berenang yang seru, Kak!"
            }
        ]

        display_images_with_data(gambar_urls, data_list)
    departemeninternal()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen SSD":
    def departemenssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zxrH1JMqPDZXLa17sgQVQvLqFx7qYUVb", #Andrian Agustinus Lumban Gaol
            "https://drive.google.com/uc?export=view&id=19qKVsNjExplwXiY-36bupKkl08PN91pX", #Adisty Syawalda Ariyanto
            "https://drive.google.com/uc?export=view&id=19aoYT1W16nCm3N0INxX7mAoaKxwoH9pQ", #Nabila Azhari
            "https://drive.google.com/uc?export=view&id=19vScNgkdMY3WBNA1-zQeP8UdLx1Y94hV", #Danang Hilal Kurniawan
            "https://drive.google.com/uc?export=view&id=19jlAHm3_j403ZjB_zdq_hCBMu7Oo_teC", #Farrel Julio Akbar
            "https://drive.google.com/uc?export=view&id=1A4THYDA8AQArtMVS0UHwyERJ3NMXYc2q", #Ahmad Rizqi
            "https://drive.google.com/uc?export=view&id=19_S8zBjW-mWiv6cMkxe8zBnqS9zoaSqn", #Tessa Kania Sagala
            "https://drive.google.com/uc?export=view&id=19c8SRRN1Yf9n-KKHdmPaIhdslFRJwdmr", #Elia Meylani Simanjuntak
            "https://drive.google.com/uc?export=view&id=19j0JccEW9M4rLfwCxW08F6Q0ZTvABcup", #Dhafin Razaqa Luthfi
        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban gaol",
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
                "nama": "Adisty Syawalda Ariyanto",
                "nim": "121450136",
                "umur": "23",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan": "Kak Adisty kesannya membawa keceriaan.",
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
                "kesan": "Kak Nabila kesannya pintar dalam mengelola keuangan.",
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
                "kesan": "Bang Danang selalu ceria dan siap membantu terus juga baik.",
                "pesan": "Semoga bisa ikut touring bareng, Kak!"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "Kak Farel kesannya punya semangat yang positif terus juga gagah!",
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
                "kesan": "Kak Rizqi kesannya cowok yang keren.",
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
                "kesan": "Kak Tessa kesannya murah hati dan kreatif.",
                "pesan": "Sukses terus kak!"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobbi": "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan": "Kak Elia kesannya berbakat dalam musik!",
                "pesan": "Semangat kak kuliah dan bermusiknya!"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangkal",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Bang Dhafin sangat introvert.",
                "pesan": "Semoga sehat selalu, Kak!"
            }
        ]

        display_images_with_data(gambar_urls, data_list)
    departemenssd()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen MEDKRAF":
    def departemenmedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-_OLHhtPgbpBrNWKTjE1XRzIdfzuG5wt", #Wahyudiyanto
            "https://drive.google.com/uc?export=view&id=1YOkrZk6ebEKmAZTT1KQXBeGbhc20X6O2", #Elok Fiola
            "https://drive.google.com/uc?export=view&id=1BnGOP6siHdSx4OREJZ34HlLsLYvGk-Xy", #Arsyiah Azahra
            "https://drive.google.com/uc?export=view&id=1NjusVrTzZAAqQw1vlyuL9VMWS1qTIsaw", #Muhammad Kaisar Firdaus
            "https://drive.google.com/uc?export=view&id=1bYMz3BTdfWgZMSAlg5eJ9NR38GU26Euc", #Muhammad Arsal Ranjana Putra
            "https://drive.google.com/uc?export=view&id=1YjoPJ8gFBZgue6_BqZBZhx32j_vfBysW", #Cintya Bella
            "https://drive.google.com/uc?export=view&id=12jeGp8YWJFkluuCsvQa_C38Yo9xc-Tex", #Eka Fidiya Putri
            "https://drive.google.com/uc?export=view&id=1iZ-U43RFR8QXKvSmYfbhodH5oWxMphyk", #Najla Juwairia
            "https://drive.google.com/uc?export=view&id=1wETIVlsErc40aUsllKkOjb64XGEe-Fmv", #Patricia Leondrea Diajeng Putri
            "https://drive.google.com/uc?export=view&id=1QCYs7Xc27O7UkhNP3gYvWd8Tuad6fDbw", #Rahma Neliyana
            "https://drive.google.com/uc?export=view&id=1dviBzux_Iy10NG43PNmAoSTC64jml3_i", #Try Yani Rizki Nur Rohmah
            "https://drive.google.com/uc?export=view&id=1n2jTja7I9dIxnq4S6kKw7qSb7wcMoCM7", #Dwi Ratna Anggraeni
            "https://drive.google.com/uc?export=view&id=1QIJf2VMUEXTqiKpA6l7OZp-CT3pPZatp", #Gymnastiar Al Khoarizmy
            "https://drive.google.com/uc?export=view&id=1QC8qXwDFXh-T0FqVLJz8P2NL5fcMKq-C", #Nasywa Nur Afifah
            "https://drive.google.com/uc?export=view&id=1zsn0-c3YQTPDGWx5Qim0X2E_cpKMah7-", #Abit Ahmad Oktarian
            "https://drive.google.com/uc?export=view&id=1VlM2_REPbVm_rjuSA4zyOWwd-1HdvH9C", #Akmal Faiz Abdillah
            "https://drive.google.com/uc?export=view&id=1ibyCjIfGf_L1qW6jM9r-p7WFbPt516oc", #Hermawan Manurung
            "https://drive.google.com/uc?export=view&id=1qvVc11We-dsmJw-eNi4vlmL2n_SXbRNi", #Khusnun Nisa
            "https://drive.google.com/uc?export=view&id=1HCQV3ZxaZPIariaJMT-2GkHEN2cXXQkY", #Priska Silvia Ferantiana
        ]
        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal": "Makassar",
                "alamat": "Sukarame",
                "hobbi": "Nonton",
                "sosmed": "@wayyulaja",
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
                "kesan": "Kak Elok keliatan cekatan dan teliti!",
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
                "kesan": "Kak Arsyiah kesannya sosok yang kuat dan selalu totalitas. Kerja kerasnya bikin salut!",
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
                "kesan": "Kak Arsal pasti kreatif banget terus pinter matematika",
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
                "kesan": "Kak Cintya kesannya cantik dan juga profesional.",
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
                "kesan": "Kak Najla kelihatan seru di ajak ngobrol dan punya banyak hal yang mau di bahas.",
                "pesan": "Tetap semangat ya, Kak Najla! Keep inspiring with your creativity."
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton Film",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kak Patricia kayaknya santai tapi produktif.",
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
                "kesan": "Kak Rahma kesannya rajin dan, pasti keren dalam coding!",
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
                "kesan": "Kak Try Yani kesannya tegas dan disiplin.",
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
                "kesan": "Kak Dwi kesannya tau banyak buku novel.",
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
                "kesan": "Kak Gym kesannya santai dan suka berbagi hal-hal yang seru kayak anime dan komiknya.",
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
                "kesan": "Kak Nasywa kesannya aktif dan seru diajak ngobrol. Antusias banget!",
                "pesan": "Keep up the energy, Kak Nasywa! Teruslah jadi sumber keceriaan tim."
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa, Labuhan Dalam",
                "hobbi": "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan": "Kak Abit kesannya fokus dan passion-nya di coding patut diacungi jempol.",
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
                "kesan": "Kak Hermawan kesannya kalem tapi tegas.",
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
                "kesan": "Kak Khusnun kesannya rajin dan selalu disiplin!",
                "pesan": "Semangat terus ya, Kak Khusnun! Jangan lupa ambil waktu buat rileks juga."
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
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenmedkraf()
