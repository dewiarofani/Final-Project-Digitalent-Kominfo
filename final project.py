from logging import PlaceHolder
from re import S
from turtle import color, left
from PIL import Image
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.set_page_config(page_title="CYBERSECURITY", page_icon="./assets/Chamomile_icon.png", layout="wide")

# ---- MAIN PAGE ----
def dashboard():
    # ---- HEADER SECTION ----
    with st.container():
        st.image("./assets/header.png")
        st.write("This website will discuss about cybersecurity. Before learning more, start our activities with enthusiasm in seeking knowledge and full of dreams!🌟")
        st.write("Because...")
        st.markdown("“_Strength and growth come only through continuous effort and struggle_.” — **Napoleon Hill**")
        st.markdown("<h2 style='text-align: center; color: #6E9BB9;'> CYBERSECURITY </h2>", unsafe_allow_html=True)
        st.write("In the real world, we are exposed to potential threats like someone trying to steal or hurt us. Of course, we can count on security forces to protect us from that. In the same way, when we enter the cyberspace, we are exposed to many potential threats. Here is where it enters the cybersecurity.")
        st.write("But...What is cybersecurity? What are those potential threats and how to protects us? Check the content below to learn about it!🧐")
        
    # DASHBOARD
        # ---- WHAT'S CYBERSECURITY? ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What is Cybersecurity?")
            st.write("Cybersecurity consist od protecting networks, systems, devices, programs or any digital assets from cybercriminals attacks.")
            st.write("This attacks usually try to steal information, change or modify it; hijack files and ask for money to recover them or use or devices for delictive acts.")
        with right_column:
            st.image("./assets/DEFINITION .jpeg")

        # ---- WHY IS CYBERSECURITY IMPORTANT? ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image("./assets/IMPORTANT.jpeg")
        with right_column:
            st.header("Why is Cybersecurity Important?")
            st.write("The importance of cybersecurity is that it protect our data and devices from attackers who want to steal it to cause some harm or to access our accounts (for example, our bank accounts).")
            st.write("This protectional is essential, given than more and more of our life is online this days (including, interaction with the government).")

        # ---- TYPES OF CYBERSECURITY THREATS ----
    with st.container():
        st.write("----")
        left_column, right_column = st.columns(2)
        with right_column:
            st.image("./assets/TYPES.jpeg")
        with left_column:
            st.header("Types of Cybersecurity Threats")
            st.write("Cybercriminals use many diffent techniques to commit their acts. This includes:")
            st.write("- Social engineering")
            st.write("- Malware")
            st.write("- Phishing")
            st.write("- Ramsomware")
        
        # ---- CYBERCRIME ----
    with st.container():
        st.write("----")
        left_column, right_column = st.columns(2)
        with right_column:
            st.image("./assets/21_02_Data-security_10.jpg")
        with left_column:
            st.header("Cybercrime")
            st.write("Cybercrime is any criminal activity that involves a computer, networked device or a network.")
            st.write("While most cybercrimes are carried out in order to generate profit for the cybercriminals, some cybercrimes are carried out against computers or devices directly to damage or disable them. Others use computers or networks to spread malware, illegal information, images or other materials. Some cybercrimes do both -- i.e., target computers to infect them with a computer virus, which is then spread to other machines and, sometimes, entire networks.")
        
        # ---- CYBERCRIME EMERGENCY IN INDONESIA AND SOLUTION ----
    with st.container():
        st.write("----")
        left_column, right_column = st.columns(2)
        with right_column:
            st.image("./assets/Cybercrime-image-.jpg")
        with left_column:
            st.header("Cyber Crime Emergency in Indonesia and Solutions")
            st.write("One of the most important things we do in the digital world is to seek information and we believe that this poses a new problem for the Indonesian netizens, in which hoaxes, fake news, and cybercrimes are so heavily widespread as we surf the Internet. This time we will show you more about how cyber crimes happen in Indonesia, real our experiences about cyber crimes and solutions to solve these problems.")

    # ---- Cybercrime charts ----
    with st.container():
        st.write("----")
        st.header("Data on The Number of Cybercrimes in Indonesia")
        left_column, right_column = st.columns(2)

        with left_column:
            cybercryme_chart()
            
        with right_column:
            cybercryme_table()
     
 
