
import sys
from xml.dom.minidom import TypeInfo
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5 import sip
from Ui_Interfaz_Principal import Ui_MainWindow
from Ui_Interfaz_k import Ui_Form2
from Ui_Interfaz_Grafica import Ui_Form3
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolBar
import matplotlib.pyplot as plt
from Controlador import Controlador


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        view = Ui_MainWindow()
        view.setupUi(self)
        view.Analizar_Dataset.triggered.connect(self.cambiar_A_Interfaz_opcion)
    
    def cambiar_A_Interfaz_opcion(self):
        interfaz_k=Interfaz_k()
        widget.addWidget(interfaz_k)
        widget.setCurrentWidget(interfaz_k)
        widget.setFixedWidth(342)
        widget.setFixedHeight(172)


#-------------------------------------------------------------------------
class Interfaz_k(QWidget):
    def __init__(self):
        super(Interfaz_k,self).__init__()
        self.view = Ui_Form2()
        self.fname=None
        self.view.setupUi(self)
        self.view.pushButton_5.clicked.connect(self.buscar_Dataset)
        self.view.pushButton_3.clicked.connect(self.cambiar_A_Interfaz_Principal)
        self.view.pushButton_4.clicked.connect(self.cambiar_A_Interfaz_opcion)

    def buscar_Dataset(self):
        self.fname=QFileDialog.getOpenFileName(self,'Open File','E:','Archivo CSV(*.csv)')
        self.view.lineEdit_4.setText(self.fname[0])

    def cambiar_A_Interfaz_Principal(self):
        self.limpiarComponentes()
        widget.setCurrentWidget(principal)
        widget.setFixedWidth(600)
        widget.setFixedHeight(320)

    def cambiar_A_Interfaz_opcion(self):
        if(not self.view.lineEdit_4.text()):
            QtWidgets.QMessageBox.critical(self, "error", "Ingrese todos los campos por favor")
        else:   
            control.obtenerDatos(self.fname[0])
            interfaz_grafica=Interfaz_Grafica()
            widget.addWidget(interfaz_grafica)
            self.limpiarComponentes()
            widget.setCurrentWidget(interfaz_grafica)
            widget.setFixedWidth(841)
            widget.setFixedHeight(993)    
    
    def limpiarComponentes(self):
        self.view.lineEdit_4.setText("")

#-------------------------------------------------------------------------     
class Interfaz_Grafica(QWidget):
    def __init__(self):
        super(Interfaz_Grafica,self).__init__()
        self.view = Ui_Form3()
        self.view.setupUi(self)
        self.size=self.view.horizontalSlider.value()
        self.view.pushButton_2.clicked.connect(self.cambiar_A_Interfaz_Principal)
        self.view.pushButton.clicked.connect(self.cambiarGrafico)
        self.view.mostrarK.setText(str(self.view.horizontalSlider.value()))
        
        self.view.horizontalSlider.valueChanged.connect(self.cambiarValor)
        self.grafica1=control.mostrarResultadoAlgoritmo()
        self.grafica2=Canvas_grafica()
        self.grafica3=control.mostrarResultadoAlgoritmoPonderado()
        self.grafica4=Canvas_grafica()
        self.navigrafica1=NavigationToolBar(self.grafica1,self)
        self.navigrafica2=NavigationToolBar(self.grafica2,self)
        self.navigrafica3=NavigationToolBar(self.grafica3,self)
        self.navigrafica4=NavigationToolBar(self.grafica4,self)




        self.view.grafica1.addWidget(self.grafica1)
        self.view.grafica2.addWidget(self.grafica2)
        self.view.grafica3.addWidget(self.grafica3)
        self.view.grafica4.addWidget(self.grafica4)
        self.view.grafica1.addWidget(self.navigrafica1)
        self.view.grafica2.addWidget(self.navigrafica2)
        self.view.grafica3.addWidget(self.navigrafica3)
        self.view.grafica4.addWidget(self.navigrafica4)
    
    def cambiarGrafico(self):
        '''
        self.grafica1.deleteLater()
        self.grafica3.deleteLater()
        self.navigrafica1.deleteLater()
        self.navigrafica3.deleteLater()
        '''
        
        #control.limpiarDatosAlgoritmo()
        
        self.grafico1=control.obtenerGraficoKnnConK(self.size)
        self.grafico3=control.obtenerGraficoKnnConK(self.size)
        self.navigrafica1=NavigationToolBar(self.grafica1,self)
        self.navigrafica3=NavigationToolBar(self.grafica3,self)
        self.view.grafica1.replaceWidget(self.grafico1)
        self.view.grafica3.replaceWidget(self.grafico3)
        self.view.grafica1.replaceWidget(self.navigrafica1)
        self.view.grafica3.replaceWidget(self.navigrafica3)
        
    
    def cambiarValor(self):
        self.size=self.view.horizontalSlider.value()
        self.view.mostrarK.setText(str(self.size))

    def cambiar_A_Interfaz_Principal(self):
        widget.setCurrentWidget(principal)
        widget.setFixedWidth(600)
        widget.setFixedHeight(320)

#-------------------------------------------------------------------------  

class Canvas_grafica(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 

        nombres = ['15', '25', '30', '35','40']
        colores = ['red','red','red','red', 'red']
        tamaño = [10, 15, 20, 25, 30]

        self.ax.bar(nombres, tamaño, color = colores)
        self.fig.suptitle('Grafica de Barras',size=9)

app= QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
control=Controlador()
principal = MainWindow()
widget.addWidget(principal)
widget.setCurrentWidget(principal)
widget.setFixedWidth(600)
widget.setFixedHeight(320)
widget.show()


try:
    sys.exit(app.exec_())
except:
    print("Ya existe")