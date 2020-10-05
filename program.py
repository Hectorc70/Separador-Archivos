
import os

from tkinter import *
from tkinter import filedialog






class Rutas:

    def __init__(self):
        self.ruta = filedialog.askdirectory()



    def recuperar_archivos(self):

        self.rutas_archivos = list()


        for ruta, carpetas, documentos in os.walk(self.ruta):

            for archivo in documentos:
                ruta = ruta.replace("/","\\") + "\\" + archivo
                self.rutas_archivos.append(ruta)
