from tkinter import *

# Creamos la raiz de nuestra aplicación
habitacion = Tk()
habitacion.geometry('500x630')
habitacion.config(borderwidth=30)
habitacion.config(relief="solid")
habitacion.config(bg="white")
texto1=Label(habitacion, text="Zona 1")
texto1.pack(side=TOP)
texto2=Label(habitacion, text="Zona 2")
texto2.pack(side=LEFT)
texto3=Label(habitacion, text="Zona 3")
texto3.pack(side=RIGHT)
texto4=Label(habitacion, text="Zona 4")
texto4.pack(side=BOTTOM)
mueble = Frame(habitacion, width=50,height=1)
mueble.config(bg='white')
mueble.place(width=146,height=350)
mueble.pack(side=LEFT)
mueble1= Frame(habitacion, width=90,height=260)
mueble1.config(bg='brown')
mueble1.pack(side=LEFT)


habitacion.mainloop()