'''
Fichero de eventos generales
'''
import var
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
import windowaviso
from windowaviso import *
from prueba import *

class Eventos():
    def salir(self):
        try:
            var.dlgaviso.show()
            if var.dlgaviso.exec():
                sys.exit()
            else:
                var.dlgaviso.hide()
        except Exception as error:
            print('Error en módulo salir ', error)

    def abrirCal(self):
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error en módulo abrir calendario ',error)

    def resizeTablaCli(self):
        try:
            header = var.ui.tabClientes.horizontalHeader()
            for i in range(5):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
                if i == 0 or i==3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        except Exception as error:
            print('Error al dar formato a tabla clientes ',error)

    def errorDNI(self):
        try:
            msgBox = QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            msgBox.setText("DNI no válido")
            msgBox.setWindowTitle("ERROR")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        except Exception as error:
            print('Error en mensaje error DNI ', error)

    def abrir(self):
        try:
            var.dlgabrir.show()
        except Exception as error:
            print('Error en evento abrir ', error)


