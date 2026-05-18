# =============================================================================
# Tugas 2 Praktikum SCPK IF-G
# Analisis & Visualisasi Data Emisi CO2 Industri
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# 1. MATRIKS EMISI CO2 BULANAN (Januari - April)
#    Sektor: Transportasi, Manufaktur, Pertanian
# =============================================================================

emisi_matriks = np.array([
    [120, 135, 150, 145],  # Transportasi
    [200, 190, 210, 220],  # Manufaktur
    [80,  85,  80,  90],   # Pertanian
])

# Slicing: data sektor Manufaktur selama 4 bulan
manufaktur = emisi_matriks[1, :]
print("Data Emisi Manufaktur (Jan-Apr):", manufaktur)

# Ubah dimensi matriks menjadi 1 dimensi
manufaktur_1d = manufaktur.flatten()
print("Manufaktur (1D)              :", manufaktur_1d)


# =============================================================================
# 2. PERSAMAAN LINIER - EMISI HARIAN PABRIK A & PABRIK B
#    3x + 2y = 120
#    x  + 4y = 140
# =============================================================================

koefisien = np.array([
    [3, 2],
    [1, 4],
])
konstanta = np.array([120, 140])

hasil = np.linalg.solve(koefisien, konstanta)
nama_pabrik = ['Pabrik A', 'Pabrik B']

print("\nHasil Persamaan Linier:")
for i in range(len(hasil)):
    print(f"  Emisi {nama_pabrik[i]} adalah {int(hasil[i])} ton")


# =============================================================================
# 3. FUNGSI PERHITUNGAN EMISI
# =============================================================================

def hitung_total_rata2(matriks_emisi):
    """Menghitung total dan rata-rata emisi per sektor."""
    total    = np.sum(matriks_emisi, axis=1)
    rata_rata = np.mean(matriks_emisi, axis=1)
    return total, rata_rata


def cari_ekstrem_emisi(matriks_emisi):
    """Mencari nilai emisi tertinggi dan terendah dari seluruh data."""
    matriks_1d   = matriks_emisi.flatten()
    data_tertinggi = matriks_1d[np.argmax(matriks_emisi)]
    data_terendah  = matriks_1d[np.argmin(matriks_emisi)]
    return data_tertinggi, data_terendah


total_emisi, rata_rata_emisi = hitung_total_rata2(emisi_matriks)
data_tertinggi, data_terendah = cari_ekstrem_emisi(emisi_matriks)

print("\nRingkasan Statistik Emisi:")
print(f"  Total Emisi per Sektor   : {total_emisi}")
print(f"  Rata-rata Emisi per Sektor: {rata_rata_emisi}")
print(f"  Emisi Tertinggi          : {data_tertinggi}")
print(f"  Emisi Terendah           : {data_terendah}")


# =============================================================================
# 4. LINE PLOT - Tren Emisi Sektor Transportasi (Jan-Apr)
# =============================================================================

bulan = ['Januari', 'Februari', 'Maret', 'April']
tren_transportasi = emisi_matriks[0, :]

plt.figure()
plt.plot(bulan, tren_transportasi, marker='o', linestyle='--', color='g')
plt.title('Tren Emisi Sektor Transportasi')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Emisi (Ton)')
plt.yticks(range(110, 161, 4))
plt.grid(True)
plt.tight_layout()
plt.show()


# =============================================================================
# 5. BAR PLOT - Perbandingan Emisi Ketiga Sektor pada Bulan April
# =============================================================================

emisi_april = emisi_matriks[:, 3]
sektor      = ['Transportasi', 'Manufaktur', 'Pertanian']
warna       = ['#fe218b', '#fed700', '#21b0fe']

plt.figure()
plt.bar(sektor, emisi_april, color=warna)
plt.title('Emisi CO2 per Sektor - Bulan April')
plt.xlabel('Sektor')
plt.ylabel('Jumlah Emisi (Ton)')
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()


# =============================================================================
# 6. PIE CHART - Persentase Kontribusi Total Emisi per Sektor (4 Bulan)
# =============================================================================

label_sektor = ['Transportasi', 'Manufaktur', 'Pertanian']

plt.figure()
plt.pie(total_emisi, labels=label_sektor, autopct='%1.1f%%')
plt.title('Kontribusi Total Emisi CO2 per Sektor (Jan-Apr)')
plt.tight_layout()
plt.show()
