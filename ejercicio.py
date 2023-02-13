from tkinter import *

# Creamos la raiz de nuestra aplicación
'''root=Tk()
root.geometry('560x690')
root.config(bg='grey')'''
habitacion = Tk()
habitacion.geometry('500x630')
habitacion.config(borderwidth=30)
habitacion.config(relief="solid")
habitacion.config(bg="white")
#habitacion.pack(side=TOP)
mueble = Frame(habitacion, width=90,height=260)
mueble.config(bg='lightblue')
mueble.place(width=146,height=350)
mueble.pack(side=LEFT)
mueble.pack()


"""#divido la habitacion en zonas

zona1 = {"largo":500,"ancho":150}
zona2 = {"largo":480,"ancho":101}
zona3 = {"largo":309,"ancho":480}
zona4 = {"largo":90,"ancho":220}

#creo una lista con las zonas para tener la zona total
zona_total = []
zona_total.append(zona1)
zona_total.append(zona2)
zona_total.append(zona3)
zona_total.append(zona4)

ventana= Frame( width=2000, height=240)"""
habitacion.mainloop()