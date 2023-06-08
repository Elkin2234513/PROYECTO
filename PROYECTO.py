"""from tkinter import *

# Crear ventana
ventana = Tk()

# Configurar fuente en un Label
label = Label(ventana, text="QUE MIRA SAPO", font=("Century Gothic", 18))
label.pack()

# Mostrar ventana
ventana.mainloop()"""""

"""from tkinter import *

# Crear ventana
ventana = Tk()

# Configurar color de fondo de la ventana
ventana.configure(bg="#A48C64")

# Mostrar ventana
ventana.mainloop()"""""



from tkinter import *

# Crear ventana
ventana = Tk()

# Función para manejar el evento de botón
def obtener_texto():
    texto = entry.get()
    print("Texto ingresado:", texto)

# Crear caja de texto
entry = Entry(ventana)
entry.pack()

# Crear botón
boton = Button(ventana, text="Obtener texto", command=obtener_texto)
boton.pack()

# Mostrar ventana
ventana.mainloop()