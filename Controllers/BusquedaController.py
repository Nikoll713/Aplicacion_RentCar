import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets

class BusquedaController():

    def __init__(self, Ui_busqueda):
        self.Ui_busqueda = Ui_busqueda

    def GoPrincipal(self, Ui_busqueda, Ui_principal):
        Ui_busqueda.hide()    
        self.busqueda = QtWidgets.QMainWindow() 
        self.ui2 = Ui_principal()
        self.ui2.setupUi(self.busqueda)
        self.busqueda.show()  