def content():
    # ---- Extra sidebar ----
    # ---- SELECT A PAGE ----

    page_names_to_funcs = {
        "All The Contents...": content_declared,
        "What is Cybersecurity?" : page2,
        "Why is Cybersecurity is Important?" : page3,
        "Types of Cybersecurity Threats" : page4,
        "What is Cybercrime? Are We a victim of Cybercrime?" :page8,
        "Cybercrime Emergency in Indonesia and Solutions":page9,
        "Data on The Number of Cybercrimes in Indonesia": graphs,
    }

    selected_page = st.sidebar.selectbox ("Select a section", page_names_to_funcs.keys(), key=2)
    page_names_to_funcs[selected_page]()

def content_declared():
    st.title("All the contents")

    # ---- WHAT'S CYBERSECURITY? ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What is Cybersecurity?")
            st.write("Cybersecurity consist od protecting networks, systems, devices, programs or any digital assets from cybercriminals attacks.")
            st.write("This attacks usually try to steal information, change or modify it; hijack files and ask for money to recover them or use or devices for delictive acts.")
            st.button("[Learn More]", on_click=page2, key=1)
        with right_column:
            st.image("./assets/DEFINITION .jpeg")

    # ---- WHY IS CYBERSECURITY IMPORTANT? ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image("./assets/IMPORTANT.jpeg")
        with right_column:
            st.header("Why is Cybersecurity Important?")
            st.write("The importance of cybersecurity is that it protect our data and devices from attackers who want to steal it to cause some harm or to access our accounts (for example, our bank accounts).")
            st.write("This protectional is essential, given than more and more of our life is online this days (including, interaction with the government).")
            st.button("[Learn More]", on_click=page3, key=2)

    # ---- TYPES OF CYBERSECURITY THREATS ----
    with st.container():
        st.write("----")
        left_column, right_column = st.columns(2)
        with right_column:
            st.image("./assets/TYPES.jpeg")
        with left_column:
            st.header("Types of Cybersecurity Threats")
            st.write("Cybercriminals use many diffent techniques to commit their acts. This includes:")
            st.write("- Social engineering")
            st.write("- Malware")
            st.write("- Phishing")
            st.write("- Ramsomware")
            st.button("[Learn More]", on_click=page4, key=3)
    
    # ---- CYBERCRIME ----
    with st.container():
        st.write("----")
        left_column, right_column = st.columns(2)
        with right_column:
            st.image("./assets/21_02_Data-security_10.jpg")
        with left_column:
            st.header("Cybercrime")
            st.write("Cybercrime is any criminal activity that involves a computer, networked device or a network.")
            st.write("While most cybercrimes are carried out in order to generate profit for the cybercriminals, some cybercrimes are carried out against computers or devices directly to damage or disable them. Others use computers or networks to spread malware, illegal information, images or other materials. Some cybercrimes do both -- i.e., target computers to infect them with a computer virus, which is then spread to other machines and, sometimes, entire networks.")        
            st.button("[Learn More]", on_click=page8, key=4)

    #------Cybercrime Emergency in Indonesia-------
    with st.container():
        st.write("----")
        left_column, right_column = st.columns(2)
        with right_column:
            st.image("./assets/Cybercrime-image-.jpg")
        with left_column:
            st.header("Cyber Crime Emergency in Indonesia and Solutions")
            st.write("One of the most important things we do in the digital world is to seek information and we believe that this poses a new problem for the Indonesian netizens, in which hoaxes, fake news, and cybercrimes are so heavily widespread as we surf the Internet. This time we will show you more about how cyber crimes happen in Indonesia, real our experiences about cyber crimes and solutions to solve these problems.")
            st.button("[Learn More]", on_click=page9, key=5)

    # ---- CYBERCRIME CHART ----
    with st.container():
        st.write("----")
        st.header("Data on The Number of Cybercrimes in Indonesia")
        left_column, right_column = st.columns(2)

        with left_column:
            cybercryme_chart()
            
        with right_column:
            cybercryme_table()
            st.button("[Learn More]", on_click=graphs, key=6)
    

def about_us():
    # ---- GET TO KNOW US ----
    with st.container():
        st.write("----")
        st.markdown("<h2 style='text-align: center; color: #6E9BB9;'> GET TO KNOW US </h2>", unsafe_allow_html=True)
        st.write("##")

        augin, dewi, wanda = st.columns(3)
        with dewi:
            image = Image.open("./assets/Ima.png")
            st.image(image)
            if st.button('Ima Dewi Arofani'):
                page5()

        with wanda:
            image = Image.open("./assets/wanda.png")
            st.image(image)
            if st.button('Awanda Ardaneswari'):
                page6()

        with augin:
            image = Image.open("./assets/Augin.png")
            st.image(image)
            if st.button('Auginstori Levinta'):
                page7()

