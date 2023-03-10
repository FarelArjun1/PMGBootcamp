from tkinter import *

# Membuat fungsi untuk menambahkan karakter ke layar kalkulator
# Fungsi add_to_display() menambahkan karakter ke string yang digunakan untuk menampilkan ekspresi yang dimasukkan oleh pengguna.
def add_to_display(char):
    global display_str
    display_str += char
    display_var.set(display_str)

# Membuat fungsi untuk menghapus karakter terakhir dari layar kalkulator
# Fungsi delete_char() menghapus karakter terakhir dari string tampilan.
def delete_char():
    global display_str
    if len(display_str) > 0:
        display_str = display_str[:-1]
        display_var.set(display_str)

# Membuat fungsi untuk menghitung hasil dari operasi matematika
# Fungsi calculate() menghitung hasil dari ekspresi yang dimasukkan dan menampilkan hasilnya pada kalkulator.
# fungsi eval() digunakan untuk menghitung hasil dari operasi matematika yang dimasukkan oleh pengguna pada layar kalkulator.+
def calculate():
    global display_str
    try:
        result = eval(display_str)
        display_str = str(result)
        display_var.set(display_str)
    except:
        display_var.set("Error")
    finally:
        display_str = ""

# Membuat fungsi untuk membuat tombol kalkulator
# berfungsi untuk menempatkan button pada kalkulator
def create_button(text, row, col, col_span=1, command=None):
    button = Button(calc_window, text=text, font=("Arial", 12), width=5, height=2,bg='black', fg='#30E3DF', command=command)
    button.grid(row=row, column=col, columnspan=col_span, padx=5, pady=5)
    return button

# Membuat fungsi untuk membuat tombol kalkulator
def create_button2(text, row, col, col_span=1, command=None):
    button = Button(calc_window, text=text, font=("Arial", 12), width=22, height=2, bg='black', fg='#30E3DF', command=command)
    button.grid(row=row, column=col, columnspan=col_span, padx=5, pady=5)
    return button

# Membuat GUI untuk kalkulator
# mengatur ukuran kalkulator
calc_window = Tk()
calc_window.title("Kalkulator Sederhana")

display_str = ""
display_var = StringVar()
display_var.set("0")

#membuat label ato untuk menampilkan angka
display_label = Label(calc_window, textvariable=display_var, font=("Arial", 20),bg='#F9F5EB', fg='black', width=18, height=2, anchor="e")
#untuk mengatur letak pada tampilan angka
display_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


create_button("7", 1, 0, command=lambda: add_to_display("7"))
create_button("8", 1, 1, command=lambda: add_to_display("8"))
create_button("9", 1, 2, command=lambda: add_to_display("9"))
create_button("/", 5, 3, command=lambda: add_to_display("/"))

create_button("4", 2, 0, command=lambda: add_to_display("4"))
create_button("5", 2, 1, command=lambda: add_to_display("5"))
create_button("6", 2, 2, command=lambda: add_to_display("6"))
create_button("*", 2, 3, command=lambda: add_to_display("*"))

create_button("1", 3, 0, command=lambda: add_to_display("1"))
create_button("2", 3, 1, command=lambda: add_to_display("2"))
create_button("3", 3, 2, command=lambda: add_to_display("3"))
create_button("-", 3, 3, command=lambda: add_to_display("-"))

create_button("0", 4, 0, command=lambda: add_to_display("0"))
create_button(".", 4, 1, command=lambda: add_to_display("."))
create_button("C", 4, 2, command=lambda: display_var.set("0"))
create_button("+", 4, 3, command=lambda: add_to_display("+"))

create_button2("=", 5, 0, col_span=3, command=calculate)
create_button("Del", 1, 3, command=delete_char)

calc_window.config(bg="black")
calc_window.mainloop()