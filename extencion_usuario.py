
from tkinter import *
import tkinter as tk
from tkinter import ttk



texto_in = lambda texto: texto.get()

def crear_entrada_datos():
    ventana     = tk.Tk()
    text = tk.StringVar()



    entrada = ttk.Entry(ventana, textvariable=text)
    entrada.config(justify="center")
    entrada.grid(row = 3, column = 2, pady=5)


    boton_star = Button(ventana, text="Start", bg = '#B2F7FE',
                        command = texto_in(text) ,
                        width=80, height= 5)
    boton_star.grid(row = 7, column = 1, columnspan = 5,
                    padx =100, pady=50)


    ventana.mainloop()

crear_entrada_datos()
