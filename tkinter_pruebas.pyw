from tkinter import *
root = Tk()



# Hijo de root, no ocurre nada
frame = Frame(root,width=480,height=320)  

# Empaqueta el frame en la raíz
frame.pack()      

# Como no tenemos ningún elemento dentro del frame, 
# no tiene tamaño y aparece ocupando lo mínimo posible, 0*0 px

# Configuracion del frame
frame.config(bg="lightblue") 
frame.config(cursor="")
frame.config(bd=25)
frame.config(relief="sunken")
frame.pack(side=RIGHT)
frame.pack(anchor=SE)



# Configuracion de la raiz
root.title("Piratas")
root.iconbitmap('multimedia/hola.ico')
root.config(relief="groove")
root.config(cursor="pirate")
root.config(bg="blue")
root.config(bd=25)


root.mainloop()  