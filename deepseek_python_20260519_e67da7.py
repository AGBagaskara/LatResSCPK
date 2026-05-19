import streamlit as st
import pandas as pd
import numpy as np

# Fungsi AHP
def normalisasi_matrix(matrix):
    return matrix / matrix.sum(axis=0)

def hitung_bobot(matrix_ternormalisasi):
    return np.mean(matrix_ternormalisasi, axis=1)

def cek_konsistensi(matrix, bobot):
    n = len(matrix)
    
    indeks_acak = {
        2: 0.00, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45,
        10: 1.51, 11: 1.53, 12: 1.54, 13: 1.56, 14: 1.57
    }
    ri = indeks_acak[n]
    
    nilai_eigen = np.mean(matrix @ bobot / bobot)
    ci = (nilai_eigen - n) / (n - 1)
    cr = ci / ri
    
    konsisten = 1 if cr <= 0.1 else 0
    return [nilai_eigen, ci, ri, cr, konsisten]

def hitung_skor_akhir(bobot_alternatif, bobot_kriteria):
    return bobot_alternatif.T @ bobot_kriteria

def buat_matrix_cost(data):
    return np.array([
        [data[0]/data[0], data[1]/data[0], data[2]/data[0], data[3]/data[0], data[4]/data[0]],
        [data[0]/data[1], data[1]/data[1], data[2]/data[1], data[3]/data[1], data[4]/data[1]],
        [data[0]/data[2], data[1]/data[2], data[2]/data[2], data[3]/data[2], data[4]/data[2]],
        [data[0]/data[3], data[1]/data[3], data[2]/data[3], data[3]/data[3], data[4]/data[3]],
        [data[0]/data[4], data[1]/data[4], data[2]/data[4], data[3]/data[4], data[4]/data[4]]
    ])

def buat_matrix_benefit(data):
    return np.array([
        [data[0]/data[0], data[0]/data[1], data[0]/data[2], data[0]/data[3], data[0]/data[4]],
        [data[1]/data[0], data[1]/data[1], data[1]/data[2], data[1]/data[3], data[1]/data[4]],
        [data[2]/data[0], data[2]/data[1], data[2]/data[2], data[2]/data[3], data[2]/data[4]],
        [data[3]/data[0], data[3]/data[1], data[3]/data[2], data[3]/data[3], data[3]/data[4]],
        [data[4]/data[0], data[4]/data[1], data[4]/data[2], data[4]/data[3], data[4]/data[4]]
    ])

# Data
daftar_hp = ["Samsung Galaxy A5S", "Xiaomi Redmi Note 13 Pro", "iPhone 15", "OPPO Reno 11", "Vivo V29"]
harga = np.array([5.5, 3.8, 13.5, 5.0, 5.2])
baterai = np.array([5000, 5100, 3877, 5000, 4600])
ram = np.array([8, 12, 6, 8, 12])
kamera = np.array([50, 200, 48, 50, 50])

st.set_page_config(page_title="SPK Smartphone", layout="wide")

data_hp = {
    "Smartphone": daftar_hp,
    "Harga (Juta Rp)": harga,
    "Baterai (mAh)": baterai,
    "RAM (GB)": ram,
    "Kamera (MP)": kamera
}
df_hp = pd.DataFrame(data_hp)

# Sidebar
st.sidebar.title("⚙️ Pengaturan")
halaman = st.sidebar.selectbox("Pilih Halaman", [
    "Data Alternatif", "Metode AHP", "Metode WP"
])

bobot_harga = st.sidebar.slider("Harga (Juta Rp)", 0.0, 1.0, 0.7, 0.1)
bobot_baterai = st.sidebar.slider("Baterai (mAh)", 0.0, 1.0, 0.5, 0.1)
bobot_ram = st.sidebar.slider("RAM (GB)", 0.0, 1.0, 0.2, 0.1)
bobot_kamera = st.sidebar.slider("Kamera (MP)", 0.0, 1.0, 0.4, 0.1)

def ada_bobot_nol():
    return 0 in [bobot_harga, bobot_baterai, bobot_ram, bobot_kamera]

