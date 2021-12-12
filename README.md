# Praktikum6
Tugas Pertemuan ke 11
data = []
#Disebut juga variable global dimana untuk menyimpan data dari data

def tampilkan():
#Merupakan fungsi untuk menampilkan semua data
print ("----------------------------------------")
#Perintah untuk mencetak  string
print (" NO |DATA YANG TERSIMPAN ")
#Perintah untuk mencetak string
print ("----------------------------------------")
#Perintah untuk mencetak string
if len(data) <= 0:
#Percabangan if-else di mana untuk kondisi pertama jika jumlah data kurang dari sama dengan 0
        print (" Tidak ada data yang di input ")
        #Merupakan statement  pertama  dan perintah untuk mencetak string
else:
#Kondisi dimana jika kondisi pertama tidak terpenuhi
        for indeks in range(len(data)):
        #Merupakan perulangan For dimana variable indeks dengan range jumlah data
            print (" [%d] %s") % (indeks, data[indeks])
            #Merupakan statement dan perintah untuk mencetak string

def tambah():
#Merupakan fungsi untuk menambahkan data
data_baru = raw_input(" Masukan data : ")
#Dengan variable data baru,untuk nilainya merupakan nilai inputan
data.append(data_baru)
#Inputan dari user kemudian diisi ke dalam list data dengan fungsi append() untuk menambahkan  
   item di akhir list
print (" ")
#Perintah untuk mencetak blank
print (" DATA BERHASIL DI SIMPAN !")
#Perintah untuk mencetak string

def ubah():
#Merupakan fungsi untuk  mengupdate/mengedit data
tampilkan()
#Untuk memangil kembali fungsi  Tampilkan
print (" ")
#Perintah untuk mencetak blank
indeks = input("Pilih NO.Data yang ingin di edit : ")
#Untuk Variable indeks dengan nilai yang merupakan inputan dari user
if(indeks > len(data)):
#Percabangan if-else di mana untuk kondisi pertama jika variable indeks lebih besar dari pada  
   jumlah data
        print( " Data tidak ditemukan ! ")
    #Perintah untuk mencetak string
else:
#Kondisi dimana jika kondisi pertama tidak terpenuhi
        print (" ")
    #Perintah untuk mencetak blank
        data_baru = raw_input(" Masukan data baru : ")
    #Untuk variable data_baru dengan nilai dari inputan user
        data[indeks] = data_baru
    #Maka data[indeks] sama dengan data_baru
        print (" ")
    #Perintah untuk mencetak blank
        print (" DATA BERHASIL DI UPDATE !")
    #Perintah untuk mencetak string

def hapus():
#Merupakan fungsi untuk  Mendelete/menghapus data
tampilkan()
#Untuk memangil kembali fungsi  Show
indeks = input(" Masukan data yang ingin di hapus : ")
#Untuk Variable indeks dengan nilai yang merupakan inputan dari user
if(indeks > len(data)):
#Percabangan if-else di mana untuk kondisi pertama jika variable indeks lebih besar dari pada  
   jumlah data
        print (" Data SALAH ! ")
    #Perintah untuk mencetak string
else:
#Kondisi dimana jika kondisi pertama tidak terpenuhi
        data.remove(data[indeks])
        #Inputan dari user kemudian diisi ke dalam list data dengan fungsi remove() untuk
          Menghapus item list

def menu():
#Merupakan fungsi  menu atau sebagai main menunya
print ("\n")
#Perintah untuk mencetak string dan \n untuk membuat line baru
print ("----------------------------------------")
#Perintah untuk mencetak string
print ("                LIST MENU           ")
#Perintah untuk mencetak string
print ("----------------------------------------")
#Perintah untuk mencetak string
print ("[1] Tampilkan")
#Perintah untuk mencetak string
print "[2] Tambah"
#Perintah untuk mencetak string
print "[3] Ubah"
#Perintah untuk mencetak string
print "[4] Hapus"
#Perintah untuk mencetak string
print "[5] Keluar "
#Perintah untuk mencetak string
print "----------------------------------------"

#Perintah untuk mencetak string
menu = input(" Pilih Menu : ")
#Untuk Variabel menu dengan nilai inputan dari user
   
if menu == 1:
#Percabangan if-elif-else di mana untuk kondisi pertama jika variable menu sama dengan 1
        tampilkan()
        #Memanggil kembali fungsi tampilkan
elif menu == 2:
#Untuk kondisi kedua jika variable menu sama dengan 2
       tambah()
        #Memanggil kembali fungsi tambah
elif menu == 3 :
#Untuk kondisi ketiga jika variable menu sama dengan 3
        ubah()
        #Memanggil kembali fungsi ubah
elif menu == 4:
#Untuk kondisi keempat jika variable menu sama dengan 4
        hapus()
        #Memanggil kembali fungsi hapus
elif menu == 5:
#Untuk kondisi kelima jika variable menu sama dengan 5
        exit()
        #Memanggil kembali fungsi exit, dimana fungsi exit telah tersedia langsu dari python-nya
else:
#Dimana jika untuk semua kondisi tidak ada yang terpenuhi
        print (" Pilihan anda tidak tersedia ")
       #Perintah untuk mencetak string
print (" ")
#Perintah untuk mencetak blank
print (" ")
#Perintah untuk mencetak blank

if __name__ == "__main__" :
#Blok main yang terdapat pada python
while(True):
#Perintah perulangan While dimana jika true
        menu()
        #Memanggil kembali Fungsi Menu
