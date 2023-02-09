from tkinter import *

# Configuración de la raíz
root = Tk()
root.title("Roomba")
root.resizable(1,1)

frame = Frame(root, width=480, height=320)
frame.pack(fill='both', expand=1)
frame.config(bd=25)



# Finalmente bucle de la aplicación
root.mainloop()  