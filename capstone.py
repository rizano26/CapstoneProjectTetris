import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(layout="wide")
st.title('Korelasi Antara Infrastruktur Listrik dengan Kualitas Pendidikan di Indonesia')
df = pd.read_excel('Kapasitas + Pendidikan.xlsx')
df['Tahun'] = df['Tahun'].astype(str)
plt.style.use('dark_background')

selectbox = st.selectbox('Pilihan',("Latar Belakang",'Chart Total Kapasitas Terpasang di Indonesia', 'Chart Persentase Penduduk yang Lulus SMA di Indonesia', 'Korelasi Antara Total Kapasitas Terpasang dan Persentase Penduduk yang Lulus SMA di Indonesia ', 'Solusi'))
if selectbox == 'Chart Total Kapasitas Terpasang di Indonesia':
    plt.plot(df['Tahun'], df['Kapasitas terpasang'])
    plt.title('Jumlah Kapasitas Terpasang di Indonesia', pad=40)
    plt.ylabel('in MegaWatt')
    st.pyplot(plt)
    st.caption('Sumber : bps.go.id')
    st.divider()
    st.write('Alasan memilih data Kapasitas listrik terpasang adalah data ini cukup mencerminkan jumlah daya yang tersedia dalam sistem kelistrikan suatu negara. Dengan mempertimbangkan kapasitas listrik terpasang, kita dapat memahami sejauh mana infrastruktur listrik telah berkembang dan seberapa besar kapasitas produksi listrik yang dapat disediakan untuk memenuhi kebutuhan.')
elif selectbox == 'Chart Persentase Penduduk yang Lulus SMA di Indonesia':
    plt.plot(df['Tahun'], df['Persentase Penduduk yang Lulus SMA'])
    plt.title('Persentase Penduduk Indonesia yang Lulus SMA', pad=40)
    plt.ylabel('in Percentage (%)')
    st.pyplot(plt)
    st.caption('Sumber : bps.go.id')
    st.divider()
    st.write('Alasan memilih data persentase penduduk Indonesia yang berhasil lulus SMA sebagai barometer kualitas pendidikan di Indonesia adalah Persentase penduduk yang berhasil lulus SMA memberikan gambaran tentang sejauh mana sistem pendidikan di Indonesia berhasil mencapai tujuan utama yaitu memastikan penduduk memiliki kualifikasi pendidikan setara dengan SMA atau disebut wajib belajar 12 tahun. Persentase lulusan SMA juga mencerminkan tingkat keterjangkauan dan kesetaraan pendidikan di Indonesia')
elif selectbox == 'Latar Belakang':
    st.header('Latar Belakang')
    st.write('Di dalam perjalanan menuju kemajuan suatu bangsa, terdapat berbagai faktor yang berperan penting dalam mencapai kesuksesan. Dalam konteks Indonesia, kita mengenal pentingnya dua aspek yang mendasar, yaitu infrastruktur listrik yang kuat dan kualitas pendidikan yang unggul. Meskipun keduanya memiliki peran signifikan dalam pembangunan negara, korelasi antara infrastruktur listrik dengan tingkat kualitas pendidikan masih menjadi misteri yang menarik untuk diungkap.')
    st.write('Indonesia, sebagai negara dengan populasi besar dan keragaman budaya yang luas, menghadapi tantangan signifikan dalam memastikan akses pendidikan berkualitas bagi seluruh warganya. Salah satu hambatan utama adalah ketidaktersediaan infrastruktur pendidikan yang memadai, yang mencakup bangunan sekolah yang aman, fasilitas belajar lengkap, dan transportasi yang layak bagi siswa di daerah terpencil. Krisis infrastruktur ini tidak hanya mempengaruhi aksesibilitas dan kualitas pendidikan, tetapi juga menimbulkan kesenjangan antara siswa di daerah perkotaan dan pedesaan.')
    st.write('Di sisi lain, pembangunan infrastruktur listrik yang memadai telah terbukti berdampak positif terhadap pertumbuhan ekonomi dan distribusi pendapatan, yang secara tidak langsung dapat mempengaruhi tingkat pendidikan. Oleh karena itu, penelitian ini bertujuan untuk menganalisis korelasi antara infrastruktur listrik dan kualitas pendidikan di Indonesia, dengan harapan dapat memberikan wawasan tentang bagaimana kedua faktor ini berkontribusi terhadap kemajuan pendidikan dan, pada akhirnya, kemajuan negara.')
