'''
Fichero de eventos generales
'''
import os.path
import shutil
import zipfile, xlrd

import var, conexion, clients
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtPrintSupport
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

    def resizeTablaArt(self):
        try:
            header = var.ui.tabArticulos.horizontalHeader()
            for i in range(2):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
                if i == 0 or i==2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        except Exception as error:
            print('Error al dar formato a tabla articulos ',error)

    def resizeTablaFac(self):
        try:
            header = var.ui.tabFacturas.horizontalHeader()
            for i in range(2):
                if i == 1:
                    header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
                if i == 0 :
                    header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        except Exception as error:
            print('Error al dar formato a tabla facturas ',error)

    def resizeTablaVen(self):
        try:
            header = var.ui.tabVentas.horizontalHeader()
            for i in range(5):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
                if i == 1 or i == 3:
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

    def Imprimir(self):
        try:
            printDialog=QtPrintSupport.QPrintDialog()
            if printDialog.exec():
                printDialog.show()
        except Exception as error:
            print('Error en evento imprimir ',error)

    def ImportarDatos(self):
        try:
            option = QtWidgets.QFileDialog.Options()
            origen, filter = var.dlgabrir.getOpenFileName(None, 'Importar Datos', '', '*.xls;;ALL',
                                                          options=option)
            try:
                msgBox = QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                msgBox.setText("Seguro que quieres importar los datos?")
                msgBox.setWindowTitle("Confirmación")
                msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                msgBox.setDefaultButton(QMessageBox.No)
                res=msgBox.exec()
                if (res==QMessageBox.Yes):
                    documento = xlrd.open_workbook(origen)
                    hoja = documento.sheet_by_index(0)
                    numRexistros = hoja.nrows
                    numColumns = hoja.ncols
                    for r in range(1, numRexistros):
                        cliente = []
                        for c in range(numColumns):
                            # Se toma el cliente y su dni
                            cliente.append(str(hoja.cell_value(r, c)))
                        conexion.Conexion.clienteExcel(cliente)
                    conexion.Conexion.cargaTabCli(self)
            except Exception as error:
                print('Error evento importar datos: ', error)
        except Exception as error:
            print('Error en evento importar datos: ',error)

    def ExportarDatos(self):
        try:
            procesado=conexion.Conexion.exportExcel(self)
            if procesado:
                try:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Information)
                    msgBox.setText("Datos exportados con éxito.")
                    msgBox.setWindowTitle("Operación completada")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()
                except Exception as error:
                    print('Error en mensaje generado exportar datos ', error)
            else:
                try:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Information)
                    msgBox.setText("No han podido exportarse los datos.")
                    msgBox.setWindowTitle("Error export datos")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()
                except Exception as error:
                    print('Error en mensaje generado backup ', error)
        except Exception as error:
            print('Error en evento exportar datos ',error)

    def labelEnvio(self):
        try:
            valor=var.ui.spinEnvio.value()
            if(valor==0):
                var.ui.lblEnvio.setText('Recogida Cliente')
            elif valor==1:
                var.ui.lblEnvio.setText('Envío Nacional Urgente')
            elif valor==2:
                var.ui.lblEnvio.setText('Envío Nacional Normal')
            else:
                var.ui.lblEnvio.setText('Envío Internacional')

        except Exception as error:
            print('Error en evento actualizar label envíos ', error)

    def acercaDe(self):
        try:
            msgBox = QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setText("Este es un proyecto de Diseño de Interfaces. "
                           "\nHa sido realizado por Sol González.")
            msgBox.setWindowTitle("Aviso")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        except Exception as error:
            print('Error al mostrar acerca de ',error)

