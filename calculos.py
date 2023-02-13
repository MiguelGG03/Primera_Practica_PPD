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