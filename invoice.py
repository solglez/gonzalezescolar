'''
GESTIÓN DE LA FACTURACIÓN
'''
from PyQt5 import QtSql
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import locale
locale.setlocale(locale.LC_ALL,'es-ES')

import conexion
import invoice
import var
class Facturas():
    def buscaCli(self):
        try:
            dni=var.ui.txtDniFac.text().upper()
            var.ui.txtDniFac.setText(dni)
            registro=conexion.Conexion.buscaCliFac(dni)
            nombre=registro[0]+', '+registro[1]
            var.ui.lblNomFac.setText(nombre)
        except Exception as error:
            print('Error en buscar cliente de facturas ',error)

    def altaFac(self):
        try:
            registro=[]
            dni = var.ui.txtDniFac.text().upper()
            var.ui.txtDniFac.setText(dni)
            fechaFac=var.ui.txtFechaFac.text()
            registro.append(str(dni))
            registro.append(str(fechaFac))
            conexion.Conexion.altaFac(registro)
            conexion.Conexion.cargaTabFac()
            codFac=conexion.Conexion.buscaCodFac(self)
            var.ui.lblCodFac.setText(str(codFac))
        except Exception as error:
            print('Error en módulo alta factura ',error)

    def cargaFac(self):
        try:
            fila = var.ui.tabFacturas.selectedItems()
            datos = [var.ui.lblCodFac, var.ui.txtFechaFac]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])
            # Ahora los datos desde la base de datos (de momento solo dni):
            datos=conexion.Conexion.buscaDatosFac(var.ui.lblCodFac.text())
            var.ui.txtDniFac.setText(datos[0])
            invoice.Facturas.buscaCli(self)
            Facturas.cargarLineaVenta(self)
            conexion.Conexion.cargarLineasVenta(str(var.ui.lblCodFac.text()))
        except Exception as error:
            print('Error en módulo cargar factura (invoice) ',error)


    def limpiaFormFac(self):
        try:
            #var.ui.tabVentas.clearContents()
            #Facturas.cargarLineaVenta(self)
            cajas = [var.ui.txtDniFac, var.ui.lblNomFac, var.ui.lblCodFac, var.ui.txtFechaFac]
            for i in cajas:
                i.setText('')
        except Exception as error:
            print('Error en módulo limpiar formulario ',error)

    def cargarLineaVenta(self):
        try:
            index=0
            #var.cmbProducto=QtWidgets.QComboBox()
            var.cmbProducto.setFixedSize(150,25)
            # Hay que cargar el combo
            conexion.Conexion.cargarCmbProducto(self)
            #var.txtCantidad=QtWidgets.QLineEdit()
            var.txtCantidad.setFixedSize(60,25)
            var.txtCantidad.setAlignment(QtCore.Qt.AlignCenter)
            var.ui.tabVentas.setRowCount(index+1)
            var.ui.tabVentas.setCellWidget(index,1,var.cmbProducto)
            var.ui.tabVentas.setCellWidget(index, 3, var.txtCantidad)
        except Exception as error:
            print('Error al cargar linea de venta ',error)

    #Esto es una prueba, pero hay problemas con el self
    def cargarLineaVentaEnIndex(index):
        try:
            index=int(index)
            #var.cmbProducto=QtWidgets.QComboBox()
            var.cmbProducto.setFixedSize(150,25)
            # Hay que cargar el combo
            conexion.Conexion.cargarCmbProducto
            #var.txtCantidad=QtWidgets.QLineEdit()
            var.txtCantidad.setFixedSize(60,25)
            var.txtCantidad.setAlignment(QtCore.Qt.AlignCenter)
            var.ui.tabVentas.setRowCount(index+1)
            var.ui.tabVentas.setCellWidget(index,1,var.cmbProducto)
            var.ui.tabVentas.setCellWidget(index, 3, var.txtCantidad)
        except Exception as error:
            print('Error al cargar linea de venta ',error)


    #Comprobar codigo:
    def procesoVenta(self):
        try:
            row = var.ui.tabVentas.currentRow()
            articulo = var.cmbProducto.currentText()
            dato = conexion.Conexion.obtenerCodPrecio(articulo)
            var.codpro=dato[0]
            #print(dato)
            var.ui.tabVentas.setItem(row, 2, QtWidgets.QTableWidgetItem(str(dato[1])))
            var.ui.tabVentas.item(row, 2).setTextAlignment(QtCore.Qt.AlignCenter)
            #Adecuamos el campo de precio para pasarlo a float y operar con el
            var.precio = dato[1].replace('€','')
            var.precio=var.precio.replace(',','.')
            var.precio = var.precio.replace(' ', '')

            # cantidad=round(float(var.txtCantidad.text().replace(',', '.')), 2)
            # print('cantidad')
            # total_venta = float(precio) * float(cantidad)
            # total_venta = round(total_venta, 2)
            #total_linea=Facturas.totalLineaVenta(precio)
        except Exception as error:
            print('error en procesoVenta en invoice', error)

    def totalLineaVenta(self=None):
        try:
            row = var.ui.tabVentas.currentRow()
            cantidad=round(float(var.txtCantidad.text().replace(',', '.')), 2)
            total_linea = round(float(var.precio)*float(cantidad),2)
            var.ui.tabVentas.setItem(row, 4, QtWidgets.QTableWidgetItem(str(total_linea)+'€'))
            var.ui.tabVentas.item(row, 4).setTextAlignment(QtCore.Qt.AlignRight)
            venta=[]
            codfac=var.ui.lblCodFac.text()
            venta.append(int(codfac))
            venta.append(int(var.codpro))
            venta.append(float(var.precio))
            venta.append(float(cantidad))
            print(venta)
            conexion.Conexion.cargarVenta(venta)

            if var.ui.lblCodFac_4.text() == 'Venta Realizada':
                var.ui.tabVentas.clearContents()
                var.cmbProducto = QtWidgets.QComboBox()
                var.txtCantidad = QtWidgets.QLineEdit()
                var.txtCantidad.editingFinished.connect(invoice.Facturas.totalLineaVenta)
                var.cmbProducto.currentIndexChanged.connect(invoice.Facturas.procesoVenta)
                invoice.Facturas.cargarLineaVenta(self)
                conexion.Conexion.cargarLineasVenta(str(var.ui.lblCodFac.text()))

        except Exception as error:
            print('Error en total linea venta de invoice: ',error)


