import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets

class PrincipalController():

    def __init__(self, Ui_principal):
        self.Ui_principal = Ui_principal

    def GoView(self, Ui_principal, Ui_Final): 
        self.busqueda = QtWidgets.QMainWindow() 
        self.ui2 = Ui_Final()
        self.ui2.setupUi(self.busqueda)
        self.busqueda.show()  
 