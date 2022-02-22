import unittest
import clients,conexion,var
from PyQt5 import QtSql, QtWidgets, QtGui, QtCore

class MyTestCase(unittest.TestCase):

    def test_conexion(self):
        value=conexion.Conexion.db_connect(var.filedb)
        msg='Conexión no válida'
        self.assertTrue(value,msg)

    def test_dni(self):
        dni='00000000T'
        value=clients.Clientes.validarDNI(dni)
        msg='Error dni'
        self.assertTrue(value,msg)

    def test_factura(self):
        valor=85.38
        codfac=12
        suma=0
        try:
            msg='Cálculos erroneos'
            query =QtSql.QSqlQuery()
            query.prepare('select codven, codprof, cantidad, precio from ventas where codfacf = :codfac')
            query.bindValue(':codfac', int(codfac))
            if query.exec_():
                while query.next():
                    codventa = query.value(0)
                    producto = conexion.Conexion.nombreDeArticulo(query.value(1))
                    cantidad = query.value(2)
                    precio = query.value(3)
                    total_linea = round(float(precio) * float(cantidad), 2)
                    suma = suma + total_linea
            iva = suma * 0.21
            total = suma + iva

        except Exception as error:
            print('Error test de factura ',error)
        self.assertEqual(round(float(valor),2), round(float(total),2),msg)

if __name__ == '__main__':
    unittest.main()
