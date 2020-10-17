import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x300")

# etiqueta = tkinter.Label(ventana, text = "Hola Mundo!", bg = "blue")

# etiqueta.pack(fill = tkinter.Y, expand = True)
# etiqueta.pack(fill = tkinter.BOTH, expand = True)
# etiqueta.pack(fill = tkinter.X)

# Para hacer un boton con dimensiones específicas
# boton_lanzar = tkinter.Button(ventana, text = "¡Lanza los dados!", padx = 30, pady = 20 )
boton_lanzar = tkinter.Button(ventana, text = "¡Lanza los dados!")
boton_lanzar.pack()

ventana.mainloop()