# ---- PAGE 2 ----
def page2():
    st.subheader("What is Cybersecurity?")
    st.write("##")
    st.markdown("Indonesia saat ini tengah dalam keadaan darurat kejahatan siber seiring dengan mudahnya internet dijangkau oleh masyarakat sipil. Berdasarkan berbagai kejadian pada beberapa tahun belakangan ini, Indonesia menjadi salah satu negara dengan predikat lemah dalam penegakan _cyber security_-nya.")
    st.image("./assets/1.png")
    st.markdown("Menurut ISO (_International Organization for Standardization_), tepatnya **ISO/IEC** 27032:2012 _Information technology - Security techniques - Guidelines for cybersecurity_. _Cybersecurity_ atau _cyberspace security_ adalah upaya yang dilakukan dalam menjaga kerahasiaan (_confidentiality_), integritas (_integrity_), dan ketersediaan (_availability_) dari informasi di _cyberspace_. Adapun _cyberspace_ merujuk pada lingkungan yang kompleks yang merupakan hasil dari interaksi antara orang, perangkat lunak, dan layanan di internet, yang didukung oleh perangkat teknologi informasi dan komunikasi (TIK) dan koneksi jaringan yang tersebar di seluruh dunia.")
    st.markdown("**CISCO** menyatakan hal yang serupa bahwa _cybersecurity_ merupakan praktik melindungi sistem, jaringan, dan program dari serangan digital. _Cybersecurity_ biasanya ditujukan untuk mengakses, mengubah, atau menghancurkan informasi sensitif, memeras uang dari pengguna, atau mengganggu operasional proses bisnis. Dengan demikian, dapat dikatan bahwa _Cyber security_ adalah kumpulan alat, kebijakan, konsep keamanan, perlindungan keamanan, pedoman, pendekatan manajemen risiko, tindakan, pelatihan, dan teknologi yang dapat digunakan untuk melindungi lingkungan _cyber_ dan organisasi serta asset pengguna. Lebih lanjut, _cybersecurity_ dimaknai sebagai semua mekanisme untuk melindungi dan meminimalkan gangguan kerahasiaan (_confidentiality_), integritas (_integrity_), dan ketersediaan (_Availability_).")

