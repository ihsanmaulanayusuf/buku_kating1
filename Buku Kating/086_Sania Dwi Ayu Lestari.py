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
            "https://drive.google.com/uc?export=view&id=1iMCqW9bXwE4KSx5QmklmzlpcRKk7-QjX",
            "https://drive.google.com/uc?export=view&id=1iJceiXU0E5BI6lKFlHeMCJ47nl4EKJ9b",
            "https://drive.google.com/uc?export=view&id=1iNot2bz55FPfcV2OYlzeRG_LIQSa5E_e",
            "https://drive.google.com/uc?export=view&id=1i6q-6USMexKlprmqHNseMH7MzVPbgO4f",
            "https://drive.google.com/uc?export=view&id=1i5Kg191Sp7sGeTWAtx8BvvI3swdx8lWb",
            "https://drive.google.com/uc?export=view&id=1iN_zu1Jt_6KkXLK96qIY73G9otzhuBjc",
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
                "kesan": "Charming person",  
                "pesan":"Semangat dan sukses selalu bang gumi"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Bukit kemuning",
                "alamat": "Pawen 2 Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni21",
                "kesan": "Charismatic dan Sociable, ngobrol sampe pagi pun ga akan keabisan topik",  
                "pesan":"semangat terus kuliahnya bang pandra!"# 2
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar alam",
                "alamat": "Kotabaru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakanya inspiring, jadi waktu ngobrol bikin kita termotivasi dan berpikir lebih jauh",  
                "pesan":"terimakasi sesi sharing session nya ka sehat selalu"# 3
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "kakanya keliatan tegas dan percaya diri",  
                "pesan":"sangat berkesan, doa terbaik buat kakak"# 4 
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "kakanya serene alias kepribadian nya kaya kalem tenang gitu",  
                "pesan":"terimakasih sudah meluangkan waktunya kak, sukses ya kak!"# 5
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kotabaru",
                "hobbi": "Dengerin bang pandra giatara",
                "sosmed": "@nadillaadr26",
                "kesan": "Fun-loving dan ceria",  
                "pesan":"semoga sukses dan cita citanya tercapai ya ka"# 1 
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fgWqssmUziuaHQFIhr_DGWdhbn4q529v", #1
            "https://drive.google.com/uc?export=view&id=1fyaC5ll6cdrFiObneJq1_ZiHe16DpQY6", #2
            "https://drive.google.com/uc?export=view&id=1g6XAp6EaGDT4VRU_P_ZzZy9YV2OjQlso", #3
            "https://drive.google.com/uc?export=view&id=1gKwnARsd07N3GCM8X465ikdrD-DEPHUW", #4
            "https://drive.google.com/uc?export=view&id=14qk7upfYCxCRKkfyquWu9qCIpRgWUbOn", #8
            "https://drive.google.com/uc?export=view&id=1fvDgdR0Wfk9_Kmg84MCOsO7TdHhSuDU5", #11
            "https://drive.google.com/uc?export=view&id=1gQ9B0HT3YhoWyrbNB3RZJVVmMdiz4GkG", #5
            "https://drive.google.com/uc?export=view&id=1gFk42bc_4efBRkvym4etYFX6WXIMPjzp", #6
            "https://drive.google.com/uc?export=view&id=1LU_c5E3NkzBBiw5WwJJ6FfCsAEy1q6rg", #7
            "https://drive.google.com/uc?export=view&id=14qbyVX3Ecvd7NjVC6K9fDRv6_PH17rIY", #9
            "https://drive.google.com/uc?export=view&id=1fjhLldMZX79mtV2naj7MXNd5BBQaDo3-", #10
            "https://drive.google.com/uc?export=view&id=1gJhtp3YxE2T4LAIQlwFHTY2RGsX3rJz-", #12
            "https://drive.google.com/uc?export=view&id=1gITGp2A-lpgSSNxPzgDuXCh4J6i79QYS", #13
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden saleh",
                "hobbi": "Bertanya sama GPT",
                "sosmed": "@trimurniaa_",
                "kesan": "Engaging sama friendly banget, cara ngomongnya bikin orang betah dengerin dan wawasannya luas jadi seru",  
                "pesan":"every small step takes you closer to your goal, semoga terus menginspirasi kak!" 
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tangerang selatan",
                "alamat": "way hui",
                "hobbi": "Membaca",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Vibes kakanya Maternal authority, kaya kalem yang lemah lembut",  
                "pesan":"Stay focused, your hard work will pay off! semangat kuliah ka!!"# 2
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton film",
                "sosmed": "@wlsbn0",
                "kesan": "definisi beauty with brains, kak kamu menginspirasi bgt!",  
                "pesan":"semangat kuliah ka, sukses selalu, stay positive, work hard, and make it happen"# 3
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jati agung",
                "hobbi": "Nonton Drachin",
                "sosmed": "@anisadini10",
                "kesan": "kakanya cantik, asik, soft spoken",  
                "pesan":"makasih atas motivasinya, "# 4
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung timur",
                "alamat": "Lampung timur",
                "hobbi": "Baca jurnal",
                "sosmed": "@dylebee",
                "kesan": "cantik bangettt",  
                "pesan":"semoga dipermudah dalam segala hal ya kak, semangat!"# 8
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Melukis",
                "sosmed": "@fhrul.pdf",
                "kesan": "abangnya baik, tapi sedikit pendiem",  
                "pesan":"semangat kuliah ya bang, semoga diperlancar dalam segala hal"# 11
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bernug Pesawaran",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakot",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak humble banget, semoga ilmunya berkah dan sukses!",  
                "pesan":"Jaga kesehatan dan semangat selalu, Kak"# 5
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Belwis",
                "hobbi": "Sholat duha",
                "sosmed": "@fer_yulius",
                "kesan": "abangnya pendiem, tapi penjelasan nya mudah dipahamin ",  
                "pesan":"Semangat bang, semoga apa yang di cita citain tercapai"# 6
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar lampung",
                "alamat": "Teluk betung",
                "hobbi": "Baca al-qur'an",
                "sosmed": "@fleurnsh",
                "kesan": "kakanya lucu, mirip temen sma ku",  
                "pesan":"Semoga sehat-sehat terus dan sukses selalu!"# 7
            },
            {
               "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main kucing",
                "sosmed": "@myrriinn",
                "kesan": "bang mirzan baik,",  
                "pesan":"semoga terus menginspirasi ya bang!"# 9
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Ogan Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari sinyal di gedung f",
                "sosmed": "@_.dheamelia",
                "kesan": "kak dhea asik, friendly banget",  
                "pesan":"semoga hari harinya terus berwarna ya kak!"# 10
            },
             {
               "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatra Barat",
                "alamat": "Way Huwi",
                "hobbi": "Baca buku, ngoding, ibadah",
                "sosmed": "@berlyyanda",
                "kesan": "kakanya baik, tapi kayanya aga introvert",  
                "pesan":"semangat terus kak, semoga hari harinya penuh energi"# 12
            },
            {
               "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Billabong, Gedong air",
                "hobbi": "Suka bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "bang jere baik banget asik jugaa  humoris jadinya seru ga tegang",  
                "pesan":"Semangat kuliahnya bang!"# 13
            },  
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator ():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mM9apWiLnliAJIgdKSU09bpdO3qNW-v8",
            "https://drive.google.com/uc?export=view&id=1mO-iRiFk11rX_qJHnp8x5iKXQJU0-RdS",
        ]
        data_list = [
            {
                "nama": "Anissa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal":"Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi": "Bernyanyi",
                "sosmed": "@annisalutfia_",
                "kesan": "kakanya asik, publik speakingnya bagus banget",  
                "pesan":"semoga terus menginspirasi ya kak upi!!" #1

            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kota baru",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "bang bintang tegas tapi bisa asik juga kalo ngobrol, waawasan nya luas jadi seru",  
                "pesan":"Jangan berhenti berbagi ilmu, ya bang!" #2

            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def departemenpsda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kxKOuBdBcNLPnHrzKeliGCvQz3ZltV8V", #1
            "https://drive.google.com/uc?export=view&id=1lGu70rWDDpkVRpa9cRGLZRMzrmBNKdGK", #2
            "https://drive.google.com/uc?export=view&id=1kjp3ld_lqrneYkR5uBaZuBrcaLypSQEQ", #3
            "https://drive.google.com/uc?export=view&id=1kk8O_bT_Qn1kUW3ePNXZyVR0EY0AtzrT", #4
            "https://drive.google.com/uc?export=view&id=1l68HV_2dJCE_fzMxiQj3kPGtUZbKYqOr", #5
            "https://drive.google.com/uc?export=view&id=1kl4fosqOdBaMur1DMlnnSy2WTqaORx83", #6
            "https://drive.google.com/uc?export=view&id=1k_N0NWKTlAgW_0eU5BPOB48XsQBcK5IM", #7
            "https://drive.google.com/uc?export=view&id=1km_WYwb3yOBevAqdP0xNV5d33myvM8Ff", #8
            "https://drive.google.com/uc?export=view&id=1l8lXiNTNVrbjGlNS-LTksZNcBCuNFWVe", #9
            "https://drive.google.com/uc?export=view&id=1kcQIhguidw01Is36N7mXwUqK_as2C95y", #10
            "https://drive.google.com/uc?export=view&id=1kdrU2AwCeOUjikTsoQmTMB50u1eQVuIt", #11
            "https://drive.google.com/uc?export=view&id=1knKy2B1gBMnkfx6Zd3sC2lWDD-gyu-Zg", #12
            "https://drive.google.com/uc?export=view&id=1kkjGxzjnaG5gznpCjpGFBECACuz8iZMz", #13
            "https://drive.google.com/uc?export=view&id=1l94wpBW5tRsqikDVwd04dYL7MZaoDWkQ", #14
            "https://drive.google.com/uc?export=view&id=1lE75AV0F5SM4BHS3IK_-5jpH61c98sVJ", #15
            "https://drive.google.com/uc?export=view&id=1lDqzBgknljRlHeJsjUTMP2TpK4NZvIwl", #16
            "https://drive.google.com/uc?export=view&id=1kU6qJ8wzb4N1REuRYXHefmJn6y_bET90", #17
            "https://drive.google.com/uc?export=view&id=1kVYbs2E6394NaYZBZJ78Z2losM3Bg7bC", #18
            "https://drive.google.com/uc?export=view&id=1lGnY5-IftXz9HH3X_5rDfS8eruEeis7o", #19
            "https://drive.google.com/uc?export=view&id=1kWg5hvU0j95IXgyqVxU1-VwvFxH5nIU8", #20
            "https://drive.google.com/uc?export=view&id=1kX0sE6FG3Py2ZUq6cAbzPcD1IP_WJdFZ", #21
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abangnya kritiss, wawasan nya luas, tegas juga, kalo jadi pemateri seruuu",  
                "pesan":"semoga semua planning nya berjalan sesuai yang udah direncanain ya bang"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@eelisabeth",
                "kesan": "Kakaknya ekspresif banget",  
                "pesan":"semangat kuliah ka abeth, semoga selalu dikelilingin orang orang baik"# 2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Marahin orang",
                "sosmed": "@afifahnsrn",
                "kesan": "Cantikk bangettt",  
                "pesan":"Keep being awesome!!"# 3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg.sakum",
                "hobbi": "Gg. Perwira Belwis",
                "sosmed": "@allyaislami_",
                "kesan": "kak allya baik seru juga asikk kalo ngobrol",  
                "pesan":"Keep it fun, kak! semoga semua impian nya terwujud"# 4
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Metro",
                "hobbi": "Nyopet",
                "sosmed": "@eksantyfebriana",
                "kesan": "vibesnya pinter ternyata emang beneran pinter, baik jugaa",  
                "pesan":"semoga terus menginspirasi ya kak, terimakasi atas ilmunya!"# 5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Bengong",
                "sosmed": "@farahanumafifah",
                "kesan": "kak hanum vibesnya kalem, tapi bisa tegas juga",  
                "pesan":"keep shining kak hanum"# 6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "19",
                "asal":"Medan",
                "alamat": " Jalan Pangeran Senopati Raya 18",
                "hobbi": "Baca Kitab Suci",
                "sosmed": "@ferdy_kevin",
                "kesan": "abangnya seruu, vibesnya tenang yang langsung aksi ga cuma ngomong",  
                "pesan":"semoga dipermudah kuliahnya ya bang, semangat!"# 7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jalan Pagar Alam Kedaton",
                "hobbi": "Ngukur Jalan",
                "sosmed": "@dransyah_",
                "kesan": "bang dery asik banget, punya cara tersendiri buat cairin suasana",  
                "pesan":"semoga terus bawa energy positif ya bang deri!"# 8
            },
            {
                "nama": "Oktavia Nurwinda Puspitasari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Travelling",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "kakanya baik, tegas, tapi sedikit pendiam",  
                "pesan":"Keep that calmness kak okta"# 9
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Duri, Riau",
                "alamat": "Pulau damar, Kobam",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "abangnya seru, asikk, bisa bikin suasana jadi ceria,",  
                "pesan":"semoga terus berbagi keceriaan ya bang!"# 10
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Asprak",
                "sosmed": "@johanneskrsjnnn",
                "kesan": "Bang jo asik, tapi kadang bikin segen juga, seru banget apalagi pas supporteran",  
                "pesan":"semangat terus menjalani hobi jadi asprak bang, terimakasi atas ilmunya"# 11
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Golf Asri",
                "hobbi": "Ngetik print hello dunia",
                "sosmed": "@kemasverii",
                "kesan": "Bang kemas asikk, vibesnya pinter ternyata beneran pinter, pj tugas terbaik",  
                "pesan":"semoga terus berbagi ilmu ya bang, dan bisa jadi inspirasi semua orang"# 12
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Kota baru",
                "hobbi": "Dengerin the adams",
                "sosmed": "@presilliamg",
                "kesan": "kak lili cantik banget, cantik yang kalem gitu",  
                "pesan":"Keep being your lovely self kak lili!"# 13
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Baca webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "vibesnya kalem",  
                "pesan":"semoga bisa lebih banyak ngobrol tentang tari ya kak!"# 14
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Depok, Jawa barat",
                "alamat": "Jalan airan raya",
                "hobbi": "Dengerin juicy luicy",
                "sosmed": "@sahid_maul19",
                "kesan": "bang sahid baik banget, enak buat diajak diskusi",  
                "pesan":"jangan berubah ya bang, terus jadi orang baik!"# 15
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Minum kopi, belajar, bikin deyvan senang",
                "sosmed": "@roselivness",
                "kesan": "kakanya baik, seru kalo ngobrol selalu punya kata kata yang tepat",  
                "pesan":"tetap ramah dan rendah hati ya ka!"# 16
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "pembawaan nya santai, friendly jugaa, suka menolong",  
                "pesan":"terus jadi orang baik ya bang! terimakasi sudah jadi orang baik"# 17
            },
            {
                "nama": "Gede Moena",
                "nim": "122450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri raya",
                "hobbi": "Belajar, game, baca komik",
                "sosmed": "@gedemoeanaa",
                "kesan": "abangnya baik, seru buat diajak ngobrol sharing sharing",  
                "pesan":"keep it up bang gede"# 18
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv",
                "kesan": "kakanya asik lucuuu, positif vibes",  
                "pesan":"keep shining and keep spreading good vibes!!"# 19
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main game",
                "sosmed": "@raflyy_pd",
                "kesan": "bang rafly baik, tapi sedikit pendiem",  
                "pesan":"semangat ya bang kuliahnya"# 20
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@syalaisha.i_",
                "kesan": "kaget ternyata kakanya kembar, kirain double job",  
                "pesan":"terus jadi diri sendiri ya kak!"# 21
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenpsda()

elif menu == "Departemen MIKFES":
    def departemen_mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kDkY9KTNHjG4e5fFM7mCMN0kPkOIX4__", #45
            "https://drive.google.com/uc?export=view&id=1jy-PYDPUWvNDz1R7uQtrtEnyirhZA5Lo", #46
            "https://drive.google.com/uc?export=view&id=1kMksdNEBMa6Ki7Fw2TxiG4p4o3cevwvW", #47
            "https://drive.google.com/uc?export=view&id=1jrm1F_aGBULyebm19gl4iDD-De8Q0S8b", #48
            "https://drive.google.com/uc?export=view&id=1jruEr76pEtxra_-HyHIlgrgY10gQpvG1", #49
            "https://drive.google.com/uc?export=view&id=1k7GsUHnJIwihWt83AgqrBy-O06Go1E4o", #50
            "https://drive.google.com/uc?export=view&id=1jvRa8gTYCLP40RlvJzfMFeZxXeBDfE-d", #51
            "https://drive.google.com/uc?export=view&id=1kF2DjhSt4IpK27adCZTeWGTc5tW2MxyI", #52
            "https://drive.google.com/uc?export=view&id=1kMmENXi1NueCKsmbGrR-YgCJndoItKO1", #53
            "https://drive.google.com/uc?export=view&id=1jql44JWq3VGxSJV6bI5TbPqv27kVnqVT", #54
            "https://drive.google.com/uc?export=view&id=1kKdsobmYmJOUQS1RxV7lzwvWMF_DwvJg", #55
            "https://drive.google.com/uc?export=view&id=1kH8BeroSMTXItrDSlVTf9B64mIdDtI5r", #56
            "https://drive.google.com/uc?export=view&id=1kRS4LToSnbO7YKnglQ9rwYjwzgCn75Ja", #57
            "https://drive.google.com/uc?export=view&id=1k8zAp2zMGyNZi8ttDxrqB8-k_LJsiLrD", #58
            "https://drive.google.com/uc?export=view&id=1jpkeQR7ysuQKABd3BAejFpTYWB_YoU7B", #59
            "https://drive.google.com/uc?export=view&id=1kAEH8NC_fM6HxUgF-IVjDuyI4asbc5m3", #60
        ]
        data_list = [
            {
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21",
                "asal":"Lubuk Linggau, Sumatera Selatan",
                "alamat": "Jl. Nangka 4",
                "hobbi": "Olahraga",
                "sosmed": "@rafadhlillahh13",
                "kesan": "abangnya baik, public speakingnya bagus ga muter muter langsung ke inti",  
                "pesan":"terus menginspirasi ya bang, tetap jadi keren" #45
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "19",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Sebesi",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "kakanya fast respond, baik banget ramah lagi",  
                "pesan":"semangat kuliah dan terus berkarya kak" #46
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "19",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "abangnya baik seru buat sharing sharing",  
                "pesan":"semangat kuliah ya bang, tetap rendah hati" #47
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl. Permadi",
                "hobbi": "Ngasprak ADS",
                "sosmed": "@mregiiii_",
                "kesan": "abangnya baik, menuruti semua request gaya lucu lucu",  
                "pesan":"semangat menjalani hari hari di itera yang panas bang, semangat menjalani berbagai kegiatan" #48
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Gg. Yudistira",
                "hobbi": "Review jurnal Bu Mika",
                "sosmed": "@",
                "kesan": "kakanya kalem pendiem, kembaran kaka yang di psda",  
                "pesan":"Semangat terus kak" #49
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "19",
                "asal":"Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@",
                "kesan": "baikk dan agag pendiam",  
                "pesan":"semangat menggapai cita cita ya bang" #50
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Resume Webinar",
                "sosmed": "@anjaniiidev",
                "kesan": "kakanya kalem gitu, asik baik jugaa murah senyum",  
                "pesan":"semoga dipermudah kuliahnya ya kak!" #51
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Membaca jurnal Bu Mika",
                "sosmed": "@dindanababan",
                "kesan": "kakak baik ",  
                "pesan":"semoga tetap humble, semangat terus kak" #52
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Review jurnal Bu Mika",
                "sosmed": "@marletacornelia",
                "kesan": "kakanya baik dan ceriaa, seru diajarin praktikum sama kaka ini",  
                "pesan":"terus berbagi ilmu ya ka, semangattttt" #53
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "19",
                "asal":"Kepulauan riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Menghitung akurasi",
                "sosmed": "@junitaa_0406",
                "kesan": "kakanya murah senyum",  
                "pesan":"semangat buat lebih berkembang kak! terus menginspirasi ya!" #54
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Membangkitkan bilangan",
                "sosmed": "@puspadr",
                "kesan": "baikk keren juga",  
                "pesan":"Semoga terus membagikan lebih banyak ilmu!" #55
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "19",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Ngoding wisata",
                "sosmed": "@rahm_adityaa",
                "kesan": "abangnya kaya pendiem kalem tapi pinter",  
                "pesan":"semoga sukses dan semangat menjalani kuliahnya bang" #56
            },
            {
                "nama": "Eggi satria",
                "nim": "122450032",
                "umur": "19",
                "asal":"Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding wisata",
                "sosmed": "@_egistr",
                "kesan": "bang egi public speakingnya jago, kerennn",  
                "pesan":"semangat untuk terus berkembang dan menginspirasi banyak orang" #57
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "19",
                "asal":"Tulang bawang",
                "alamat": "Jl. Kelengkeng Raya",
                "hobbi": "Review jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "cantik banget lucu juga, tapi keknya aga introvert",  
                "pesan":"terus berbagi ilmu ya kak, semangat studinya!" #58
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@sudo.syahrulramadhann",
                "kesan": "abangnya asik, jelasin nya gampang dimengerti pas lagi ngasprak",  
                "pesan":"semoga beneran jadi data scientist yang keren ya bang!" #59
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "abangnya keliatan pinter",  
                "pesan":"tetap jadi diri sendiri ya bang" #60
            },
         ]
        display_images_with_data(gambar_urls, data_list)
    departemen_mikfes()

elif menu == "Departemen Eksternal":
    def departemeneksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hR6zHwJo9c7GsY5XZGcF_r9ROQPMhdpH", #1
            "https://drive.google.com/uc?export=view&id=1hKWeDIwI-h373OEM6wfpofvXhUlIkGGh", #2
            "https://drive.google.com/uc?export=view&id=1h-OKHg-df0KcIkw073PG3hlpk7IN3_Xj", #3
            "https://drive.google.com/uc?export=view&id=1gpLmmWiOzRv4hujh6keQfK4xrvO_GaL3", #4
            "https://drive.google.com/uc?export=view&id=1hDnxPSsf4Vb_j1RIsgUxpSGUCtJLs-ui", #5
            "https://drive.google.com/uc?export=view&id=1hUi9lkyO_TO4Oo6ZFF7JQXNvCLYisgLu", #6
            "https://drive.google.com/uc?export=view&id=1h3yB9qNUbfvu9uD-6c0wQCzAlilcmEP_", #7
            "https://drive.google.com/uc?export=view&id=1gviXPnfeOzKW8dZHvV3Jd1xwZsn0DK4Q", #8
            "https://drive.google.com/uc?export=view&id=1hPj409PAuAvDfBYsI9PgVOYNjfOp8rg_", #9
            "https://drive.google.com/uc?export=view&id=1gx7ADYCMVTTwyloaKR9tHDyPXF5enlIX", #10
            "https://drive.google.com/uc?export=view&id=1hFys3GoNumh6EZj8MlQWUhK9LRegqLVh", #11
            "https://drive.google.com/uc?export=view&id=1i3GXDU9pazfI_0hEN_LGg-YJpeaGw_fD", #12
            "https://drive.google.com/uc?export=view&id=1hMVy0BWkTjqZG0ozIucFmXb9YskhMD4v", #13
            "https://drive.google.com/uc?export=view&id=1hf2aBq5pJYBPPxoeSwrkVMdMoHLZOILV", #14
            "https://drive.google.com/uc?export=view&id=1htDgk71JGmDie7tGgMO9-BV84uir31ke", #15
            "https://drive.google.com/uc?export=view&id=1hV-bUOD_u5FoTdlIcWbGv5iGzoR0B-X5", #16
            "https://drive.google.com/uc?export=view&id=1gYzQZYQbyLrm-XL5klCAn3pC53JlzkZh", #17
            "https://drive.google.com/uc?export=view&id=1hye4-QsRpgF8amcTN8xgX3I_ciLjHrOS", #18
            "https://drive.google.com/uc?export=view&id=1gthlph_hZj4nS6try4JrSAo41GHsdGSF", #19
            "https://drive.google.com/uc?export=view&id=1gQFr30FWnX9K8D-jtdMXp_c7bIYpV7NZ", #20
            
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
                "kesan": "public speakingnya keren",
                "pesan": "semoga diperlancar menuju jalan sukses"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "kakanya lucu, bisa request gaya lucu lucu",
                "pesan": "tetap ceria kak"
            },
            {
                "nama": "Nazwa Nabila",
                "nim": "121450122",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main Golf",
                "sosmed": "@nazwanbilla",
                "kesan": "kakanya seru public speakingnya bagus",
                "pesan": "semangat dan semoga terus berbagi ilmu ya kak"
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "Menggambar",
                "sosmed": "@bastiansilaban_",
                "kesan": "abangnya sedikit pendiem tapi baik",
                "pesan": "jangan bosen berbagi ilmu ya bang"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Berkebun",
                "sosmed": "@deaa.rsn",
                "kesan": "baikk sekali",
                "pesan": "semoga dipermudah segala urusan nya ya kak"
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan": "kakaknya asik lucuu",
                "pesan": "stay humble kak"
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Surfing",
                "sosmed": "@nateee__15",
                "kesan": "lucu sekali ekspresif",
                "pesan": "semangat menjalani hari hari di itera kak"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "kalem",
                "pesan": "semoga studinya diperlancar dan sesuai harapan"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan": "kakanya baik sama lucu",
                "pesan": "semoga kuliahnya lancar"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan": "bang tobias baik, asik seruu, enak buat diajak diskusi",
                "pesan": "stay humble bang tob!",
                "jabatan": "Staff Divisi Hubungan Luar"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "kakanya baik tapi sedikit pendiam",
                "pesan": "semoga ilmunya makin luas ya kak!"
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "public speakingnya oke, seru buat sharing sharing",
                "pesan": "keep it up, sukses selalu ya bang"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "keliatannya seru si, humble",
                "pesan": "stay humble and keep inspiring"
            },
            {
                "nama": "Asa Doa Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "kakanya baik banget",
                "pesan": "terus jadi orang baik ya ka, semoga kuliahnya diperlancar"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan": "mukanya ga bosenin",
                "pesan": "semangat terus jadi contoh yang baik"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan": "seru buat diajak sharing pengalamannya banyak",
                "pesan": "semoga lancar segala urusan nya ya bang",
                "jabatan": "Staff Divisi Pengabdian Masyarakat"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan": "kak izza asik banget seru huble parah",
                "pesan": "Stay humble dan keep inspiring ya, Kak!"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "kak alyaa baik sekali, cantik banget lagi lucuuuuu",
                "pesan": "stay humble ya kak, and keep spreading those good vibes"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Nemenin Tobias lari",
                "sosmed": "@rayths_",
                "kesan": "baik tapi sedikit pendiem",
                "pesan": "semangat ya menjalani kegiatan pengmasnya!"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Way Dadi",
                "hobbi": "Olahraga",
                "sosmed": "@triayunanni",
                "kesan": "cantik, kakanya receh banget",
                "pesan": "tetep receh ya kak ketawanya nular soalnya"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemeneksternal()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen Internal":
    def departemeninternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mGyNPx5HD2e6EmyJ36kBf2GxIJ5Hmgo7", #1
            "https://drive.google.com/uc?export=view&id=1lxUU8I-vZJPS2iL0qaG832wHRIF02jnI", #2
            "https://drive.google.com/uc?export=view&id=1lqDLuteV8HtBu-x2DerrfiuFZ1UqX-T8", #3
            "https://drive.google.com/uc?export=view&id=1lnE9JX35MKdtoaRgl-G0M0Y9BxmdviwJ", #4
            "https://drive.google.com/uc?export=view&id=1lnt23jdvWFZ9W2MObk-cb1MKcvsup4BL", #5
            "https://drive.google.com/uc?export=view&id=1lgrbWy_O4TsmCI72xXNxuWtShb_2Ucyc", #6
            "https://drive.google.com/uc?export=view&id=1lpcSqwS3sPDwAEN_jVZjBZuX1AF7Fqe1", #7
            "https://drive.google.com/uc?export=view&id=1m-dAQylJ-YIFi2Ono6Yc5Noi8QF9VQPl", #8
            "https://drive.google.com/uc?export=view&id=1m8PBgRGBPOPmjFB0B50HNdNV5KA82ckB", #9
            "https://drive.google.com/uc?export=view&id=1mEzUxjxva6h_t4N9wB14666ckulCIr_8", #10
            "https://drive.google.com/uc?export=view&id=1lqpt1AoHM82GFNoFNudrvq7-xaVJCON4", #11
            "https://drive.google.com/uc?export=view&id=1luIGhQtMTZM7RjB8MAk6y1KtbBmIIQ9l", #12
            "https://drive.google.com/uc?export=view&id=1mDEfNHWGG8f1ZbQZ4cv5NBilL1DGQOVe", #13
            
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
                "kesan": "public speakingnya bagus banget banget",
                "pesan": "terus menginspirasi dan berbagi ilmu ya bang",
                "jabatan": "Kepala Departemen Internal" #1
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "lucu kakanya kalem",
                "pesan": "stay postive kak" #2
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Pasaruntung",
                "hobbi": "Mengoleksi Dino",
                "sosmed": "@akbar_restika",
                "kesan": "punya jiwa leadership",
                "pesan": "semoga sukses ya kak studinya", #3
            },
            {
               "nama": "Rani Puspita sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "kakanya baik tapi keliatannya aga introvert",  
                "pesan":"semangat kuliah nya kak rani" #kak rani4
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Membaca dan Memancing",
                "sosmed": "@renita.shn",
                "kesan": "kakanya kalem pendiem",
                "pesan": "sukses selalu ya kak",
                "jabatan": "Staff Keharmonisasian" #5
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Ngeliat cogann",
                "sosmed": "@slwfhn_694",
                "kesan": "asik",
                "pesan": "semoga hari harinya selalu bertemu cogan" #6
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "bang rendra seru, asik suka becanda",
                "pesan": "semangat nulis lagunya bang semoga bisa release",
                "jabatan": "Staff Keharmonisasian" #7
            },
            {
                "nama": "Yosia Letare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi": "Nungguin ayam betina berkokok",
                "sosmed": "@yosiabanurea",
                "kesan": "abangnya aga pendiem",
                "pesan": "semangat bang semoga apa yang dijalani membuahkan hasil" #8
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "abangnya lumayan seru buat sharing sharing",
                "pesan": "semoga suskes disetiap langkahnya",
                "jabatan": "Kepala Divisi Kerohanian" #9
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan": "baik, ramah, kalem",
                "pesan": "semangat berkebun kak",
                "jabatan": "Staff Kerohanian" #10
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@meirasty_",
                "kesan": "kalem bangett",
                "pesan": "stay kalem ya kak, sukses selalu",
                "jabatan": "Staff Kerohanian" #11
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Berenang di Laut",
                "sosmed": "@rexander",
                "kesan": "abangnya kayanya introvert",
                "pesan": "sukses untuk kuliahnya ya bang!", #12
            },
            {
                "nama": "Josua Alfa Viando Panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Ngejokes",
                "sosmed": "@josuapanggabean_",
                "kesan": "baik, humoris",
                "pesan": "semoga lulus dengan hasil sesuai harapan" #13
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemeninternal()

elif menu == "Departemen SSD":
    def departemenssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ldYzEB5XBwoNiYmscLgsHG0G_0UUIc98", #101
            "https://drive.google.com/uc?export=view&id=1lbX7GsAh_F0VbS4qxM93nidxGQeKF39A", #102
            "https://drive.google.com/uc?export=view&id=1lbJiqY55RmJO_xcR5lil8oJGNpco8mJj", #103
            "https://drive.google.com/uc?export=view&id=1lcuVLe0bV6YJ8XOaRXU4mBreTNEn0c5e", #104
            "https://drive.google.com/uc?export=view&id=1lJ7Ms-O2eZcLZgKT4u6N7LVRCSnW2MLv", #105
            "https://drive.google.com/uc?export=view&id=1lS6cieOYvSl2loQzZ4EA-SVPwlm9jAzY", #106
            "https://drive.google.com/uc?export=view&id=1lW2xzGaNRTYSYyOUXq-RMcE4nmlR6ruJ", #107
            "https://drive.google.com/uc?export=view&id=1ldHe9cZnZB7n7nxCxwl1F8RBbbyZA2mv", #108
            "https://drive.google.com/uc?export=view&id=1lXfkdHzIKiMEAqVvzdGjsVyXaH3FLPJj", #109
            "https://drive.google.com/uc?export=view&id=1lbwFKnfFAQe7tGmJZaUa984vJybAGXhr", #110
            "https://drive.google.com/uc?export=view&id=1lXOVXhEyMYWv1ZWlK__Gn3DAsjvOoE34", #111

        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "21",
                "asal": "Panjibako",
                "alamat": "Jl. Bel",
                "hobbi": "Mencari Uang",
                "sosmed": "@andriangaol",
                "kesan": "abangnya seruu wawasan nya luas public speakingnya juga keren",  
                "pesan": "Semangat terus bang kuliahnya" #101
            },
            {
                "nama": "Adisty Syawalda Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "kakanya sedikit pendiam tapi baik",  
                "pesan": "semoga sukses dan bahagia selalu kak" #102
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun, Sumut",
                "alamat": "Airan",
                "hobbi": "Hitung uang",
                "sosmed": "@zhjung_",
                "kesan": "seru ngobrol bareng kakanya baik",  
                "pesan": "semoga kakak selalu dikelilingi orang baik!" #103
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukittinggi",
                "alamat": "Airan",
                "hobbi": "Badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "abangnya baik meskipun sedikit pendiam",  
                "pesan": "semoga semua mimpinya tercapai ya bang!" #104
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Nyuruh-nyuruh",
                "sosmed": "@dananghk_",
                "kesan": "bang danang seru abiss dengan 1001 topik yang gaperna abis, asik bgt kalo diajak sharing",  
                "pesan": "stay humble and inspiring ya bang danang!" #105
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobbi": "Apa aja",
                "sosmed": "@farrel_julio",
                "kesan": "Abang ini asik, tegas, baik, pemikirannya luas seru apalagi pas supporteran",  
                "pesan": "semangat jadi capo satunya bang farel, semoga kuliahnya lancar" #106
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun, Sumut",
                "alamat": "Pemda",
                "hobbi": "Suka nulis",
                "sosmed": "@tesakanias",
                "kesan": "ramah banget murah senyum",  
                "pesan": "tetep murah senyum ya kak, semoga kuliahnya lancar" #107
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "kakanya baik keliatan sabar",  
                "pesan": "semoga diperlancar dalam segala hal ya kak" #108
            },
            {
                "nama": "Alvia Asrinda Br.Ginting",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobbi": "Nonton windah",
                "sosmed": "@alviagnting",
                "kesan": "Kakaknya baik, ramah dan lucu",  
                "pesan": "semoga sukses studinya!" #109
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Balam",
                "alamat": "Jalan Nangka 1",
                "hobbi": "Tidur",
                "sosmed": "@dhafinrzqa",
                "kesan": "abangnya baik keliatan rendah hati",  
                "pesan": "tetep rendah hati ya bang, dan semoga sukses!" #110
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobbi": "Badminton",
                "sosmed": "@meylanielia",
                "kesan": "kakanya seruu pas sharing sharing, asik pokoknya",  
                "pesan": "stay humbke kak, semoga ada kesempatan buat sharing sharing lagi" #111
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenssd()

elif menu == "Departemen MEDKRAF":
    def departemenmedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jageJSMOzzw5aOCjPYGZ1yj5ZmF1jaxD", #112
            "https://drive.google.com/uc?export=view&id=1iRIraDeyF28Rq_wFyH2dJLaJG-8OMg1h", #113
            "https://drive.google.com/uc?export=view&id=1jX6--z7UySt26pn_XkvZsOUGmGr-w-qJ", #114
            "https://drive.google.com/uc?export=view&id=1iRtRRMMZpgMMw-2elgqsHKxV1Dx222Vo", #115
            "https://drive.google.com/uc?export=view&id=1izXd0Pvq8OHOP0djGJt6kiY-sEy-cJK8", #116
            "https://drive.google.com/uc?export=view&id=1iOrqOWEARcixkVVC6n3GwgCLoUDMjzNS", #117
            "https://drive.google.com/uc?export=view&id=1jb0UEirjObw-kDcdiG5dQ7YYZBg-aKZ_", #118
            "https://drive.google.com/uc?export=view&id=1imo67Za72BsPyeMTvhdvZZIpWYr2KPGN", #119
            "https://drive.google.com/uc?export=view&id=1iPNR32msR4tRl58kFqn3p9lyKXZsc3ec", #120
            "https://drive.google.com/uc?export=view&id=1jM2tugYdM2__W0vvda53J_SUE0j_e53P", #121
            "https://drive.google.com/uc?export=view&id=1j2mnUGoAWZWp7plDkGMHmyb-VFSG0Yew", #122
            "https://drive.google.com/uc?export=view&id=1j61rdAOavKMXL8VkKvaPo6BNQqX_ZR8N", #123
            "https://drive.google.com/uc?export=view&id=1jQWgBjHbw_JIO0Rl17qGoSw6SqfZEa3x", #124
            "https://drive.google.com/uc?export=view&id=1jmxBwJkCGA9WzPGw0kTTZ9dZQ_C5bwb0", #125
            "https://drive.google.com/uc?export=view&id=1jntnMkuH1KZtR3oKFbhD0uA8mYpEqQ3t", #126
            "https://drive.google.com/uc?export=view&id=1iuAmoIh7ehqhMx1caO9Xp5kH-gAWZfYb", #127
            "https://drive.google.com/uc?export=view&id=1j-d2IFcIs6tnxfqxuomtOOjaz-Ll3YZs", #128
            "https://drive.google.com/uc?export=view&id=1jOhEf9saRdkGaTAuBlgD8kgDbJgNC-gi", #129
            "https://drive.google.com/uc?export=view&id=1jR5ONXami6hPGp-Au3eqswpaCmZwibzF", #130
            
        ]
        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal": "Makassar, Sulawesi Selatan",
                "alamat": "Sukarame",
                "hobbi": "Nonton",
                "sosmed": "@",
                "kesan": "bang tao seruu, asikkk",  
                "pesan":"Semangat bang semoga bisa cepat lulus" #112
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "kakanya cantikk, aga suka sarkas tapi seruuu",  
                "pesan":"stay positive ya kak!" #113
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": " Nugas",
                "sosmed": "@arsyiah._",
                "kesan": "kak aci seruu bangett, friendly, asik banget kalo diajak sharing sharing ",  
                "pesan":"stay humble dan semangat ka acii kuliahnya" #114
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "kak cibel cantik banget, baik, cantik yang kalem gituu",  
                "pesan":"keep shining kak cibell" #115
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": "122450045",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Menyibukkan diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "kak eka baikk sekali, ramah",  
                "pesan":"tetap jadi orang yang fun dan positive ya kak!" #116
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Nulis, baca, fangirling",
                "sosmed": "@nanana.minjoo",
                "kesan": "kak juju baikk tapi kayanya aga introvert, kalem gituu",  
                "pesan":"semoga kuliahnya diperlancar dan happy selalu" #117
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton film",
                "sosmed": "@patriciadiajeng",
                "kesan": "kak cia cantik banget, lucuu ekspresif banget, positif vibesnya",  
                "pesan":"tetap jadi orang keren yang terus menginspirasi ya kak!" #118
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan": "Kak nelii seruu bangettt asikk",  
                "pesan":"stay humble ya kak nelii" #119
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "kak cia cantik, seruu jugaaa asikk",  
                "pesan":"semangat kuliahnya ka cia" #120
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Lagi Nyari",
                "sosmed": "@dino_kiper",
                "kesan": "asik, wawasan nya luas jadi kalo ngobrol seru",  
                "pesan":"semoga semua planningnya tercapai tepat waktu" #121
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Jalan durian 5 pemda",
                "hobbi": "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan": "kalem banget kakanya",  
                "pesan":"stay positive dimanapun dan kapanpun ya kak!" #122
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapanfan Golf UIN",
                "hobbi": "Baca komik",
                "sosmed": "@jimnn.as",
                "kesan": "abangnya asik buat sharing sharing, friendly",  
                "pesan":"Tetap jadi sosok keren yang selalu humble!" #123
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi": "Nonton drakor",
                "sosmed": "@nsywanaf",
                "kesan": "baik ramah banget",  
                "pesan":"semoga bisa ketemu aktor favorit!" #124
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jl. Nangka 2",
                "hobbi": "Baca novel yang bikin nangis",
                "sosmed": "@prskslv",
                "kesan": "asikk kakanya ramah banget",  
                "pesan":"Sukses selalu dan terus menebar semangat positif ya, Kak!" #125
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 3",
                "hobbi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "wawasannya luas dan ga pelit berbagi ilmu",  
                "pesan":"semoga ngodingnya ga ada error ya bang" #126
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi": "Mengerjakan tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "positive vibes, baik, ramah, dan friendly ",  
                "pesan":"keep inspiring ya kak, semangat ngoleksi lanyard panitiaannya!" #127
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa Labuhan dalam",
                "hobbi": "Ngoding, gaming",
                "sosmed": "@anitahmad",
                "kesan": "abangnya lucuu baik banget",  
                "pesan":"semangat design bang jangan lupa berbagi ilmu" #128
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "121450090",
                "umur": "21",
                "asal": "Panjibako",
                "alamat": "Jl. Bel",
                "hobbi": "Mencari Uang",
                "sosmed": "@andriangaol",
                "kesan": "bang akmal asikk baik juga, ramah banget",  
                "pesan":"Sukses selalu dan terima kasih buat inspirasinya!" #129
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Wisma Hana Hani",
                "hobbi": "Bengong/ Membaca buku",
                "sosmed": "linkedin",
                "kesan": "abangnya asikk, friendly, becandanya suka bikin panik tapi, tapi baik banget jugaaa",  
                "pesan":"Sukses selalu dan terus menebar semangat positif ya bang" #130
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenmedkraf()
