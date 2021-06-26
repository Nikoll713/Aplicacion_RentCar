import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets

class PrincipalController():

    def __init__(self, Ui_principal):
        self.Ui_principal = Ui_principal

    def logIn(self,user,password, Ui_Principal, LogIn):
        if user and password:
            user = self.user.getUser(user,password)
            if user:
                LogIn.hide()
                self.log_in.Form = QtWidgets.QMainWindow()
                self.log_in.ui = Ui_Principal()
                self.log_in.ui.setupUi(self.log_in.Form)
                self.log_in.Form.show()
                print('Estas logeado')
            else:
                print('No estas logeado')