# ---- PAGE 3 ----
def page3():
    st.subheader("Why is Cybersecurity Important?")
    st.write("##")
    st.write("Pada era globalisasi saat ini, keberadaan suatu informasi mempunyai arti dan peranan yang sangat penting bagi semua aspek kehidupan, serta merupakan salah satu kebutuhan hidup bagi semua orang baik individual maupun organisasi, sehingga dapat dikatakan bahwa dalam masyarakat, informasi telah berfungsi sebagaimana layaknya aliran darah sumber kehidupan bagi tubuh manusia. Salah satu temuan yang memberikan pengaruh paling besar dalam masyarakat adalah ditemukannya internet. Hadirnya internet sebagai bentuk teknologi baru menyebabkan manusia tidak mampu terlepas dari arus komunikasi dan informasi.")
    st.write("Perkembangan teknologi informasi juga telah memberikan perubahan signifikan mengenai konsep keamanan, kini ruang interaksi tidak bisa hanya dibatasi secara fisik melainkan dapat meluas ke dunia maya. Konsekuensinya, negara harus beradaptasi dengan perkembangan ini, konsep keamanan dunia maya sudah saatnya ditetapkan sebagai salah satu “wilayah” negara yang menjaga keamanannya sebagaimana kewajiban negara mengamankan teritorialnya. Apalagi, serangan _cyber_ tidak hanya terjadi pada institusi publik saja, namun juga menyerang institusi pemerintah. Faktanya, penanganan kejahatan siber masih belum maksimal serta rendahnya kesadaran masyarakat sipil akan adanya ancaman _cyber attack_ yang akan berdampak pada lumpuhnya infrastruktur vital, seperti sistem radar penerbangan di Bandara Internasional Soekarno Hatta yang beberapa kali mengalami gangguan.")
    st.write("Berdasarkan uraian tersebut, dapat diketahui bahwa keamaanan siber perlu di maksimalkan. Adapun urgensi _cyber security_ antara lain:")
    st.write("##")
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((1, 2))
        with left_column:
            image = Image.open("./assets/icon_comp.png")
            st.image(image)
        with right_column:
            st.write("##")
            st.markdown("**“_Melindungi jaringan, komputer, program dan data dari serangan, kerusakan atau akses yang tidak sah_“**")
            st.markdown("Memperhatikan dan menggunakan _Cyber Security_ dalam menyimpan, mengakses, dan mengambil informasi penting. Melindungi informasi dan data merupakan sebuah kebutuhan sebagian besar perusahaan dan instansi pemerintah, karena data merupakan aset berharga dari suatu perusahaan dan bisa menjadi masalah apabila terjadi kebocoran data.")
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((1, 2))
        with left_column:
            image = Image.open("./assets/information.png")
            st.image(image)
        with right_column:
            st.write("##")
            st.markdown("**“_Melindungi informasi dari penyalahgunaan akses_“**")
            st.markdown("_Cyber Security_ juga penting untuk menjaga dan mencegah penyalahgunaan akses maupun pemanfaatan data dalam sistem teknologi informasi dari seseorang yang tidak memiliki hak untuk mengakses maupun memanfaatkan data dalam sistem tersebut")
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((1, 2))
        with left_column:
            image = Image.open("./assets/IMG-20220807-WA0036.jpg")
            st.image(image)
        with right_column:
            st.write("##")
            st.markdown("**“_Melindungi produktivitas perusahaan atau pengguna_“**")
            st.markdown("Melalui keamanan siber yang maksimal maka berimplikasi pada kinerja perusahaan/pengguna karena jaringan dan sistem yang digunakan terlindung dari _malware_")
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((1, 2))
        with left_column:
            image = Image.open("./assets/security-services-icon-cyber-security-icon-11562900266u4grfuhmp3-removebg-preview.png")
            st.image(image)
        with right_column:
            st.write("##")
            st.markdown("**“_Waktu pemulihan yang singkat_“**")
            st.markdown("Meskipun terjadi data _breach_ atau gangguan yang lainnya, apabila perusahaan/pengguna telah terlebih dahulu membentengi sistem/jaringan dengan _security_ yang baik, maka tak perlu memakan waktu lama untuk proses _recovery_ data atau sistem yang diretass.")
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((1, 2))
        with left_column:
            image = Image.open("./assets/IMG-20220807-WA0035.jpg")
            st.image(image)
        with right_column:
            st.write("##")
            st.markdown("**“_Meningkatkan kepercayaan customers_“**")
            st.markdown("Bagi sebuah perusahaan, loyalitas konsumen menjadi hal yang paling utama, maka dengan memberikan jaminan keamanan kerahasiaan data yang kuat, konsumen tidak akan merasa cemas.")

# ---- PAGE 4 ----
def page4():
    st.subheader("Types of Cybersecurity Threats")
    st.write("##")
    st.write("Berikut ini adalah jenis-jenis ancaman keamanan siber, antara lain:")
    st.write("##")

    with st.container():
        st.write("---")
        left_column, right_column = st.columns((1, 2))
        with left_column:
            st.write("PHISING")
            image = Image.open("./assets/phising.jpg")
            st.image(image)
        with right_column:
            st.write("##")
            st.markdown('<div style="text-align: justify;">Kata phishing diambil dari istilah “fishing” yang artinya “memancing”. Tujuan phishing dilakukan adalah untuk mengambil data pribadi, data akun social media, dan data financial seperti informasi kartu kredit maupun nomor rekening. Pelaku kejahatan phishing ini biasanya menggunakan email palsu yang hampir mirip dengan website aslinya, sehingga para korban tidak curiga dan tidak akan sadar.</div>', unsafe_allow_html=True)

    with st.container():
        st.write("---")
        left_column, right_column = st.columns((1, 2))
        with left_column:
            st.write("RANSOMWARE")
            image = Image.open("./assets/Ransomware.webp")
            st.image(image)
        with right_column:
            st.write("##")
            st.markdown('<div style="text-align: justify;">Ransomware adalah jenis malware yang pada awalnya akan menginfeksi dan menyerang pengguna komputer. Setelah menginfeksi komputer, serangan ini akan melacak dan mengenkripsi data penggunanya dengan kode rahasia unik yang hanya diketahui oleh pembuat serangan ransomware atau bisa juga disebut hacker. Setelah itu, mereka akan meminta uang tebusan ke para korban</div>', unsafe_allow_html=True)

    with st.container():
        st.write("---")
        left_column, right_column = st.columns((1, 2))
        with left_column:
            st.write("MALEWARE")
            image = Image.open("./assets/Malware.jpg")
            st.image(image)
        with right_column:
            st.write("##")
            st.markdown('<div style="text-align: justify;">Malware adalah perangkat lunak yang dibuat dengan tujuan memasuki dan terkadang merusak sistem komputer, jaringan, atau server tanpa diketahui oleh pemiliknya. Istilah malware diambil dari gabungan potongan dua kata yaitu malicious “berniat jahat” dan software “perangkat lunak”. Tujuannya tentu untuk merusak atau mencuri data dari perangkat yang dimasuki.</div>', unsafe_allow_html=True)

    with st.container():
        st.write("---")
        left_column, right_column = st.columns((1, 2))
        with left_column:
            st.write("SOCIAL ENGINEERING")
            image = Image.open("./assets/Social Engineering.webp")
            st.image(image)
        with right_column:
            st.write("##")
            st.markdown('<div style="text-align: justify;">Social engineering adalah bentuk kejahatan yang dilakukan dengan manipulasi psikologi untuk mengelabui pengguna, baik disadari atau tidak, supaya memberikan informasi pribadi atau melakukan tindakan tertentu yang menguntungkan pelaku. Serangan social engineering dapat bersifat non-teknis dan tidak harus melibatkan eksploitasi perangkat lunak atau sistem.</div>', unsafe_allow_html=True)