# Normalisasi bobot untuk WP
total_bobot_raw = bobot_harga + bobot_baterai + bobot_ram + bobot_kamera
w_harga_norm = bobot_harga / total_bobot_raw
w_baterai_norm = bobot_baterai / total_bobot_raw
w_ram_norm = bobot_ram / total_bobot_raw
w_kamera_norm = bobot_kamera / total_bobot_raw

st.sidebar.subheader("Bobot Ternormalisasi (WP)")
st.sidebar.caption(f"Harga: {w_harga_norm:.4f}")
st.sidebar.caption(f"Baterai: {w_baterai_norm:.4f}")
st.sidebar.caption(f"RAM: {w_ram_norm:.4f}")
st.sidebar.caption(f"Kamera: {w_kamera_norm:.4f}")

if ada_bobot_nol():
    st.sidebar.error("⚠️ Ada bobot bernilai 0! Metode AHP tidak bisa diproses.")

# HALAMAN DATA
if halaman == "Data Alternatif":
    st.header("📱 Data Alternatif Smartphone")
    st.dataframe(df_hp, use_container_width=True, hide_index=True)

    st.subheader("Keterangan Kriteria")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.error("**Harga**\n\nTipe: Cost\n*Semakin murah semakin baik*")
    with col2:
        st.success("**Baterai**\n\nTipe: Benefit\n*Semakin besar semakin baik*")
    with col3:
        st.success("**RAM**\n\nTipe: Benefit\n*Semakin besar semakin baik*")
    with col4:
        st.success("**Kamera**\n\nTipe: Benefit\n*Semakin besar semakin baik*")

# HALAMAN AHP
elif halaman == "Metode AHP":
    st.header("📊 Metode AHP")
    
    if ada_bobot_nol():
        st.error("❌ ERROR: Bobot tidak dapat bernilai 0!")
        st.warning("Silakan atur semua bobot kriteria menjadi lebih dari 0 (minimal 0.1) untuk menggunakan AHP.")
        st.stop()
    
    st.subheader("Matriks Perbandingan Berpasangan")
    
    matrix_kriteria = np.array([
        [bobot_harga/bobot_harga, bobot_harga/bobot_baterai, bobot_harga/bobot_ram, bobot_harga/bobot_kamera],
        [bobot_baterai/bobot_harga, bobot_baterai/bobot_baterai, bobot_baterai/bobot_ram, bobot_baterai/bobot_kamera],
        [bobot_ram/bobot_harga, bobot_ram/bobot_baterai, bobot_ram/bobot_ram, bobot_ram/bobot_kamera],
        [bobot_kamera/bobot_harga, bobot_kamera/bobot_baterai, bobot_kamera/bobot_ram, bobot_kamera/bobot_kamera]
    ])
    
    df_matrix_kriteria = pd.DataFrame(
        matrix_kriteria,
        index=["Harga", "Baterai", "RAM", "Kamera"],
        columns=["Harga", "Baterai", "RAM", "Kamera"]
    )
    st.dataframe(df_matrix_kriteria, use_container_width=True)
    
    st.subheader("Bobot Prioritas (Eigen Vector)")
    matrix_norm = normalisasi_matrix(matrix_kriteria)
    bobot_kriteria = hitung_bobot(matrix_norm)
    
    df_bobot = pd.DataFrame({
        "Kriteria": ["Harga", "Baterai", "RAM", "Kamera"],
        "Bobot": bobot_kriteria
    })
    st.dataframe(df_bobot, use_container_width=True, hide_index=True)
    
    st.subheader("Uji Konsistensi")
    hasil_konsistensi = cek_konsistensi(matrix_kriteria, bobot_kriteria)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("λ maks", f"{hasil_konsistensi[0]:.4f}")
    with col2:
        st.metric("CI", f"{hasil_konsistensi[1]:.4f}")
    with col3:
        st.metric("RI", f"{hasil_konsistensi[2]:.4f}")
    with col4:
        st.metric("CR", f"{hasil_konsistensi[3]:.4f}")
    
    if hasil_konsistensi[4] == 1:
        st.success("✅ Matriks konsisten (CR ≤ 0.1)")
    else:
        st.error("❌ Matriks tidak konsisten (CR > 0.1)")
    
    st.subheader("Perankingan Alternatif")
    
    # Hitung bobot tiap alternatif untuk tiap kriteria
    bobot_harga_alt = hitung_bobot(normalisasi_matrix(buat_matrix_cost(harga)))
    bobot_baterai_alt = hitung_bobot(normalisasi_matrix(buat_matrix_benefit(baterai)))
    bobot_ram_alt = hitung_bobot(normalisasi_matrix(buat_matrix_benefit(ram)))
    bobot_kamera_alt = hitung_bobot(normalisasi_matrix(buat_matrix_benefit(kamera)))
    
    matrix_bobot_alternatif = np.array([bobot_harga_alt, bobot_baterai_alt, bobot_ram_alt, bobot_kamera_alt])
    skor_akhir = hitung_skor_akhir(matrix_bobot_alternatif, bobot_kriteria)
    
    indeks_ranking = np.argsort(skor_akhir)[::-1]
    
    df_ranking = pd.DataFrame({
        "Smartphone": [daftar_hp[i] for i in indeks_ranking],
        "Skor AHP": [skor_akhir[i] for i in indeks_ranking],
        "Ranking": range(1, 6)
    })
    st.dataframe(df_ranking, use_container_width=True, hide_index=True)
    
    pemenang = daftar_hp[np.argmax(skor_akhir)]
    st.success(f"🏆 **Kesimpulan:** Smartphone terbaik adalah **{pemenang}** dengan skor {max(skor_akhir):.4f}")

