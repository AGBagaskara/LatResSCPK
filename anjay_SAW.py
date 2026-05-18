import pandas as pd
import numpy as np

# daftar kriteria untuk saw
daftar_kriteria = ['Harga', 'Rating', 'Prosessor', 'Ram', 'Baterai'] 

# daftar kriteria dari harga (contoh jika kriteria > 8000000 makan nilainya adalah 5)
kriteria_harga = [8000000, 6000000, 4000000, 2000000, 0] 

# sama kayak atas bedanya ratingnya kayak ipk aokwoak
kriteria_rating = [85, 75, 65, 55, 0] 

# iki preferensi pribadi sih (bionic top 1 men fanboy iphone seneng awkawkawo)
kriteria_prosesor = ['Bionic', 'Snapdragon', 'Dimensity', 'Exynos', 'Helio']

# iki aneh asline, dadi ngitung kriteria e ki seko penjumlahan ram karo penyimpanan ben gampang seko datasheet e walaupun rodo ra masuk akal
# waguh tak ganti
# kriteria_ram = [512, 256, 128, 64, 0] 
kriteria_ram = [8, 6, 4, 2, 0]

# iki yo aneh, le ngitung penjumlahan kapasitas baterai + watt charger misal 5000 + 66w total skor e dadi 5066
# iki yo waguh tapi watt e ra terlalu ngaruh
kriteria_baterai = [5000, 4000, 3000, 2000, 0] 

# daftar alternatif
daftar_hp = ['Xiaomi Redmi Note 12 Pro 5G', 
             'Vivo V25 5G',
             'IQOO 11 5G',
             'Samsung Galaxy A54 5G',
             'Xiaomi 13 5G',
             'Apple iphone 15 Plus']

# baca datasheet smartphones.csv, iki tekan bagian matriks_saw ra penting nggo sistem tee mbenake datasheet sek ra jelas
anjay = pd.read_csv('smartphones.csv') 

# jikuk data hp seko datasheet sesuai alternatif
df = anjay[anjay['model'].str.contains('|'.join(daftar_hp), case=False)] 

# datatype datasheet di ubah dadi string kabeh, ra penting iki ra ngaruh
df = df.astype('string') 

# ngilangi simbol rupee, datasheet e seko india
df['price'] = df['price'].str.replace('₹', '') 
# ganti , dadi . men ra eror pas dadi float
df['price'] = df['price'].str.replace(',', '.') 
# ubah data type rating karo price dadi float
df[['rating', 'price']] = df[['rating','price']].astype('float') 

# ubah price seko india neng indonesia, biar apa? biar keren
df['price'] = df['price'] * 95000 

# data processor di pisah perkata terus jikuk kata pertama koyo bionic, exynos dll
df['processor'] = df['processor'].str.split().str[0] 

# iki podo sek mau bedane njikuk kata ke 1 karo ke 3 terus di ubah dadi float terus ditambah
# rasido waguh
# df['ram'] = df['ram'].str.split().str[0].astype(float) + df['ram'].str.split().str[3].astype(float) 
df['ram'] = df['ram'].str.split().str[0].astype(float)

# iki podo sek ram tapi luweh simple, jikuk kabeh angka terus dijumlah kabeh angkane
# iki yo waguh
# df['battery'] = df['battery'].str.findall('(\\d+)').apply(lambda x: sum(float(i) for i in x)) 
df['battery'] = df['battery'].str.split().str[0].astype(float)

# datasheet e mau di ubah dadi matriks
sample_fiks = df[['model','price','rating','processor', 'ram', 'battery']]
matriks = sample_fiks.to_numpy()

# misah matriks, iki rodo edan sitik 
# karo sisan wadah hasil nilai e
# eh iki matriks po array lek jenenge
matriks_model = matriks[:, 0]
matriks_harga = matriks[:, 1]
matriks_nilai_harga = np.zeros_like(matriks_harga) # ra nganggo iki rapopo asline
matriks_rating = matriks[:, 2]
matriks_nilai_rating = np.zeros_like(matriks_rating)
matriks_prosessor= matriks[:, 3]
matriks_nilai_prosessor = np.zeros_like(matriks_prosessor)
matriks_ram = matriks[:, 4]
matriks_nilai_ram = np.zeros_like(matriks_ram)
matriks_baterai = matriks[:, 5]
matriks_nilai_baterai = np.zeros_like(matriks_baterai)

# fungsi untuk memberi nilai kriteria
def beriNilaiKriteriaInt(matriks_kriteria, batas_kriteria):
    hasil_nilai = np.zeros_like(matriks_kriteria)
    for n in range(len(matriks_kriteria)):
        if matriks_kriteria[n] >= batas_kriteria[0]:
            hasil_nilai[n] = 5
        elif matriks_kriteria[n] >= batas_kriteria[1]:
            hasil_nilai[n] = 4
        elif matriks_kriteria[n] >= batas_kriteria[2]:
            hasil_nilai[n] = 3
        elif matriks_kriteria[n] >= batas_kriteria[3]:
            hasil_nilai[n] = 2
        elif matriks_kriteria[n] >= batas_kriteria[4]:
            hasil_nilai[n] = 1
        else:
            hasil_nilai[n] = -1
    return hasil_nilai

