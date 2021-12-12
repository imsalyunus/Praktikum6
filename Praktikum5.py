data = []

def menu():
    print ("\n")
    print ("----------------------------------------")
    print ("                LIST MENU           ")
    print ("----------------------------------------")
    print ("[1] Tampilkan")
    print ("[2] Tambah")
    print ("[3] Ubah")
    print ("[4] Hapus")
    print ("[5] Keluar ")
    print ("----------------------------------------")
    menu = input(" Pilih Menu : ")
    
    if menu == 1:
        tampilkan()
    elif menu == 2:
        tambah()
    elif menu == 3 :
        ubah()
    elif menu == 4:
        hapus()
    elif menu == 5:
        keluar()
    else:
        print (" Pilihan anda tidak tersedia ")
    print (" ")
    print (" ")

def tampilkan():
    print ("----------------------------------------")
    print (" NO |DATA YANG TERSIMPAN ")
    print ("----------------------------------------")
    if len(data) <= 0:
        print (" Tidak ada data yang di input ")
    else:
        for indeks in range(len(data)):
            print (" [%d] %s") % (indeks, data[indeks])

def tambah():
    data_baru = raw_input(" Masukan data : ")
    data.append(data_baru)
    print (" ")
    print (" DATA BERHASIL DI SIMPAN !")


def ubah():
    tampilkan()
    print (" ") 
    indeks = input("Pilih NO.Data yang ingin di edit : ")
    if(indeks > len(data)):
        print (" Data tidak ditemukan ! ")
    else:
        print (" ")
        data_baru = raw_input(" Masukan data baru : ")
        data[indeks] = data_baru
        print (" ")
        print (" DATA BERHASIL DI UPDATE !")

def hapus():
    tampilkan()
    indeks = input(" Masukan data yang ingin di hapus : ")
    if(indeks > len(data)):
        print (" Data SALAH ! ")
    else:
        data.remove(data[indeks])

if __name__ == "__main__" :

    while(True):
        menu()