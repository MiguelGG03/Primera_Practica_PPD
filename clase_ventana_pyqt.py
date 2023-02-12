from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QSpinBox, QLineEdit, QHBoxLayout, QComboBox 
 
# Definición de una QMainWindow personalizada para poder 
# crear instancias de futuros widgets en ella. 
class MainWindow(QMainWindow): 
    def __init__(self): 
        super(MainWindow, self).__init__()

# Si el módulo es ejecutado como programa principal,
# se crea una instancia de la clase MainWindow y se
# inicia el bucle de eventos de la aplicación.
# El valor de retorno del bucle de eventos se utilizará
# como código de salida de la ejecución.
# 
# El código de la aplicación se coloca dentro de esta
# condición para evitar que se ejecute cuando el módulo
# es importado por otro módulo.
#   
# El módulo __name__ es una variable especial que contiene
# el nombre del módulo en el que se está ejecutando.
# Si el módulo es ejecutado como programa principal,
# su valor es '__main__'. 
 
if __name__ == '__main__': 
 
    # Requisitos para obtener sys.argv. 
    import sys 
 
    # QApplication requiere la lista de argumentos pasadas 
    # al ejecutable durante su instanciación. 
    app = QApplication(sys.argv) 
 
    # Creación de la ventana principal. 
    window = MainWindow() 
 
    # Visualización de la ventana principal. 
    window.show() 
 
    # Inicio del bucle de eventos, cuyo valor 
    # de retorno se utilizará como código de salida de la ejecución. 
    sys.exit(app.exec_())