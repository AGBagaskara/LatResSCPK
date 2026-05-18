import streamlit as st
import pandas as pd
import numpy as np


# Rumus
def normalize_comparation(m): #normalisasi matriks
    sumCol = m.sum(axis=0)
    norm = m/sumCol
    return norm

def weight(m): #menghitung bobot
    return np.mean(m, axis=1)

def validity_check(m, w):
    n = len(m)
    
    list_RI = {
        2: 0.00, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45,
        10: 1.51, 11: 1.53, 12: 1.54, 13: 1.56, 14: 1.57
    }
    RI = list_RI[n]
    
    CV = m @ w / w
    
    eigen = np.mean(CV)
    
    CI = (eigen - n)/(n-1)
    
    CR = CI/RI
    
    if CR <= 0.1:
        konsisten = 1;
    else:
        konsisten = 0;
    hasil = [eigen, CI, RI, CR, konsisten]
    return hasil
    
        
def final_weight(w_alt, w_crit):
    w_fin = w_alt.T @ w_crit
    return w_fin

def matriks_perbandingan_cost(data):
    MP = np.array([
            [data[0]/data[0],data[1]/data[0],data[2]/data[0],data[3]/data[0],data[4]/data[0]],
            [data[0]/data[1],data[1]/data[1],data[2]/data[1],data[3]/data[1],data[4]/data[1]],
            [data[0]/data[2],data[1]/data[2],data[2]/data[2],data[3]/data[2],data[4]/data[2]],
            [data[0]/data[3],data[1]/data[3],data[2]/data[3],data[3]/data[3],data[4]/data[3]],
            [data[0]/data[4],data[1]/data[4],data[2]/data[4],data[3]/data[4],data[4]/data[4]]
        ])
    return MP

def matriks_perbandingan_benefit(data):
    MP = np.array([
            [data[0]/data[0],data[0]/data[1],data[0]/data[2],data[0]/data[3],data[0]/data[4]],
            [data[1]/data[0],data[1]/data[1],data[1]/data[2],data[1]/data[3],data[1]/data[4]],
            [data[2]/data[0],data[2]/data[1],data[2]/data[2],data[2]/data[3],data[2]/data[4]],
            [data[3]/data[0],data[3]/data[1],data[3]/data[2],data[3]/data[3],data[3]/data[4]],
            [data[4]/data[0],data[4]/data[1],data[4]/data[2],data[4]/data[3],data[4]/data[4]]
        ])
    return MP

# data 
smartphone = ["Samsung Galaxy A5S", "Xiaomi Redmi Note 13 Pro", "iPhone 15", "OPPO Reno 11", "Vivo V29"]
harga = np.array([5.5, 3.8, 13.5, 5.0, 5.2])
baterai = np.array([5000, 5100, 3877, 5000, 4600])
ram = np.array([8, 12, 6, 8, 12])
kamera = np.array([50, 200, 48, 50, 50])

# --- 1. KONFIGURASI HALAMAN ---
# Mengatur layout menjadi lebar (wide) agar tabel terlihat jelas
st.set_page_config(page_title="SPK Smartphone", layout="wide")

# --- 2. DATA ALTERNATIF ---
# Menyiapkan data ke dalam bentuk Pandas DataFrame
data = {
    "Smartphone": smartphone,
    "Harga (Juta Rp)": harga,
    "Baterai (mAh)": baterai,
    "RAM (GB)": ram,
    "Kamera (MP)": kamera
}
df = pd.DataFrame(data)

# --- 3. SIDEBAR (PENGATURAN BOBOT) ---
st.sidebar.title("⚙️ Pengaturan")
pilihan = st.sidebar.selectbox("Pilih Halaman : ",
                               ("Page 1 - Data Alternatif", "Page 2 - AHP", "Page 3 - WP"))

# Menggunakan slider untuk input bobot (kamu bisa sesuaikan min, max, dan default valuenya)
bobot_harga = st.sidebar.slider("Harga (Juta Rp)", min_value=1.0, max_value=5.0, value=2.0, step=0.1)
bobot_baterai = st.sidebar.slider("Baterai (mAh)", min_value=1.0, max_value=5.0, value=2.5, step=0.1)
bobot_ram = st.sidebar.slider("RAM (GB)", min_value=1.0, max_value=5.0, value=3.0, step=0.1)
bobot_kamera = st.sidebar.slider("Kamera (MP)", min_value=1.0, max_value=5.0, value=2.5, step=0.1)

