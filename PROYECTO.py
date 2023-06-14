from tkinter import *
from tkinter import messagebox

# FUNCIONES DE LA APP
# def REGLA503020():
#     if int(SUELDO.get()) > 1300606:
#         Gastos_basicos = int(SUELDO.get())*0.5
#         GASTOS_EXTRA = int(SUELDO.get())*0.3
#         AHORRO = int(SUELDO.get())*0.2
#         t_resultados.insert(INSERT, f"\n {int(SUELDO.get())*0.5} = {Gastos_basicos} $")
#         t_extra.insert(INSERT, f"\n {int(SUELDO.get())*0.3} = {GASTOS_EXTRA} $")
#         t_ahorros.insert(INSERT, f"\n {int(SUELDO.get())*0.2} = {AHORRO} $")
#     else:
#         toplevel_de_eleccion.insert(INSERT, "¡¡NO ES SUFICIENTE!!")

# def REGLA60101020(Sueldo):
#    global RTA_ESENCIAL, RTA_EXTRA, RTA_AHORRO, RTA_INVENTIR
#   if SUELDO > 1300606:
#     AHORROS = SUELDO*0.1
#      INVERTIR = SUELDO*0.1
#      GASTOS_EXTRA = SUELDO*0.2
#      RTA_ESENCIAL.insert(INSERT, f"\n {Gasto_basicos}$")
#      RTA_EXTRA.insert(INSERT, f"\n {GASTOS_EXTRA}$")
#      RTA_AHORRO.insert(INSERT, f"\n {AHORROS}$")
#      RTA_INVENTIR.insert(INSERT, f"\n {INVERTIR}$" )

#   else:
#      toplevel_de_eleccion.insert(INSERT, "¡¡NO ES SUFICIENTE!!")  





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
    bt_SAVINGS = Button(toplevel_de_eleccion, text="MORE SAVINGS", width=20, height=3, command=lambda: abrir_toplevel_more_savings(SUELDO.get()))
    bt_SAVINGS.place(x=100, y=500)
    bt_INVEST = Button(toplevel_de_eleccion, text="LEARN TO INVEST", width=20, height=3, command = abrir_toplevel_learn_invest)
    bt_INVEST.place(x=450, y=500)


# boton izquierdo
def abrir_toplevel_more_savings(sueldo):
    def REGLA503020():
        valor = int(TSUELDO.get())
        if valor > 1300606:
            print(valor)
            Gastos_basicos = valor*0.5
            GASTOS_EXTRA = valor*0.3
            AHORRO = valor*0.2
            t_resultados.insert(INSERT, str(Gastos_basicos))
            t_extra.insert(INSERT, str(GASTOS_EXTRA))
            t_ahorros.insert(INSERT, str(AHORRO))
        else:
            toplevel_de_eleccion.insert(INSERT, "¡¡NO ES SUFICIENTE!!")
    
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

    # sueldo
    TSUELDO = Entry(toplevel_de_eleccion, textvariable= sueldo)
    TSUELDO.config(bg="#A48C64", fg="white", font=("Century Gothic", 20), width=27)
    TSUELDO.focus_set()
    TSUELDO.place(x=25,y=100)

    t_resultados = Text(toplevel_de_eleccion)
    t_resultados.config(bg="#A48C64", fg="white", font=("Century Gothic", 24))
    t_resultados.place(x=50,y=200,width=380,height=50)

    t_extra = Text(toplevel_de_eleccion)
    t_extra.config(bg="#A48C64", fg="white", font=("Century Gothic", 24))
    t_extra.place(x=50,y=300,width=380,height=50)

    t_ahorros = Text(toplevel_de_eleccion)
    t_ahorros.config(bg="#A48C64", fg="white", font=("Century Gothic", 24))
    t_ahorros.place(x=50,y=400,width=380,height=50)

    bt_EXPLICACION = Button(toplevel_de_eleccion,text="EXPLICATION", command= abrir_explicacion)
    bt_EXPLICACION.config(bg="#A48C64", fg="white", font=("Century Gothic", 18), width=15)
    bt_EXPLICACION.place(x=100, y=550, height=50)
    
    # boton que imprime el valor de TSUELDO
    bt_CALCULAR = Button(toplevel_de_eleccion,text="CALCULATE", command=REGLA503020)
    bt_CALCULAR.config(bg="#A48C64", fg="white", font=("Century Gothic", 18), width=15)
    bt_CALCULAR.place(x=450, y=50, height=50)

    bt_volver = Button(toplevel_de_eleccion,text="COME BACK", command=comeback)
    bt_volver.config(bg="#A48C64", fg="white", font=("Century Gothic", 14), width=15)
    bt_volver.place(x=0, y=0, height=20)
 
 