# podo bedane nggo sek string
def beriNilaiKriteriaString(matriks_kriteria, batas_kriteria):
    hasil_nilai = np.zeros_like(matriks_kriteria)
    for n in range(len(matriks_kriteria)):
        if matriks_kriteria[n] == batas_kriteria[0]:
            hasil_nilai[n] = 5
        elif matriks_kriteria[n] == batas_kriteria[1]:
            hasil_nilai[n] = 4
        elif matriks_kriteria[n] == batas_kriteria[2]:
            hasil_nilai[n] = 3
        elif matriks_kriteria[n] == batas_kriteria[3]:
            hasil_nilai[n] = 2
        elif matriks_kriteria[n] == batas_kriteria[4]:
            hasil_nilai[n] = 1
        else:
            hasil_nilai[n] = -1
    return hasil_nilai

# manggil fungsi
matriks_nilai_harga = beriNilaiKriteriaInt(matriks_harga, kriteria_harga)
matriks_nilai_rating = beriNilaiKriteriaInt(matriks_rating, kriteria_rating)
matriks_nilai_prosessor = beriNilaiKriteriaString(matriks_prosessor, kriteria_prosesor)
matriks_nilai_ram = beriNilaiKriteriaInt(matriks_ram, kriteria_ram)
matriks_nilai_baterai = beriNilaiKriteriaInt(matriks_baterai, kriteria_baterai)
print(matriks_nilai_baterai)
print(matriks_baterai)

# matriks per kriteria dijadikan satu matriks
matriks_saw = np.vstack((matriks_nilai_harga, matriks_nilai_rating,matriks_nilai_prosessor,matriks_nilai_ram,matriks_nilai_baterai))
matriks_bobot= [0.30, 0.25, 0.20, 0.15, 0.10] # daftar bobot kriteria, iki kudune nduwur
c1 = matriks_saw[0, :] # iki asline buang buang line aowoakwowkao
c2 = matriks_saw[1, :] # wes digabung malah di pisah
c3 = matriks_saw[2, :]
c4 = matriks_saw[3, :]
c5 = matriks_saw[4, :]

# fungsi menghitung normalisasi kriteria
def hitungKriteria(kriteria, jenis_kriteria):
    hasil_kriteria = np.zeros_like(kriteria)
    terendah = np.min(kriteria)
    tertinggi = np.max(kriteria)
    if jenis_kriteria == True:
        for n in range(len(kriteria)):
            hasil_kriteria[n] = terendah/kriteria[n]
    else:
        for n in range(len(kriteria)):
            hasil_kriteria[n] = kriteria[n]/tertinggi
    return hasil_kriteria

# panggil fungsi
normalisasi_c1 = hitungKriteria(c1, True)
normalisasi_c2 = hitungKriteria(c2, False)
normalisasi_c3 = hitungKriteria(c3, False)
normalisasi_c4 = hitungKriteria(c4, False)
normalisasi_c5 = hitungKriteria(c5, False)

# menggabung matriks normalisasi jadi satu 
matriks_normalisasi_kriteria = np.vstack((normalisasi_c1,normalisasi_c2,normalisasi_c3,normalisasi_c4,normalisasi_c5))

# fungsi menghitung bobot kriteria
def hitungBobot():
    hasil_kali_bobot = np.zeros_like(matriks_normalisasi_kriteria)
    for x in range(len(matriks_bobot)):
        for y in range(len(daftar_hp)):
            hasil_kali_bobot[x,y] = matriks_normalisasi_kriteria[x,y] * matriks_bobot[x]
        
    return hasil_kali_bobot

# panggil fungsi 
matriks_hasil_kali_bobot = hitungBobot()

# test
# print(matriks_saw)
# print(matriks_normalisasi_kriteria)
# print(matriks_hasil_kali_bobot)

# fungsi menghitung hasil akhir rekomendasi
def hitungSkor():
    hasil_akhir = np.zeros(len(daftar_hp))
    for n in range(len(daftar_hp)):
        hasil_akhir[n] = np.sum(matriks_hasil_kali_bobot[:, n])
    return hasil_akhir

#panggil fungsi
skor_akhir = hitungSkor()

# perulangan untuk menampilkan hasil, anjay rampung
for n in range(len(daftar_hp)):
    print(daftar_hp[n], " = ", skor_akhir[n])

print(matriks_hasil_kali_bobot)
print(matriks_model)
print(skor_akhir)
print(df['price'])

