from tkinter import Tk, Frame, Label, PhotoImage, Entry, Text, Scrollbar, Button, StringVar
# from tkinter import *

raiz = Tk()
raiz.title("Simulador de dados")
# raiz.resizable(0,0) # Ancho/width, Alto/Height
# si los parametros son 0,0 estamos prohibiendo la redimension en ANCHO y ALTO
# son valores BOOLEANOS btw, es decir pueden ser 0's, 1's y True's y False's
""" raiz.resizable(True, False) """
#raiz.iconbitmap("dado.ico") POSIBLEMENTE ESTO NO FUNCIONE EN UBUNTU/LINUX
# raiz.geometry("650x350") # FIJAMOS LAS MEDIDAS DE LA VENTANA POR DEFAULT    
# raiz.config(bg = "purple")

# first_frame = Frame()
# first_frame.pack()
# first_frame.config(bg = "blue", width = "1024", height = "768")
#first_frame.config(bd = 35, elief = "groove")

# first_label = Label(first_frame, text = "SIMULADOR DE DADOS")
# first_label.place(x = 200, y = 200)
#Label(first_frame, text = "Simulador de Dados", fg = "black", font = ("Product Sans", 18) ).place(x = 200, y = 200)

# imagen = PhotoImage( file = "dado.png") # Método para insertar imágenes dentro de la interfaz
# Label(first_frame, image = imagen).place(x = 250, y =100)


""" Si queremos que el cuadro de texto esté sobvre un frame
y NO sobre la raíz directamente como aquí:
cuadro_de_texto = Entry(raiz)
cuadro_de_texto.pack()
"""
"""crearemos un frame"""
mi_frame = Frame(raiz, width=1200, height=600)
mi_frame.pack()

mi_nombre = StringVar()

#cuadro_de_texto = Entry(mi_frame)
# cuadro_de_texto.place(x=100, y=100) # ESTA NO ES UNA FORMA RECOMENDABLE PARA POSICIONAR
# cuadro_de_texto.grid(row = 0, column = 1) # ESTA SÍ

#nombre_label = Label(mi_frame, text = "Nombre:")
# nombre_label.place(x = 100, y = 100) # ESTA NO ES UNA FORMA RECOMENDABLE PARA POSICIONAR
#nombre_label.grid(row = 0, column = 0) # ESTA SÍ


nombre_label = Label(mi_frame, text = "Nombre:")
nombre_label.grid(row = 0, column = 0, sticky = "w", padx = 10, pady= 10)

apellido_label = Label(mi_frame, text = "Apellido:")
apellido_label.grid(row = 1, column = 0, sticky = "w", padx = 10, pady= 10)

email_label = Label(mi_frame, text = "Email:")
email_label.grid(row = 2, column = 0, sticky = "w", padx = 10, pady= 10)

direccion_label = Label(mi_frame, text = "Direccion:")
direccion_label.grid(row = 3, column = 0, sticky = "w", padx = 10, pady= 10)

bio_label = Label(mi_frame, text = "Biografía:")
bio_label.grid(row = 4, column = 0, sticky = "w", padx = 10, pady= 10)


cuadro_nombre = Entry(mi_frame, textvariable = mi_nombre)
cuadro_nombre.grid(row = 0, column = 1, padx = 10, pady= 10)
# cuadro_nombre.config(fg = "red", justify = "right") #Con este MÉTODO podemos especificar el formato

cuadro_apellido = Entry(mi_frame)
cuadro_apellido.grid(row = 1, column = 1, padx = 10, pady= 10)

cuadro_email = Entry(mi_frame)
cuadro_email.grid(row = 2, column = 1, padx = 10, pady= 10)

cuadro_password = Entry(mi_frame)
cuadro_password.grid(row = 3, column = 1, padx = 10, pady= 10)
cuadro_password.config(show = "*") # Editamos el formato para que se muestren solo asteriscos

texto_bio = Text(mi_frame, width = 20, height = 5)
texto_bio.grid(row = 4, column = 1,padx = 10, pady= 10)

scroll_vertical = Scrollbar(mi_frame, command = texto_bio.yview) # texto_bio es a quien pertenece, yvie es para que sea vertical
scroll_vertical.grid(row = 4, column = 2, sticky = "nsew")

texto_bio.config(yscrollcommand = scroll_vertical.set) # Este permite agregar una barra vertical que se adapta al tamaño del texto dentro del cuadri TEXT


def codigo_boton():

    mi_nombre.set("Archie")

# boton_submit = Button(raiz, text = "Enviar")
# boton_submit.pack()
boton_submit = Button(mi_frame, text = "Enviar", command = codigo_boton)
boton_submit.grid(row = 5, column = 1, padx = 10, pady = 10)

raiz.mainloop()