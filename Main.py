#from model.daftar_nilai import tambah_data, hapus_data, cari_data
#from view.input_nilai import input_data

print("=======================================")
print("===\t Nama \t : Miftahu Rizkiyah \t===")
print("===\t NIM \t : 312010014 \t\t\t===")
print("===\t Kelas \t : T1.20.B1 \t\t\t===")
print("=======================================")
print()
print("========\t | Ujian Akhir Semester Ganjil |\t ======")
print()


print("===== APLIKASI PENGOLAHAN DATA NILAI MAHASISWA =====")
while True:
    print("MENU : \n 1. Tambah Data \n 2. Ubah Data \n 3. Hapus Data \n 4. Cari Data \n 5. Keluar Aplikasi")
    pilih = int(input("Pilih Menu (1/2/3/4/5) : "))
    if pilih == 1:
        tambah_data()
        input_data()
    elif pilih == 2:
        print("Data siapa yang akan diubah ?")
        siapa = input("Masukkan Nama Mahasiswa yang akan diubah : ")
        #daftar_nilai.ubah_data(xsiapa=siapa)
    elif pilih == 3:
        hapus_data()
    elif pilih == 4:
        cari_data()
    elif pilih == 5:
        break
    else:
        print("!!! === ERROR! Anda Memasukkan Pilihan yang Salah === !!!")