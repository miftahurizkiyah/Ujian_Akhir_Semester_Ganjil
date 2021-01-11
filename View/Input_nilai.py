print("=======================================")
print("===\t Nama \t : Miftahu Rizkiyah \t===")
print("===\t NIM \t : 312010014 \t\t\t===")
print("===\t Kelas \t : T1.20.B1 \t\t\t===")
print("=======================================")
print()
print("========\t | Ujian Akhir Semester Ganjil |\t ======")
print()


#from model.daftar_nilai import tampunglist
#from prettytable import PrettyTable


# Fungsi : input_data

class PrettyTable(object):
    pass


x = PrettyTable()
# tampunglist = {}


def input_data(tnama='', tnim=''):
    print("aaa")
    print("tampunglist.items()")
    print("tampunglist.values()")
    # print(tampunglist[tnama])
    print("FORM INPUT DATA NILAI")
    ttugas = int(input("Masukkan Nilai Tugas Mahasiswa : "))
    tuts = int(input("Masukkan Nilai UTS Mahasiswa : "))
    tuas = int(input("Masukkan Nilai UAS Mahasiswa : "))
    takhir = 0.3 * float(ttugas) + 0.35 * float(tuts) + 0.35 * float(tuas)
    print(takhir)
    tampunglist[tnama] = tnim, ttugas, tuts, tuas, takhir
    print(tampunglist[tnama])
    no = 0
    x.field_names = ["NO", "NAMA", " NIM", "TUGAS", "UTS", "UAS", "AKHIR"]
    for tdata in tampunglist.items():
        no += 1
        x.add_row([no, tdata[0], tdata[1][0], tdata[1][1], tdata[1][2], tdata[1][3], tdata[1][4]])
    print(x)