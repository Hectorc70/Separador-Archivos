


from interfaz import UI


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

        self.crear_entrada_datos()
        self.entrada_ruta_destino()

        self.ventana.mainloop()















interfaz = UI_In()

interfaz.mostrar_ui()
