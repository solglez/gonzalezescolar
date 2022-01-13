'''
GESTIÓN DE LA FACTURACIÓN
'''
from PyQt5 import QtSql
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

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
        except Exception as error:
            print('Error en módulo cargar factura (invoice) ',error)

    def limpiaFormFac(self):
        try:
            cajas = [var.ui.txtDniFac, var.ui.lblNomFac, var.ui.lblCodFac, var.ui.txtFechaFac]
            for i in cajas:
                i.setText('')
        except Exception as error:
            print('Error en módulo limpiar formulario ',error)

    def cargarLineaVenta(self):
        try:
            index=0
            var.cmbProducto=QtWidgets.QComboBox()
            var.cmbProducto.setFixedSize(150,25)
            # Hay que cargar el combo
            var.txtCantidad=QtWidgets.QLineEdit()
            var.txtCantidad.setFixedSize(60,25)
            var.txtCantidad.setAlignment(QtCore.Qt.AlignCenter)
            var.ui.tabVentas.setRowCount(index+1)
            var.ui.tabVentas.setCellWidget(index,1,var.cmbProducto)
            var.ui.tabVentas.setCellWidget(index, 3, var.txtCantidad)
        except Exception as error:
            print('Error al cargar linea de venta ',error)

