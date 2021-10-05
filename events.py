'''
Fichero de eventos generales
'''
import var
import sys
class Eventos():
    def salir(self):
        try:
            sys.exit()
        except Exception as error:
            print('Error en módulo salir ', error)