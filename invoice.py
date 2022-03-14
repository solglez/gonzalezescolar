'''
GESTIÓN DE LA FACTURACIÓN
'''
from PyQt5 import QtCore, QtWidgets
import locale
locale.setlocale(locale.LC_ALL,'es-ES')
import conexion
import invoice
import var
class Facturas():
    def buscaCli(self):
        """

        Método que carga los datos de cliente en la interfaz de facturación tomando su dni desde la información de
        la factura y consultando Conexion.buscaCliFac.

        """
        try:
            dni=var.ui.txtDniFac.text().upper()
            var.ui.txtDniFac.setText(dni)
            registro=conexion.Conexion.buscaCliFac(dni)
            nombre=registro[0]+', '+registro[1]
            var.ui.lblNomFac.setText(nombre)
            #conexion.Conexion.cargarFacturasCli(dni)
        except Exception as error:
            print('Error en buscar cliente de facturas ',error)

    def cargaCliFacs(self):
        try:
            dni=var.ui.txtDniFac.text().upper()
            var.ui.txtDniFac.setText(dni)
            registro=conexion.Conexion.buscaCliFac(dni)
            nombre=registro[0]+', '+registro[1]
            var.ui.lblNomFac.setText(nombre)
            conexion.Conexion.cargarFacturasCli(dni)
        except Exception as error:
            print('Error en buscar cliente de facturas ',error)

    def altaFac(self):
        """

        Método que lanza el proceso de guardar una nueva factura y actualiza la interfaz.
        Llama a Conexion.altaFac, cargaTabFac y buscaCodFac.

        """
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
        """

        Método que consulta los datos de una factura seleccionada en tabla con Conexion.buscaDatosFac
        y rellena sus respectivos campos en la interfaz.
        Tambien carga sus lineas de venta con Conexion.cargarLineasVenta.

        """
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

            var.ui.lblDescuento.setText('0')
            var.ui.txtDescuento.setText('0')
        except Exception as error:
            print('Error en módulo cargar factura (invoice) ',error)


    def limpiaFormFac(self):
        """

        Método que vacía el formulario de la interfaz de facturación para poder realizar otros procesos.

        """
        try:
            cajas = [var.ui.txtDniFac, var.ui.lblNomFac, var.ui.lblCodFac, var.ui.txtFechaFac]
            for i in cajas:
                i.setText('')
            Facturas.vaciarTabVentas()
            var.ui.lblCodFac_4.setText('')
            var.ui.lblCodFac_4.setStyleSheet('QLabel{color:black;}')
            conexion.Conexion.cargaTabFac()
        except Exception as error:
            print('Error en módulo limpiar formulario ',error)

    def cargarLineaVenta(self):
        """

        Método que genera una nueva linea de venta vacía en la primera linea de la tabla de ventas.
        Carga en el combobox todos los productos con Conexion.cargarCmbProducto.

        """
        try:
            index=0
            var.cmbProducto.setFixedSize(150,25)
            # Hay que cargar el combo
            conexion.Conexion.cargarCmbProducto(self)
            var.txtCantidad.setFixedSize(60,25)
            var.txtCantidad.setAlignment(QtCore.Qt.AlignCenter)
            var.ui.tabVentas.setRowCount(index+1)
            var.ui.tabVentas.setCellWidget(index,1,var.cmbProducto)
            var.ui.tabVentas.setCellWidget(index, 3, var.txtCantidad)
        except Exception as error:
            print('Error al cargar linea de venta ',error)

    #Esto es una prueba, pero hay problemas con el self
    '''
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
            
    '''
    #Comprobar codigo:
    def procesoVenta(self):
        """

        Método que guarda todos los datos de la linea de venta al procesarla.

        """
        try:
            row = var.ui.tabVentas.currentRow()
            articulo = var.cmbProducto.currentText()
            if (articulo!=''):
                dato = conexion.Conexion.obtenerCodPrecio(articulo)
                var.codpro=dato[0]
                var.ui.tabVentas.setItem(row, 2, QtWidgets.QTableWidgetItem(str(dato[1])))
                var.ui.tabVentas.item(row, 2).setTextAlignment(QtCore.Qt.AlignCenter)
                #Adecuamos el campo de precio para pasarlo a float y operar con el
                var.precio = dato[1].replace('€','')
                var.precio=var.precio.replace(',','.')
                var.precio = var.precio.replace(' ', '')
            else:
                var.ui.tabVentas.setItem(row, 2, QtWidgets.QTableWidgetItem(''))

        except Exception as error:
            print('error en procesoVenta en invoice', error)

    def totalLineaVenta(self=None):
        """

        Método que calcula el total de una linea de venta y llama a Conexion.cargarVenta para guardarla en la base de
        datos. También actualiza la interfaz en consecuencia.

        """
        try:
            row = var.ui.tabVentas.currentRow()
            cantidad=round(float(var.txtCantidad.text().replace(',', '.')), 2)
            total_linea = round(float(var.precio)*float(cantidad),2)
            var.ui.tabVentas.setItem(row, 4, QtWidgets.QTableWidgetItem(str('{:.2f}'.format(total_linea))+'€'))
            var.ui.tabVentas.item(row, 4).setTextAlignment(QtCore.Qt.AlignRight)
            venta=[]
            codfac=var.ui.lblCodFac.text()
            venta.append(int(codfac))
            venta.append(int(var.codpro))
            venta.append(float(var.precio))
            venta.append(float(cantidad))
            conexion.Conexion.cargarVenta(venta)
            conexion.Conexion.cargaTabArtSinSelf()

            if var.ui.lblCodFac_4.text() == 'Venta Realizada':
                Facturas.vaciarTabVentas()
                conexion.Conexion.cargarLineasVenta(str(var.ui.lblCodFac.text()))

        except Exception as error:
            print('Error en total linea venta de invoice: ',error)

    def eliminarVenta(self):
        """

        Método que elimina una linea de venta de la bbdd apoyándose en Conexion.eliminarLineaVenta.

        """
        try:
            row = var.ui.tabVentas.selectedItems()
            codVenta=row[0].text()
            conexion.Conexion.eliminarLineaVenta(codVenta)
        except Exception as error:
            print('Error al eliminar venta: ',error)

    def vaciarTabVentas(self=None):
        """

        Método que vacía la tabla y los campos referentes a las lineas de venta en la interfaz para futuras operaciones.

        """
        try:
            var.ui.tabVentas.clearContents()
            var.cmbProducto = QtWidgets.QComboBox()
            var.txtCantidad = QtWidgets.QLineEdit()
            var.txtCantidad.editingFinished.connect(invoice.Facturas.totalLineaVenta)
            var.cmbProducto.currentIndexChanged.connect(invoice.Facturas.procesoVenta)
            invoice.Facturas.cargarLineaVenta(self)
            var.ui.lblSubtotal.setText('')
            var.ui.lblIva.setText('')
            var.ui.lblTotal.setText('')
            var.ui.lblDescuento.setText('0')
            var.ui.txtDescuento.setText('0')
        except Exception as error:
            print('Error en vaciarTabVentas: ',error)

    def aplicarDescuento(self):
        try:
            descuento=var.ui.txtDescuento.text()
            if(descuento==''):
                descuento=0
                var.ui.txtDescuento.setText('0')
            else:
                try:
                    descuento = float(var.ui.txtDescuento.text())
                except Exception as error2:
                    var.ui.txtDescuento.setText('0')
                    print('Descuento incorrecto')
            subtotal=var.ui.lblSubtotal.text()
            subtotal=subtotal.replace(',', '.')
            subtotal = subtotal[:(len(subtotal) - 2)]
            subtotal=float(subtotal)
            totalDescuento=subtotal*(descuento/100)
            iva=(subtotal-totalDescuento)*0.21
            total=subtotal-totalDescuento+iva

            var.ui.lblDescuento.setText(str('{:.2f}'.format(round(totalDescuento, 2))) + '€')
            var.ui.lblIva.setText(str('{:.2f}'.format(round(iva, 2))) + '€')
            var.ui.lblTotal.setText(str('{:.2f}'.format(round(total, 2))) + '€')

        except Exception as error:
            print('Error al aplicar descuento ', error)
