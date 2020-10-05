

from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as font

from tkinter import filedialog

#from rutas import recuperar_archivos
#from copy_file import Extenciones
#from extencion_usuario import obtener_extension_introducida





class UI():

    def __init__(self):

        self.ventana     = tk.Tk()
        self.dimensiones = self.ventana.geometry("800x600+10+20")
        self.titulo      = self.ventana.title('Separar Archivos')

        self.entrada = tk.StringVar()
        self.entrada_ruta = tk.StringVar()

        self.crear_botones()
        self.crear_textos()


    def crear_botones(self):
        """Crea Botones en la ventana"""

        btn = Button(self.ventana, text="ABRIR", command = None)
        btn.config(justify='right')
        btn.grid(row = 2, column = 2,)

        boton_star = Button(self.ventana, text="COMENZAR", bg = '#B2F7FE',
                            command = None,
                            width=80, height= 5)
        boton_star.grid(row = 5, column = 1, columnspan = 5,
                        padx =100, pady=50)







    def crear_textos(self):

        label_b = Label(self.ventana, text= "BUSCAR EN CARPETAS: ",
                                fg='black',

                                font=("Helvetica", 16))
        label_b.grid(row = 2, column = 1, padx=20, pady=10, sticky = "w")


        label_e = Label(self.ventana, text= "EXTENSION DEL ARCHIVO: ",
                                fg='black',
                                font=("Helvetica", 16))
        label_e.grid(row = 3, column = 1, padx=20,  pady=10, sticky = "w")

        label_ruta = Label(self.ventana, text= "RUTA DE SALIDA: ",
                                fg='black',
                                font=("Helvetica", 16))
        label_ruta.grid(row = 4, column = 1, padx=20,  pady=10, sticky = "w")






    def crear_radiobotons(self):
        """Crea Radiobutton de cada tipo de archivos
            en el Diccionario"""

        self.crear_botones()


        archivos = [
                    ("Python",1),
                    ("Excel",2),
                    ("IMAGENES PNG",3),
                    ("IMAGENES JPG",4),
                    ("WORD",5),
                    ("PDF",6)
                    ]

        posx_rb = 10
        posy_rb = 5

        v = tk.IntVar()

        for val, t_archivo in enumerate(archivos):
            posy_rb +=5


            tk.Radiobutton(self.ventana,
                            text    = t_archivo,
                            padx    = posx_rb,
                            pady    = posy_rb,
                            variable = v,
                            command  = None,
                            value    = val).pack(anchor=tk.W)





class UI_In(UI):
    def __init__(self):
        UI.__init__(self)
        self.textos = list()
        self.ruta_dest = list()



        self.crear_entrada_datos()





    def crear_entrada_datos(self):

        entrada = ttk.Entry(self.ventana, textvariable=self.entrada)
        entrada.config(justify="center")
        entrada.grid(row = 3, column = 2, pady=5)
        entrada.get()

        def lista():
            #for texto in self.entrada.get():
            self.textos.append(self.entrada.get())
            print(self.textos)

        lista_textos_in = lambda :self.textos.append(self.entrada.get())

        boton_ext = Button(self.ventana, text="ACEPTAR",
                            command = lista,
                            width=10)
        boton_ext.grid(row = 3, column = 3, padx = 5, pady=10)

    def entrada_ruta_destino(self):
        """Crea la entrada para la ruta de destino de lista_textos_in
            Archivos copiados"""





        in_ruta_destino= ttk.Entry(self.ventana, textvariable=self.entrada_ruta)
        in_ruta_destino.config(justify="left")
        in_ruta_destino.grid(row = 4, column = 2, pady=5)


        def lista():
            self.ruta_dest.append(self.entrada_ruta.get())
            print(self.ruta_dest)



        boton_in = Button(self.ventana, text="ACEPTAR",
                         command = lista,
                         width=10)
        boton_in.grid(row = 4, column = 3, padx = 5)




    def mostrar_textos():
            pass

    def mostrar_ui(self):

        #self.crear_entrada_datos()
        #self.entrada_ruta_destino()

        self.ventana.mainloop()

        
interfaz = UI_In()
interfaz.mostrar_ui()






















#ui = UI()
#ui.mostrar_ui()
