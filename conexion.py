from PyQt5 import QtSql, QtWidgets
from PyQt5.QtWidgets import *
from datetime import *
import xlwt
import conexion
import var


class Conexion():
    def db_connect(filename):
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName(filename)
            if not db.open():
                QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos. \nHaz click para continuar.',
                                               QtWidgets.QMessageBox.Cancel)
                return False
            else:
                print('Conexión establecida')
                return True
        except Exception as error:
            print('Problemas al establecer conexion con base de datos: ', error)

    '''
    Modulos gestión base de datos cliente
    '''

    def altaCli(newCli):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'insert into clientes (dni, alta, apellidos, nombre, direccion, provincia, municipio, sexo, pago, envio)'
                'values (:dni, :alta, :apellidos, :nombre, :direccion, :provincia, :municipio, :sexo, :pago, :envio)')
            query.bindValue(':dni', str(newCli[0]))
            query.bindValue(':apellidos', str(newCli[2]))
            query.bindValue(':alta', str(newCli[1]))
            query.bindValue(':nombre', str(newCli[3]))
            query.bindValue(':direccion', str(newCli[4]))
            query.bindValue(':provincia', str(newCli[5]))
            query.bindValue(':municipio', str(newCli[6]))
            query.bindValue(':sexo', str(newCli[7]))
            query.bindValue(':pago', str(newCli[8]))
            query.bindValue(':envio', str(newCli[9]))

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
            print('Error al guardar cliente: ', error)

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
                    index += 1
        except Exception as error:
            print('Error al cargar tabla clientes ', error)

    def bajaCli(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('DELETE FROM clientes WHERE dni =:dni')
            query.bindValue(':dni', str(dni))
            if query.exec_():
                try:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Information)
                    texto = str('Cliente con dni ' + str(dni) + ' dado de baja.')
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
            query.prepare(
                'SELECT municipio FROM municipios WHERE provincia_id = (SELECT id FROM provincias WHERE provincia =:prov)')
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
            query = QtSql.QSqlQuery()
            query.prepare(
                'SELECT alta, apellidos, nombre, direccion, provincia, municipio, sexo, pago, envio  FROM clientes WHERE dni =:dni')
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
                    datosCli.append(query.value(8))
        except Exception as error:
            print('Error en buscar cliente (conexión) ', error)
        return datosCli

    def modifCli(modCliente):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('UPDATE clientes SET alta=:alta, apellidos=:apellidos, nombre=:nombre, direccion=:direccion, '
                          'provincia=:provincia, municipio=:municipio, sexo=:sexo, pago=:pago, envio=:envio WHERE dni=:dni')
            query.bindValue(':dni', str(modCliente[0]))
            query.bindValue(':apellidos', str(modCliente[2]))
            query.bindValue(':alta', str(modCliente[1]))
            query.bindValue(':nombre', str(modCliente[3]))
            query.bindValue(':direccion', str(modCliente[4]))
            query.bindValue(':provincia', str(modCliente[5]))
            query.bindValue(':municipio', str(modCliente[6]))
            query.bindValue(':sexo', str(modCliente[7]))
            query.bindValue(':pago', str(modCliente[8]))
            query.bindValue(':envio', str(modCliente[9]))
            if query.exec_():
                try:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Information)
                    msgBox.setText("Cliente modificado correctamente")
                    msgBox.setWindowTitle("Operación completada")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()
                except Exception as error:
                    print('Error en mensaje cliente modificado ', error)
            else:
                print(query.lastError().text())
                try:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                    msgBox.setText("No se pudo modificar el cliente")
                    msgBox.setWindowTitle("ERROR")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()
                except Exception as error:
                    print('Error en mensaje cliente no modificado ', error)

        except Exception as error:
            print('Error al modificar cliente (conexion) ', error)

    def comprobarExisteCli(dni):
        respuesta=False
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'SELECT nombre  FROM clientes WHERE dni =:dni')
            query.bindValue(':dni', str(dni))
            if query.exec_():
                while query.next():
                    respuesta=True
        except Exception as error:
            print('Error en comprobar existe cliente ', error)
        return respuesta

    def clienteExcel(cliente):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'insert into clientes (dni, alta, apellidos, nombre, direccion, provincia, municipio, sexo, pago, envio)'
                'values (:dni, :alta, :apellidos, :nombre, :direccion, :provincia, :municipio, :sexo, :pago, :envio)')
            if conexion.Conexion.comprobarExisteCli(cliente[0]):
                query.prepare(
                    'UPDATE clientes SET alta=:alta, apellidos=:apellidos, nombre=:nombre, direccion=:direccion, '
                    'provincia=:provincia, municipio=:municipio, sexo=:sexo, pago=:pago, envio=:envio WHERE dni=:dni')
            query.bindValue(':dni', str(cliente[0]))
            query.bindValue(':apellidos', str(cliente[2]))
            query.bindValue(':alta', str(cliente[1]))
            if str(cliente[1]).__eq__(''):
                data = (datetime.today().strftime('%d/%m/%Y'))
                query.bindValue(':alta', str(data))
            query.bindValue(':nombre', str(cliente[3]))
            query.bindValue(':direccion', str(cliente[4]))
            query.bindValue(':provincia', str(cliente[5]))
            query.bindValue(':municipio', str(cliente[6]))
            query.bindValue(':sexo', str(cliente[7]))
            query.bindValue(':pago', str(cliente[8]))
            if len(cliente)>9:
                query.bindValue(':envio', str(cliente[9]))
            else:
                query.bindValue(':envio', str(0))

            if query.exec_():
                while query.next():
                    print('insertado')
        except Exception as error:
            print('Error en manejar cliente de excel ', error)

    def exportExcel(self):
        procesado = False
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = (str(fecha) + '_dataExport.xls')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Exportar datos', var.copia, '.xls',
                                                                options=option)
            wb = xlwt.Workbook()
            sheet1 = wb.add_sheet('Hoja 1')

            # Cabeceras
            sheet1.write(0, 0, 'DNI')
            sheet1.write(0, 1, 'ALTA')
            sheet1.write(0, 2, 'APELIDOS')
            sheet1.write(0, 3, 'NOME')
            sheet1.write(0, 4, 'DIRECCION')
            sheet1.write(0, 5, 'PROVINCIA')
            sheet1.write(0, 6, 'MUNICIPIO')
            sheet1.write(0, 7, 'SEXO')
            sheet1.write(0, 8, 'PAGO')
            sheet1.write(0, 9, 'ENVIO')
            f = 1
            query = QtSql.QSqlQuery()
            query.prepare('SELECT *  FROM clientes')
            if query.exec_():
                while query.next():
                    for c in range(10):
                        sheet1.write(f, c, query.value(c))
                    f+=1
            procesado=True
            wb.save(directorio)

        except Exception as error:
            print('Error en conexion para exportar excel ',error)
        return procesado