def abrir_toplevel_learn_invest():
    def REGLA60101020():
        valor = int(TSUELDO.get())
        if valor > 0:
            Gastos_basicos = valor * 0.6
            GASTOS_EXTRA = valor * 0.2
            AHORRO = valor * 0.1
            INVERSION = valor * 0.1
            t_esencial.insert(INSERT, str(Gastos_basicos))
            t_extra.insert(INSERT, str(GASTOS_EXTRA))
            t_ahorros.insert(INSERT, str(AHORRO))
            t_inversion.insert(INSERT, str(INVERSION))
        else:
            toplevel_de_eleccion.insert(INSERT, "¡¡ERROR!!")

    global toplevel_de_eleccion
    toplevel_de_eleccion = Toplevel()
    toplevel_de_eleccion.title("60/10/10/10/20")
    toplevel_de_eleccion.resizable(False, False)
    toplevel_de_eleccion.geometry("700x700")
    toplevel_de_eleccion.config(bg="aquamarine")

    lb_logo3 = Label(toplevel_de_eleccion, image=LOGO4, bg="aquamarine")
    lb_logo3.place(x=-50, y=400)

    SALARIO = Label(toplevel_de_eleccion, text="ENTER YOUR SALARY")
    SALARIO.config(bg="White", fg="medium sea green", font=("Century Gothic", 28))
    SALARIO.place(x=263, y=50)

    ESENCIAL = Label(toplevel_de_eleccion, text="ESSENTIAL EXPENSES")
    ESENCIAL.config(bg="White", fg="medium sea green", font=("Century Gothic", 28))
    ESENCIAL.place(x=325, y=150)

    EXTRA = Label(toplevel_de_eleccion, text="EXTRA EXPENSES")
    EXTRA.config(bg="White", fg="medium sea green", font=("Century Gothic", 28))
    EXTRA.place(x=394, y=250)

    AHORROS = Label(toplevel_de_eleccion, text="SAVINGS")
    AHORROS.config(bg="White", fg="medium sea green", font=("Century Gothic", 28))
    AHORROS.place(x=520, y=350)

    INVERTIR = Label(toplevel_de_eleccion, text="TO INVEST")
    INVERTIR.config(bg="White", fg="medium sea green", font=("Century Gothic", 28))
    INVERTIR.place(x=500, y=450)

    TSUELDO = Entry(toplevel_de_eleccion, textvariable=SUELDO)
    TSUELDO.config(bg="sea green", fg="white", font=("Bodoni MT", 20), width=27)
    TSUELDO.focus_set()
    TSUELDO.place(x=270, y=100)

    t_esencial = Text(toplevel_de_eleccion)
    t_esencial.config(bg="sea green", fg="white", font=("Bodoni MT", 24))
    t_esencial.place(x=300, y=200, width=380, height=50)

    t_extra = Text(toplevel_de_eleccion)
    t_extra.config(bg="sea green", fg="white", font=("Bodoni MT", 24))
    t_extra.place(x=300, y=300, width=380, height=50)

    t_ahorros = Text(toplevel_de_eleccion)
    t_ahorros.config(bg="sea green", fg="white", font=("Bodoni MT", 24))
    t_ahorros.place(x=300, y=400, width=380, height=50)

    t_inversion = Text(toplevel_de_eleccion)
    t_inversion.config(bg="sea green", fg="white", font=("Bodoni MT", 24))
    t_inversion.place(x=300, y=500, width=380, height=50)

    bt_EXPLICACION = Button(toplevel_de_eleccion, text="EXPLICATION", command=abrir_explicacion_mas_invertir)
    bt_EXPLICACION.config(bg="medium sea green", fg="white", font=("Bodoni MT", 18), width=15)
    bt_EXPLICACION.place(x=400, y=600, height=50)

    bt_CALCULAR = Button(toplevel_de_eleccion, text="CALCULATE", command=REGLA60101020)
    bt_CALCULAR.config(bg="medium sea green", fg="white", font=("Bodoni MT", 18), width=15)
    bt_CALCULAR.place(x=25, y=75, height=50)

    bt_volver = Button(toplevel_de_eleccion, text="COME BACK", command=come_back)
    bt_volver.config(bg="medium sea green", fg="white", font=("Bodoni MT", 14), width=15)
    bt_volver.place(x=0, y=0, height=20)




