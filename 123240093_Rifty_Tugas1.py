# ----------------------------------------------------------------
# if you're left on read, don't worry you just too deep comprehend
# ----------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------
# Mas sebelumnya, menurut saya ini salah tabelnya harusnya bulan 1, 2, 3 bukan produk 1, 2, 3 jadi bingung uy '_'
# ---------------------------------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import os
login = False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Matriks produksi (jumlah unit yang diproduksi per bulan):
P = np.array([[120,150,170],
              [100,130,160],
              [110,140,180]])

# Matriks biaya produksi per unit (dalam ribu rupiah):
C = np.array([[50,55,60],
              [48,52,58],
              [47,50,57]])

# Matriks harga jual per unit (dalam ribu rupiah):
H = np.array([[80,85,90],
              [78,82,88],
              [75,80,85]])

TotalBiayaProduksi = P * C
TotalPendapatan = P * H
TotalLaba = TotalPendapatan - TotalBiayaProduksi

# Fungsi tampil matriks biar keren
def tampilkanMatriks(X):
    print("+-----------+--------+--------+--------+")
    print("|           |  B1    |  B2    |  B3    |")
    print("+-----------+--------+--------+--------+")

    for i, row in enumerate(X):
        print(f"| Pabrik {i+1}  |"
              f" {row[0]:<6} |"
              f" {row[1]:<6} |"
              f" {row[2]:<6} |")
        print("+-----------+--------+--------+--------+")

# Tugas 
# Nomor 1 Hitung total biaya produksi untuk setiap pabrik perbulan
def totalBiaya():
    
    tampilkanMatriks(TotalBiayaProduksi)
    

# Nomor 2 Hitung total pendapatan dari penjualan setiap pabrik perbulan
def totalPendapatan():
    
    tampilkanMatriks(TotalPendapatan)

# Nomor 3 Hitung laba bersih perbulan untuk setiap pabrik
def totalLaba():
    
    tampilkanMatriks(TotalLaba)

# Nomor 4 Tentukan pabrik dengan laba bersih
def labaBersihTertinggi():
    # Menambahkan kolom agar jadi total laba dalam 3 bulan
    LabaBersih3Bulan = TotalLaba.sum(axis=1)
    # Mengurutkan matriks total laba bersih
    # ini nggak tahu pabrik mana yang tertinggi hanya nilainya saja
    TtlLb3BlnUrt = np.sort(LabaBersih3Bulan) 
    print("Laba Tertinggi adalah ", TtlLb3BlnUrt[2])
    # yang ini tahu index dari laba tertinggi
    IndexlabaBersihTertinggi = np.argmax(LabaBersih3Bulan)
    print("Milik Pabrik ", IndexlabaBersihTertinggi+1)
    

# Visualisasi Tren Produksi
def VslTrenProduksi():
    # Grafik Tren Produksi per Pabrik
    # Pecah Produksi pabrik menjadi 3 matriks per pabrik
    Pabrik1 = P[0,:]
    Pabrik2 = P[1,:]
    Pabrik3 = P[2,:]

    # label pada sumbu x dibawah label x
    bulan = ["Bulan 1", "Bulan 2", "Bulan 3"]

    # ini grafik per pabrik
    plt.figure()
    plt.plot(bulan, Pabrik1, marker='o', color='#d00000', label="Pabrik 1")
    plt.plot(bulan, Pabrik2, marker='o', color='#ffba08', label="Pabrik 2")
    plt.plot(bulan, Pabrik3, marker='o', color='#3f88c5', label="Pabrik 3")

    # ini legenda grafik anjay
    plt.title("Tren Produksi Per Bulan")
    plt.xlabel("Bulan")
    plt.ylabel("Total (Unit)")
    plt.legend()
    plt.show()

