'''
Funciones gestión clientes
'''
from PyQt5 import QtSql
import clients
import conexion
import events
import invoice
from prueba import *
import var

class Clientes():
    def validarDNI():
        try:
            var.ui.txtDNI.setText(var.ui.txtDNI.text().upper()) #asegurar letra en mayúsculas
            dni = var.ui.txtDNI.text()
            tabla='TRWAGMYFPDXBNJZSQVHLCKE' #letras dni
            dig_ext='XYZ' #dígito de extranjero
            reemp_dig_ext={'X':'0', 'Y':'1', 'Z':'2'} #reemplazar el dígito extranjero
            numeros='1234567890'
            #dni=dni.upper() #asegurar letra en mayúsculas
            if len(dni)==9:
                dig_control=dni[8]
                dni=dni[:8]
                if dni[0] in dig_ext:
                    dni=dni.replace(dni[0],reemp_dig_ext[dni[0]])
                if len(dni)==len([n for n in dni if n in numeros]) and tabla[int(dni)%23]==dig_control:
                    var.ui.txtDNI.setStyleSheet('QLineEdit{background - color: rgb(255, 255, 255);}')
                    var.ui.lblValidoDNI.setStyleSheet('QLabel{color:green;}')
                    var.ui.lblValidoDNI.setText(' V')
                    var.ui.txtDNI.setStyleSheet('')
                else:
                    var.ui.txtDNI.setStyleSheet('QLineEdit{background-color:pink;}')
                    var.ui.lblValidoDNI.setStyleSheet('QLabel{color:red;}')
                    var.ui.lblValidoDNI.setText(' X')
            else:
                var.ui.txtDNI.setStyleSheet('QLineEdit{background-color:pink;}')
                var.ui.lblValidoDNI.setStyleSheet('QLabel{color:red;}')
                var.ui.lblValidoDNI.setText(' X')
        except Exception as error:
            print('Error en módilo validar DNI: ', error)
    '''
    def SelSexo(self):
        try:
            if var.ui.rbtFem.isChecked():
                print('Marcado femenino.')
            if var.ui.rbtHom.isChecked():
                print('Marcado masculino.')
        except Exception as error:
            print('Error en módulo seleccionar sexo: ',error)

    def SelPago(self):
        try:
            if var.ui.chkEfectivo.isChecked():
                print('Has seleccionado efectivo')
            if var.ui.chkTarjeta.isChecked():
                print('Has seleccionado tarjeta.')
            if var.ui.chkCargoCuenta.isChecked():
                print('Has seleccionado cargo en la cuenta.')
            if var.ui.chkTransfe.isChecked():
                print('Has seleccionado transferencia.')
        except Exception as error:
            print('Error en módulo seleccionar forma de pago: ',error)
    '''
    def cargaProv(self):
        try:
            var.ui.cmbProv.clear()
            prov=conexion.Conexion.listaProvincias(self)
            for i in prov:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Error en módulos al cargar provinvia, ',error)
    '''
    def selProv(prov):
        try:
            print('Has seleccionado la provincia de ',prov)
            return prov
        except Exception as error:
            print('Error en módulos de seleccionar provincia, ',error)
    '''
    def cargaMun(self):
        try:
            var.ui.cmbMun.clear()
            prov=var.ui.cmbProv.currentText()
            mun=conexion.Conexion.listaMunicipios(prov)
            for i in mun:
                var.ui.cmbMun.addItem(i)
        except Exception as error:
            print('Error en módulo de cargar municipio, ',error)

    def selMun(mun):
        try:
            print('Has seleccionado el municipio de ',mun)
            return mun
        except Exception as error:
            print('Error en módulo de seleccionar municipio, ',error)

    def cargarFecha(qDate):
        try:
            #qDate pondría por orden año, mes y día. Usamos format para variar el orden y darle formato.
            data=('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            if var.ui.tabPrograma.currentIndex()==0:
                var.ui.txtAltaCli.setText(str(data))
            elif var.ui.tabPrograma.currentIndex()==1:
                var.ui.txtFechaFac.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error en módulo de cargar fecha ', error)

    def formatoMayus():
        try:
            if len(var.ui.txtNome.text())>0:
                var.ui.txtNome.setText(var.ui.txtNome.text().title())
            if len(var.ui.txtApel.text()) > 0:
                var.ui.txtApel.setText(var.ui.txtApel.text().title())
            if len(var.ui.txtDir.text()) > 0:
                var.ui.txtDir.setText(var.ui.txtDir.text().title())
        except Exception as error:
            print('Error al aplicar formato de texto ',error)

    def guardaCli(self):
        try:
            if(var.ui.lblValidoDNI.text()==' V'):
                #Preparamos el registro
                # Para la base de datos
                newCli=[]
                cliente=[var.ui.txtDNI, var.ui.txtAltaCli, var.ui.txtApel, var.ui.txtNome, var.ui.txtDir]
                # Para representación en tableView
                #tabcli= []
                #client= [var.ui.txtDNI, var.ui.txtApel, var.ui.txtNome, var.ui.txtAltaCli]
                pagos = []
                #Código para cargar en tabla

                for i in cliente:
                    newCli.append(i.text())
                #for i in client:
                    #tabcli.append(i.text())
                newCli.append(var.ui.cmbProv.currentText())
                newCli.append(var.ui.cmbMun.currentText())
                if var.ui.rbtFem.isChecked():
                    newCli.append('Mujer')
                elif var.ui.rbtHom.isChecked():
                    newCli.append('Hombre')
                if var.ui.chkCargoCuenta.isChecked():
                    pagos.append('Cargo Cuenta')
                if var.ui.chkTransfe.isChecked():
                    pagos.append('Transferencia')
                if var.ui.chkTarjeta.isChecked():
                    pagos.append('Tarjeta')
                if var.ui.chkEfectivo.isChecked():
                    pagos.append('Efectivo')
                pagos = set(pagos)
                newCli.append(', '.join(pagos))
                newCli.append(var.ui.spinEnvio.value())
                '''
                tabcli.append(', '.join(pagos))
                row = 0
                column = 0
                var.ui.tabClientes.insertRow(row)               
                for campo in tabcli:
                    cell=QtWidgets.QTableWidgetItem(str(campo))
                    var.ui.tabClientes.setItem(row, column,cell)
                    column+=1
                
                '''
                #Codigo para grabar en base de datos
                conexion.Conexion.altaCli(newCli)
                conexion.Conexion.cargaTabCli(self)
            else:
                #Mensaje de error
                events.Eventos.errorDNI(self)
        except Exception as error:
            print('Error en módulo guardar cliente ', error)

    def limpiaFormCli(self):
        try:
            cajas = [var.ui.txtApel, var.ui.txtNome, var.ui.txtAltaCli, var.ui.txtDNI, var.ui.txtDir]
            for i in cajas:
                i.setText('')
            var.ui.chkTarjeta.setChecked(False)
            var.ui.chkEfectivo.setChecked(False)
            var.ui.chkTransfe.setChecked(False)
            var.ui.chkCargoCuenta.setChecked(False)
            var.ui.rbtGroupSex.setExclusive(False)
            var.ui.rbtHom.setChecked(False)
            var.ui.rbtFem.setChecked(False)
            var.ui.rbtGroupSex.setExclusive(True)
            var.ui.cmbProv.setCurrentIndex(0)
            var.ui.cmbMun.setCurrentIndex(0)
            var.ui.lblValidoDNI.setStyleSheet('')
            var.ui.lblValidoDNI.setText('')
            var.ui.txtDNI.setStyleSheet('QLineEdit{background - color: rgb(255, 255, 255);}')
            var.ui.spinEnvio.setValue(0)
        except Exception as error:
            print('Error en módulo limpiar formulario ',error)

    def cargaCli(self):
        '''
        Carga los datos del cliente al seleccionar en tabla
        :return:
        '''
        try:
            fila=var.ui.tabClientes.selectedItems()
            datos=[var.ui.txtDNI, var.ui.txtApel, var.ui.txtNome, var.ui.txtAltaCli]
            if fila:
                row=[dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])
            pagos=row[4]
            #Primero limpiamos los checks y luego refrescamos:
            var.ui.chkTarjeta.setChecked(False)
            var.ui.chkEfectivo.setChecked(False)
            var.ui.chkTransfe.setChecked(False)
            var.ui.chkCargoCuenta.setChecked(False)

            if 'Tarjeta' in pagos:
                var.ui.chkTarjeta.setChecked(True)
            if 'Efectivo' in pagos:
                var.ui.chkEfectivo.setChecked(True)
            if 'Transferencia' in pagos:
                var.ui.chkTransfe.setChecked(True)
            if 'Cargo Cuenta' in pagos:
                var.ui.chkCargoCuenta.setChecked(True)
            #Ahora los datos desde la base de datos:
            query = QtSql.QSqlQuery()
            orden=('SELECT direccion, provincia, municipio, sexo, envio FROM clientes WHERE dni="'+var.ui.txtDNI.text()+'"')
            query.prepare(orden)
            if query.exec_():
                while query.next():
                    var.ui.txtDir.setText(query.value(0))
                    index = var.ui.cmbProv.findText(query.value(1), QtCore.Qt.MatchFixedString)
                    var.ui.cmbProv.setCurrentIndex(index)
                    indexM = var.ui.cmbMun.findText(query.value(2), QtCore.Qt.MatchFixedString)
                    var.ui.cmbMun.setCurrentIndex(indexM)
                    if (query.value(3)=='Mujer'):
                        var.ui.rbtFem.setChecked(True)
                        var.ui.rbtHom.setChecked(False)
                    elif (query.value(3)=='Hombre'):
                        var.ui.rbtFem.setChecked(False)
                        var.ui.rbtHom.setChecked(True)
                    try:
                        var.ui.spinEnvio.setValue(query.value(4))
                    except:
                        var.ui.spinEnvio.setValue(0)

            #Para que aparezca el DNI como válido en caso de querer guardarse:
            clients.Clientes.validarDNI()
            #Lo cargamos en la ventana de facturación
            var.ui.txtDniFac.setText(var.ui.txtDNI.text())
            invoice.Facturas.buscaCli(self)
        except Exception as error:
            print('Error en módulo cargar cliente ',error)

    def bajaCli(self):
        try:
            dni=var.ui.txtDNI.text()
            conexion.Conexion.bajaCli(dni)
            conexion.Conexion.cargaTabCli(self)
        except Exception as error:
            print('Error al dar de baja cliente ', error)

    def modifCli(self):
        try:
            modcliente=[]
            cliente=[var.ui.txtDNI, var.ui.txtAltaCli, var.ui.txtApel, var.ui.txtNome, var.ui.txtDir]
            for i in cliente:
                modcliente.append(i.text())
            modcliente.append(var.ui.cmbProv.currentText())
            modcliente.append(var.ui.cmbMun.currentText())
            if var.ui.rbtFem.isChecked():
                modcliente.append('Mujer')
            elif var.ui.rbtHom.isChecked():
                modcliente.append('Hombre')
            pagos=[]
            if var.ui.chkCargoCuenta.isChecked():
                pagos.append('Cargo Cuenta')
            if var.ui.chkTransfe.isChecked():
                pagos.append('Transferencia')
            if var.ui.chkTarjeta.isChecked():
                pagos.append('Tarjeta')
            if var.ui.chkEfectivo.isChecked():
                pagos.append('Efectivo')
            pagos = set(pagos)
            modcliente.append(', '.join(pagos))
            modcliente.append(var.ui.spinEnvio.value())
            conexion.Conexion.modifCli(modcliente)
            conexion.Conexion.cargaTabCli(self)
        except Exception as error:
            print('Error al modificar cliente ',error)
    '''
    def buscaCli(self):
        try:
            dni=var.ui.txtDNI.text()
            datos=conexion.Conexion.selecCliente(dni)
            print(datos)
            var.ui.txtDir.setText(datos[3])
            var.ui.txtNome.setText(datos[2])
            var.ui.txtApel.setText(datos[1])
            var.ui.txtAltaCli.setText(datos[0])
            pagos = datos[7]
            # Primero limpiamos los checks y luego refrescamos:
            var.ui.chkTarjeta.setChecked(False)
            var.ui.chkEfectivo.setChecked(False)
            var.ui.chkTransfe.setChecked(False)
            var.ui.chkCargoCuenta.setChecked(False)
            if 'Tarjeta' in pagos:
                var.ui.chkTarjeta.setChecked(True)
            if 'Efectivo' in pagos:
                var.ui.chkEfectivo.setChecked(True)
            if 'Transferencia' in pagos:
                var.ui.chkTransfe.setChecked(True)
            if 'Cargo Cuenta' in pagos:
                var.ui.chkCargoCuenta.setChecked(True)
            if (datos[6] == 'Mujer'):
                var.ui.rbtFem.setChecked(True)
                var.ui.rbtHom.setChecked(False)
            elif (datos[6] == 'Hombre'):
                var.ui.rbtFem.setChecked(False)
                var.ui.rbtHom.setChecked(True)

            #Falta provincia y actualizar la tabla
        except Exception as error:
            print('Error al buscar cliente ', error)
    '''
