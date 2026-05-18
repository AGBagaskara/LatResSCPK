import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Streamlit Keren", layout="wide")

# Judul
st.title("1. Elemen Dasar di Streamlit")
st.header("Ini adalah Header (Level 2)")
st.subheader("Ini adalah Subheader (Level 3)")

# Garis Pembatas
st.divider()

# Teks
st.write("Ini pakai **st.write()**. Bisa buat nampilin teks, dataframe, dll")
st.markdown("Ini pakai **st.markdown()**. Cocok buat teks panjang dengan *styling* khusus.")
st.text("Ini pakai st.text(). Styling bintang **tidak** jadi tebal.")
st.caption("Ini pakai st.caption(). Teks kecil dan pudar, cocok buat footnote.")

st.divider()

df = pd.read_csv('data_hp.csv')

st.write("Bisa juga nampilin data:")
st.write(df)

st.write("Visualisasi Data:")
fig = plt.figure(figsize=(10, 5))

plt.bar(df['ID_HP'],df['Terjual_Bulan_Ini'], color='skyblue')
plt.title("Total Penjualan Smartphone Bulan Ini")
plt.xlabel("ID Smartphone")
plt.ylabel("Jumlah Terjual (Unit)")
st.pyplot(fig)

st.divider()

# Kode
st.write("Ini contoh menampilkan kodingan pakai `st.code()`:")
st.code("""
# Script Python
def halo():
    print("hai gengs")""", language="python")

st.write("Ini contoh rumus matematika pakai `st.latex()`:")
st.latex("E = mc^2")

st.title("2. Widget Dasar di Streamlit")
st.write("Widget biar bisa interaksi sama user")
st.divider()

# Input
nama = st.text_input("Siapa namamu?", placeholder="Masukkan nama panggilan")
umur = st.number_input("Berapa umurmu?", min_value=18, max_value=28, step=2)
pesan = st.text_area("Tulis pesan singkat untuk hari ini:")

st.divider()

# Option
gender = st.radio("Gendermu apa?", ["Laki-laki", "Perempuan", "Custom"])
if gender == "Custom":
    custom_gender = st.text_input("Custom Gender jir:")

hobi = st.selectbox("Hobi apa gengs?", ["Makan", "Tidur", "Main Game", "Nonton Anime"])
skills = st.multiselect("Skillmu apa?", ["MAIN VALO 24 JAM", "ngoding tanpa AI"])

st.divider()

# Slider & Checkbox
Rating = st.slider("Kasih rating buat pemerintah", min_value=0, max_value=10, step=1)
setuju = st.checkbox("Setuju kalau pemerintah kerjaannya cuma makan gaji buta?")

st.divider()

st.title("3. Widget Lanjutan di Streamlit")
st.write("Widget yang lebih kompleks buat interaksi yang lebih seru")

# Sidebar
with st.sidebar:
    st.header("Siderbar coy")
    rating_sidebar = st.slider("Kasih rating buat pemerintah (di sidebar)", min_value=0, max_value=10, step=1)
    st.write(f"Rating di sidebar: {rating_sidebar}")
    btn = st.button("HIDUP JOKOWI")
    if btn:
        st.sidebar.success("JOKOWI HIDUP!!")
        st.error("JOKOWI MATI!!")

# Tab
tab1, tab2, tab3 = st.tabs(["Jokowi", "Prabowo", "Anies"])

with tab1:
    st.header("Tab Jokowi")
    st.write("Jokowi adalah Presiden Indonesia yang ke-7. Dia dikenal dengan gaya kepemimpinannya yang merakyat dan program-program pembangunan infrastruktur yang ambisius.")
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7BmXRAmkKx69NHnHYdAKOc3Yj6F6r4LR0Hw&s')

with tab2:
    st.header("Tab Prabowo")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("ini kolom 1 - kiri")
    with col2:
        st.warning("ini kolom 2 - tengah")
    with col3:
        st.error("ini kolom 3 - kanan")


with tab3:

    st.header("Tab Anies")
    
    # Expander
    with st.expander("KLIK KALAU KAMU SUKA ANIES"):
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8QMIeKPROE2T0kipLp5oLAEcygEoB-ZLP-g&s')
        st.markdown("""
            Anies Baswedan adalah seorang politisi Indonesia yang pernah menjabat sebagai Gubernur DKI Jakarta. Dia dikenal dengan kebijakan-kebijakan kontroversialnya, seperti penutupan tempat hiburan malam dan pembatasan kegiatan seni di Jakarta. Meskipun begitu, Anies juga memiliki basis pendukung yang kuat yang mengagumi gaya kepemimpinannya yang tegas dan fokus pada pembangunan infrastruktur.
        """)

    # container
    with st.container(border=True):
        st.write("Ini adalah container. Semua elemen di dalamnya akan tetap berdekatan.")
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1RmOyvevzAHrEroy6q6zsHWFE8o_bgl3oSg&s')