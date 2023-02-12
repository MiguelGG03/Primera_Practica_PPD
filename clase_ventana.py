from tkinter import *

class Ventana(Frame):

    def __init__(self, master=None):
        super(Ventana,self).__init__(master,width=3200,height=2400,bg='black')
        self.master.title("Roomba")
        # Sin el self.pack() no se muestran los cambios realizados
        self.pack()

    def initWidgets(self): 
        # Declaración de una etiqueta que muestra el texto 'F'. 
        # El primer argumento es el widget 'padre' 
        # que contendrá esta etiqueta, es decir, self, 
        # el frame principal. 
        self.FTexto = Label (self, text = 'F') 
 
        # Declaración de un cursor que mostrará los grados 
        # Fahrenheit. Los parámetros llamados del constructor 
        # permiten personalizar el widget: su orientación 
        # es horizontal y los valores que recorre van 
        # de -148 a 212. 
        self.FCursor = Scale(self, orient=HORIZONTAL, from_=-148, 
                             to=212) 
 
        # Idem aquí para los grados Celsius. 
        self.CTexto = Label(self, text='C') 
        self.CCursor = Scale(self, orient=HORIZONTAL, from_=-100, 
                             to=100) 
 
        # Creamos una lista de widgets sobre la que hacemos un bucle ... 
        for widget in [self.CTexto, self.CCursor, self.FTexto, 
                       self.FCursor]: 
            # El widget actual está "pegado" a la izquierda 
            # en la ventana de la aplicación. 
            widget.pack(side=LEFT) 
    
    # Método llamado cuando el cursor de grados Celsius 
    # se ha movido. Calcula la equivalencia en grados Fahrenheit 
    # y modifica el valor del cursor de esta escala de 
    # grados en consecuencia.
    def convertirCEnF(self, valor): 
        C = float(valor) 
        F = C * 9/5 + 32 
        self.FCursor.set(F) 
 
    # Como convertirCEnF(), pero en el sentido opuesto 
    # de conversión de escalas de grados. 
    def convertirFEnC(self, valor): 
        F = float(valor) 
        C = (F - 32) * 5/9 
        self.CCursor.set(C)

if __name__=='__main__':
    # Instanciación de la ventana. 
    mi_ventana = Ventana() 
    # Inicialización de los widgets. 
    mi_ventana.initWidgets() 
    # Asociación de los eventos a los métodos.
    mi_ventana.CCursor.config(command=mi_ventana.convertirCEnF)
    mi_ventana.FCursor.config(command=mi_ventana.convertirFEnC)
    # Lanzamiento del bucle principal. 
    mi_ventana.mainloop()