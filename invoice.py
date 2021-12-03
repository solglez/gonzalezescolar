'''
GESTIÓN DE LA FACTURACIÓN
'''
import conexion
import var
class Facturas():
    def buscaCli(self):
        try:
            dni=var.ui.txtDniFac.text().upper()
            var.ui.txtDniFac.setText(dni)
            registro=conexion.Conexion.buscaCliFac(dni)
            nombre=registro[0]+', '+registro[1]
            var.ui.txtClienteFac.setText(nombre)
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
        except Exception as error:
            print('Error en módulo alta factura ',error)