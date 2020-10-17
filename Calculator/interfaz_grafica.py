# from tkinter import *
from tkinter import Tk, Frame, Entry, Button, StringVar

raiz = Tk() # Creo la ventana

calculadora_frame = Frame(raiz) # Creo el frame donde descansará mi calculadora
calculadora_frame.pack() # La empaquetamos en la raiz

operacion = ""

resultado = 0

# ----------------------- PANTALLA: DISPLAY ---------------------------------

numero_pantalla = StringVar()

display = Entry(calculadora_frame, textvariable = numero_pantalla)
display.grid(row=1, column=1, padx=10, pady=10, columnspan=4) # El COLUMNSPAN sirve para decir CUANTAS COLUMNAS va a ocupar la PANTALLA: 4 columnas
display.config(background="black", fg="#98FB98", justify="right")

# ---------------------- pulsaciones teclado ------------------------

def numero_pulsado(num):

    global operacion 
    
    if operacion != "":

        numero_pantalla.set(num)

        operacion = ""

    else:
        numero_pantalla.set(numero_pantalla.get() + num) # Lo que YA HAYA EN PANTALLA CONCATENADO con "4"

""" funcion Suma """
def suma(num):

    global operacion
    global resultado

    resultado +=  int(num)
    operacion = "suma"

    numero_pantalla.set(resultado)

"""funcion el_resultado"""
def el_resultado():

    global resultado

    numero_pantalla.set(resultado+int(numero_pantalla.get()))

    resultado = 0

# ------ -------------------- FILA 1 ----------------------------------

boton7 = Button(calculadora_frame, text="7", width=3, command = lambda:numero_pulsado("7"))
boton7.grid(row=2, column=1)
boton8 = Button(calculadora_frame, text="8", width=3, command = lambda:numero_pulsado("8"))
boton8.grid(row=2, column=2)
boton9 = Button(calculadora_frame, text="9", width=3, command = lambda:numero_pulsado("9"))
boton9.grid(row=2, column=3)
boton_dividir = Button(calculadora_frame, text="/", width=3)
boton_dividir.grid(row=2, column=4)

# -------------------------- FILA 2 ----------------------------------

boton4 = Button(calculadora_frame, text="4", width=3, command = lambda:numero_pulsado("4") )
boton4.grid(row=3, column=1)
boton5 = Button(calculadora_frame, text="5", width=3, command = lambda:numero_pulsado("5"))
boton5.grid(row=3, column=2)
boton6 = Button(calculadora_frame, text="6", width=3, command = lambda:numero_pulsado("6"))
boton6.grid(row=3, column=3)
boton_multiplicar = Button(calculadora_frame, text="x", width=3)
boton_multiplicar.grid(row=3, column=4)

# -------------------------- FILA 3 ----------------------------------

boton1 = Button(calculadora_frame, text="1", width=3, command = lambda:numero_pulsado("1"))
boton1.grid(row=4, column=1)
boton2 = Button(calculadora_frame, text="2", width=3, command = lambda:numero_pulsado("2"))
boton2.grid(row=4, column=2)
boton3 = Button(calculadora_frame, text="3", width=3, command = lambda:numero_pulsado("3"))
boton3.grid(row=4, column=3)
boton_resta = Button(calculadora_frame, text="-", width=3)
boton_resta.grid(row=4, column=4)

# -------------------------- FILA 4 ----------------------------------

boton_punto = Button(calculadora_frame, text=".", width=3, command = lambda:numero_pulsado("."))
boton_punto.grid(row=5, column=1)
boton0 = Button(calculadora_frame, text="0", width=3, command = lambda:numero_pulsado("0"))
boton0.grid(row=5, column=2)
boton_igual = Button(calculadora_frame, text="=", width=3, command=lambda:el_resultado())
boton_igual.grid(row=5, column=3)
boton_suma = Button(calculadora_frame, text="+", width=3, command=lambda:suma(numero_pantalla.get()))
boton_suma.grid(row=5, column=4)



raiz.mainloop()