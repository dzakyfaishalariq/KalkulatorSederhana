from component.function_tombol import *
from tkinter import *

root = Tk()
root.geometry("600x700")

# position fitur
frame_header = Frame(root, bg="green")
frame_header.place(
    width=550,
    height=150,
    relx=0.04
)

frame_number = Frame(root, bg="red")
frame_number.place(
    width=275,
    height=480,
    relx=0.04,
    rely=0.25
)

frame_oprator = Frame(root, bg="blue")
frame_oprator.place(
    width=274,
    height=480,
    relx=0.5,
    rely=0.25
)

# function


def tombol1():
    inputan.insert(len(inputan.get()), "1")


def tombol2():
    inputan.insert(len(inputan.get()), "2")


def tombol3():
    inputan.insert(len(inputan.get()), "3")


def tombol4():
    inputan.insert(len(inputan.get()), "4")


def tombol5():
    inputan.insert(len(inputan.get()), "5")


def tombol6():
    inputan.insert(len(inputan.get()), "6")


def tombol7():
    inputan.insert(len(inputan.get()), "7")


def tombol8():
    inputan.insert(len(inputan.get()), "8")


def tombol9():
    inputan.insert(len(inputan.get()), "9")


def tombol0():
    inputan.insert(len(inputan.get()), "0")


def tombol_tambah():
    inputan.insert(len(inputan.get()), "+")


def tombol_kurang():
    inputan.insert(len(inputan.get()), "-")


def tombol_bagi():
    inputan.insert(len(inputan.get()), "/")


def tombol_kali():
    inputan.insert(len(inputan.get()), "*")


def tombol_modulus():
    inputan.insert(len(inputan.get()), "%")


def tombol_samadengan():
    hasil = hitung(inputan.get())
    inputan.delete(0, END)
    convert_string = str(hasil)
    inputan.insert(0, convert_string)

def tombol_hapus():
    inputan.delete(0, END)


judul = Label(frame_header, text="Kalkulator", font=("Consol", 20))
judul.pack(pady=10)
inputan = Entry(frame_header, font=("Consol", 30))
inputan.pack(pady=10)

button1 = Button(frame_number, text="1", font=("Consol", 30), command=tombol1)
button1.place(
    width=60,
    height=60,
    relx=0.06,
    rely=0.1
)
button2 = Button(frame_number, text="2", font=("Consol", 30), command=tombol2)
button2.place(
    width=60,
    height=60,
    relx=0.36,
    rely=0.1
)
button3 = Button(frame_number, text="3", font=("Consol", 30), command=tombol3)
button3.place(
    width=60,
    height=60,
    relx=0.66,
    rely=0.1
)
button4 = Button(frame_number, text="4", font=("Consol", 30), command=tombol4)
button4.place(
    width=60,
    height=60,
    relx=0.06,
    rely=0.31
)
button5 = Button(frame_number, text="5", font=("Consol", 30), command=tombol5)
button5.place(
    width=60,
    height=60,
    relx=0.36,
    rely=0.31
)
button6 = Button(frame_number, text="6", font=("Consol", 30), command=tombol6)
button6.place(
    width=60,
    height=60,
    relx=0.66,
    rely=0.31
)
button7 = Button(frame_number, text="7", font=("Consol", 30), command=tombol7)
button7.place(
    width=60,
    height=60,
    relx=0.06,
    rely=0.52
)
button8 = Button(frame_number, text="8", font=("Consol", 30), command=tombol8)
button8.place(
    width=60,
    height=60,
    relx=0.36,
    rely=0.52
)
button9 = Button(frame_number, text="9", font=("Consol", 30), command=tombol9)
button9.place(
    width=60,
    height=60,
    relx=0.66,
    rely=0.52
)
button0 = Button(frame_number, text="0", font=("Consol", 30), command=tombol0)
button0.place(
    width=60,
    height=60,
    relx=0.36,
    rely=0.72
)

button_plus = Button(frame_oprator, text="+",
                     font=("Consol", 30), command=tombol_tambah)
button_plus.place(
    width=60,
    height=60,
    relx=0.06,
    rely=0.1
)
button_minus = Button(frame_oprator, text="-",
                      font=("Consol", 30), command=tombol_kurang)
button_minus.place(
    width=60,
    height=60,
    relx=0.36,
    rely=0.1
)
button_bagi = Button(frame_oprator, text="/",
                     font=("Consol", 30), command=tombol_bagi)
button_bagi.place(
    width=60,
    height=60,
    relx=0.66,
    rely=0.1
)
button_kali = Button(frame_oprator, text="*",
                     font=("Consol", 30), command=tombol_kali)
button_kali.place(
    width=60,
    height=60,
    relx=0.06,
    rely=0.31
)
button_modulus = Button(frame_oprator, text="%", font=(
    "Consol", 30), command=tombol_modulus)
button_modulus.place(
    width=60,
    height=60,
    relx=0.36,
    rely=0.31
)
button_samadengan = Button(frame_oprator, text="=", font=(
    "Consol", 30), command=tombol_samadengan)
button_samadengan.place(
    width=60,
    height=60,
    relx=0.66,
    rely=0.31
)
button_hapus = Button(frame_oprator, text="C", font=(
    "Consol", 30), command=tombol_hapus)
button_hapus.place(
    width=60,
    height=60,
    relx=0.36,
    rely=0.61
)

root.mainloop()
