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
                "sosmed": "@gumilangkharisma",
                "kesan" : "Ramah, keren banget, dan asik diajak diskusi",  
                "pesan" :"Semoga apa yang diimpikan bisa terwujud bang"#1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Bukit Kemuning",
                "alamat": "Pawen 2 Sukarame",
                "hobi": "Main gitar",
                "sosmed": "@pndrinsni21",
                "kesan": "Abangnya asik diajak diskusi dan buat suasana jadi rame",  
                "pesan":"Semangat terus kuliahnya bang dan sehat selalu ya"#2
            },
            {
               "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kota Baru",
                "hobi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakaknya seru dan penjelasan dari kakak mudah dimengerti",  
                "pesan":"Semoga semua urusan perkuliahannya lancar ya kak"#3

            },
            {
                "nama": "Hartiti Fadhilaj",
                "nim": "12145031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakaknya lucu dan ramah",  
                "pesan":"Semoga sukses dalam karir dan studinya kak!" #4

            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "Nangka 4",
                "hobi": "Dengerin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakaknya baik dan pendiam",  
                "pesan":"Jaga kesehatan dan tetap semangat kak!"#5

            },
            {
               "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobi": "Dengerin bang Pandra gitaran",
                "sosmed": "@nadillaadr26",
                "kesan": "Seru banget dan baik",  
                "pesan":"Semoga sukses di masa depan kak!" #6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ljb9SvoosMi5KmnZeK4zVxS7voKFkgcU",#1
            "https://drive.google.com/uc?export=view&id=1aHSlA8xzCqpjE3uVzhRNStT0zyX5POUo",#2
            "https://drive.google.com/uc?export=view&id=10HlLY9RZ2J11NaAI-lcOv_6u1Ku6nBvh",#3
            "https://drive.google.com/uc?export=view&id=1Dp07vXIkUG2iC04B3wIEpvQCNVvxq4Z1",#4
            "https://drive.google.com/uc?export=view&id=1-MvEud_r36XP_pI3_uSzFHUy6O_2NWt4",#5
            "https://drive.google.com/uc?export=view&id=1Ffk9SXS1tLeogQlM8nqmscilaqXUXQSE",#6
            "https://drive.google.com/uc?export=view&id=1gqKqs1xSchDmHs-yV6Hvbe2j_t7wNO3G",#7
            "https://drive.google.com/uc?export=view&id=1bYhvJJVKOw-qTvuDtJ2PmqvkIPJrUMXi",#8
            "https://drive.google.com/uc?export=view&id=1mcaAXEfl3s1SelPYauHeh7YucCyRvxJn",#9
            "https://drive.google.com/uc?export=view&id=1NjhtffCc82MtBFUSA2fzTAVC5_imxkkg",#10
            "https://drive.google.com/uc?export=view&id=1XLwRMp-nUeR7mkaMEHv4Thx8NQKygWUg",#11
            "https://drive.google.com/uc?export=view&id=1hUiGkZy3YhqCfERBH08wPtevcIY9vPbM",#12
            "https://drive.google.com/uc?export=view&id=1sJah5S-pKWQjvjRxYrAj_Wc5zcAxnWkO",#13
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
                "kesan": "Asik banget dan saya suka cara kakak menyampaikan sesuatu",  
                "pesan":"Terus menginspirasi dan semoga lancar dalam setiap langkahnya kak!" #1
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Way Hui",
                "hobi": "Membaca",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Pendiam dan murah senyum",  
                "pesan":"Semoga diberikan kelancaran dalam setiap aktivitasnya dan semangat kuliahnya kak" #2
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Menonton Film",
                "sosmed": "@wlsbn0",
                "kesan": "Baik banget, kalem dan mukanya adem",  
                "pesan": "Semoga sukses dalam perkuliahannya kak dan semangat dalam mengejar cita-cita kak" #3
            },
            {
               "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jati Agung",
                "hobi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "Seru diajak diskusi, asik, dan murah senyum",  
                "pesan": "Semangat menjalani kuliahnya kak dan jaga kesehatan ya" #4
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bernung, Pesawaran",
                "alamat": "Bandar Lampung",
                "hobi": "Nonton Drakor",
                "sosmed": "@ansftynn_",
                "kesan": "Kalem dan baik",  
                "pesan":"Semoga tugas-tugas kuliahnya lancar dan semoga cepat lulus kak!" #5

            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Belwis",
                "hobi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Baik, pendiam, dan keren banget jurnal nya diterbitin",  
                "pesan":"Semanagat menjalani hari-hari dan sukses dalam studinya bang!" #6
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobi": "Baca Al-qur’an",
                "sosmed": "@fleurnsh",
                "kesan": "Ramah dan lucu",  
                "pesan": "Semoga impiannya bisa terwujud kak!" #7
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakanya baik banget dan kalem",  
                "pesan":"Semoga sukses dalam karirnya kak!" #8
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Kayak anime dan tinggi",  
                "pesan":"Semoga dalam setiap aktivitasnya lancar ya bang" #9
            },
            {
                "nama": "Dhea Amelia Putr",
                "nim": "122450004",
                "umur": "20",
                "asal":"Ogan Ilir",
                "alamat": "Natar",
                "hobi": "Nyari Sinyal di Gedung F",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakaknya lucu banget dan banyak bercandanya jadi seru",  
                "pesan":"Semoga cepat lulus kuliah kak!" #10
            },
            {
                "nama": "Muhammad fahrul Aditya",
                "nim": "121450126",
                "umur": "22",
                "asal":"Surakarta",
                "alamat": "Sukarame",
                "hobi": "Melukis",
                "sosmed": "@fhrul.pdf",
                "kesan": "Pendiam dan baik",  
                "pesan":"Sukses di masa depan dan lancar studinya bang" #11

            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Billabong, Gedong Air",
                "hobi": "Suka Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "Abangnya keren, asik, dan aktif menjawaab pertanyaan",  
                "pesan":"Semangat menjalani hari-harinya dan lancar dalam semua aktivitasnya bang" #12

            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Way Huwi",
                "hobi": "Baca Buku, Ngoding, Ibadah",
                "sosmed": "@berlyyanda",
                "kesan": "Seru banget dan baik",  
                "pesan":"Jaga kesehatan dan bahagia selalu kak!" #13
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
                "kesan": "Baik, keren, serta cara berkomunikasinya enak didengar dan dipahami",  
                "pesan":"Semoga cepat lulus dan sukses dalam karirnya kak!" #1
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kota baru",
                "hobi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "Tegas, keren, dan saya suka cara abang menjelaskan sesuatu",  
                "pesan":"Sehat selalu dan semoga lancar dalam setiap aktivitasnya bang!" #2

            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()
    
elif menu == "Departemen PSDA":
    def departemenpsda ():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bGrtJvqxyagI71zr0yOgCYOATjcdjnSv", #bang econ
            "https://drive.google.com/uc?export=view&id=1hd_ZBV8YXCjifW3POxChGh5B9432VlOo", #kak abeth
            "https://drive.google.com/uc?export=view&id=1zAV8ubsdhEP8hLGSx6D0l-Cy-SrKCdUw", #kak afifah
            "https://drive.google.com/uc?export=view&id=1T1Y3AmgHVb38M74tIlajAdv0LU0a_BzY", #kak allya
            "https://drive.google.com/uc?export=view&id=1c1c6ZOytsjEGJeWPLiSPIFy9w56z-ioi", #kak eksanty
            "https://drive.google.com/uc?export=view&id=15O1wFRBBL-6CnyHdG03sZiObWNUIpNOf", #kak farahanum
            "https://drive.google.com/uc?export=view&id=1SJBR8830ArwIeedJJ5rpBZu4-uVP1jPZ", #bang ferdy
            "https://drive.google.com/uc?export=view&id=1Dkk4HDAX80mKS7KyeYuhAx3fKY-f45IO", #bang deri
            "https://drive.google.com/uc?export=view&id=17T8mQu7JoIJ34Gp4OtIW7OehaRj-mMjl", #kak okta
            "https://drive.google.com/uc?export=view&id=1I1D_PIcLwCclXzN6l7Zmlnagt8nAlCrQ", #bang depan
            "https://drive.google.com/uc?export=view&id=1TXUm18LQjY9Vjesd-fC5joWipaepGa7l", #bang jo
            "https://drive.google.com/uc?export=view&id=1M2bkf0VH4oIOoN1cjJCqwBgg70PH_NAz", #bag kem
            "https://drive.google.com/uc?export=view&id=137TseVQV8bjwy8rpn7jFVH3Hdf-0HLXg", #kak presilia
            "https://drive.google.com/uc?export=view&id=1ChmIvTdvsivyaMx54qkCcHKr1Cq_oO5Z", #kak rafa
            "https://drive.google.com/uc?export=view&id=1OIJyWN2aU_A7NqdDMYghhCX3uutNS3Q7", #bang sahid
            "https://drive.google.com/uc?export=view&id=1o_Gu7xby0jCOwP50ngKqo-CkzjPS9dMq", #kak vanes 
            "https://drive.google.com/uc?export=view&id=1N8IaM0W29s9Pw1UV48uidylVqw6vdfPC", #bang ateng
            "https://drive.google.com/uc?export=view&id=1FgME2Ar8gTqa5X7to2dkLgsn0rG-8AS9", #bang gede
            "https://drive.google.com/uc?export=view&id=12kIyMuSNELwUt6GZk_lPGgBsY6I9Y2CB", #kak jaclin
            "https://drive.google.com/uc?export=view&id=1KyUWdpG4tnwBO98Izq3bB-nFT4qpF7iP", #bang rafly
            "https://drive.google.com/uc?export=view&id=1SngJUeMi49X6v7qNbO_OianmKTZvv4r9", #kak syalaisha
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
                "kesan": "Mempunyai pembawaan yang tegas dan mempunyai public speaking yang keren",  
                "pesan": "Terus menginspirasi bang dan semoga impiannya bisa terwujud" #bang econ
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
                "sosmed": "@celisabeth",
                "kesan": "Punya senyum yang lucu dan asik",  
                "pesan":"Sukses dalam studinya dan semangat mengejar cita-cita kak" #kak abeth
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Marahin orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "Tegas dan seru juga",  
                "pesan": "Semangat terus kuliahnya kak dan tugas nya lancar semua!" #kak affifah
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobi": "Main",
                "sosmed": "@allyaislami_",
                "kesan": "Ramah, asik, dan baik",  
                "pesan": "Semoga sehat selalu, bahagia selalu, dan sukses dalam karirnya" #kak allya
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiyati",
                "nim": "122450001",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Metro",
                "hobi": "Nyopet",
                "sosmed": "@eksantyfebriana",
                "kesan": "Ramah, baik dan murah senyum",  
                "pesan": "Semangat terus kuliahnya kak dan semoga impiannya bisa terwujud kak!" #Kak eksanty
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobi": "Bengong",
                "sosmed": "@farahanumafifahh",
                "kesan": "Murah senyum dan keren",  
                "pesan":"Semoga segala urusannya lancar dan selalu jaga kesehatan kak!" #kak farahanum
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Jalan Pangeran Senopati Raya 18",
                "hobi": "Baca Kitab Suci",
                "sosmed": "@ferdy_kevin",
                "kesan": "Kalem dan baik",  
                "pesan":"Semangat menjalani hari-hari di perkuliahan dan semangat sukses dalam studinya bang!" #bang ferdy
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jalan Pagar Alam Kedaton",
                "hobi": "Ngukur Jalan",
                "sosmed": "@dransyh_",
                "kesan": "Abangnya lucu banget, asik, dan murah senyum",  
                "pesan":"Terus lucu ya bang dan semoga cepat lulus kuliah!" #bang deri

            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Travelling",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Baik dan keren", 
                "pesan":"Tetap semangat kak dan semoga tugas-tugasnya lancar semua" #kak okta

            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Duri, Riau",
                "alamat": "Pulau Damar Kobam",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abangnya lucu banget dan seru",  
                "pesan":"Jangan pernah cape menghibur orang ya bang" #bang depan
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobi": "Asprak",
                "sosmed": "@johanneskrsjnnn",
                "kesan": "Abangnya baik dan seru",  
                "pesan":"Semangat ngeaspraknya bang, jangan cape kalau kita tanyain terus ya!" #bang jo
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
                "pesan": "Semangat terus kuliahnya bang dan jangan cape ajarin kita" #bang kemas
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
                "pesan":"Semangat terus kuliahnya kak!" #kak presilia

            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450122",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobi": "Baca webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakaknya baik dan lucu",  
                "pesan": "Semangat terus kuliahnya kak!" #kak rafa
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok, Jabar",
                "alamat": "Jalan Airan Raya",
                "hobi": "Dengerin juicy luicy",
                "sosmed": "@sahid_maul19",
                "kesan": "Abangnya baik banget dan pembawaan bicara nya enak didengar",  
                "pesan":"Semangat terus kuliahnya bang!" #bang sahid
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Perum Korpri",
                "hobi": "Minum kopi, belajar, bikin deyvan senang",
                "sosmed": "@roselivness__",
                "kesan": "Kakaknya jago basket, asik, dan baik",  
                "pesan":"Semangat terus kuliahnya dan basketnya kak!" #kak vanessa
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
                "pesan":"Semangat terus kuliahnya bang!" #bang ateng
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
                "pesan":"Semangat terus kuliahnya bang!" #bang gede
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
                "pesan": "Semangat terus kuliahnya kak!" #kak jaclin

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
                "pesan": "Semangat terus kuliahnya bang!" #bang rafly

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
                "pesan":"Semangat terus kuliahnya kak!" #kak syalaisha
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenpsda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17PkJXwqPqa4lyeBMno1iCsnvqGy1ytYd", #bang rafi
            "https://drive.google.com/uc?export=view&id=1VV6PXcclOuKPR3mgIlaQ4H1Hljal7x3A", #kak anova
            "https://drive.google.com/uc?export=view&id=1WEWD6nfOI4FUHhnC2ohQjbc3SQXlTpQA", #bang ahmad
            "https://drive.google.com/uc?export=view&id=1SH5Ep3AglNZL-k1rkBGSmzKBD25iFGx0", #bang regi
            "https://drive.google.com/uc?export=view&id=1U7d0QQNQjA7SZuPS49q-lezyfmJv9by7", #kak syalaisha
            "https://drive.google.com/uc?export=view&id=1h00eL-OCFb9fgoTX6BRQSKVqKjFirDJw", #bang anwar
            "https://drive.google.com/uc?export=view&id=1tnIfxuKgWTPuwW5h4YrdnrIHD2iqtlGE", #kak deva
            "https://drive.google.com/uc?export=view&id=1bKU_PYXcMkF3IA6wdXRKYkDsB39k0cAc", #kak dinda
            "https://drive.google.com/uc?export=view&id=1ufAiRZrrKLPFSdZtEMviJAeGhqrLgfbE", #kak marleta
            "https://drive.google.com/uc?export=view&id=1VZkHwMbxchrmLkJZ_2nj3odt-mNVnmRJ", #kak rut
            "https://drive.google.com/uc?export=view&id=1qHkw0rNj60mtNRZi4az493RHbr5OYmWg", #kak syadza
            "https://drive.google.com/uc?export=view&id=1CXYxfH77XFnJ4ZbMXCjSwyVxxTcPopdc", #bang adit
            "https://drive.google.com/uc?export=view&id=10HtMXzV8oBASuu8L7UKsruQ_O3NmxmhB", #bang eggi
            "https://drive.google.com/uc?export=view&id=1Cp_sIhIu5a70rheKW0-_A5NXfv7cRNxj", #kak febiya
            "https://drive.google.com/uc?export=view&id=1Cziha9Z0PhCGP0fVjSDi4mM3KCF1cfo6", #bang happy
            "https://drive.google.com/uc?export=view&id=1VXrs2jQNsJHC_aUDj2nV2KVQCufotrR4", #bang randa
        ]
        data_list = [
          {
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21",
                "asal": "Lubuk Linggau",
                "alamat": "Jl. Nangka 4",
                "hobi": "Olahraga",
                "sosmed": "@rafadhilillahh13",
                "kesan": "Abangnya baik dan jago main badminton",
                "pesan": "Semangat terus kuliahnya bang!"
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Kakaknya baik dan asik",
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Abangnya baik dan seru",
                "pesan": "Semangat terus kuliahnya bang! "
            },
            {
                "nama"  : "Muhammad Regi Abdi Putra Amanta",
                "nim"   : "122450031",
                "umur"  : "19",
                "asal"  :"Palembang",
                "alamat": "Jl. Permadi",
                "hobi" : "Ngasprak ADS",
                "sosmed": "@mregiiii_",
                "kesan" : "Abangnya asik diajak bermacam gaya poto dan baik",  
                "pesan" :"Semangat terus ngeasprak dan kuliahnya bang!"

            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Gg. Yudistira",
                "hobi": "Review jurnal bu mika",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakaknya baik dan seru",  
                "pesan":"Semangat menjalani perkuliahan kak dan semoga tugasnya lancar semua"
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal":"Bukittinggi",
                "alamat": "Korpri",
                "hobi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "Abangnya baik dan pendiam",  
                "pesan":"Semangat terus kuliahnya bang!" 
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobi": "Resume Webinar",
                "sosmed": "@anjaniiidev",
                "kesan": "Kakaknya baik dan asik",  
                "pesan":"Semangat terus kuliahnya kak!"

            },
            {
               "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobi": "Membaca jurnal bu mika",
                "sosmed": "@dindanababan",
                "kesan": "Kakaknya baik dan asik",  
                "pesan":"Semangat terus kuliahnya kak!" 
            },
            {
                "nama"  : "Marleta Cornelia Leander",
                "nim"   : "122450092",
                "umur"  : "20",
                "asal"  :"Depok",
                "alamat": "Gg. Nangka 3",
                "hobi" : "Review jurnal bu mika",
                "sosmed": "@marletacornelia",
                "kesan" : "Kakaknya baik dan lembut",  
                "pesan" :"Semangat ngeaspraknya dan kuliahnya kak!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kepulauan Riau",
                "alamat": "Gg. Nangka 3",
                "hobi": "Menghitung akurasi",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakaknya baik dan murah senyum",  
                "pesan":"Semangat terus kuliahnya kak!" #kak rut

            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450074",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobi": "Membangkitkan bilangan",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya baik dan asik",  
                "pesan":"Semangat terus kuliahnya kak!" 
            },
            {
                "nama"  : "Aditya Rahman",
                "nim"   : "122450113",
                "umur"  : "20",
                "asal"  :"Metro",
                "alamat": "Korpri",
                "hobi" : "Ngoding wisata",
                "sosmed": "@rahm.adityaa",
                "kesan" : "Abangnya baik dan jago ngoding",  
                "pesan" :"Semangat terus kuliahnya bang!"
            },
            {
                "nama": "Eggi satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Korpri",
                "hobi": "Ngoding wisata",
                "sosmed": "@_egistr",
                "kesan": "Abangnya keren dan baik",  
                "pesan":"Semangat terus kuliahnya bang!"
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl. Kelengkeng Raya",
                "hobi": "Review jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakaknya lucu dan baik",  
                "pesan":"Semangat terus kuliahnya kak!"

            },
            {
               "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main game",
                "sosmed": "@sudo.syahrulramadhan",
                "kesan": "Abangnya baik dan keren",  
                "pesan":"Semangat terus kuliahnya bang!"
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Abangnya baik dan seru",  
                "pesan":"Semangat teruskuliahnya bang!" 
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal ():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1K3gjaEX0QaFYeqnuuXJPpjuM7MIZ1nlk", #bang sae tama
            "https://drive.google.com/uc?export=view&id=1kYyuqz6v6nrerLvOB22lrXvgCTDL4eXr", #kak ramadhita
            "https://drive.google.com/uc?export=view&id=1WvZPP4-CUlByfUCnNsomsyNvdFqS63bX", #kak nazwa
            "https://drive.google.com/uc?export=view&id=1PTwxv9zYpSDhnl9Agto_ECllWiefRCtc", #bang bastian
            "https://drive.google.com/uc?export=view&id=1lTb-LMphsoR3weXlKQb21jMRJNUOV9rG", #kak dea
            "https://drive.google.com/uc?export=view&id=1XJR1jNP5eKI2zMTcli948IGUrUZKnhBz", #kak ester
            "https://drive.google.com/uc?export=view&id=1zM5hQyLBKyNIP66W2qOHVqmpoLGP5LSo", #kak natasya
            "https://drive.google.com/uc?export=view&id=1HvSxj500hgqIqxnaP7wYoDkHBYfIpGaY", #kak novelia
            "https://drive.google.com/uc?export=view&id=1y4vbk9B0FYMaq2gm68yTWzg4clw7Tcj6", #kak ratu
            "https://drive.google.com/uc?export=view&id=1VO-6ifn935lDzGa4RuIFS7av4CKBAc07", #bang tobias
            "https://drive.google.com/uc?export=view&id=15vZdjkoD6aCdIi0_rROH1ILSTwnwYdkV", #kak yohana
            "https://drive.google.com/uc?export=view&id=1ioiUQOdGSIBAUeWCbbLR3Hky7Ggq4xgb", #bang rizki
            "https://drive.google.com/uc?export=view&id=1YCcxZv-qPFsM7izvH489iz0toQmMCdmr", #bang arafi
            "https://drive.google.com/uc?export=view&id=1ZqI4mEx8i1_uOvNtKHVSnxjQcTmQfzVe", #kak asa
            "https://drive.google.com/uc?export=view&id=1KU4BcP7U4LLp0UBPRFUrWZWhFi3rdwr-", #kak chalifia
            "https://drive.google.com/uc?export=view&id=1oU4G-vUWZLe7Vgia70TprppiUW7-kU2_", #bang irvan
            "https://drive.google.com/uc?export=view&id=1io1qk6Y9aVbb33kEBuEBHmKxyjcotP6O", #kak izza
            "https://drive.google.com/uc?export=view&id=1wv-ANiAqBiA8PXkxVSYhKAmaCraMjNkc", #kak alyaa
            "https://drive.google.com/uc?export=view&id=1p2IRB8hNjsyo8GmUECT3g367spF-tvIV", #bang raid
            "https://drive.google.com/uc?export=view&id=1jvg21cKs7nQbXcvyI_JaRVRarUpSHMwW", #kak yuna
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
                "kesan": "Abangnya baik dan tegas",  
                "pesan":"Semangat terus kuliahnya bang!" #bang sae tama

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
                "pesan":"Semangat terus kuliahnya kak!" #kak ramadhita
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Way Kandis",
                "hobi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakaknya baik dan seru",  
                "pesan":"Semangat terus kuliahnya kak!" #kak nazwa
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Belwis",
                "hobi": "Main Game",
                "sosmed": "@bastiansilaban_",
                "kesan": "Abangnya baik dan tinggi",  
                "pesan":"Semangat terus kuliahnya bang!" #bang bastian
            },
            {
                "nama"  : "Dea Mutia Risani",
                "nim"   : "122450099",
                "umur"  : "20",
                "asal"  :"Sumatera Barat",
                "alamat": "Korpri",
                "hobi" : "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan" : "Kakaknya baik dan seru",  
                "pesan" :"Semangat terus kuliahnya kak!" #kak dea
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450005",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Kirim BC-an",
                "sosmed": "@esteriars",
                "kesan": "Kakaknya baik dan seru",  
                "pesan":"Semangat terus kuliahnya kak!" #kak ester
            },
            {
               "nama": " Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobi": "Jadi Humas",
                "sosmed": "@natee__15",
                "kesan": "Kakaknya baik dan asik banget",  
                "pesan":"Semangat terus kuliahnya kak!" #kak natasya
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "20",
                "asal":"Saburai",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kakaknya baik dan lucu",  
                "pesan":"Semangat terus kuliahnya kak!" #kak novelia

            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobi": "Pulang malam",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya baik, seru, dan bicara nya enak didengar",  
                "pesan":"Semangat terus kuliahnya kak!" #kak ratu
            },
            {
               "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobi": "Berkebun",
                "sosmed": "@tobiassiagian",
                "kesan": "Abangnya baik, seru, dan lucu",  
                "pesan":"Semangat terus kuliahnya bang!" #bang tobias
            },
            {
                "nama"  : "Yohana Manik",
                "nim"   : "122450",
                "umur"  : "20",
                "asal"  :"Sumatera Utara",
                "alamat": "Belwis",
                "hobi" : "Menimba ilmu",
                "sosmed": "@yo_anamnk",
                "kesan" : "Kakaknya baik, ramah, dan lucu",  
                "pesan" :"Semangat terus kuliahnya kak!" #kak yohana

            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "TVRI",
                "hobi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "Abangnya baik dan seru",  
                "pesan":"Semangat terus kuliahnya bang!" #bang rizki
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Way huwi",
                "hobi": "Imam TVRI",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "Kirain abangnya pendiam ternyata orangnya rame",  
                "pesan": "Semoga lucu terus bang" #bang arafi

            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal":"Muara enim",
                "alamat": "Korpri",
                "hobi": "Nyuci baju",
                "sosmed": "@u_yippy",
                "kesan": "Kakaknya baik, asik, dan rame orangnya",  
                "pesan":"Semangat terus kuliahnya kak!" #kak asa
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobi": "Q-Time",
                "sosmed": "@chlfawww",
                "kesan": "Kakaknya baik dan lucu",  
                "pesan":"Semangat terus kuliahnya kak!" #kak chalifia

            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya baik dan murah senyum",  
                "pesan":"Semangat terus kuliahnya bang!" #bang irvan
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan": "Kakaknya ramah banget, asik, dan counternya bokem",  
                "pesan":"Semangat ngaspraknya kak, jangan cape ajarin kita ya kak" #kak izza
            },
            {
               "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Jadi daplok kelompok 1",
                "sosmed": "@alyaavanefi",
                "kesan": "Kakaknya lucu gemes, baik banget, dan seru",  
                "pesan":"Semangat terus kuliahnya ya kak dan jangan pernah cape ajarin dan ingetin kita" #kak alyaa

            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Telat",
                "sosmed": "@rayths_",
                "kesan": "Abangnya baik dan pendiam",  
                "pesan":"Semangat terus kuliahnya bang!" #bang raid
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Sukarame",
                "hobi": "Membaca chat",
                "sosmed": "@tria_y062",
                "kesan": "Kakaknya baik, orangnya rame, dan asik",  
                "pesan":"Semangat terus kuliahnya kak, jangan cape ajarin kita ya kak!" #kak yuna
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1T-p_S1yFRkSIwtXB4PShNKRf_LMID3Rv", #bang dimas
            "https://drive.google.com/uc?export=view&id=1uyY8GKyHfBTbUKKWeYLWRItCeqeOkewv", #kak catherine
            "https://drive.google.com/uc?export=view&id=12ZdBE9sVhvJP87daxMutDX5M1MMc9CdW", #bang akbar
            "https://drive.google.com/uc?export=view&id=1ORrab4Xz_trIxvrXMfPd8ZTVsRs1psFL", #kak rani
            "https://drive.google.com/uc?export=view&id=10f49Q00x1DmXOGdU_nY8sCo0wows2Aeh", #bang rendra
            "https://drive.google.com/uc?export=view&id=1du6sGu33HnIzkyqUoAufvF9WhUGYl4jg", #kak salwa
            "https://drive.google.com/uc?export=view&id=1WvV7wEN1GqJsvu_dxXaXrRn9WX_ucIdZ", #bang ari
            "https://drive.google.com/uc?export=view&id=1neTbnPqJF2KbE1ymCRA1edeY_MQ8B2mQ", #kak azizah
            "https://drive.google.com/uc?export=view&id=1IBiR6PkvU-0ZVzFZ2y6AdaVPUrV8VOne", #kak meira
            "https://drive.google.com/uc?export=view&id=1CxOxBUQwjb1QZNJsTdzTWSlsmiO0oseR", #bang rendi
            "https://drive.google.com/uc?export=view&id=1Ab1aeuMbgGCVnsIHWPAAnda3H533IrBF", #kak renta
            "https://drive.google.com/uc?export=view&id=1HC-IN_oBQ_lqdc-SdUWYiC4M5nnLS6d4", #bang yosia
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
                "kesan": "Pembawaan abangnya asik banget dan banyak bercandanya jadi seru",  
                "pesan": "Semangat terus bang kuliahnya semoga cepat lulus" #bang dimas
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca novel",
                "sosmed": "@Catherine.sinaga",
                "kesan": "Kakaknya baik dan kalem",  
                "pesan":"Semangat terus kuliahnya kak!" #kak catherine

            },
            {
                "nama": "Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Labuhan Dalam",
                "hobi": "Memelihara Dino",
                "sosmed": "@akbar_resdika",
                "kesan": "Abangnya baik dan asik",  
                "pesan":"Semangat terus kuliahnya bang!" #bang akbar
            },
            {
               "nama": "Rani Puspita sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Kakaknya baik dan ramah",  
                "pesan":"Semangat terus kuliahnya kak!" #kak rani
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobi": "Nulis lagu",
                "sosmed": "@rendaepr",
                "kesan": "Abangnya baik dan seru",  
                "pesan":"Semangat ngeasprak dan kuliahnya bang!" #bang rendra

            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan raya",
                "hobi": "Ngeliat cogan",
                "sosmed": "@slwfn_694",
                "kesan": "Kakaknya baik dan asik",  
                "pesan":"Semangat terus kuliahnya kak!" #kak salwa

            },
            {
                "nama": "Ari Sigit",
                "nim": "121450",
                "umur": "23",
                "asal":"Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobi": "Main Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "Abangnya baik dan asik",  
                "pesan":"Semangat terus kuliahnya bang!" #bang ari
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Jati Mulyo",
                "hobi": "Bangun Pagi",
                "sosmed": "@azizahksmh15",
                "kesan": "Kakaknya baik dan ramah",  
                "pesan":"Semangat terus kuliahnya kak!" #kak azizah
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobi": "Nonton",
                "sosmed": "@meirasty_",
                "kesan": "Kakaknya baik dan seru",  
                "pesan":"Semangat terus kuliahnya kak!" #kak meira
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Benawang",
                "hobi": "Berenang di Laut",
                "sosmed": "@rexander",
                "kesan": "Abangnya baik dan kalem",  
                "pesan":"Semangat terus kuliahnya bang!" #bang rendi
            },
            {
                "nama": "Renita Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobi": "Membaca dan Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya baik dan seru",  
                "pesan":"Semangat terus kuliahnya kak!" #kak renta
            },
            {
                "nama": "Yosia Retare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobi": "Nungguin ayam betina berkokok",
                "sosmed": " @yosiabanurea",
                "kesan": "Abangnya baik dan asik",  
                "pesan":"Semangat terus kuliahnya bang!" #bang yosia
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd ():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1wh-E-p6hkTcVH7VRuz8wUM2mDZ9EnjaT", #bang andrian
            "https://drive.google.com/uc?export=view&id=18K5C4MZiqz2pQ5P_Z-UIvrz0fTM6ecv5", #kak adisty
            "https://drive.google.com/uc?export=view&id=1caPOnmQF3qfq6WL_yoAPkvdXo_sbgR9l", #kak nabila
            "https://drive.google.com/uc?export=view&id=1Mhmlk24CVjZv3mvihOpYNWHVy8nMsFio", #bang ahmad
            "https://drive.google.com/uc?export=view&id=1MCjv-TtCuDNK-aRtA-ztVyfUEy8zAc-q", #bang danang
            "https://drive.google.com/uc?export=view&id=1q5kjAwp0G7evmtneWRpvIdaDcMsJYtPN", #bang farrel
            "https://drive.google.com/uc?export=view&id=1Xhupp8cLRiKnT2AkV-tVnfYZAVpzfsCD", #kak tessa
            "https://drive.google.com/uc?export=view&id=1TTpGU3TBnPPgFNpjE8Na3wUlQO5wM-rd", #kak nabilah
            "https://drive.google.com/uc?export=view&id=1QqFmmKlM1iW_RNj1d4lY7Zj_hPGnzZ3m", #kak alvia
            "https://drive.google.com/uc?export=view&id=1UchEzLHtPoYekdnrJGJNOet-WDX9KeO-", #bang dhafin
            "https://drive.google.com/uc?export=view&id=1xmNuEJyqxWCkN5psRDOoBPTNyDKMswyb", #kak elia
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
                "kesan": "Abangnya baik dan seru banget",  
                "pesan":"Semangat terus kuliahnya bang!" #bang andrian

            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Kakaknya baik dan seru",  
                "pesan":"Semangat terus kuliahnya kak!" #kak adisty
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal":"Simalungun, Sumut",
                "alamat": "Airan",
                "hobi": "Hitung uang",
                "sosmed": "@zhjung_",
                "kesan": "Kakaknya baik dan asik",  
                "pesan":"Semangat terus kuliahnya kak!" #kak nabila

            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Bukittinggi",
                "alamat": "Airan 1",
                "hobi": "Badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "Abangnya baik dan keren",  
                "pesan":"Semangat terus kuliahnya bang!" #bang ahmad
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Airan",
                "hobi": "Nyuruh-nyuruh",
                "sosmed": "@dananghk_",
                "kesan": "Abangnya lucu suka ngelawak, seru banget, dan baik banget",  
                "pesan":"Semangat jualan dan kuliahnya bang!" #bang danang
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Lapas",
                "hobi": "Apa aja",
                "sosmed": "@farrel_julio",
                "kesan": "Abangnya baik dan asik",  
                "pesan":"Semangat terus kuliahnya bang!" #bang farrel

            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Simalungun, Sumut",
                "alamat": "Pemda",
                "hobi": "Suka nulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakaknya baik dan seru", 
                "pesan":"Semangat terus kuliahnya kak!" #kak tessa
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal":"Kedaton",
                "alamat": "Kedaton",
                "hobi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Kakaknya baik dan seru",  
                "pesan":"Semangat terus kuliahnya kak!" #kak nabilah
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobi": "Nonton windah",
                "sosmed": "@alviagnting",
                "kesan": "Kakaknya baik dan kalem",  
                "pesan":"Semangat terus kuliahnya kak!" #kak alvia
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Balam",
                "alamat": "Jalan Nangka 1",
                "hobi": "Tidur",
                "sosmed": "@dhafinrzqa",
                "kesan": "Abangnya baik dan seru",  
                "pesan":"Semangat terus kuliahnya kak!" #bang dhafin
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobi": "Badminton",
                "sosmed": "@meylanielia",
                "kesan": "Kakaknya baik dan seru",  
                "pesan":"Semangat terus kuliahnya kak!" #kak elia
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1e1pYUq3PoQA6sH9TmpviNGl_Xi3QdPB1", #bang wahyu
            "https://drive.google.com/uc?export=view&id=1sFmFz-X3SGwSrySZO43uIlrKuT--_oPw", #kak elok
            "https://drive.google.com/uc?export=view&id=12o_S0QQssjQ1G1x-NprCk_KEieMDMUx9", #kak arsyiah
            "https://drive.google.com/uc?export=view&id=1E2kaV8ZMNrf02MR55ZfcDqUxsfAqk7m1", #kak cibel
            "https://drive.google.com/uc?export=view&id=1XeDPBqw3BnABTpiT0lDOGVHLR9Q1z-KF", #kak eka
            "https://drive.google.com/uc?export=view&id=1WYOp2q4Dj3QN9_nBzi3LwOcUSILo5MG1", #kak najla
            "https://drive.google.com/uc?export=view&id=1-QL3uLt-Xi610DGmFhUzdVw5wRfGJAQW", #kak cia
            "https://drive.google.com/uc?export=view&id=1it1hAhKz1afPONuFGUrddfG8gYJtQH5I", #kak rahma
            "https://drive.google.com/uc?export=view&id=1HXLT18rQH6E6HTYR_QHnGtfnMkIZdTOF", #kak try
            "https://drive.google.com/uc?export=view&id=1tRMBKV75gX5tvVeK7euGp41PgL9HvqKv", #bang kaisar
            "https://drive.google.com/uc?export=view&id=1TbEJbBSg_dBwTwaiUR5-ADf266s7dJUR", #kak dwi
            "https://drive.google.com/uc?export=view&id=1RXBLddKM8ZShOPJtK4Ie2ZWfg1e5FI3h", #bang gym
            "https://drive.google.com/uc?export=view&id=10MMcm2PpO-1Kze2rJ9hJ7SZbqw0IULCR", #kak nasywa
            "https://drive.google.com/uc?export=view&id=1f-dhjqMJ4SoB0wDaH-T-oHJq3hThFJcp", #kak priska
            "https://drive.google.com/uc?export=view&id=1UNB2u9mWwncigR5M1XLcCW-uRS7Qn-hm", #bang arsal
            "https://drive.google.com/uc?export=view&id=17hZAx1uwJsfGYF2PZLBhcp-pHdd4g4Kv", #kak khusnun
            "https://drive.google.com/uc?export=view&id=1bZRdue4fowxRS6K8AIVN_98bnk-tnS-E", #bang abit 
            "https://drive.google.com/uc?export=view&id=1lWeVU6njoLCfkLICaTQ2wWUzirFttTY4", #bang akmal
            "https://drive.google.com/uc?export=view&id=1hgQwAS5CYwQ_O0CO3A342bAH7tFtN9rA", #bang hermawan
            
        ]
        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal":"Makassar",
                "alamat": "Sukarame",
                "hobi": "Nonton",
                "sosmed": "@",
                "kesan": "Abangnya baik dan pembawaan bicaranya enak didengar",  
                "pesan":"Semangat terus kuliahnya bang!" #bang wahyu
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "Kakaknya baik dan asik",  
                "pesan":"Semangat terus kuliahnya kak!" #kak elok
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobi": "Nugas",
                "sosmed": "@arsyiah._",
                "kesan": "Kakaknya baik dan lucu",  
                "pesan":"Semangat terus kuliahnya kak!" #kak arsyiah
            },
            {
               "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Kakaknya baik dan tinggi",  
                "pesan":"Semangat terus kuliahnya kak!" #kak cibel
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": "122450045",
                "umur": "20",
                "asal":"Natar, Lampung Selatan",
                "alamat": "Natar, Lampung Selatan",
                "hobi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "Kakaknya baik dan ramah",  
                "pesan":"Semangat terus kuliahnya kak!" #kak eka
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "Kakaknya baik dan keren",  
                "pesan":"Semangat terus kuliahnya kak!" #kak najla
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobi": "Nonton Film",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakaknya baik dan seru",  
                "pesan":"Semangat ngeasprak dan kuliahnya kak!" #kak patricia
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Sukarame",
                "hobi": "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan": "Kakaknya baik, ramah banget, dan lucu",  
                "pesan":"Semangat terus kuliahnya kak!" #kak rahma
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakaknya baik dan seru",  
                "pesan":"Semangat terus kuliahnya kak!" #kak try
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar",
                "hobi": "Lagi Nyari",
                "sosmed": "@dino_kiper",
                "kesan": "Abangnya baik dan tinggi",  
                "pesan":"Semangat terus kuliahnya bang!" #bang muhammad
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobi": "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan": "Kakaknya baik dan kalem",  
                "pesan":"Semangat terus kuliahnya kak!" #kak dwi
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf UIN",
                "hobi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "Abangnya baik dan seru",  
                "pesan":"Semangat terus kuliahnya bang!" #bang gym
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobi": "Nonton drakor",
                "sosmed": "@nsywanaf",
                "kesan": "Kakaknya baik dan asik",  
                "pesan":"Semangat terus kuliahnya kak!" #kak nasywa
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. Nangka 2",
                "hobi": "Baca Novel yang Bikin Nangis",
                "sosmed": "@prskslv",
                "kesan": "Kakaknya baik dan ramah",  
                "pesan":"Semangat terus kuliahnya kak!" #kak priska
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka 4",
                "hobi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "Abangnya baik dan seru",  
                "pesan":"Semangat terus kuliahnya bang!" #bang arsal
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Belwis",
                "hobi": "Mengerjakan Tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Kakaknya baik, seru, dan enak diajak diskusi",  
                "pesan":"Semangat terus kuliahnya kak!" #kak khusnun
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa Labuhan dalam",
                "hobi": "Ngoding, gaming",
                "sosmed": "@abitahmad",
                "kesan": "Abangnya murah senyum, lucu, dan seru",  
                "pesan":"Semangat terus kuliahnya bang!" #bang abit
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Kelihatannya abangnya asik, baik dan seru",  
                "pesan":"Semangat terus kuliahnya bang!" #bang akmal
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani)",
                "hobi": "Bengong/Membaca Buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Asik banget, sangat friendly, dan lucu",  
                "pesan":"Semangat ngeasprak dan menjalani hari-harinya di perkuliahan bang!" #bang hermawan
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

    

