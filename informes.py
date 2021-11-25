import os,var
from reportlab.lib.colors import yellow, red, black,white, beige,blue,brown
from reportlab.pdfgen import canvas
class Informes():
    def listadoClientes(self):
        try:

            #Crea el lienzo
            var.cv=canvas.Canvas('Informes/listadoClientes.pdf')
            Informes.cabecera(self)
            #Escribimos en lienzo
            #En cuanto a coordenadas:
            #   x: va de derecha a izquierda
            #   y: va de abajo a arriba
            var.cv.setFont('Helvetica-Bold',16)
            var.cv.drawString(100,600,'Listado Clientes')
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
            var.cv.line(40,800,500,800)
            var.cv.setFont('Helvetica-Bold',14)
            var.cv.drawString(50,785,'Import-Export Vigo')
            var.cv.setFont('Helvetica',10)
            var.cv.drawString(50,770,'CIF: A0000000H')
            var.cv.drawString(50, 755, 'Dirección: Av. Galicia, 101')
            var.cv.drawString(50, 740, 'Vigo - 36216 - Spain')
            var.cv.drawString(50, 725, 'nohaynadie@algocreible.cow')
            var.cv.line(40, 720, 500, 720)
        except Exception as error:
            print('Error en cabecera informe ',error)