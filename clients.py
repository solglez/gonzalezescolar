'''
Funciones gestión clientes
'''
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

    def cargaProv(self):
        try:
            var.ui.cmbProv.clear()
            prov=['','A Coruña','Lugo','Ourense','Pontevedra','Vigo']
            for i in prov:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Error en módulos al cargar provinvia, ',error)

    def selProv(prov):
        try:
            print('Has seleccionado la provincia de ',prov)
            return prov
        except Exception as error:
            print('Error en módulos de seleccionar provincia, ',error)

    def cargaMun(self):
        try:
            var.ui.cmbMun.clear()
            mun=['','Cangas do Morrazo','Moaña','Vigo']
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
            var.ui.txtAltaCli.setText(str(data))
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
            #Preparamos el registro
            newCli=[]
            client=[ var.ui.txtApel, var.ui.txtNome, var.ui.txtAltaCli]
            for i in client:
                newCli.append(i.text())
            #Cargamos en la tabla
            row = 0
            column = 0
            var.ui.tabClientes.insertRow(row)
            for campo in newCli:
                cell=QtWidgets.QTableWidgetItem(campo)
                var.ui.tabClientes.setItem(row, column,cell)
                column+=1

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
            var.ui.txtDNI.setStyleSheet('')
        except Exception as error:
            print('Error en módulo limpiar formulario ',error)