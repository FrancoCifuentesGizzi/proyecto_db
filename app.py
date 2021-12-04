import tkinter as tk
from tkinter import Menu
from tkinter import LabelFrame, Label, Frame
from tkinter import Button
from PIL import Image, ImageTk

from database import Database


class administrador:
    def __init__(self, db):
        self.db = db
        # Main window
        window = tk.Tk ()

        # Algunas especificaciones de tamaño y título de la ventana
        window.geometry ( "760x420" )
        window.title ( "Administrador" )
        # color de ventana
        window.config(background = "goldenrod")

        frame = LabelFrame ( window, text="", relief=tk.FLAT )
        frame.place ( x=151, y=10, relwidth=0.6, relheight=0.7 )

        image = Image.open ( "foto2.jpg" )
        photo = ImageTk.PhotoImage ( image.resize ( (480, 300), Image.ANTIALIAS ) )
        label = Label ( frame, image=photo )
        label.image = photo
        label.pack ()

        # Empieza a correr la interfaz.
        window.mainloop ()






class App:
    def __init__(self, db):
        self.db = db
        # Main window
        self.root = tk.Tk ()

        # Algunas especificaciones de tamaño y título de la ventana
        self.root.geometry ( "760x420" )
        self.root.title ( "GOOD - TECH" )
        # color de ventana
        self.root.config(background = "royalblue4")

        # creación de botones e imagen
        self.__crea_botones_principales ()
        self.__agrega_imagen_principal ()

        # Empieza a correr la interfaz.
        self.root.mainloop ()


    # botones principales.
    def __crea_botones_principales(self):
        padx = 2
        pady = 2

        #
        frame = LabelFrame ( self.root, text="Seleccionar perfil", relief=tk.GROOVE )
        frame.place ( x=144, y=315, width=475,  relheight=0.13 )
        frame.config ( background="royalblue4" )

        #
        b1 = Button ( frame, text="Administrador", width=20 )
        b1.grid ( row=1, column=0, padx=padx, pady=pady )
        b1.bind ( '<Button-1>', administrador )
        b1.config(background = "cyan4")

        #
        b2 = Button ( frame, text="Empleado sucursal", width=20 )
        b2.grid ( row=1, column=2, padx=padx, pady=pady )
        b2.bind ( '<Button-1>', self.__graficos )
        b2.config ( background="cyan4" )

        b3 = Button ( frame, text="Administración de bodega", width=20 )
        b3.grid ( row=1, column=3, padx=padx, pady=pady )
        b3.bind ( '<Button-1>', self.__graficos )
        b3.config ( background="cyan4" )

    # imagen principal.
    def __agrega_imagen_principal(self):
        #
        frame = LabelFrame ( self.root, text="", relief=tk.FLAT )
        frame.place ( x=151, y=10, relwidth=0.6, relheight=0.7 )

        image = Image.open ( "foto.jpg" )
        photo = ImageTk.PhotoImage ( image.resize ( (480, 300), Image.ANTIALIAS ) )
        label = Label ( frame, image=photo )
        label.image = photo
        label.pack ()









    # muestra ventana equipos.
    def __mostrar_equipos(self):
        equipo ( self.root, self.db )

    # muestra ventana jugadores.
    def __mostrar_jugadores(self, button):
        jugador ( self.root, self.db )

    def __graficos(self, button):
        graficos ( self.root, self.db )


def main():
    # Conecta a la base de datos
    db = Database ()
    # La app xD
    App ( db )


if __name__ == "__main__":
    main ()
