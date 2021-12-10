import os,var

from PyQt5 import QtSql
from reportlab.lib.colors import yellow, red, black,white, beige,blue,brown
from reportlab.pdfgen import canvas
from datetime import datetime
class Informes():
    def listadoClientes(self):
        try:

            #Crea el lienzo
            var.cv=canvas.Canvas('Informes/listadoClientes.pdf')
            Informes.cabecera(self)
            #Escribimos en lienzo

                    #   En cuanto a coordenadas:
                    #       x: va de derecha a izquierda
                    #       y: va de abajo a arriba

            '''
            #Esto soy yo dibujando una diana
            var.cv.setFillColor(red)
            var.cv.line(50,580,550,580)
            var.cv.setFillColor(red)
            var.cv.circle(400,400,100,stroke=1,fill=1)
            var.cv.setFillColor(beige)
            var.cv.circle(400, 400, 80, stroke=1, fill=1)
            var.cv.setFillColor(red)
            var.cv.circle(400, 400, 60, stroke=1, fill=1)
            var.cv.setFillColor(beige)
            var.cv.circle(400, 400, 40, stroke=1, fill=1)
            var.cv.setFillColor(red)
            var.cv.circle(400, 400, 20, stroke=1, fill=1)
            
            text='Este es un parrafo muy parrafo dentro de un informe muy informe'
            var.cv.setFont('Courier-Oblique', 10)
            var.cv.setFillColor(blue)
            var.cv.drawString(100,200,text)
            '''

            var.cv.setFont('Helvetica-Bold', 9)
            textotitulo = 'LISTADO CLIENTES'
            var.cv.drawString(255, 690, textotitulo)
            var.cv.line(40,685,530,685)
            items=['DNI','Nombre','Formas de Pago']
            var.cv.drawString(65,675,items[0])
            var.cv.drawString(220, 675, items[1])
            var.cv.drawString(400, 675, items[2])
            var.cv.line(40,670,530,670)
            Informes.pie(textotitulo)
            query=QtSql.QSqlQuery()
            query.prepare('select dni, apellidos, nombre, pago from clientes order by apellidos')
            var.cv.setFont('Helvetica',8)
            if query.exec_():
                i=50
                j=655
                while query.next():
                    if j<=80:
                        #Para saltar de página y colocar pie y cabecera en la nueva
                        var.cv.drawString(460,65,'Página siguiente...') #Ellos están poniendo esta línea más abajo
                        var.cv.showPage() #Avanza la página
                        var.cv.setFont('Helvetica-Bold', 10)
                        textotitulo = 'LISTADO CLIENTES'
                        var.cv.drawString(255, 690, textotitulo)
                        var.cv.line(40, 685, 530, 685)
                        items = ['DNI', 'Nombre', 'Formas de Pago']
                        var.cv.drawString(65, 675, items[0])
                        var.cv.drawString(220, 675, items[1])
                        var.cv.drawString(400, 675, items[2])
                        var.cv.line(40, 670, 530, 670)
                        Informes.cabecera(self)
                        Informes.pie(textotitulo)
                        i = 50
                        j = 655
                    var.cv.drawString(i,j,str(query.value(0)))
                    var.cv.drawString(i+150,j,(str(query.value(1))+', '+str(query.value(2))))
                    var.cv.drawString(i+310,j,str(query.value(3)))
                    j-=20

            #Propiedades del documento
            var.cv.setFont('Helvetica', 8)
            var.cv.setTitle('Listado Clientes')
            var.cv.setAuthor('Departamento de administración')

            #Guarda el lienzo
            var.cv.save()
            rootPath='.\\Informes'
            cont=0

            #Abrimos el archivo. Usa un for porque le quedó así de "veces anteriores"
            #dice que luego puede ser útil
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))

        except Exception as error:
            print('Error al listar clientes informe ',error)
    def cabecera(self):
        try:
            logo='.\\img\logo.png'
            var.cv.drawImage(logo, 425, 722)
            var.cv.line(40,800,530,800)
            var.cv.setFont('Helvetica-Bold',14)
            var.cv.drawString(50,785,'Import-Export Vigo')
            var.cv.setFont('Helvetica',10)
            var.cv.drawString(50,770,'CIF: A0000000H')
            var.cv.drawString(50, 755, 'Dirección: Av. Galicia, 101')
            var.cv.drawString(50, 740, 'Vigo - 36216 - Spain')
            var.cv.drawString(50, 725, 'nohaynadie@algocreible.cow')
            var.cv.line(40, 718, 530, 718)
        except Exception as error:
            print('Error en cabecera informe ',error)

    def pie(texto):
        try:
            var.cv.line(50,50,530,50)
            fecha=datetime.today()
            fecha=fecha.strftime('%d.%m.%Y %H.%M.%S')
            var.cv.setFont('Helvetica',6)
            var.cv.drawString(70,40,str(fecha))
            var.cv.drawString(255,40,str(texto))
            var.cv.drawString(500,40,str('Página %s '%var.cv.getPageNumber()))
        except Exception as error:
            print('Error al crear pie de informe clientes ',error)