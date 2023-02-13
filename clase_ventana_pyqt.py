from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QSpinBox, QLineEdit, QVBoxLayout, QComboBox 
 
# Definición de una QMainWindow personalizada para poder 
# crear instancias de futuros widgets en ella. 
class MainWindow(QMainWindow): 
    def __init__(self): 
        super(MainWindow, self).__init__()

        # Widget básico que sirve como base para la jerarquía de los sub-widgets. 
        widget = QWidget () 
 
        # Especifica que el widget principal de la ventana es el widget que se acaba de instanciar. 
        self.setCentralWidget(widget) 
 
        # Nueva distribución vertical. 
        diseño = QVBoxLayout () 
        # Asignación del diseño vertical al widget principal. 
        widget.setLayout(diseño) 
 
        # Los operandos se representan por spinboxes. 
        self.operando1 = QSpinBox () 
        self.operando2 = QSpinBox () 
 
        # Un menú desplegable le permite elegir la operación que se debe aplicar. Primero tiene que instanciarla. 
        self.operacion = QComboBox () 
        # Luego, insertamos los símbolos en el menú para poder seleccionarlos más tarde. 
        [self.operacion.addItem(op) for op in ["+", "-", "*", "/"]] 
 
        # Finalmente, el resultado de la operación está representado por una zona de texto. 
        self.resultado = QLineEdit() 
 
        # Uso de un generador para agregar fácilmente los widgets al layout. 
        widgets = [self.operando1, self.operacion, self.operando2, QLabel("="), self.resultado] 
        [diseño.addWidget(widget) for widget in widgets] 
 
        # La clase QSpinBox emite una señal valueChanged(int) 
        # cuando se modifica el valor mostrado en el spinbox. 
        # Conectamos esta señal al slot calcular(), que es un 
        # método de la clase MainWindow. Los prototipos son 
        # diferentes, pero el hecho de perder el parámetro de 
        # la señal, es irrelevante porque el slot puede recuperar 
        # el nuevo valor accediendo directamente a la spinbox. 
        self.operando1.valueChanged.connect(self.calcular) 
        self.operando2.valueChanged.connect(self.calcular) 
 
        # La clase QComboBox emite una señal 
        # currentTextChanged(QString) cuando el usuario ha 
        # seleccionado un nuevo valor del menú desplegable. 
        # Conectamos esta señal al slot calcular(). Aquí también, 
        # el nuevo texto del menú desplegable que lleva la 
        # señal, se puede ignorar. 
        self.operacion.currentIndexChanged.connect(self.calcular) 
 
        # Para que el widget que muestra el resultado esté actualizado 
        # tan pronto como se realiza la construcción de la ventana, 
        # realizamos el cálculo desde el constructor. 
        self.calcular()

    def calcular(self):

        a=self.operando1.value()
        b=self.operando2.value()
        
        if(self.operacion.currentText()=='+'):
            resultado=str(a+b)
        elif(self.operacion.currentText()=='-'):
            resultado=str(a-b)
        elif(self.operacion.currentText()=='*'):
            resultado=str(a*b)
        elif(self.operacion.currentText()=='/'):
            try:
                resultado=str(a/b)
            except ZeroDivisionError as e:
                resultado='No se puede dividir por cero'
        self.resultado.setText(resultado)
 
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