# ---- PAGE CYBERCRIME----
def page8():
    st.subheader("What is Cyber Crime? Are We a Victim of Cyber Crime?")
    st.write("##")
    st.markdown("**_“Negara-negara yang memiliki tingkat pembajakan yang lebih tinggi dan pengetahuan keamanan dunia maya lebih rendah cenderung lebih banyak terkena dampak dari ancaman dunia siber“_**")
    st.markdown("**-Haris Izmee, Presiden Director Microsoft Indonesia-**")
    st.markdown("_Cybercrime_ adalah tindak criminal yang dilakukan dengan menggunakan teknologi computer sebegai alat kejahatan utama. _Cybercrime_ memanfaatkan perkembangan teknologi komputer khususnya internet sebagai sarana melakukan kejahatan. _Cybercrime_ juga didefinisikan sebagai perbuatan yang melanggar hukum dengan memanfaatkan teknologi komputer berbasis kecanggihan perkembangan teknologi internet.")
    st.markdown("Beberapa Jenis- jenis _Cybercrime_ berdasarkan jenis aktivitasnya yang sangat dekat sekali dengan kehidupan kita sehari-hari, antara lain:")
    st.write("##")
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((1, 2))
        with left_column:
            image = Image.open("./assets/11.png")
            st.image(image)
        with right_column:
            st.write("##")
            st.markdown("**“_Unauthorized Access to Computer System and Service_“**")
            st.markdown("Kejahatan yang dilakukan dengan cara masuk/ menyusup kedalam sebuah sistem jaringan komputer dengan secara tidak sah atau tanpa izin pemilik sistem jaringan komputer.")
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((1, 2))
        with right_column:
            image = Image.open("./assets/illegal-content-144678831-removebg-preview.png")
            st.image(image)
        with left_column:
            st.write("##")
            st.markdown("**“_Illegal Contents_“**")
            st.markdown("Kejahatan dengan memasukkan data atau informasi yang belum jelas kebenarannya atau bahkan mungkin sama sekali tidak benar sehingga dapat mengganggu ketertiban umum di masyarakat.")
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((1, 2))
        with right_column:
            image = Image.open("./assets/111.png")
            st.image(image)
        with left_column:
            st.write("##")
            st.markdown("**“_Infringements of Privacy_“**")
            st.markdown("Kejahatan ditujukan terhadap informasi seseorang yang sifatnya pribadi. Data pribadi yang terkomputerisasi diretas oleh orang yang tidak bertanggung jawab dan menggunakan data tersebut untuk tujuan yang tidak baik. Contohnya identitas KTP, nomor Kartu Kredit, Nomor PIN ATM")
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((1, 2))
        with left_column:
            image = Image.open("./assets/Carding.png")
            st.image(image)
        with right_column:
            st.write("##")
            st.markdown("**“_Carding_“**")
            st.markdown("Kejahatan dengan menggunakan teknologi komputer untuk melakukan transaksi menggunakan data CC orang lain.")

