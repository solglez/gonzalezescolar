from PyQt5 import QtSql, QtWidgets
from PyQt5.QtWidgets import *
import var
class Conexion():
    def db_connect(filename):
        try:
            db=QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName(filename)
            if not db.open():
                QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos. \nHaz click para continuar.',
                                               QtWidgets.QMessageBox.Cancel)
                return False
            else:
                print('Conexión establecida')
                return True
        except Exception as error:
            print('Problemas al establecer conexion con base de datos: ',error)
    '''
    Modulos gestión base de datos cliente
    '''
    def altaCli(newCli):
        try:
            query=QtSql.QSqlQuery()
            query.prepare('insert into clientes (dni, alta, apellidos, nombre, direccion, provincia, municipio, sexo, pago)'
                          'values (:dni, :alta, :apellidos, :nombre, :direccion, :provincia, :municipio, :sexo, :pago)')
            query.bindValue(':dni',str(newCli[0]))
            query.bindValue(':apellidos', str(newCli[2]))
            query.bindValue(':alta', str(newCli[1]))
            query.bindValue(':nombre', str(newCli[3]))
            query.bindValue(':direccion', str(newCli[4]))
            query.bindValue(':provincia', str(newCli[5]))
            query.bindValue(':municipio', str(newCli[6]))
            query.bindValue(':sexo', str(newCli[7]))
            query.bindValue(':pago', str(newCli[8]))

            if query.exec_():
                try:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Information)
                    msgBox.setText("Cliente guardado correctamente")
                    msgBox.setWindowTitle("Operación completada")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()
                except Exception as error:
                    print('Error en mensaje cliente guardado ', error)
            else:
                print(query.lastError().text())
                try:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                    msgBox.setText("No se pudo guardar el cliente")
                    msgBox.setWindowTitle("ERROR")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()
                except Exception as error:
                    print('Error en mensaje cliente guardado ', error)
        except Exception as error:
            print('Error al guardar cliente: ',error)

    def cargaTabCli(self):
        try:
            index = 0
            var.ui.tabClientes.setRowCount(index)
            query = QtSql.QSqlQuery()
            query.prepare('select dni, apellidos, nombre, alta, pago from clientes order by apellidos')
            if query.exec_():
                while query.next():
                    dni = query.value(0)
                    apellidos = query.value(1)
                    nombre = query.value(2)
                    alta = query.value(3)
                    pago = query.value(4)
                    # Creamos la fila y cargamos datos
                    var.ui.tabClientes.setRowCount(index + 1)
                    var.ui.tabClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(dni))
                    var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                    var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(alta))
                    var.ui.tabClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(pago))
                    index+=1
        except Exception as error:
            print('Error al cargar tabla clientes ', error)

    def bajaCli(dni):
        try:
            query=QtSql.QSqlQuery()
            query.prepare('DELETE FROM clientes WHERE dni =:dni')
            query.bindValue(':dni', str(dni))
            if query.exec_():
                try:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Information)
                    texto=str('Cliente con dni '+str(dni)+' dado de baja.')
                    msgBox.setText(texto)
                    msgBox.setWindowTitle("Aviso")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()
                except Exception as error:
                    print('Error en mensaje cliente eliminado ', error)
        except Exception as error:
            print('Error en baja cliente (conexión) ', error)

    def listaMunicipios(prov):
        municipios = []
        try:
            query = QtSql.QSqlQuery()
            query.prepare('SELECT municipio FROM municipios WHERE provincia_id = (SELECT id FROM provincias WHERE provincia =:prov)')
            query.bindValue(':prov', str(prov))
            if query.exec_():
                while query.next():
                    municipios.append(query.value(0))
        except Exception as error:
            print('Error en lista municipios (conexión) ', error)
        return municipios

    def listaProvincias(self):
        provincias = []
        try:
            query = QtSql.QSqlQuery()
            query.prepare('SELECT provincia FROM provincias')
            if query.exec_():
                while query.next():
                    provincias.append(query.value(0))
        except Exception as error:
            print('Error en lista municipios (conexión) ', error)
        return provincias

    def selecCliente(dni):
        datosCli = []
        try:
            query=QtSql.QSqlQuery()
            query.prepare('SELECT alta, apellidos, nombre, direccion, provincia, municipio, sexo, pago  FROM clientes WHERE dni =:dni')
            query.bindValue(':dni', str(dni))
            if query.exec_():
                while query.next():
                    datosCli.append(query.value(0))
                    datosCli.append(query.value(1))
                    datosCli.append(query.value(2))
                    datosCli.append(query.value(3))
                    datosCli.append(query.value(4))
                    datosCli.append(query.value(5))
                    datosCli.append(query.value(6))
                    datosCli.append(query.value(7))
        except Exception as error:
            print('Error en buscar cliente (conexión) ', error)
        return datosCli

