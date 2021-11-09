# This is a sample Python script.
import clients, sys, var, events, datetime, locale
import conexion
from prueba import *
from windowaviso import *
from windowcal import *
from datetime import *
locale.setlocale(locale.LC_ALL, 'es-ES')

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        '''
        Clase ventana calendario
        '''
        super(DialogCalendar, self).__init__()
        var.dlgcalendar= Ui_windowcal()
        var.dlgcalendar.setupUi(self)
        diaactual=datetime.now().day
        mesactual=datetime.now().month
        anoactual=datetime.now().year
        var.dlgcalendar.Calendar.setSelectedDate((QtCore.QDate(anoactual,mesactual,diaactual)))
        var.dlgcalendar.Calendar.clicked.connect(clients.Clientes.cargarFecha)


class DialogAviso(QtWidgets.QDialog):
    def __init__(self):
        '''
        Clase que inicia la ventana de aviso al salir.
        '''
        super(DialogAviso, self).__init__()
        var.dlgaviso = Ui_windowaviso()
        var.dlgaviso.setupUi(self)
        var.dlgaviso.btnBoxAviso.accepted.connect(self.accept)
        var.dlgaviso.btnBoxAviso.rejected.connect(self.reject)

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        '''
        Eventos de botón
        '''
        var.ui.btnSalir.clicked.connect(events.Eventos.salir)
        #var.ui.rbtGroupSex.buttonClicked.connect(clients.Clientes.SelSexo)
        #var.ui.chkGroupPago.buttonClicked.connect(clients.Clientes.SelPago)
        var.ui.btnCalendar.clicked.connect(events.Eventos.abrirCal)
        var.ui.btnGrabaCli.clicked.connect(clients.Clientes.guardaCli)
        var.ui.btnLimpiaCli.clicked.connect(clients.Clientes.limpiaFormCli)
        var.ui.btnBajaCli.clicked.connect(clients.Clientes.bajaCli)
        var.ui.btnBuscarCli.clicked.connect(clients.Clientes.buscaCli)
        var.ui.btnModifCli.clicked.connect(clients.Clientes.modifCli)

        '''
        Eventos de la barra de menús
        '''
        var.ui.actionSalir.triggered.connect(events.Eventos.salir)
        '''
        Eventos de la caja de texto
        '''
        var.ui.txtDNI.editingFinished.connect(clients.Clientes.validarDNI)
        var.ui.txtNome.editingFinished.connect(clients.Clientes.formatoMayus)
        var.ui.txtApel.editingFinished.connect(clients.Clientes.formatoMayus)
        var.ui.txtDir.editingFinished.connect(clients.Clientes.formatoMayus)

        '''
        Eventos de comboBox
        '''
        var.ui.cmbProv.currentIndexChanged.connect(clients.Clientes.cargaMun)
        #var.ui.cmbProv.activated[str].connect(clients.Clientes.selProv)
        #clients.Clientes.cargaMun(self)
        #var.ui.cmbMun.activated[str].connect(clients.Clientes.selMun)

        '''
        Barra de estado
        '''
        var.ui.statusbar.addPermanentWidget(var.ui.lblFecha,1)
        var.ui.lblFecha.setText(datetime.today().strftime('%H:%M - %A, %d de %B de %Y'))


        '''
        Eventos QTabWidget
        '''
        events.Eventos.resizeTablaCli(self)
        var.ui.tabClientes.clicked.connect(clients.Clientes.cargaCli)
        var.ui.tabClientes.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        '''
        Base de datos
        '''
        conexion.Conexion.db_connect(var.filedb)
        conexion.Conexion.cargaTabCli(self)
        clients.Clientes.cargaProv(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    desktop = QtWidgets.QApplication.desktop()
    x=(desktop.width()-window.width())//2
    y=(desktop.height()-window.height())//2
    window.move(x,y)
    var.dlgaviso = DialogAviso()
    var.dlgcalendar=DialogCalendar()
    window.show()
    sys.exit(app.exec())