#---- PAGE CYBERCRIME EMERGENCY IN INDONESIA----
def page9():
    st.subheader("CYBER CRIME EMERGENCY IN INDONESIA AND SOLUTIONS OF CYBERCRIMES")
    st.subheader("Fenomena Kasus Kejahatan Siber di Indonesia, Walaupun Terlihat Konyol Namun Hal Tersebut Dapat Merugikan")
    st.write("##")
    st.markdown("Berdasarkan laporan data anomaly trafik BSSN(2021) sepanjang tahun 2020 Indonesia tercatat telah mengalami serangan siber sebanyak 495,3 juta atau meningkat 41 persen dari tahun 2019.")
    st.image("./assets/fenomena.png")
    st.markdown("Sebenarnya saat ini kita berada dalam lingkaran kejahatan siber, yang mungkin kita menjadi salah satu korbannya namun sayangnya kita tidak dalam kesadaran dan pengetahuan yang cukup baik sehingga kita tidak tau bagaimana cara mengatasi hal tersebut.")
    st.markdown("Mengutip dari beberapa koran digital Indonesia, beberapa kejahatan siber di Indonesia yang fenomenal antara lain:")
    st.write("##")
    st.markdown("**1._Pencurian dan Penggunaan Akun Internet Milik Oranglain_**")
    st.markdown("Berbeda dengan mencuri sandal atau TV, pencurian ini cukup dengan menangkap user_id dan password target saja. Tujuan dari pencurian ini bermacam-macam, hanya karena iseng saja menjajal aji-aji kemampuan hacker nya atau memang digunakan untuk murni merugikan orang lain. Yang dicuripun tidak akan sadar karena tidak ada bukti fisik yang dapat dilacak. Modus kejahatan ini termasuk dalam jenis _unauthorized access_ dengan sasaran menyerang hak milik.")
    st.write("Contoh kasus :")
    st.markdown("Si Bejo, mencoba untuk menggunakan _e-banking_ BCA. Karena sudah larut malam dan matanya sedikit buram, ketika mengetik urlnya salah. Harusnya masuk ke url e-banking.bca.co.id, namun justru masuk ke ebankingbca.co.id. Bejo memasukkan user_id dan password seperti biasanya. Bejo tidak menyadari bahwa link tersebut adalah palsu sehingga data yang dimasukkan Bejo akhirnya disalah gunakan oleh si pembuat web palsu tersebut untuk bertransaksi secara digital.")

    st.write("---")
    with st.container():
        st.write("##")
        st.markdown("**2._Info Nyeleneh Situs KPU pada Tahun 2004 (Detik.com)_**")
        st.markdown("Tahun 2004 Indonesia sedang melakukan hajatan besar pemilihan lansung Presiden dan Wakil Presiden Indonesia. Tim IT komisi Pemilihan Umum pun meluncurkan situs KPU yang bernilai Rp 152 miliar dan digadang-gadang mustahil di-_hack_.")
        st.markdown("_Hacker_ fenomenal itu bernama **Xnuxer (Dani Firmansyah)** yang merasa tergelitik dengan statement tim IT KPU tersebut.")
        st.markdown("Xnuxer mencoba meretas dengan melakukan XSS atau menyuntikkan kode berbahaya ke Website KPU namun gagal, akhirnya dia mencoba untuk spoofing atau mengalihkan IP website sehingga dapat merebut kendali situs sehingga Ia dapat melakukan SQL injection yang berakibat hacker ini dapat memodifikasi halaman web dan mengubah informasi pada situs KPU. Nama partai misalnya, berubah menjadi Partai Si Yoyo, Partai Kolor Ijo, Partai Dibenerin Dulu Webnya.")
        st.image("./assets/KPU.png")
    
    st.write("---")
    with st.container():
        st.subheader(" CYBER CRIMES'S EXPERIENCES")
        st. write("Uraian di atas merupakan beberapa contoh kasus dengan korbannya adalah orang lain atau instansi, kami sebagai anggota tim Camomile juga tak luput menjadi korban kejahatan siber. Pengalaman-pengalaman tersebut antara lain:")
        st.markdown("**1._Pengalaman Awanda_**")
        st.image("./assets/Facebook hacked.webp")
        st.markdown("Pada awal tahun 2015 masih gencar-gencarnya penggunaan Facebook. Facebook tak lagi hanya menjadi media social, namun juga teman curhat serta buku diary digital. Segala keluh kesah tentang dosen killer, atau sekedar curhat sang pacar tidak kunjung membalas pesan BB juga tertuang dalam diary digital itu. Singkat cerita, tiba tiba salah satu teman mengirimkan screenshot percakapan antara saya dengan teman saya, yang isinya lebih kurang saya mau meminjam sejumlah uang untuk tambah tambah biaya kuliah. Saya sebagai pemilik akun merasa tidak pernah mengirim pesan tersebut, setelah saya buka akun saya, ternyata tidak hanya teman saya yang dikirimi pesan musabab pinjam uang itu, namun hampir seluruh teman saya. Akhirnya saya menyadari bahwa akun FB saya dibajak atau di hack istilah kerennya. Saya pun merelakan akun FB saya dan menutup akun tersebut dan mengubur semua bersama kenangan didalamnya.")
        st.markdown("**2._Pengalaman Augin_**")    
        st.image("./assets/Adware.png")    
        st.markdown("Pengalaman ini terjadi ketika saya mulai menggunakan PC dan mempelajari bagaimana caranya _browsing_ hal-hal yang saya tidak ketahui. Saat browsing, terkadang _browser_ secara otomatis menampilkan sebuah halaman iklan tertentu. Iklan-Iklan ini muncul dalam bentuk **_pop-up_**. Meskipun hal ini tidak merusak komputer namun hal ini cukup mengganggu _browsing_ saya. Saya juga mengalami hal yang sama ketika _browsing_ di ponsel. Saat itu, saya tidak sengaja klik iklan tersebut, terkadang secara otomatis saya diarahkan untuk menginstal suatu aplikasi yang menyebabkan kinerja ponsel menjadi lambat,mengambil kuota, dan memakan memori ponsel tanpa diketahui. Saya mencoba untuk mempelajari sebenarnya apa yang menyebabkan hal tersebut terjadi, ternyata itu adalah _Adware_. Salah satu bahaya _adware_ adalah berpotensi untuk mencuri data pribadi kita, sehingga dari kejadian tersebut saya mencoba untuk melakukan hal-hal yang dapat menghindari bahayanya _Adware_ baik di PC maupun di ponsel saya.")
        st.markdown("**3._Pengalaman Dewi_**")    
        st.image("./assets/pengalaman kak ima.jpeg")    
        st.markdown("Sejujurnya, saya tidak pernah mengalami kejahatan siber, mudah-mudahan kedepannya tidak. Namun, salah satu teman saya pernah. teman saya pernah mengalami akun whatsappnya disadap oleh seseorang. temen saya sadar saat ada device yg tidak dikenalnya ada di linked device. Walaupun teman saya sudah me-logout device tersebut, akhirnya ia memutuskan mengganti nomornya karena takut kejadiannya terulang lagi.")
        
    st.write("---")
    with st.container():
        st.subheader("SOLUTIONS FOR CYBER CRIMES")
        st. write("Beberapa solusi yang dapat dilakukan sebagai masyarakat sipil yang awam tentang IT, meskipun mungkin tidak menutup kemungkinan tetap saja berpeluang untuk jadi korban kejahatan siber antara lain :")
    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((1, 2))
        with left_column:
            image = Image.open("./assets/firewall.png")
            st.image(image)
        with right_column:
            st.write("##")
            st.markdown("**“_Penggunaan Firewall_“**")
            st.markdown("Firewall digunakan untuk menjaga agar akses dari orang yang tidak berwenang. Program ini merupakan perangkat yang diletakkan antara internet dan jaringan internal. _Firewall_ bekerja dengan mengamati paket IP yang melewatinya.")
    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((1, 2))
        with left_column:
            image = Image.open("./assets/closed-icon.webp")
            st.image(image)
        with right_column:
            st.write("##")
            st.markdown("**“_Menutup Service yang Tidak Digunakan_“**")
            st.markdown("Menggunakan aplikasi yang sah (bukan bajakan) untuk menghindari adanya virus atau malware yang disisipkan didalamnya")

    with st.container():
        st.write("---")
        left_column, right_column = st.columns((1, 2))
        with left_column:
            image = Image.open("./assets/Backup-PNG-Free-Image.png")
            st.image(image)
        with right_column:
            st.write("##")
            st.markdown("**“_Melakukan Back Up Secara Rutin_“**")
            st.markdown("Kegiatan ini wajib hukumnya apalagi jika komputer yang biasa kita gunakan untuk kerja menyimpan berbagai informasi penting. Kita perlu melakukan _back-up_ dengan meng-upload data penting ke _cloud_ atau yang lebih simple menyimpan copy-an ke dalam _flashdisk_ yang tentunya dipastikan tidak ada virusnya.")