# Menghitung bobot ternormalisasi
total_bobot = bobot_harga + bobot_baterai + bobot_ram + bobot_kamera
w_harga = bobot_harga / total_bobot
w_baterai = bobot_baterai / total_bobot
w_ram = bobot_ram / total_bobot
w_kamera = bobot_kamera / total_bobot

st.sidebar.subheader("Bobot Ternormalisasi")
st.sidebar.caption(f"Harga: {w_harga:.4f}")
st.sidebar.caption(f"Baterai: {w_baterai:.4f}")
st.sidebar.caption(f"RAM: {w_ram:.4f}")
st.sidebar.caption(f"Kamera: {w_kamera:.4f}")


# --- 4. NAVIGASI HALAMAN (TABS) ---
# ==========================================
# HALAMAN 1: DATA ALTERNATIF
# ==========================================
match pilihan:
    case "Page 1 - Data Alternatif":
        st.header("Data Alternatif Smartphone")
        st.write("Sistem pendukung keputusan ini membantu memilih smartphone terbaik berdasarkan empat kriteria utama.")
        
        # Menampilkan tabel
        st.dataframe(df, use_container_width=True, hide_index=True)

        st.subheader("Keterangan Kriteria")
        # Membagi layout menjadi 4 kolom untuk kotak keterangan
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.error("**Harga (Juta Rp)**\n\nTipe: Cost\n\n*Semakin murah semakin baik*")
        with col2:
            st.success("**Baterai (mAh)**\n\nTipe: Benefit\n\n*Semakin besar semakin baik*")
        with col3:
            st.success("**RAM (GB)**\n\nTipe: Benefit\n\n*Semakin besar semakin baik*")
        with col4:
            st.success("**Kamera (MP)**\n\nTipe: Benefit\n\n*Semakin besar semakin baik*")

