from tkinter import *

# Creamos la raiz de nuestra aplicación
root=Tk(width=560, height=690)
root.config(bg='grey')
habitacion = Frame(root, width=500, height=630)

#divido la habitacion en zonas

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

ventana= Frame( width=2000, height=240)
ventana.mainloop()