# HALAMAN WP
else:
    st.header("📈 Metode Weighted Product")
    
    st.subheader("Bobot Kriteria")
    df_bobot_wp = pd.DataFrame({
        "Kriteria": ["Harga (Cost)", "Baterai (Benefit)", "RAM (Benefit)", "Kamera (Benefit)"],
        "Bobot Awal": [bobot_harga, bobot_baterai, bobot_ram, bobot_kamera],
        "Bobot Ternormalisasi": [w_harga_norm, w_baterai_norm, w_ram_norm, w_kamera_norm]
    })
    st.dataframe(df_bobot_wp, use_container_width=True, hide_index=True)
    
    st.subheader("Vektor S")
    st.latex(r"S_i = \prod_{j=1}^{n} X_{ij}^{w_j}")
    
    pangkat = np.array([-w_harga_norm, w_baterai_norm, w_ram_norm, w_kamera_norm])
    
    vektor_s = []
    for i in range(len(daftar_hp)):
        s = (harga[i] ** pangkat[0]) * (baterai[i] ** pangkat[1]) * (ram[i] ** pangkat[2]) * (kamera[i] ** pangkat[3])
        vektor_s.append(s)
    vektor_s = np.array(vektor_s)
    
    df_vektor_s = pd.DataFrame({
        "Smartphone": daftar_hp,
        "Vektor S": vektor_s
    })
    st.dataframe(df_vektor_s, use_container_width=True, hide_index=True)
    
    st.subheader("Vektor V dan Ranking")
    st.latex(r"V_i = \frac{S_i}{\sum S}")
    
    vektor_v = vektor_s / np.sum(vektor_s)
    
    df_ranking_wp = pd.DataFrame({
        "Smartphone": daftar_hp,
        "Vektor V": vektor_v
    })
    df_ranking_wp = df_ranking_wp.sort_values("Vektor V", ascending=False).reset_index(drop=True)
    df_ranking_wp["Ranking"] = range(1, 6)
    
    st.dataframe(df_ranking_wp, use_container_width=True, hide_index=True)
    
    pemenang_wp = df_ranking_wp.iloc[0]["Smartphone"]
    skor_wp = df_ranking_wp.iloc[0]["Vektor V"]
    st.success(f"🏆 **Kesimpulan:** Smartphone terbaik adalah **{pemenang_wp}** dengan nilai {skor_wp:.4f}")