elif selectbox == 'Solusi':
    st.header('Solusi')
    st.write('Untuk memperkuat dan memanfaatkan korelasi yang kuat antara infrastruktur listrik dan tingkat kualitas pendidikan di Indonesia guna memajukan negara, beberapa solusi yang dapat dipertimbangkan antara lain:')
    st.subheader('1. Investasi dalam infrastruktur listrik') 
    st.write('Pemerintah perlu terus meningkatkan investasi dalam pembangunan dan pemeliharaan infrastruktur listrik di seluruh wilayah. Pembangkit listrik, jaringan transmisi, dan gardu distribusi harus ditingkatkan agar dapat memberikan pasokan listrik yang andal dan stabil kepada institusi pendidikan di seluruh negeri.')
    st.subheader('2. Penyediaan listrik berkelanjutan di daerah terpencil')
    st.write(' Fokus pada penyediaan akses listrik yang terjangkau dan berkelanjutan di daerah terpencil dan terisolasi. Hal ini akan memastikan bahwa institusi pendidikan di daerah terpencil juga mendapatkan manfaat dari infrastruktur listrik yang berkualitas, sehingga kesenjangan pendidikan dapat dikurangi.')
    st.subheader('3. Pengembangan program pelatihan guru')
    st.write('Dukungan dan pelatihan kontinu bagi guru dan tenaga pendidik dalam pemanfaatan teknologi pendidikan dan penggunaan sumber daya listrik yang modern akan meningkatkan kualitas pembelajaran. Program pelatihan ini dapat membantu guru dalam mengintegrasikan teknologi ke dalam proses pembelajaran dan meningkatkan kemampuan mereka dalam memanfaatkan sumber daya listrik yang tersedia.')
    st.subheader('4. Kerjasama antara pemerintah dan sektor swasta')
    st.write('Mendorong kerjasama yang kuat antara pemerintah dan sektor swasta dalam mengembangkan infrastruktur listrik dan pendidikan. Kemitraan ini dapat melibatkan perusahaan energi, penyedia teknologi, dan lembaga pendidikan untuk menciptakan solusi inovatif dan berkelanjutan yang dapat memperkuat kualitas pendidikan melalui infrastruktur listrik yang handal.')
    st.subheader('5. Peningkatan literasi energi')
    st.write('Meningkatkan pemahaman masyarakat tentang pentingnya infrastruktur listrik yang baik dan hubungannya dengan kualitas pendidikan. Pendidikan dan kesadaran energi yang lebih baik dapat memberdayakan masyarakat untuk mengambil tindakan yang mendukung penggunaan energi yang efisien dan berkelanjutan, serta mendorong partisipasi dalam upaya peningkatan infrastruktur listrik.')
    st.subheader('6. Peningkatan akses internet')
    st.write('Menyediakan akses internet yang luas dan terjangkau di seluruh negeri. Internet memainkan peran penting dalam pendidikan modern, memungkinkan akses ke sumber daya pendidikan online, pembelajaran jarak jauh, dan kolaborasi antara siswa dan guru. Dengan meningkatnya akses internet, institusi pendidikan dapat memanfaatkan potensi teknologi untuk meningkatkan kualitas pendidikan.')
    
else:
    fig, ax1 = plt.subplots()
    ax1.plot(df['Tahun'], df['Kapasitas terpasang'], label='Kapasitas terpasang')
    ax1.set_ylabel('in MegaWatt')
    ax1.set_ylim(55000, 70000)

    ax2 = ax1.twinx()
    ax2.plot(df['Tahun'], df['Persentase Penduduk yang Lulus SMA'], label='Persentase Penduduk yang Lulus SMA', color='orange')
    ax2.set_ylabel('in Percentage (%)')
    ax2.set_ylim(55, 70)

    plt.title('Korelasi Antara Infrastruktur Listrik dan Kualitas Pendidikan di Indonesia', pad=40)
    fig.legend(loc='lower center')
    plt.subplots_adjust(bottom=0.2)
    st.pyplot(plt)
    st.caption('Sumber : bps.go.id')
    korelasiKapasitasPendidikan = df['Kapasitas terpasang'].corr(df['Persentase Penduduk yang Lulus SMA'])
    st.subheader('Koefisien Korelasi adalah : ' + str(korelasiKapasitasPendidikan) )
    st.divider()
    st.write('Dari koefisien korelasi diatas dapat disimpulkan bahwa jika angka kapasitas listrik meningkat, maka kualitas pendidikan di Indonesia akan cenderung meningkat juga.')
    st.write('Dengan adanya infrastruktur listrik yang kuat, pendidikan di Indonesia dapat meningkat secara keseluruhan. Stabilitas pasokan daya listrik memungkinkan lembaga pendidikan beroperasi dengan lancar dan efisien. Penggunaan teknologi modern dalam pembelajaran menjadi lebih mudah dan terjangkau, memberikan peluang untuk mengadopsi metode pengajaran yang inovatif.')
