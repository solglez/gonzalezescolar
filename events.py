'''
Fichero de eventos generales
'''
import os.path
import shutil
import zipfile

import var, conexion, clients
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
import windowaviso
from windowaviso import *
from prueba import *
from datetime import date, datetime
from zipfile import *

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

    def crearBackup(self):
        try:
            fecha=datetime.today()
            fecha=fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia=(str(fecha)+'_backup.zip')
            option=QtWidgets.QFileDialog.Options()
            directorio, filename=var.dlgabrir.getSaveFileName(None, 'Guardar Copia', var.copia, '.zip', options=option)
            if var.dlgabrir.Accept and filename !='':
                fichzip=zipfile.ZipFile(var.copia, 'w')
                fichzip.write(var.filedb, os.path.basename(var.filedb), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(var.copia), str(directorio))
                try:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Information)
                    msgBox.setText("Backup generado con éxito.")
                    msgBox.setWindowTitle("Generated Backup")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()
                except Exception as error:
                    print('Error en mensaje generado backup ', error)

        except Exception as error:
            print('Error en evento crear backup ',error)

    def restaurarBackup(self):
        try:
            restaurado=False
            option = QtWidgets.QFileDialog.Options()
            origen, filter = var.dlgabrir.getOpenFileName(None,'Restaurar copia de seguridad ','','*.zip;;ALL',options=option)

            with ZipFile(origen, 'r') as obj_zip:
                FileNames = obj_zip.namelist()
                for fileName in FileNames:
                    if fileName==('bbdd.sqlite'):
                        obj_zip.extract(fileName, os.getcwd())
                        restaurado=True

            if restaurado:
                conexion.Conexion.db_connect(var.filedb)
                conexion.Conexion.cargaTabCli(self)
                clients.Clientes.cargaProv(self)
                try:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Information)
                    msgBox.setText("Se ha restaurado la base de datos.")
                    msgBox.setWindowTitle("Restaurada BD")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()
                except Exception as error:
                    print('Error en mensaje generado backup ', error)
            else:
                try:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Information)
                    msgBox.setText("Hay un error en su archivo backup.")
                    msgBox.setWindowTitle("Error de archivo")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()
                except Exception as error:
                    print('Error en mensaje generado backup ', error)

        except Exception as error:
            print('Error al restaurar backup ',error)
