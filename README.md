# Primera_Practica_PPD

El enlace al repositorio: [GitHub](https://github.com/migueliiin/Primera_Practica_PPD.git)
### Para realizar este trabajo, hemos seguido los siguientes pasos:
1. Hemos creado la interfaz gráfica utilizando la libreria thkinter, utilizando algunos widgets como
   Tk,Label,Frame para poder dividir la habitacion en las zonas que nos indica el ejercicio, ademas de situar la mesa 
   en la posicion indicada

2. Hemos utilizado funciones sencillas para realizar los calculos que nos pide el ejercicio,
   para ello hemos supuesto una velocidad optima para el roomba y utilizado las formulas adecuadas
   
3. Creacion del Main para que el codigo a ejecutar sea el menor posible


## Código interfaz gráfica
```
from tkinter import *

def pantalla_pintada():
    # Creamos la raiz de nuestra aplicación
    habitacion = Tk()
    habitacion.geometry('500x630')
    habitacion.config(borderwidth=30)
    habitacion.config(relief="solid")
    habitacion.config(bg="white")
    texto1=Label(habitacion, text="Zona 1")
    texto1.place(x=200,y=50)
    texto2=Label(habitacion, text="Zona 2")
    texto2.place(x=30,y=220)
    texto3=Label(habitacion, text="Zona 3")
    texto3.place(x=300,y=330)
    texto4=Label(habitacion, text="Zona 4")
    texto4.place(x=115,y=480)
    mueble1= Frame(habitacion, width=90,height=260)
    mueble1.config(bg='brown')
    mueble1.place(x=92,y=155)
    raya1=Frame(habitacion, width=440,height=1)
    raya1.config(bg='green')
    raya1.place(x=0,y=155)
    raya2=Frame(habitacion, width=1,height=415)
    raya2.config(bg='green')
    raya2.place(x=91,y=155)
    raya3=Frame(habitacion, width=1,height=415)
    raya3.config(bg='green')
    raya3.place(x=182,y=155)

    habitacion.mainloop()
```

## Código cálculos
```
from tkinter import *
import turtle


def area(b, h):
    area = b * h
    return area

def tiempo(a, v):
    tiempo = a/v
    return tiempo

def calculado_todo():
    print(u'El roomba va a una velocidad de 0.1 m²/s')
    vel = 1000 #cm²/s
    area1 = area(500, 150)
    tiempo1 = tiempo(area1, vel)
    area2 = area(101, 480)
    tiempo2 = tiempo(area2, vel)
    area3 = area(309, 480)
    tiempo3 = tiempo(area3, vel)
    area4 = area(90, 220)
    tiempo4 = tiempo(area4, vel)

    print('El tiempo que tarda en limpiar cada zona es de:\nZona 1: {} min\nZona 2: {} min\nZona 3: {} min\nZona 4: {} min'.format(tiempo1/60, round(tiempo2/60,2), round(tiempo3/60,2), tiempo4/60))
    tiempoT = tiempo1 + tiempo2 + tiempo3 + tiempo4
    print('El roomba tardara ' + str(round(tiempoT/60,2)) + ' minutos')
```

## Código Main

```
from interfaz_grafica import *
from calculos import *

def main():
    calculado_todo()
    pantalla_pintada()
    
if __name__=='__main__':
    main()
```

# Resultados

La interfaz gráfica de la roomba es la siguiente

![roomba](https://user-images.githubusercontent.com/91721552/223159685-73216fda-5249-4925-ab82-42084b37dfbb.PNG)

Los resultados de tiempo son los siguientes

![tiempos](https://user-images.githubusercontent.com/91721552/223159811-90fc46fe-4ef4-4991-8c1d-98e9a5f736a0.PNG)
