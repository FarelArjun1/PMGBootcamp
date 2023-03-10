#Mengimpor modul tkinter yang digunakan untuk membuat GUI pada program kalkulator.
from tkinter import*
#Mengimpor modul font dari tkinter untuk mengatur ukuran font pada label dan tombol di kalkulator.
import tkinter.font as font
import math

#Membuat objek root sebagai tampilan utama dari kalkulator.
root = Tk()
#Memberikan judul pada tampilan kalkulator.
root.title("KALKULATOR")
root["bg"] = "#C0DEFF"
#Mengatur ukuran tampilan kalkulator.
root.geometry("310x400")


#Membuat objek myfont sebagai objek font dengan ukuran 15.
myfont  = font.Font(size=15)

#Membuat objek e sebagai widget Entry yang digunakan untuk menampilkan angka dan hasil operasi matematika.
e = Entry(root,width=25,borderwidth=0)
e["font"]= myfont
e["bg"] = "#C0DEFF"
e.grid(row = 0,columnspan=4,pady=20,padx=20)


#Membuat fungsi cetak yang akan menampilkan angka pada widget Entry saat tombol angka ditekan.
def cetak(nilai):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current)+str(nilai))
#Membuat fungsi tambah yang akan menambahkan dua angka.
def tambah():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "penjumlahan"
    n_awal = int(nomor_awal)
    e.delete(0,END)
#Membuat fungsi kurang yang akan mengurangkan dua angka.
def kurang():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "pengurangan"
    n_awal = int(nomor_awal)
    e.delete(0,END)
#Membuat fungsi bagi yang akan membagi dua angka.
def bagi():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "pembagian"
    n_awal = int(nomor_awal)
    e.delete(0,END)
#Membuat fungsi kali yang akan mengalikan dua angka.
def kali():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "perkalian"
    n_awal = int(nomor_awal)
    e.delete(0,END)

#Membuat fungsi sisabagi yang akan menghitung sisa hasil bagi dari dua angka.
def sisabagi():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "sisabagi"
    n_awal = int(nomor_awal)
    e.delete(0,END)

#Membuat fungsi pangkat yang akan menghitung hasil pangkat dua dari suatu angka.
def pangkat():
    nomor_awal = e.get()
    global n_awal
    n_awal = int(nomor_awal)
    e.delete(0,END)
    e.insert(0,n_awal **2)

#Membuat fungsi akar yang akan menghitung akar kuadrat dari suatu angka.
def akar():
    nomor_awal = e.get()
    global n_awal
    n_awal = int(nomor_awal)
    e.delete(0,END)
    e.insert(0,math.sqrt(n_awal))


#Membuat fungsi hapus yang akan menghapus angka yang ada di widget Entry.
def hapus():
    e.delete(0,END)
#Membuat fungsi samadengan yang akan menghitung hasil operasi matematika dan menampilkannya di widget Entry.
def samadengan():
    nomor_akhir = e.get()
    e.delete(0,END)
#if perulangan mtk = penjumlahan maka akan menjalankan fungsi penjumlahan dst,n_awl=inputan awal sebelum oprasi,angka akhir= angka sesudah oprasi
#oprasi itu tmbh,bgi,kurang dll
#elif=selain if
#try_except=error handling

    if mtk == "penjumlahan":
        e.insert(0,n_awal + int(nomor_akhir))
    elif mtk == "pengurangan":
        e.insert(0,n_awal - int(nomor_akhir))
    elif mtk == "pembagian":
        try:
            hitung = n_awal / int(nomor_akhir)
            e.insert(0,hitung)
        except ZeroDivisionError:
            e.insert(0,"maaf komputer anda kurang mampu")
            
    elif mtk == "perkalian":
        e.insert(0,n_awal * int(nomor_akhir))
    elif mtk == "sisabagi":
        e.insert(0,n_awal % int(nomor_akhir))
    

#Membuat tombol angka 1 pada kalkulator.
btn  = Button(root,text="1",padx = 30,bg="#F7EFE5",fg="#20262E", pady = 19,command=lambda:cetak(1))
btn2  = Button(root,text="2",padx = 30,bg="#F7EFE5",fg="#20262E", pady = 19,command=lambda:cetak(2))
btn3  = Button(root,text="3",padx = 30,bg="#F7EFE5",fg="#20262E", pady = 19,command=lambda:cetak(3))
btn4  = Button(root,text="4",padx = 30,bg="#F7EFE5",fg="#20262E", pady = 19,command=lambda:cetak(4))
btn5 = Button(root,text="5",padx = 30,bg="#F7EFE5",fg="#20262E", pady = 19,command=lambda:cetak(5))
btn6  = Button(root,text="6",padx = 30,bg="#F7EFE5",fg="#20262E", pady = 19,command=lambda:cetak(6))
btn7  = Button(root,text="7",padx = 30,bg="#F7EFE5",fg="#20262E", pady = 19,command=lambda:cetak(7))
btn8  = Button(root,text="8",padx = 30,bg="#F7EFE5",fg="#20262E", pady = 19,command=lambda:cetak(8))
btn9  = Button(root,text="9",padx = 30,bg="#F7EFE5",fg="#20262E", pady = 19,command=lambda:cetak(9))
btn0  = Button(root,text="0",padx = 30,bg="#F7EFE5",fg="#20262E", pady = 19,command=lambda:cetak(0))
#Membuat tombol operasi tambah pada kalkulator.
tam = Button(root,text="+",padx = 30,bg="#FFE7CC",fg="#20262E", pady = 19,command=tambah)
kur = Button(root,text="-",padx = 30,bg="#FFE7CC",fg="#20262E", pady = 19,command=kurang)
bag  = Button(root,text="/",padx = 30,bg="#FFE7CC",fg="#20262E", pady = 19,command=bagi)
kal = Button(root,text="x",padx = 30,bg="#FFE7CC",fg="#20262E", pady = 19,command=kali)
pang = Button(root,text="x2",padx = 30,bg="#FFE7CC",fg="#20262E", pady = 19,command=pangkat)
ak2 = Button(root,text="sq2",padx = 25,bg="#FFE7CC",fg="#20262E", pady = 19,command=akar)
sisbag = Button(root,text="%",padx = 30,bg="#FFE7CC",fg="#20262E", pady = 19,command=sisabagi)
hap = Button(root,text="C",padx = 30,bg="#FFE7CC",fg="#20262E", pady = 19,command=hapus)
equal = Button(root,text="=",padx = 66,bg="#7B8FA1", pady = 19,command=samadengan)


btn.grid(row=3,column=0,pady=2)
btn2.grid(row=3,column=1,pady=2)
btn3.grid(row=3,column=2,pady=2)
btn4.grid(row=2,column=0,pady=2)
btn5.grid(row=2,column=1,pady=2)
btn6.grid(row=2,column=2,pady=2)
btn7.grid(row=1,column=0,pady=2)
btn8.grid(row=1,column=1,pady=2)
btn9.grid(row=1,column=2,pady=2)
btn0.grid(row=4,column=1,pady=2)

tam.grid(row=1,column=3,pady=2)
kur.grid(row=2,column=3,pady=2)
bag.grid(row=3,column=3,pady=2)
kal.grid(row=4,column=3,pady=2)
hap.grid(row=4,column=0,pady=2)
equal.grid(row=5,column=2,columnspan=2)
pang.grid(row =5,column=0,pady=2)
ak2.grid(row =5,column=1,pady=2)
sisbag.grid(row =4,column=2,pady=2)



root.mainloop()