# Visualisasi Biaya Produksi
def VslBiayaProduksi():
    # Grafik Biaya Produksi per Pabrik
    # Pecah Biaya Produksi pabrik menjadi 3 matriks per pabrik
    Pabrik1 = TotalBiayaProduksi[0,:]
    Pabrik2 = TotalBiayaProduksi[1,:]
    Pabrik3 = TotalBiayaProduksi[2,:]

    # label pada sumbu x dibawah label x
    bulan = ["Bulan 1", "Bulan 2", "Bulan 3"]

    # ambil array bulan, hitung panjangnya, di ubah jadi array index 
    x = np.arange(len(bulan))  # [0,1,2]
    width = 0.25  # lebar batang

    plt.figure()
    plt.bar(x - width, Pabrik1, width, color='#fe218b', label="Pabrik 1")
    plt.bar(x,         Pabrik2, width, color='#fed700', label="Pabrik 2")
    plt.bar(x + width, Pabrik3, width, color='#21b0fe', label="Pabrik 3")

    plt.xticks(x, bulan)
    plt.xlabel("Bulan")
    plt.ylabel("Biaya Produksi Perbulan (Rupiah)")
    plt.title("Biaya Produksi Perbulan")
    plt.legend()
    plt.ylim(0, 12000)
    plt.yticks(range(0, 12001, 1000))

    plt.show()

# Visualisasi Laba Bersih
def VslLabaBersih():
    # Grafik Laba Bersih per Pabrik
    # Pecah Matriks Laba Bersih tiap pabrik menjadi 3 matriks per pabrik
    Pabrik1 = TotalLaba[0,:]
    Pabrik2 = TotalLaba[1,:]
    Pabrik3 = TotalLaba[2,:]

    # label pada sumbu x dibawah label x
    bulan = ["Bulan 1", "Bulan 2", "Bulan 3"]

    # ini grafik per pabrik
    plt.figure()
    plt.plot(bulan, Pabrik1, marker='o', color='#ffbf00', label="Pabrik 1")
    plt.plot(bulan, Pabrik2, marker='o', color='#e83f6f', label="Pabrik 2")
    plt.plot(bulan, Pabrik3, marker='o', color='#2274a5', label="Pabrik 3")

    # ini legenda grafik anjay
    plt.title("Laba Bersih Per Bulan")
    plt.xlabel("Bulan")
    plt.ylabel("Laba Bersih (Rupiah)")
    plt.legend()
    plt.yticks(range(2800, 5201, 100))
    plt.show()

if __name__ == "__main__":
    while True:
        if not login:
            print(" ██████╗ ██╗███████╗████████╗██╗   ██╗")
            print(" ██╔══██╗██║██╔════╝╚══██╔══╝╚██╗ ██╔╝")
            print(" ██████╔╝██║█████╗     ██║    ╚████╔╝ ")
            print(" ██╔══██╗██║██╔══╝     ██║     ╚██╔╝  ")
            print(" ██║  ██║██║██║        ██║      ██║   ")
            print(" ╚═╝  ╚═╝╚═╝╚═╝        ╚═╝      ╚═╝   ")
            input("\n Tekan Enter Untuk Lanjut....")
            login = True
        clear_screen()
        print("+------------------- MENU -------------------+")
        print("|1. Total Biaya Produksi                     |")
        print("|2. Total Pendapatan                         |")
        print("|3. Laba Bersih                              |")
        print("|4. Pabrik dengan Laba Tertinggi             |")
        print("|5. Visualisasi Tren Produksi                |")
        print("|6. Visualisasi Biaya Produksi               |")
        print("|7. Visualisasi Laba Bersih                  |")
        print("|8. Keluar                                   |")
        print("+--------------------------------------------+")

        pilihan = input("Pilih menu (1-6): ")

        match pilihan:
            case "1":
                print("Menampilkan Total Biaya Produksi\n")
                totalBiaya()
            case "2":
                print("Menampilkan Total Pendapatan\n")
                totalPendapatan()
            case "3":
                print("Menampilkan Laba Bersih\n")
                totalLaba()
            case "4":
                print("Menampilkan Pabrik dengan Laba Tertinggi\n")
                labaBersihTertinggi()
            case "5":
                print("Menampilkan Visualisasi Tren Produksi Per Bulan\n")
                VslTrenProduksi()
            case "6":
                print("Menampilkan Visualisasi Biaya Produksi Per Bulan\n")
                VslBiayaProduksi()
            case "7":
                print("Menampilkan Visualisasi Laba Bersih Per Bulan\n")
                VslLabaBersih()
            case "8":
                print("Keluar dari program. Sampai jumpa!")
                login = False
                break
            case _:
                print("Pilihan tidak valid, silakan coba lagi.\n")
        input("\nTekan Enter untuk melanjutkan...")
