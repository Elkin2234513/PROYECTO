from tkinter import *
from tkinter import messagebox

# FUNCIONES DE LA APP
def abrir_toplevel_de_eleccion():
    global toplevel_de_eleccion
    toplevel_de_eleccion = Toplevel()
    toplevel_de_eleccion.title("choose the best decision")
    toplevel_de_eleccion.resizable(False, False)
    toplevel_de_eleccion.geometry("700x700")
    toplevel_de_eleccion.config(bg="DarkOrange2")

    # logo de la app
    lb_logo2 = Label(toplevel_de_eleccion, image=LOGO2, bg="white")
    lb_logo2.place(x=0, y=0)
    titulo = Label(toplevel_de_eleccion, text="WHAT DO YOU PREFER")
    titulo.config(bg="White", fg="Black", font=("constantia", 28))
    titulo.place(x=150, y=400)
    bt_SAVINGS = Button(toplevel_de_eleccion, text="MORE SAVINGS", width=20, height=3, command = abrir_toplevel_more_savings)
    bt_SAVINGS.place(x=100, y=500)
    bt_INVEST = Button(toplevel_de_eleccion, text="LEARN TO INVEST", width=20, height=3, command = abrir_toplevel_learn_invest)
    bt_INVEST.place(x=450, y=500)



def abrir_toplevel_more_savings():
    global toplevel_de_eleccion
    toplevel_de_eleccion = Toplevel()
    toplevel_de_eleccion.title("50/30/20")
    toplevel_de_eleccion.resizable(False, False)
    toplevel_de_eleccion.geometry("700x700")
    toplevel_de_eleccion.config(bg="#D4C39A")

    SALARIO = Label(toplevel_de_eleccion, text="ENTER YOUR SALARY")
    SALARIO.config(bg="White", fg="#A48C64", font=("Bodoni MT", 28))
    SALARIO.place(x=25, y=50)

    ESENCIAL = Label(toplevel_de_eleccion, text="ESSENTIAL EXPENSES")
    ESENCIAL.config(bg="White", fg="#A48C64", font=("Bodoni MT", 28))
    ESENCIAL.place(x=50, y=150)

    EXTRA = Label(toplevel_de_eleccion, text="EXTRA EXPENSES")
    EXTRA.config(bg="White", fg="#A48C64", font=("Bodoni MT", 28))
    EXTRA.place(x=50, y=250)

    AHORROS = Label(toplevel_de_eleccion, text="SAVINGS")
    AHORROS.config(bg="White", fg="#A48C64", font=("Bodoni MT", 28))
    AHORROS.place(x=50, y=350)

    lb_logo3 = Label(toplevel_de_eleccion, image=LOGO3, bg="#D4C39A")
    lb_logo3.place(x=400, y=400)

    TSUELDO = Entry(toplevel_de_eleccion, textvariable= SUELDO)
    TSUELDO.config(bg="#A48C64", fg="white", font=("Century Gothic", 20), width=27)
    TSUELDO.focus_set()
    TSUELDO.place(x=25,y=100)

    t_resultados = Text(toplevel_de_eleccion)
    t_resultados.config(bg="#A48C64", fg="white", font=("Century Gothic", 24))
    t_resultados.place(x=50,y=200,width=380,height=50)

    t_resultados = Text(toplevel_de_eleccion)
    t_resultados.config(bg="#A48C64", fg="white", font=("Century Gothic", 24))
    t_resultados.place(x=50,y=300,width=380,height=50)

    t_resultados = Text(toplevel_de_eleccion)
    t_resultados.config(bg="#A48C64", fg="white", font=("Century Gothic", 24))
    t_resultados.place(x=50,y=400,width=380,height=50)

    bt_EXPLICACION = Button(toplevel_de_eleccion,text="EXPLICATION")
    bt_EXPLICACION.config(bg="#A48C64", fg="white", font=("Century Gothic", 18), width=15)
    bt_EXPLICACION.place(x=100, y=550, height=50)


    bt_CALCULAR = Button(toplevel_de_eleccion,text="CALCULATE")
    bt_CALCULAR.config(bg="#A48C64", fg="white", font=("Century Gothic", 18), width=15)
    bt_CALCULAR.place(x=450, y=50, height=50)



