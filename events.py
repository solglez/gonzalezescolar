'''
Fichero de eventos generales
'''
import var
import sys
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
            for i in range(4):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
                if i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        except Exception as error:
            print('Error al dar formato a tabla clientes ',error)


