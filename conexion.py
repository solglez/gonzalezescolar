from PyQt5 import QtSql, QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from datetime import *
import xlwt
import conexion
import invoice
import var
import locale
locale.setlocale(locale.LC_ALL,'es-ES')


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
            var.ui.tabFacturas.clearContents()
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
            #Borramos primero las ventas que pueda tener asociadas la factura:
            query.prepare('delete from ventas where codfacf = :codfac')
            query.bindValue(':codfac', int(numfac))
            if query.exec_():
                pass
            #Eliminamos ahora la factura:
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
                invoice.Facturas.vaciarTabVentas()

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

    def cargarVenta(venta):
        try:
            query=QtSql.QSqlQuery()
            query.prepare('insert into ventas(codfacf, codprof, precio, cantidad) values (:codfac, :codpro, :precio, :cantidad)')
            query.bindValue(':codfac', int(venta[0]))
            query.bindValue(':codpro', int(venta[1]))
            query.bindValue(':precio', float(venta[2]))
            query.bindValue(':cantidad', float(venta[3]))
            if query.exec_():
                var.ui.lblCodFac_4.setText('Venta Realizada')
                var.ui.lblCodFac_4.setStyleSheet('QLabel{color:black;}')
            else:
                var.ui.lblCodFac_4.setText('Error en Venta')
                var.ui.lblCodFac_4.setStyleSheet('QLabel{color:red;}')

        except Exception as error:
            print("Erroe en cargar venta conex ",error)

    def buscaCodFac(self):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select codfac from facturas order by codfac desc limit 1')
            if query.exec_():
                while query.next():
                    dato=query.value(0)
            return dato
        except Exception as error:
            print('Error en buscaCodFac en conexión ',error)

    def nombreDeArticulo(codpro):
        try:
            nombre=''
            query = QtSql.QSqlQuery()
            query.prepare('select nombre from articulos where codigo = :codpro')
            query.bindValue(':codpro', int(codpro))
            if query.exec_():
                while query.next():
                    nombre=query.value(0)
            return nombre
        except Exception as error:
            print('Error al obtener nombre de articulo en conexión: ',error)

    def cargarLineasVenta(codfac):
        try:
            #var.ui.tabVentas.clearContents()
            index=1
            suma=0
            query=QtSql.QSqlQuery()
            query.prepare('select codven, codprof, cantidad, precio from ventas where codfacf = :codfac')
            query.bindValue(':codfac', int(codfac))
            if query.exec_():
                while query.next():
                    codventa = query.value(0)
                    producto= conexion.Conexion.nombreDeArticulo(query.value(1))
                    cantidad=query.value(2)
                    precio=query.value(3)
                    total_linea = round(float(precio) * float(cantidad), 2)
                    suma=suma+total_linea
                    var.ui.tabVentas.setRowCount(index + 1)
                    var.ui.tabVentas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codventa)))
                    var.ui.tabVentas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(producto)))
                    var.ui.tabVentas.setItem(index, 2, QtWidgets.QTableWidgetItem(str('{:.2f}'.format(precio))))
                    var.ui.tabVentas.setItem(index, 3, QtWidgets.QTableWidgetItem(str(cantidad)))
                    var.ui.tabVentas.setItem(index, 4, QtWidgets.QTableWidgetItem(str('{:.2f}'.format(total_linea))+'€'))
                    var.ui.tabVentas.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                    var.ui.tabVentas.item(index, 2).setTextAlignment(QtCore.Qt.AlignRight)
                    var.ui.tabVentas.item(index, 3).setTextAlignment(QtCore.Qt.AlignRight)
                    var.ui.tabVentas.item(index, 4).setTextAlignment(QtCore.Qt.AlignRight)
                    index = index + 1


            iva = suma * 0.21
            total = suma + iva
            #Damos formato a los totales
            var.ui.lblSubtotal.setText(str('{:.2f}'.format(round(suma,2))) + '€')
            var.ui.lblIva.setText(str('{:.2f}'.format(round(iva, 2))) + '€')
            var.ui.lblTotal.setText(str('{:.2f}'.format(round(total, 2))) + '€')

        except Exception as error:
            print('Error en cargar lineas de venta conexión: ',error)

    def eliminarLineaVenta(codigo):

        try:
            numfac = var.ui.lblCodFac.text()
            query = QtSql.QSqlQuery()
            query.prepare('delete from ventas where codven = :codigo')
            query.bindValue(':codigo', int(codigo))
            if query.exec_():
                Conexion.cargarLineasVenta(numfac)
                var.ui.lblCodFac_4.setText('Venta Eliminada')
                var.ui.lblCodFac_4.setStyleSheet('QLabel{color:blue;}')
            else:
                var.ui.lblCodFac_4.setText('Error al eliminar venta')
                var.ui.lblCodFac_4.setStyleSheet('QLabel{color:red;}')


        except Exception as error:
          print('Error en eliminar venta conexion', error)