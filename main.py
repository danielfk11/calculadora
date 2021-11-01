from tkinter import *
from typing import Match

root = Tk()
root.title("Calculadora")
root.config(background='grey')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#e.insert(0, "")

# DEFINIR AS FUNCOES

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)


def button_igual():
    second_number = e.get()
    e.delete(0, END)

    if math == "adicionar":
        e.insert(0, f_num + int(second_number))
    
    if math == "subtrair":
        e.insert(0, f_num - int(second_number))

    if math == "dividir":
        e.insert(0, f_num / int(second_number))    

    if math == "multiplicar":
        e.insert(0, f_num * int(second_number))


def button_sub():
    first_number = e.get()
    global f_num 
    global math
    math = "subtrair"
    f_num = int(first_number)
    e.delete(0, END)

def button_multip():
    first_number = e.get()
    global f_num 
    global math
    math = "multiplicar"
    f_num = int(first_number)
    e.delete(0, END)

def button_divd():
    first_number = e.get()
    global f_num 
    global math
    math = "dividir"
    f_num = int(first_number)
    e.delete(0, END)

def button_adicionar():
    first_number = e.get()
    global f_num 
    global math
    math = "adicionar"
    f_num = int(first_number)
    e.delete(0, END)

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))

button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))

button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))

button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_soma = Button(root, text="+", padx=40, pady=20, command=button_adicionar)
button_menos = Button(root, text="-", padx=40, pady=20, command=button_sub)
button_multi = Button(root, text="x", padx=40, pady=20, command=button_multip)
button_div = Button(root, text="÷", padx=40, pady=20, command=button_divd)

button_igual = Button(root, text="=", padx=80, pady=20, command=button_igual)
button_limpar = Button(root, text="Limpar", padx=80, pady=20, command=button_clear)


button_1.grid(row= 3, column=0)
button_2.grid(row= 3, column=1)
button_3.grid(row= 3, column=2)

button_4.grid(row=2 , column=0)
button_5.grid(row=2 , column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1 , column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4 , column=0)

button_soma.grid(row=1, column=3)
button_div.grid(row=2, column=3)
button_multi.grid(row= 3, column=3)
button_menos.grid(row=4, column=3)

button_limpar.grid(row=5, column=0, columnspan=2) 
button_igual.grid(row=5, column=2, columnspan=4)

root.mainloop()