def graphs():
    st.subheader("Data on the number of cybercrimes in indonesia")
    st.write("##")
    st.write("berikut ini adalah JUMLAH KEJAHATAN SIBER INDONESIA")
    st.write("##")
    left_column, right_column = st.columns((5,4), gap="large")
    with left_column:
        cybercryme_chart()
        cybercryme_table()
    with right_column:
        kontent_negatif_terbanyak()
        platform_terlapor_tertinggi()

# ---- PAGE 5 DEWI ----
def page5():
    st.subheader("Ima Dewi Arofani")
    st.write("Hi!👋")
    st.write("Hi, my name is Dewi. I'm university student. My hobbies are reading and watching movies/series. Let's be friend on instagram :") 
    st.write("📍[dewiarofani](https://www.instagram.com/dewiarofani/)")
    st.write("Merci!")

# ---- PAGE 6 WANDA ----
def page6():
    st.subheader("Awanda Ardaneswari")
    st.write("Hi!🤗")
    st.write("My name is Awanda and you can call me wanda. My age is 28 years old. One of my hobbies is Reading. For getting more about me, here my Instagram account:")
    st.write("📍[awawawanda](https://www.instagram.com/awawawanda/)")
    st.write("Thank you!")

# ---- PAGE 7 AUGIN ----    
def page7():
    st.subheader("Auginstori Levinta")
    st.write("Hola!😊") 
    st.write("my name is augin and you can call me ojin. I'm turning 22 years old. I'm a student at Lampung university in Mathematics education. I really like cooking, sport, art, design, etc. for getting more about me, here is my Instagram account🤗:")
    st.write("📍[ojinnnn08](https://www.instagram.com/ojinnnn08/)")
    st.write("Gracias!")

