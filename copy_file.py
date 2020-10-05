

import os

import shutil
from tkinter import *
from tkinter import filedialog


from interfaz import UI_In
from rutas import Rutas





class Extenciones(UI_In,Rutas):
    """Exteniones de archivos"""


    def __init__(self):
        UI_In.__init__(self)
        Rutas.__init__(self)
        self.recuperar_archivos()


        #self.ext = self.textos




extencion = Extenciones()
extencion.copiar_archivos_py()