def abrir_toplevel_learn_invest():
    global toplevel_de_eleccion
    toplevel_de_eleccion = Toplevel()
    toplevel_de_eleccion.title("60/10/10/10/20")
    toplevel_de_eleccion.resizable(False, False)
    toplevel_de_eleccion.geometry("700x700")
    toplevel_de_eleccion.config(bg="DarkOrange2")

    lb_logo3 = Label(toplevel_de_eleccion, image=LOGO4, bg="#D4C39A")
    lb_logo3.place(x=200, y=200)

    SALARIO = Label(toplevel_de_eleccion, text="ENTER YOUR SALARY")
    SALARIO.config(bg="White", fg="#A48C64", font=("Bodoni MT", 28))
    SALARIO.place(x=25, y=50)

    ESENCIAL = Label(toplevel_de_eleccion, text="ESSENTIAL EXPENSES")
    ESENCIAL.config(bg="White", fg="#A48C64", font=("Bodoni MT", 28))
    ESENCIAL.place(x=50, y=150)

    EXTRA = Label(toplevel_de_eleccion, text="EXTRA EXPENSES")
    EXTRA.config(bg="White", fg="#A48C64", font=("Bodoni MT", 28))
    EXTRA.place(x=50, y=250)

    AHORROS = Label(toplevel_de_eleccion, text="SAVINGS")
    AHORROS.config(bg="White", fg="#A48C64", font=("Bodoni MT", 28))
    AHORROS.place(x=50, y=350)

    INVERTIR = Label(toplevel_de_eleccion, text="TO INVEST")
    INVERTIR.config(bg="White", fg="#A48C64", font=("Bodoni MT", 28))
    INVERTIR.place(x=50, y=450)
 
    TSUELDO = Entry(toplevel_de_eleccion, textvariable= SUELDO)
    TSUELDO.config(bg="#A48C64", fg="white", font=("Century Gothic", 20), width=27)
    TSUELDO.focus_set()
    TSUELDO.place(x=25,y=100)

    t_resultados = Text(toplevel_de_eleccion)
    t_resultados.config(bg="#A48C64", fg="white", font=("Century Gothic", 24))
    t_resultados.place(x=50,y=200,width=380,height=50)

    t_resultados = Text(toplevel_de_eleccion)
    t_resultados.config(bg="#A48C64", fg="white", font=("Century Gothic", 24))
    t_resultados.place(x=50,y=300,width=380,height=50)

    t_resultados = Text(toplevel_de_eleccion)
    t_resultados.config(bg="#A48C64", fg="white", font=("Century Gothic", 24))
    t_resultados.place(x=50,y=400,width=380,height=50)

    bt_EXPLICACION = Button(toplevel_de_eleccion,text="EXPLICATION")
    bt_EXPLICACION.config(bg="#A48C64", fg="white", font=("Century Gothic", 18), width=15)
    bt_EXPLICACION.place(x=100, y=550, height=50)


    bt_CALCULAR = Button(toplevel_de_eleccion,text="CALCULATE")
    bt_CALCULAR.config(bg="#A48C64", fg="white", font=("Century Gothic", 18), width=15)
    bt_CALCULAR.place(x=450, y=50, height=50)



# aceptar
def aceptar():
    global cent
    cent = int(c.get())
    toplevel_de_eleccion.destroy()


def obtener_texto():
    texto = int(Entry.get())
    print("Texto ingresado:", texto)

# ventana principal de la app

# se declara una variable llamada ventana_principal, que adquiere las características de un objeto Tk()
ventana_principal = Tk()
# tamaño de la ventana
ventana_principal.geometry("700x700")
# deshabilitar botón de maximizar
ventana_principal.resizable(False, False)
# color de fondo de la ventana
ventana_principal.config(bg="DarkOrange2")
# título de la ventana principal
ventana_principal.title("PERSONAL FINANCES")

# Variables globales
c = StringVar()
SUELDO = StringVar()


# frame PORTADA
frame_portada = Frame(ventana_principal)
frame_portada.config(bg="gray6", width=680, height=680)
frame_portada.place(x=10, y=10)

# Logo de la app
LOGO = PhotoImage(file="img/LOGOBRR.png")
lb_LOGO = Label(frame_portada, image=LOGO, bg="gray6")
lb_LOGO.place(x=170, y=60)

LOGO2 = PhotoImage(file="img/CHOOSE.png")
LOGO3 = PhotoImage(file="img/AHORROS.png")
LOGO4 = PhotoImage(file="img/INVERCION.png")

# Título de la app
titulo = Label(frame_portada, text="YOUR PERSONAL FINANCES")
titulo.config(bg="gray6", fg="DarkOrange2", font=("Small Fonts", 20))
titulo.place(x=230, y=480)
titulo = Label(frame_portada, text="UPGRADE")
titulo.config(bg="gray6", fg="DarkOrange2", font=("Small Fonts", 28))
titulo.place(x=20, y=470)

# Botón para abrir Toplevel para ingresar a preguntar el tipo de ahorro que quiere
bt_CODIGOS = Button(frame_portada, text="LETS GO!!", width=20, height=3, foreground="#ff0000",
                    activeforeground="#FFA500", command=abrir_toplevel_de_eleccion)
bt_CODIGOS.place(x=270, y=600)



ventana_principal.mainloop()