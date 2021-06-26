import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)



from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PaginaPrincipal(object):
    def setupUi(self, PaginaPrincipal):
        PaginaPrincipal.setObjectName("PaginaPrincipal")
        PaginaPrincipal.resize(800, 602)
        PaginaPrincipal.setStyleSheet("background-color: rgb(51, 51, 51);")
        self.centralwidget = QtWidgets.QWidget(PaginaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(170, 80, 491, 201))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(90)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(186, 0, 0);\n"
"background-color: rgb(51, 51, 51);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 230, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(35)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(51, 51, 51);\n"
"color: rgb(236, 236, 236);")
        self.label_3.setObjectName("label_3")
        self.btn_busqueda = QtWidgets.QPushButton(self.centralwidget)
        self.btn_busqueda.setGeometry(QtCore.QRect(40, 370, 341, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.btn_busqueda.setFont(font)
        self.btn_busqueda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_busqueda.setStyleSheet("border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(186, 0, 0);\n"
"background-color: rgb(51, 51, 51);\n"
"color: rgb(186, 0, 0);\n"
"border-radius: 25px;")
        self.btn_busqueda.setObjectName("btn_busqueda")
        self.btn_salida = QtWidgets.QPushButton(self.centralwidget)
        self.btn_salida.setGeometry(QtCore.QRect(420, 370, 341, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.btn_salida.setFont(font)
        self.btn_salida.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_salida.setStyleSheet("border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(186, 0, 0);\n"
"background-color: rgb(51, 51, 51);\n"
"color: rgb(186, 0, 0);\n"
"border-radius: 25px;")
        self.btn_salida.setObjectName("btn_salida")
        PaginaPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(PaginaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(PaginaPrincipal)

    def retranslateUi(self, PaginaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        PaginaPrincipal.setWindowTitle(_translate("PaginaPrincipal", "MainWindow"))
        self.label.setText(_translate("PaginaPrincipal", "RentCar"))
        self.label_3.setText(_translate("PaginaPrincipal", "Welcome"))
        self.btn_busqueda.setText(_translate("PaginaPrincipal", "Sistema de busqueda"))
        self.btn_salida.setText(_translate("PaginaPrincipal", "Programacion de salidas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PaginaPrincipal = QtWidgets.QMainWindow()
    ui = Ui_PaginaPrincipal()
    ui.setupUi(PaginaPrincipal)
    PaginaPrincipal.show()
    sys.exit(app.exec_())
