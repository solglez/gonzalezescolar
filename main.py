# This is a sample Python script.
import clients, sys, var, events, datetime
from prueba import *
from windowaviso import *
from windowcal import *
from datetime import *
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
        var.ui.rbtGroupSex.buttonClicked.connect(clients.Clientes.SelSexo)
        var.ui.chkGroupPago.buttonClicked.connect(clients.Clientes.SelPago)
        var.ui.btnCalendar.clicked.connect(events.Eventos.abrirCal)
        '''
        Eventos de la barra de menús
        '''
        var.ui.actionSalir.triggered.connect(events.Eventos.salir)
        '''
        Eventos de la caja de texto
        '''
        var.ui.txtDNI.editingFinished.connect(clients.Clientes.validarDNI)
        '''
        Eventos de comboBox
        '''
        clients.Clientes.cargaProv(self)
        var.ui.cmbProv.activated[str].connect(clients.Clientes.selProv)
        clients.Clientes.cargaMun(self)
        var.ui.cmbMun.activated[str].connect(clients.Clientes.selMun)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgaviso = DialogAviso()
    var.dlgcalendar=DialogCalendar()
    window.show()
    sys.exit(app.exec())