def cybercryme_chart():
        labels = ['2015', '2016', '2017', '2018', '2019', '2020']
        laporan = [2609, 3110, 3109, 4360, 4568, 2259]
        selesai = [624, 908, 1610, 2273, 2284, 527]

        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, laporan, width, label='Laporan', color="grey")
        rects2 = ax.bar(x + width/2, selesai, width, label='Selesai', color="orange")

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_title('Jumlah Kejahatan Siber Indonesia')
        ax.set_xticks(x, labels)
        ax.legend()

        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)

        fig.tight_layout()

        st.pyplot(fig)

def platform_terlapor_tertinggi():
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    
    labels = ['Telepon', 'SMS', 'Facebook', 'Instagram', 'Whatsapp']
    data = [299, 700, 854, 1_781, 1_874]

    ax.barh(labels, data, color="#ed593bff")
    ax.set_title('Jumlah Kejahatan Siber Indonesia')

    st.pyplot(fig)

def kontent_negatif_terbanyak():
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    
    labels = ['Pemerasan:', 'Tindakan merugian:', 'Pengancaman:', 'Penghinaan:', 'Penipuan:']
    data = [218, 314, 320, 580, 3_190]

    ax.barh(labels, data, color="#ed593bff")
    ax.set_title('Kontent Negatif Terbanyak')
    
    st.pyplot(fig)

def cybercryme_table():
    df = pd.DataFrame({
    'Tahun': [2018, 2019, 2020],
    'Aduan': [1, 1_443, 5_093],
    'Kerugian (Rupiah)': ["210 ribu", "49,5 miliar", "17,69 miliar"]
    })

    st.subheader("Kerugian")
    st.table(df)
    st.write("Keterangan *Pertengahan Juni")

# ---- SELECT A PAGE ----
st.sidebar.image ("./assets/Chamomile_Logo (2).png")
page_names_to_funcs = {
    "Dashboard": dashboard,
    "Content" : content,
    "About us" : about_us,
}

selected_page = st.sidebar.selectbox ("Select a page ", page_names_to_funcs.keys(), key="first")
page_names_to_funcs[selected_page]()

# ---- CONTACT ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

with st.container():
    st.write("----")
    st.subheader("Get In Touch With Us!")
    st.write("##")

    # Documentation : https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/dewi.arofani@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
