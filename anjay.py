# nama = "anjay"
# number = 15

# print("hello world")
# print(nama)

# if number >= 10:
#     print(f"nama saya {nama} dan saya berumur {number} tahun")

# def anjayFungsi(umur):
#     if umur > 17:
#         return "Anjay"
#     else:
#         return "Elek"
        
# umur = float(input("Masukkan Umurmu : "))

# print(anjayFungsi(umur))



# mtk = float(input("Masukkan Nilai Matematika : "))
# ing = float(input("Masukkan Nilai Bahasa Inggris : "))
# ipa = float(input("Masukkan Nilai Ilmu Pengetahuan Alam : "))

# rr = (mtk + ing + ipa) / 3

# def anjayLulus(rr):
#     if rr > 89 and rr < 101:
#         return "Sangat Baik"
#     elif rr > 79 and rr < 90:
#         return "Baik"
#     elif rr > 69 and rr < 80:
#         return "Cukup"
#     elif rr > 59 and rr < 70:
#         return "Perlu Perbaikan"
#     else:
#         return "Goblok"
    
# print(anjayLulus(rr))

# def main():
#     while True:
#         print("Menu:")
#         print("1. Pilihan 1")
#         print("2. Pilihan 2")
#         print("3. Pilihan 3")
#         print("4. Keluar")

#         try:
#             pilihan = int(input("Masukkan pilihan Anda (1/2/3/4): "))
            
#             if pilihan == 1:
#                 print("Anda memilih Pilihan 1.")
#             elif pilihan == 2:
#                 print("Anda memilih Pilihan 2.")
#             elif pilihan == 3:
#                 print("Anda memilih Pilihan 3.")
#             elif pilihan == 4:
#                 print("Keluar dari program. Terima kasih!")
#                 break
#             else:
#                 print("Pilihan tidak valid. Silakan masukkan pilihan yang benar (1/2/3/4).")
#         except ValueError:
#             print("Input tidak valid. Masukkan angka saja.")

# if __name__ == "__main__":
#     main()



def ATManjay():
    keluar = False
    saldo = 1000000
    while keluar == False:
        print("1. Cek Saldo")
        print("2. Setor Tunai")
        print("3. Tarik Tunai")
        print("4. Keluar")
        
        pilihan = int(input("Masukkan Pilihan: "))
        if pilihan == 1:
            print(saldo)

        elif pilihan == 2:
            setor = int(input("Masukkan nominal setor"))
            saldo = setor + saldo
            
        elif pilihan == 3:
            tarik = int(input("Masukkan nominal tarik"))
            saldo = saldo - tarik
            
        elif pilihan == 4:
            print("terimakasih.")
            keluar == True
            break
            
        else:
            print("salah blok isi ulang")
            
            

ATManjay()