# This is a sample Python script.
import articulos, informes, invoice
import clients, sys, var, events, datetime, locale
import conexion
from prueba import *
from windowaviso import *
from windowcal import *
from datetime import *
locale.setlocale(locale.LC_ALL, 'es-ES')

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        '''
        Ventana abrir explorador windows
        '''
        super(FileDialogAbrir,self).__init__()

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
        conexion.Conexion.create_db(var.filedb)
        '''
        Eventos de botón
        '''
        #var.ui.btnSalir.clicked.connect(events.Eventos.salir)
        #var.ui.rbtGroupSex.buttonClicked.connect(clients.Clientes.SelSexo)
        #var.ui.chkGroupPago.buttonClicked.connect(clients.Clientes.SelPago)
        var.ui.btnCalendar.clicked.connect(events.Eventos.abrirCal)
        var.ui.btnGrabaCli.clicked.connect(clients.Clientes.guardaCli)
        var.ui.btnLimpiaCli.clicked.connect(clients.Clientes.limpiaFormCli)
        var.ui.btnBajaCli.clicked.connect(clients.Clientes.bajaCli)
        #var.ui.btnBuscarCli.clicked.connect(clients.Clientes.buscaCli)
        var.ui.btnModifCli.clicked.connect(clients.Clientes.modifCli)
        var.ui.btnGuardaArt.clicked.connect(articulos.Articulos.guardaArticulo)
        var.ui.btnModifArt.clicked.connect(articulos.Articulos.modifArt)
        var.ui.btnBorrarArt.clicked.connect(articulos.Articulos.bajaArt)
        var.ui.btnBuscaArt.clicked.connect(articulos.Articulos.buscaArticulo)
        var.ui.btnLimpiaArt.clicked.connect(articulos.Articulos.limpiaFormArt)
        var.ui.btnBuscaCliFac.clicked.connect(invoice.Facturas.buscaCli)
        var.ui.btnFechaFac.clicked.connect(events.Eventos.abrirCal)
        var.ui.btnFacturar.clicked.connect(invoice.Facturas.altaFac)
        var.ui.btnLimpiaFac.clicked.connect(invoice.Facturas.limpiaFormFac)
        var.ui.btnPdfCli.clicked.connect(informes.Informes.listadoClientes)
        var.ui.btnPdfArt.clicked.connect(informes.Informes.listadoProductos)
        var.ui.btnEliminarVenta.clicked.connect(invoice.Facturas.eliminarVenta)
        var.ui.btnReportFac.clicked.connect(informes.Informes.factura)

        '''
        Eventos de spin
        '''
        var.ui.spinEnvio.valueChanged.connect(events.Eventos.labelEnvio)
        var.ui.spinEnvio.setValue(0);
        var.ui.spinEnvio.setRange(0, 3);
        '''
        Eventos de la barra de menús y de herramientas
        '''
        var.ui.actionSalir.triggered.connect(events.Eventos.salir)
        var.ui.action_Abrir.triggered.connect(events.Eventos.abrir)
        var.ui.actionCrear_Backup.triggered.connect(events.Eventos.crearBackup)
        var.ui.actionRestaurar_Backup.triggered.connect(events.Eventos.restaurarBackup)
        var.ui.actionImprimir.triggered.connect(events.Eventos.Imprimir)
        var.ui.actionImportar_Datos.triggered.connect(events.Eventos.ImportarDatos)
        var.ui.actionExportar_Datos.triggered.connect(events.Eventos.ExportarDatos)
        var.ui.actionListado_Clientes.triggered.connect(informes.Informes.listadoClientes)
        var.ui.actionFacturas.triggered.connect(informes.Informes.factura)
        var.ui.actionInformacion.triggered.connect(events.Eventos.acercaDe)
        '''
        Eventos de la caja de texto
        '''
        var.ui.txtDNI.editingFinished.connect(clients.Clientes.validarDNI)
        var.ui.txtNome.editingFinished.connect(clients.Clientes.formatoMayus)
        var.ui.txtApel.editingFinished.connect(clients.Clientes.formatoMayus)
        var.ui.txtDir.editingFinished.connect(clients.Clientes.formatoMayus)
        var.ui.txtPrecioArticulo.editingFinished.connect(articulos.Articulos.formatoPrecio)
        var.ui.txtNombreArticulo.editingFinished.connect(articulos.Articulos.formatoMayus)

        #Hay que instanciar var.txtCantidad porque se crea en tiempo de ejecución y no en QtDesigner
        var.txtCantidad=QtWidgets.QLineEdit()
        var.txtCantidad.editingFinished.connect(invoice.Facturas.totalLineaVenta)


        '''
        Eventos de comboBox
        '''
        var.ui.cmbProv.currentIndexChanged.connect(clients.Clientes.cargaMun)
        #var.ui.cmbProv.activated[str].connect(clients.Clientes.selProv)
        #clients.Clientes.cargaMun(self)
        #var.ui.cmbMun.activated[str].connect(clients.Clientes.selMun)
        # Hay que instanciar var.cmbProducto porque se crea en tiempo de ejecución y no en QtDesigner
        var.cmbProducto = QtWidgets.QComboBox()
        var.cmbProducto.currentIndexChanged.connect(invoice.Facturas.procesoVenta)




        '''
        Barra de estado
        '''
        var.ui.statusbar.addPermanentWidget(var.ui.lblFecha,1)
        var.ui.lblFecha.setText(datetime.today().strftime('%H:%M - %A, %d de %B de %Y'))

        '''
        Eventos menú herramientas
        '''
        var.ui.actionBarSalir.triggered.connect(events.Eventos.salir)
        var.ui.actionabrirCarpeta.triggered.connect(events.Eventos.abrir)
        var.ui.actionHacerBackup.triggered.connect(events.Eventos.crearBackup)
        var.ui.actionRestaurarBackup.triggered.connect(events.Eventos.restaurarBackup)
        var.ui.actionBarImpresora.triggered.connect(events.Eventos.Imprimir)
        '''
        Eventos QTabWidget
        '''
        events.Eventos.resizeTablaCli(self)
        events.Eventos.resizeTablaArt(self)
        events.Eventos.resizeTablaFac(self)
        events.Eventos.resizeTablaVen(self)
        var.ui.tabClientes.clicked.connect(clients.Clientes.cargaCli)
        var.ui.tabClientes.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabArticulos.clicked.connect(articulos.Articulos.cargaArt)
        var.ui.tabArticulos.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabFacturas.clicked.connect(invoice.Facturas.cargaFac)
        var.ui.tabFacturas.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabVentas.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        #invoice.Facturas.prepararTabFac(self)


        '''
        Base de datos
        '''
        conexion.Conexion.db_connect(var.filedb)
        conexion.Conexion.cargaTabCli(self)
        conexion.Conexion.cargaTabArt(self)
        conexion.Conexion.cargaTabFac()
        conexion.Conexion.cargaTabArt(self)
        clients.Clientes.cargaProv(self)

        invoice.Facturas.cargarLineaVenta(self)

        #var.cmbProducto.currentIndexChanged.connect(invoice.Facturas.procesoVenta)
        #var.txtCantidad.editingFinished.connect(invoice.Facturas.totalLineaVenta)
        #var.txtCantidad.editingFinished.connect(invoice.Facturas.prueba)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    desktop = QtWidgets.QApplication.desktop()
    x=(desktop.width()-window.width())//2
    y=(desktop.height()-window.height())//2
    window.move(x,y)
    var.dlgaviso = DialogAviso()
    var.dlgcalendar=DialogCalendar()
    var.dlgabrir=FileDialogAbrir()
    window.show()
    sys.exit(app.exec())
