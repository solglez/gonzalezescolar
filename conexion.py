from PyQt5 import QtSql, QtWidgets, QtGui, QtCore
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

    def cargaTabArt(self):
        try:
            index = 0
            var.ui.tabArticulos.setRowCount(index)
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, nombre, precio from articulos order by codigo')
            if query.exec_():
                while query.next():
                    codigo = query.value(0)
                    nombre = query.value(1)
                    precio = query.value(2)
                    # Creamos la fila y cargamos datos
                    var.ui.tabArticulos.setRowCount(index + 1)
                    var.ui.tabArticulos.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codigo)))
                    var.ui.tabArticulos.setItem(index, 1, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabArticulos.setItem(index, 2, QtWidgets.QTableWidgetItem(precio))
                    index += 1
        except Exception as error:
            print('Error al cargar tabla articulos ', error)

    def modifArticulo(modArt):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('UPDATE articulos SET nombre=:nombre, precio=:precio WHERE codigo=:codigo')
            query.bindValue(':codigo', str(modArt[0]))
            query.bindValue(':nombre', str(modArt[1]))
            query.bindValue(':precio', str(modArt[2]))
            if query.exec_():
                try:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Information)
                    msgBox.setText("Artículo modificado correctamente")
                    msgBox.setWindowTitle("Operación completada")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()
                except Exception as error:
                    print('Error en mensaje articulo modificado ', error)
            else:
                print(query.lastError().text())
                try:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                    msgBox.setText("No se pudo modificar el articulo")
                    msgBox.setWindowTitle("ERROR")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()
                except Exception as error:
                    print('Error en mensaje articulo no modificado ', error)

        except Exception as error:
            print('Error al modificar articulo (conexion) ', error)

    def selecArticulo(codigo):
        datosArt = []
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'SELECT nombre, precio  FROM articulos WHERE codigo =:codigo')
            query.bindValue(':codigo', str(codigo))
            if query.exec_():
                while query.next():
                    datosArt.append(query.value(0))
                    datosArt.append(query.value(1))

        except Exception as error:
            print('Error en buscar articulo (conexión) ', error)
        return datosArt

    def bajaArt(codigo,nombre):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('DELETE FROM articulos WHERE codigo =:codigo')
            query.bindValue(':codigo', str(codigo))
            if query.exec_():
                try:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Information)
                    texto = str('Artículo ' + str(nombre) + ' dado de baja.')
                    msgBox.setText(texto)
                    msgBox.setWindowTitle("Aviso")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()
                except Exception as error:
                    print('Error en mensaje articulo eliminado ', error)
        except Exception as error:
            print('Error en baja articulo (conexión) ', error)

    def altaArt(newArt):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'insert into articulos (nombre, precio) values (:nombre, :precio)')
            query.bindValue(':nombre', str(newArt[0]))
            query.bindValue(':precio', str(newArt[1]))

            if query.exec_():
                try:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Information)
                    msgBox.setText("Artículo guardado correctamente")
                    msgBox.setWindowTitle("Operación completada")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()
                except Exception as error:
                    print('Error en mensaje articulo guardado ', error)
            else:
                print(query.lastError().text())
                try:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                    msgBox.setText("No se pudo guardar el articulo")
                    msgBox.setWindowTitle("ERROR")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()
                except Exception as error:
                    print('Error en mensaje articulo guardado ', error)
        except Exception as error:
            print('Error al guardar articulo: ', error)

    def buscaArt(nombre):
        datosArt = []
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'SELECT codigo, precio  FROM articulos WHERE nombre =:nombre')
            query.bindValue(':nombre', str(nombre))
            if query.exec_():
                while query.next():
                    datosArt.append(query.value(0))
                    datosArt.append(query.value(1))

        except Exception as error:
            print('Error en buscar articulo por nombre (conexión) ', error)
        return datosArt

    def cargaTabBuscaArt(codigo):
        try:
            index = 0
            var.ui.tabArticulos.setRowCount(index)
            query = QtSql.QSqlQuery()
            query.prepare('select nombre, precio from articulos WHERE codigo =:codigo')
            query.bindValue(':codigo', str(codigo))
            if query.exec_():
                while query.next():
                    nombre = query.value(0)
                    precio = query.value(1)
                    # Creamos la fila y cargamos datos
                    var.ui.tabArticulos.setRowCount(index + 1)
                    var.ui.tabArticulos.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codigo)))
                    var.ui.tabArticulos.setItem(index, 1, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabArticulos.setItem(index, 2, QtWidgets.QTableWidgetItem(precio))
                    index += 1
        except Exception as error:
            print('Error al cargar tabla articulos ', error)

    '''
    GESTIÓN DE FACTURAS
    '''
    def buscaCliFac(dni):
        try:
            cliente = []
            try:
                query = QtSql.QSqlQuery()
                query.prepare('SELECT apellidos, nombre  FROM clientes WHERE dni =:dni')
                query.bindValue(':dni', str(dni))
                if query.exec_():
                    while query.next():
                        cliente.append(query.value(0))
                        cliente.append(query.value(1))
            except Exception as error:
                print('Error en buscar articulo por nombre (conexión) ', error)
            return cliente
        except Exception as error:
            print('Error en buscar cliente factura, conexión: ',error)

    def altaFac(registro):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('INSERT INTO facturas (dni, fechafac) VALUES (:dni, :fecha) ')
            query.bindValue(':dni', registro[0])
            query.bindValue(':fecha', registro[1])
            if query.exec_():
                try:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Information)
                    msgBox.setText("Se ha guardado la factura")
                    msgBox.setWindowTitle("Operación completada")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()
                except Exception as error:
                    print('Error en mensaje factura guardada ', error)
            else:
                print(query.lastError().text())
                try:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                    msgBox.setText("No se pudo guardar la factura")
                    msgBox.setWindowTitle("ERROR")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec()
                except Exception as error:
                    print('Error en mensaje factura guardada ', error)
        except Exception as error:
            print('Error en conexión alta factura ',error)

    def cargaTabFac():
        try:
            index = 0
            var.ui.tabArticulos.setRowCount(index)
            query = QtSql.QSqlQuery()
            query.prepare('select codfac, fechafac from facturas order by fechafac DESC')
            if query.exec_():
                while query.next():
                    codigo = query.value(0)
                    fecha = query.value(1)

                    var.btnfacdel = QtWidgets.QPushButton()
                    var.btnfacdel.setFixedSize(24, 24)
                    icopapelera = QtGui.QPixmap("img/papelera.png")
                    var.btnfacdel.setIcon(QtGui.QIcon(icopapelera))


                    # Creamos la fila y cargamos datos
                    var.ui.tabFacturas.setRowCount(index + 1)
                    var.ui.tabFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codigo)))
                    var.ui.tabFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(fecha))


                    cell_widget = QtWidgets.QWidget()
                    lay_out = QtWidgets.QHBoxLayout(cell_widget)
                    lay_out.setContentsMargins(0,0,0,0)
                    lay_out.addWidget(var.btnfacdel)
                    var.btnfacdel.clicked.connect(Conexion.bajaFac)
                    lay_out.setAlignment(QtCore.Qt.AlignVCenter)
                    var.ui.tabFacturas.setCellWidget(index, 2, cell_widget)
                    var.ui.tabFacturas.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                    var.ui.tabFacturas.item(index, 1).setTextAlignment(QtCore.Qt.AlignCenter)

                    index += 1
        except Exception as error:
            print('Error al cargar tabla facturas ', error)

    def buscaDatosFac(codigo):
        datosFac = []
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'SELECT dni FROM facturas WHERE codfac =:codigo')
            query.bindValue(':codigo', str(codigo))
            if query.exec_():
                while query.next():
                    datosFac.append(query.value(0))


        except Exception as error:
            print('Error en buscar datos factura (conexión) ', error)
        return datosFac

    # --------- COMPROBAR ESTE CODIGO---
    def bajaFac():

        try:

            numfac = var.ui.lblCodFac.text()
            query = QtSql.QSqlQuery()
            query.prepare('delete from facturas where codfac = :codfac')
            query.bindValue(':codfac', int(numfac))
            if query.exec_():
                Conexion.cargaTabFac()
                msgBox = QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Information)
                msgBox.setText("La factura ha sido dada de baja")
                msgBox.setWindowTitle("Aviso")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()

        except Exception as error:
          print('Error en dar baja factura', error)

    #Revisar:
    def cargarCmbProducto(self):
        try:
            var.cmbProducto.clear()
            query = QtSql.QSqlQuery()
            var.cmbProducto.addItem('')
            query.prepare('select nombre from articulos order by nombre')
            if query.exec_():
                while query.next():
                    var.cmbProducto.addItem(str(query.value(0)))
        except Exception as error:
            print('Fallo en cargarCmbProducto en conexion', error)

    def obtenerCodPrecio(articulo):
        try:
            dato = []
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, precio from articulos where nombre = :nombre')
            query.bindValue(':nombre', articulo)
            if query.exec_():
                while query.next():
                    dato.append(int(query.value(0)))
                    dato.append(str(query.value(1)))
            return dato
        except Exception as error:
            print('Fallo en obtenerCodPrecio en conexion', error)

