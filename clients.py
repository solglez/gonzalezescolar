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