# aceptar
def aceptar():
    global cent
    cent = int(c.get())
    toplevel_de_eleccion.destroy()


def obtener_texto():
    texto = int(Entry.get())
    print("Texto ingresado:", texto)



def abrir_explicacion():
    global explicacion_window
    explicacion_window = Toplevel()
    explicacion_window.title("EXPLICATION")
    explicacion_window.resizable(False, False)
    explicacion_window.geometry("700x500")
    explicacion_window.config(bg="DarkOrange2")#A48C64

    # Texto de explicación
    texto_explicacion = "ESSENTIAL EXPENSES = En gastos esenciales se refiere a los mas basico\n que se necesita para vivir por ejemplo lo que es el mercado del mes\n y los implementos de aseo personal y de la casa tambien,\n otro gasto basico seria el arriendo o la hipoteca del banco\n o los impuesto dependiendo la situacio\n\n EXTRA EXPENSES  = los gastos extra son por ejemplo una menbrecia de \n gimnacio, una o dos suscripciones a distintas plataformas de \n entretenimiento tambien internet fijo de internet, datos moviles,\nn comidas rapidas, alcohol y gastos de una sola ves osea un gasto personal \n\n SAVINGS =  Un ahorro de emergencia el cual busca tener \nel despues de seis mese el equivalente al 50% para \n cualquier problema que se presente o tambien vacaciones que quieras \n o algo que pretendas comprar. "
    label_explicacion = Label(explicacion_window, text=texto_explicacion, bg="DarkOrange2", fg="white", font=("Small Fonts", 14), justify=LEFT)
    label_explicacion.place(x=10, y=50)

def abrir_explicacion_mas_invertir():
    global explicacion_window
    explicacion_window = Toplevel()
    explicacion_window.title("EXPLICATION")
    explicacion_window.resizable(False, False)
    explicacion_window.geometry("700x600")
    explicacion_window.config(bg="DarkOrange1")#A48C64

    # Texto de explicación
    texto_explicacion = "ESSENTIAL EXPENSES = En gastos esenciales se refiere a los mas basico\n que se necesita para vivir por ejemplo lo que es el mercado del mes\n y los implementos de aseo personal y de la casa tambien,\n otro gasto basico seria el arriendo o la hipoteca del banco\n o los impuesto dependiendo la situacio\n\n EXTRA EXPENSES  = los gastos extra son por ejemplo una menbrecia de \n gimnacio, una o dos suscripciones a distintas plataformas de \n entretenimiento tambien internet fijo de internet, datos moviles,\nn comidas rapidas, alcohol y gastos de una sola ves osea un gasto personal \n\n SAVINGS =  Un ahorro de emergencia el cual busca tener \nel despues de seis mese el equivalente al 50% para \n cualquier problema que se presente o tambien vacaciones que quieras \n o algo que pretendas comprar. \n\n\n INVETS = Este porcentaje de tu dinero puedes usarlo \n para invertir y probar cosas nuevas, es mas recomendables \n para los jovenes ya que asi puede hacer prueba y error \n y invertir sin mucho margen de error. Tambien se puede\n  utilizar para emprender y crear tu nueva empresa. "
    label_explicacion = Label(explicacion_window, text=texto_explicacion, bg="DarkOrange1", fg="white", font=("Small Fonts", 14), justify=LEFT)
    label_explicacion.place(x=10, y=50)


def come_back():
    toplevel_de_eleccion.destroy()

def comeback():
    toplevel_de_eleccion.destroy()

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
SUELDO =StringVar()
RTA_INVERTIR = StringVar()
global t_resultados, t_extra, t_ahorros


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
