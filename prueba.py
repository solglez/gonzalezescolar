# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prueba.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.414, y1:1, x2:0.46, y2:0, stop:0 rgba(55, 155, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 100, 291, 122))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblClientes = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setUnderline(True)
        self.lblClientes.setFont(font)
        self.lblClientes.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.011, y1:1, x2:0.358, y2:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255))")
        self.lblClientes.setObjectName("lblClientes")
        self.verticalLayout.addWidget(self.lblClientes, 0, QtCore.Qt.AlignHCenter)
        self.txtDatos = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtDatos.setObjectName("txtDatos")
        self.verticalLayout.addWidget(self.txtDatos)
        self.btnAceptar = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnAceptar.setFont(font)
        self.btnAceptar.setObjectName("btnAceptar")
        self.verticalLayout.addWidget(self.btnAceptar)
        self.btnSalir = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnSalir.setFont(font)
        self.btnSalir.setObjectName("btnSalir")
        self.verticalLayout.addWidget(self.btnSalir)
        self.lblDNI = QtWidgets.QLabel(self.centralwidget)
        self.lblDNI.setGeometry(QtCore.QRect(90, 300, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblDNI.setFont(font)
        self.lblDNI.setObjectName("lblDNI")
        self.txtDNI = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDNI.setGeometry(QtCore.QRect(140, 300, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtDNI.setFont(font)
        self.txtDNI.setObjectName("txtDNI")
        self.lblValidoDNI = QtWidgets.QLabel(self.centralwidget)
        self.lblValidoDNI.setGeometry(QtCore.QRect(340, 300, 47, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblValidoDNI.setFont(font)
        self.lblValidoDNI.setText("")
        self.lblValidoDNI.setObjectName("lblValidoDNI")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionGuardar_como = QtWidgets.QAction(MainWindow)
        self.actionGuardar_como.setObjectName("actionGuardar_como")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IMPORT - EXPORT TEIS"))
        self.lblClientes.setText(_translate("MainWindow", "XESTIÓN CLIENTES"))
        self.btnAceptar.setText(_translate("MainWindow", "Aceptar"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))
        self.lblDNI.setText(_translate("MainWindow", "DNI: "))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionGuardar_como.setText(_translate("MainWindow", "Guardar como..."))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Alt+S"))
