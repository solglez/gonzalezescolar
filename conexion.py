from PyQt5 import QtSql, QtWidgets

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
            pass
        except Exception as error:
            print('Error en altaCli: ',error)