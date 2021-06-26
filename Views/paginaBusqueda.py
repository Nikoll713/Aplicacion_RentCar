from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PaginaBusqueda(object):

    def setupUi(self, PaginaBusqueda):
        PaginaBusqueda.setObjectName("PaginaBusqueda")
        PaginaBusqueda.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        PaginaBusqueda.setFont(font)
        PaginaBusqueda.setStyleSheet("background-color: rgb(51, 51, 51);")
        self.centralwidget = QtWidgets.QWidget(PaginaBusqueda)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 40, 571, 91))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(51, 51, 51);\n"
        "color: rgb(186, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 190, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(236, 236, 236);\n"
        "background-color: rgb(51, 51, 51);")
        self.label.setObjectName("label")
        self.input_precio = QtWidgets.QLineEdit(self.centralwidget)
        self.input_precio.setGeometry(QtCore.QRect(350, 185, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(16)
        self.input_precio.setFont(font)
        self.input_precio.setStyleSheet("color: rgb(236, 236, 236);\n"
        "border-radius: 5px;")
        self.input_precio.setObjectName("input_precio")
        self.btn_barato = QtWidgets.QPushButton(self.centralwidget)
        self.btn_barato.setGeometry(QtCore.QRect(510, 150, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_barato.setFont(font)
        self.btn_barato.setStyleSheet("border-style: solid;\n"
        "border-width: 3px;\n"
        "border-color: rgb(186, 0, 0);\n"
        "background-color: rgb(51, 51, 51);\n"
        "color: rgb(186, 0, 0);\n"
        "border-radius: 25px;")
        self.btn_barato.setObjectName("btn_barato")
        self.btn_caro = QtWidgets.QPushButton(self.centralwidget)
        self.btn_caro.setGeometry(QtCore.QRect(510, 220, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_caro.setFont(font)
        self.btn_caro.setStyleSheet("border-style: solid;\n"
        "border-width: 3px;\n"
        "border-color: rgb(186, 0, 0);\n"
        "background-color: rgb(51, 51, 51);\n"
        "color: rgb(186, 0, 0);\n"
        "border-radius: 25px;")
        self.btn_caro.setObjectName("btn_caro")
        self.table_auto = QtWidgets.QTableWidget(self.centralwidget)
        self.table_auto.setGeometry(QtCore.QRect(90, 290, 631, 271))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(12)
        self.table_auto.setFont(font)
        self.table_auto.setStyleSheet("QHeaderView::section { color: rgb(186, 0, 0); background-color: rgb(51, 51, 51); }\n"
        "\n"
        "QTableWidget {\n"
        "\n"
        "    color: rgb(186, 0, 0);\n"
        "}")
        self.table_auto.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.table_auto.setObjectName("table_auto")
        self.table_auto.setColumnCount(3)
        self.table_auto.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        item.setFont(font)
        self.table_auto.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        item.setFont(font)
        self.table_auto.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        item.setFont(font)
        self.table_auto.setHorizontalHeaderItem(2, item)
        self.table_auto.horizontalHeader().setDefaultSectionSize(209)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setBold(True)
        font.setWeight(75)
        PaginaBusqueda.setCentralWidget(self.centralwidget)

        self.retranslateUi(PaginaBusqueda)
        QtCore.QMetaObject.connectSlotsByName(PaginaBusqueda)

    def retranslateUi(self, PaginaBusqueda):
        _translate = QtCore.QCoreApplication.translate
        PaginaBusqueda.setWindowTitle(_translate("PaginaBusqueda", "MainWindow"))
        self.label_2.setText(_translate("PaginaBusqueda", "Busca tu auto por precio"))
        self.label.setText(_translate("PaginaBusqueda", "Ingresa el precio inicial:"))
        self.input_precio.setPlaceholderText(_translate("PaginaBusqueda", "Precio"))
        self.btn_barato.setText(_translate("PaginaBusqueda", "Mas barato"))
        self.btn_caro.setText(_translate("PaginaBusqueda", "Mas caro"))
        item = self.table_auto.horizontalHeaderItem(0)
        item.setText(_translate("PaginaBusqueda", "Marca"))
        item = self.table_auto.horizontalHeaderItem(1)
        item.setText(_translate("PaginaBusqueda", "Color"))
        item = self.table_auto.horizontalHeaderItem(2)
        item.setText(_translate("PaginaBusqueda", "Precio"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PaginaBusqueda = QtWidgets.QMainWindow()
    ui = Ui_PaginaBusqueda()
    ui.setupUi(PaginaBusqueda)
    PaginaBusqueda.show()
    sys.exit(app.exec_())