# ==========================================
# HALAMAN 2: METODE AHP
# ==========================================
    case "Page 2 - AHP":
        st.header("Penyelesaian dengan Metode AHP")
        
        st.subheader("3.1 Matriks Perbandingan Berpasangan")
        
        # Matriks Perbandingan Bobot Kriteria
        MPBK = np.array([
            [bobot_harga/bobot_harga, bobot_harga/bobot_baterai, bobot_harga/bobot_ram, bobot_harga/bobot_kamera],
            [bobot_baterai/bobot_harga, bobot_baterai/bobot_baterai, bobot_baterai/bobot_ram, bobot_baterai/bobot_kamera],
            [bobot_ram/bobot_harga, bobot_ram/bobot_baterai, bobot_ram/bobot_ram, bobot_ram/bobot_kamera],
            [bobot_kamera/bobot_harga, bobot_kamera/bobot_baterai, bobot_kamera/bobot_ram, bobot_kamera/bobot_kamera]
        ])

        # Tampil Tabel perbandingan Kriteria
        df_perbandingan_kriteria = pd.DataFrame({
            "Kriteria": ["Harga (Cost)", "Baterai (Benefit)", "RAM (Benefit)", "Kamera (Benefit)"],
            "Harga (Cost)": MPBK[0,:],
            "Baterai (Benefit)": MPBK[1,:],
            "RAM (Benefit)": MPBK[2,:],
            "Kamera (Benefit)": MPBK[3,:]
        })
        
        st.dataframe(df_perbandingan_kriteria, use_container_width=True, hide_index=True)
        
        st.subheader("3.2 Bobot Prioritas (Eigen Vector)")
        
        # Normalisasi MPBK
        MPBK_norm = normalize_comparation(MPBK)
        # Bobot Kriteria
        wk = weight(MPBK_norm)
        
        df_bobot_prioritas = pd.DataFrame({
            "Kriteria": ["Harga (Cost)", "Baterai (Benefit)", "RAM (Benefit)", "Kamera (Benefit)"],
            "Bobot Prioritas": [wk[0],wk[1],wk[2],wk[3]]
        })
        
        st.dataframe(df_bobot_prioritas, use_container_width=True, hide_index=True)
        
        
        st.subheader("3.3 Nilai Konsistensi (CI, RI, CR)")
        
        # Validity check
        hasil_konsistensi = validity_check(MPBK, wk)
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.write("λ maks")
            st.subheader(hasil_konsistensi[0])
        with col2:
            st.write("CI")
            st.subheader(hasil_konsistensi[1])
        with col3:
            st.write("RI")
            st.subheader(hasil_konsistensi[2])
        with col4:
            st.write("CR")
            st.subheader(hasil_konsistensi[3])

        
        st.subheader("3.4 Keterangan Konsistensi")
        # TODO: Logika IF ELSE. Jika CR < 0.1, st.success("Konsisten"), else 
        if hasil_konsistensi[4] == 1:
            st.success("Konsisten")
        else:
            st.error("Tidak Konsisten")
        
        st.subheader("3.5 Skor Akhir dan Ranking")
        # TODO: Kalikan matriks alternatif dengan eigen vector, urutkan, dan tampilkan hasilnya
        
        #   Menghitung AHP Lanjutan
        
        # harga
        MPBa = matriks_perbandingan_cost(harga)
        MPBa_norm = normalize_comparation(MPBa)
        wa = weight(MPBa_norm)
        
        # baterai
        MPBb = matriks_perbandingan_benefit(baterai)
        MPBb_norm = normalize_comparation(MPBb)
        wb = weight(MPBb_norm)
        
        # ram
        MPBc = matriks_perbandingan_benefit(ram)
        MPBc_norm = normalize_comparation(MPBc)
        wc = weight(MPBc_norm)
        
        #kamera
        MPBd = matriks_perbandingan_benefit(kamera)
        MPBd_norm = normalize_comparation(MPBd)
        wd = weight(MPBd_norm)
        
        # hitung akhir
        w_total = np.array([wa,wb,wc,wd])
        w_final = final_weight(w_total, wk)
        
        # urutin pemenang
        index_sort = np.argsort(w_final)[::-1]
        
        df_perangkingan = pd.DataFrame({
            "Smartphone": [smartphone[index_sort[0]],smartphone[index_sort[1]],smartphone[index_sort[2]],smartphone[index_sort[3]],smartphone[index_sort[4]]],
            "Skor AHP": [w_final[index_sort[0]],w_final[index_sort[1]],w_final[index_sort[2]],w_final[index_sort[3]],w_final[index_sort[4]]],
            "Ranking": [1,2,3,4,5]
        })
        
        st.dataframe(df_perangkingan, use_container_width=True, hide_index=True)
        
        # index pemenang anjay
        pemenang = np.argmax(w_final)
        st.success(f"🏆 **Kesimpulan AHP:**\n\nBerdasarkan metode AHP, smartphone terbaik adalah {smartphone[pemenang]} dengan skor {w_final[pemenang]}")

# ==========================================
# HALAMAN 3: METODE WP
# ==========================================
    case "Page 3 - WP":
        st.header("Penyelesaian dengan Metode WP")
        
        st.subheader("4.1 Bobot Kriteria (W)")
        # Menampilkan bobot yang sudah dinormalisasi dari sidebar
        df_bobot_wp = pd.DataFrame({
            "Kriteria": ["Harga (Cost)", "Baterai (Benefit)", "RAM (Benefit)", "Kamera (Benefit)"],
            "Bobot Awal": [bobot_harga, bobot_baterai, bobot_ram, bobot_kamera],
            "Bobot Ternormalisasi": [w_harga, w_baterai, w_ram, w_kamera]
        })
        st.dataframe(df_bobot_wp, use_container_width=True, hide_index=True)

        st.subheader("4.2 Vektor S")
        # TODO: Tulis logika matematika WP untuk Vektor S di sini
        # Ingat: Kriteria Cost pangkatnya negatif (-w_harga), Benefit pangkatnya positif (+w_baterai)
        st.info("Area untuk tabel perhitungan Vektor S")

        st.subheader("4.3 Vektor V dan Ranking Akhir")
        # TODO: Tulis logika Vektor V (Nilai S alternatif dibagi Total nilai S), lalu urutkan rankingnya
        st.info("Area untuk tabel hasil Vektor V dan Ranking")
        
        st.success("🏆 **Kesimpulan Weighted Product (WP):**\n\nBerdasarkan metode WP, rekomendasi utama adalah ... dengan nilai ...")