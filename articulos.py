import math
from PyQt5 import QtSql, QtWidgets
from PyQt5.QtWidgets import *

import clients
import conexion
import events
from prueba import *
import var
import locale
locale.setlocale(locale.LC_ALL, 'es-ES')

class Articulos():
    def guardaArticulo(self):
        try:
            if (Articulos.validarPrecio(self)):
                # Preparamos el registro
                # Para la base de datos
                artMoneda=locale.currency(float(var.ui.txtPrecioArticulo.text()))
                artMoneda.replace(',','.')
                newArt = [var.ui.txtNombreArticulo.text(), artMoneda]
                #articulo = [var.ui.txtNombreArticulo.text(), var.ui.txtPrecioArticulo]
                # Para representación en tableView
                # tabcli= []
                # client= [var.ui.txtDNI, var.ui.txtApel, var.ui.txtNome, var.ui.txtAltaCli]

                # Código para cargar en tabla

                #for i in articulo:
                   # newArt.append(i.text())

                # Codigo para grabar en base de datos
                conexion.Conexion.altaArt(newArt)
                conexion.Conexion.cargaTabArt(self)
        except Exception as error:
            print('Error en módulo guardar articulo ', error)

    def limpiaFormArt(self):
        try:
            var.ui.lblCodArt.setText('Auto')
            var.ui.txtPrecioArticulo.setText('')
            var.ui.txtNombreArticulo.setText('')
        except Exception as error:
            print('Error en módulo limpiar formulario articulos ', error)

    def cargaArt(self):

        try:
            fila = var.ui.tabArticulos.selectedItems()
            print('Metodo')
            datos = [var.ui.lblCodArt, var.ui.txtNombreArticulo, var.ui.txtPrecioArticulo]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                if i==2:
                    precio = row[i]
                    precio= precio.replace(',', '.')
                    precio = precio[:(len(precio) - 2)]
                    dato.setText(precio)
                else:
                    dato.setText(row[i])

            # Ahora los datos desde la base de datos:
            query = QtSql.QSqlQuery()
            orden = (
                        'SELECT nombre, precio WHERE codigo="' + var.ui.lblCodArt.text() + '"')
            query.prepare(orden)
            if query.exec_():
                while query.next():
                    print('Query')
                    var.ui.txtNombreArticulo.setText(query.value(0))
                    #sinMoneda=query.value(1)
                    #sinmoneda=sinmoneda[1:(len(sinMoneda)-2)]
                    var.ui.txtPrecioArticulo.setText(query.value(1))

            # Para que aparezca el DNI como válido en caso de querer guardarse:
            #clients.Clientes.validarDNI()
        except Exception as error:
            print('Error en módulo cargar articulo ', error)

    def bajaArt(self):
        try:
            codigo = var.ui.lblCodArt.text()
            nombre = var.ui.txtNombreArticulo.text()
            conexion.Conexion.bajaArt(codigo,nombre)
            conexion.Conexion.cargaTabArt(self)
        except Exception as error:
            print('Error al dar de baja articulo ', error)

    def modifArt(self):
        try:
            if(Articulos.validarPrecio(self)):
                artMoneda = locale.currency(float(var.ui.txtPrecioArticulo.text()))
                artMoneda.replace(',', '.')
                articulo = [var.ui.lblCodArt.text(), var.ui.txtNombreArticulo.text(), artMoneda]
                conexion.Conexion.modifArticulo(articulo)
                conexion.Conexion.cargaTabArt(self)
        except Exception as error:
            print('Error al modificar articulo ', error)

    def validarPrecio(self):
        res=False
        try:
            precio = float(var.ui.txtPrecioArticulo.text())
            #truncado = (math.trunc(precio * 100) / 100)
            truncado=round(precio, 2)
            formatPrecio = str(truncado)
            if formatPrecio[-2]=='.':
                formatPrecio += '0'
            var.ui.txtPrecioArticulo.setText(formatPrecio)
            res=True


        except Exception as error:
            print('Error en validar precio articulo ',error)
            try:
                msgBox = QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                msgBox.setText("El precio introducido no es válido.")
                msgBox.setWindowTitle("ERROR")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
            except Exception as error:
                print('Error en mensaje articulo no modificado ', error)
        return res

    def formatoPrecio():
        try:
            precio = float(var.ui.txtPrecioArticulo.text())
            # truncado = (math.trunc(precio * 100) / 100)
            truncado = round(precio, 2)
            truncado= str('{:.2f}'.format(round(precio,2)))
            # formatPrecio = str(truncado)
            # if formatPrecio[-2]=='.':
            #     formatPrecio += '0'
            # var.ui.txtPrecioArticulo.setText(formatPrecio)
            # if (formatPrecio == str(precio)):
            #     pass
            # else:
            var.ui.txtPrecioArticulo.setText(truncado)

            #res = True
        except Exception as error:
            print('Error en validar precio articulo ', error)
            try:
                msgBox = QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                msgBox.setText("El precio introducido no es válido.")
                msgBox.setWindowTitle("ERROR")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
            except Exception as error:
                print('Error en mensaje articulo no modificado ', error)

    def buscaArticulo(self):
        try:
            busqueda=conexion.Conexion.buscaArt(var.ui.txtNombreArticulo.text())
            if (len(busqueda)>0):
                var.ui.lblCodArt.setText(str(busqueda[0]))
                var.ui.txtPrecioArticulo.setText(busqueda[1])
                conexion.Conexion.cargaTabBuscaArt(busqueda[0])
            else:
                try:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                    msgBox.setText("No se ha encontrado el artículo "+var.ui.txtNombreArticulo.text())
                    msgBox.setWindowTitle("Articulo no encontrado")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()
                except Exception as error:
                    print('Error en mensaje articulo no modificado ', error)

        except Exception as error:
            print('Error al buscar artículo (articulos) ',error)

    def formatoMayus():
        try:
            if len(var.ui.txtNombreArticulo.text())>0:
                var.ui.txtNombreArticulo.setText(var.ui.txtNombreArticulo.text().title())

        except Exception as error:
            print('Error al aplicar formato de texto en articulo ',error)

    def limpiaFormArt(self):
        try:
            var.ui.lblCodArt.setText('Auto')
            var.ui.txtNombreArticulo.setText('')
            var.ui.txtPrecioArticulo.setText('')
            conexion.Conexion.cargaTabArt(self)
        except Exception as error:
            print('Error en módulo limpiar formulario ',error)
