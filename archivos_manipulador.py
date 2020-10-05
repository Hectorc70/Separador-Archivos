
import os

from tkinter import filedialog
import shutil


class Rutas:
    def __init__(self):
        self.abrir = filedialog.askdirectory()
        self.ruta_destino_in = input("carpeta_destino: ")
        self.archivos_py = list()
        self.archivos_img = list()
        self.archivos_pdf = list()
        self.archivos_rar = list()
        self.archivos_excel = list()
        self.archivos_word  = list()
        self.archivos_firma = list()

    def in_tipo_archivo(self):

        print("elije una opcion de archivo'\n'", "python = py'\n'",
          "excel = xlsx'\n'","imagenes = png-jpg\n'",
          "Archivos_PDF = pdf'\n'", "Nomina - PDF Y XML = RECI-XML'\n'",
          "Winrar = rar'\n'")

        self.opcion = input("Introduce aqui: ")
        print("Introdujo: ", self.opcion)

    def recuperar_archivos(self):

        #self.guardar = filedialog.asksaveasfilename()
        #self.ext = tipo_ext
        for ruta, carpetas, documentos in os.walk(self.abrir):

            for archivo in documentos:
                rutas = ruta.replace("/","\\") + "\\" + archivo
                archivo_ext = archivo.split('.')[-1]

                if archivo_ext == 'py':
                    print("rutas Archivos PYTHON")
                    self.archivos_py.append(rutas)
                elif archivo_ext == 'jpg' or archivo_ext == 'png':
                    print("rutas imagenes")
                    self.archivos_img.append(rutas)

                elif archivo_ext == 'pdf':
                    print("rutas Archivos PDF")
                    self.archivos_pdf.append()

                elif archivo_ext == 'rar':
                    print("rutas Archivos RAR")
                    #print(rutas)
                    self.archivos_rar.append(rutas)

                elif archivo_ext == 'doc' or archivo_ext == 'docx':
                    print("rutas Archivos Documentos")
                    #print(rutas)
                    self.archivos_word.append(rutas)

                elif archivo_ext == 'cer' or archivo_ext == 'req' or archivo_ext == 'key':
                    print("rutas Archivos Documentos")
                    self.archivos_firma.append(rutas)


    def copiar_archivos_py(self):
        self.recuperar_archivos()

        for ruta_ori in self.archivos_py:
            archivo = ruta_ori.split("\\")[-1]
            self.ruta_destino =  self.ruta_destino_in.replace('/','\\') +"\\" + archivo

            shutil.move(ruta_ori, self.ruta_destino)
            print("MOVIENDO A LA RUTA'\n'", self.ruta_destino)

        print("--Termino--")


    def copiar_imagenes(self):
        self.recuperar_archivos()


        for ruta_ori in self.archivos_img:
            archivo = ruta_ori.split("\\")[-1]

            self.ruta_destino =  self.ruta_destino_in.replace('/','\\') +"\\" + archivo

            shutil.move(ruta_ori, self.ruta_destino)
            print("MOVIENDO A LA RUTA'\n'", self.ruta_destino)


        print("--Termino--")


    def copiar_archivos_pdf(self):
        self.recuperar_archivos()


        for ruta_ori in self.archivos_pdf:
            archivo = ruta_ori.split("\\")[-1]

            self.ruta_destino =  self.ruta_destino_in.replace('/','\\') +"\\" + archivo

            shutil.move(ruta_ori, self.ruta_destino)
            print("MOVIENDO A LA RUTA'\n'", self.ruta_destino)


        print("--Termino--")


    def copiar_recibos_timbres(self):
        self.in_tipo_archivo()

        if self.opcion == 'RECI-XML' or self.opcion == 'reci-xml':
            self.copiar_archivos_py()
        elif (self.opcion == 'png' or self.opcion == 'PNG' or
            self.opcion == 'jpg' or self.opcion == 'JPG'):

            self.copiar_imagenes()

        elif self.opcion == 'pdf' or self.opcion == 'PDF':
            self.copiar_archivos_pdf()

    def copiar_archivos_winrar(self):
        self.recuperar_archivos()


        for ruta_ori in self.archivos_rar:
            archivo = ruta_ori.split("\\")[-1]

            self.ruta_destino =  self.ruta_destino_in.replace('/','\\') +"\\" + archivo

            shutil.move(ruta_ori, self.ruta_destino)
            print("MOVIENDO A LA RUTA'\n'", self.ruta_destino)


        print("--Termino--")

    def copiar_archivos_excel(self):
        self.recuperar_archivos()
        for ruta_ori in self.archivos_excel:
            archivo = ruta_ori.split("\\")[-1]

            self.ruta_destino =  self.ruta_destino_in.replace('/','\\') +"\\" + archivo

            shutil.move(ruta_ori, self.ruta_destino)
            print("MOVIENDO A LA RUTA'\n'", self.ruta_destino)


        print("--Termino--")

    def copiar_archivos_word(self):

        self.recuperar_archivos()

        for ruta_ori in self.archivos_word:
            archivo = ruta_ori.split("\\")[-1]

            self.ruta_destino =  self.ruta_destino_in.replace('/','\\') +"\\" + archivo

            shutil.move(ruta_ori, self.ruta_destino)
            print("MOVIENDO A LA RUTA'\n'", self.ruta_destino)


        print("--Termino--")



    def copiar_e_firma(self):
        self.recuperar_archivos()

        for ruta_ori in self.archivos_firma:
            archivo = ruta_ori.split("\\")[-1]

            self.ruta_destino =  self.ruta_destino_in.replace('/','\\') +"\\" + archivo

            shutil.move(ruta_ori, self.ruta_destino)
            print("MOVIENDO A LA RUTA'\n'", self.ruta_destino)


        print("--Termino--")




    def ejecutar(self):
        self.in_tipo_archivo()

        if self.opcion == 'py' or self.opcion == 'PY':
            self.copiar_archivos_py()
        elif (self.opcion == 'png' or self.opcion == 'PNG' or
              self.opcion == 'jpg' or self.opcion == 'JPG'):

            self.copiar_imagenes()

        elif self.opcion == 'pdf' or self.opcion == 'PDF':
            self.copiar_archivos_pdf()

        elif self.opcion == 'rar' or self.opcion == 'RAR':
            self.copiar_archivos_winrar()

        elif self.opcion == 'xlsx' or self.opcion == 'xlsx':
            self.copiar_archivos_excel()

        elif self.opcion == 'doc' or self.opcion == 'docx':
            self.copiar_archivos_word()
        else:
            self.copiar_e_firma()















ext  = Rutas()
ext.ejecutar()
