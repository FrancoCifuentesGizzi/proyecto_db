import tkinter as tk
from tkinter import ttk

class ciudad:
    #Configuración de la ventana principal
    def __init__(self, root):
        self.root = tk.Toplevel()
        self.root.geometry('300x400')
        self.root.title("Ciudad")
        self.root.resizable(width=0, height=0)
        self.root.transient(root)
        #Contenido Ventana
        self.__config_treeview_ciudad()
        self.__config_buttons_ciudad()

        self.root.mainloop()

    #Configuración de las tablas y su tamaño
    def __config_treeview_ciudad(self):
        self.treeview = ttk.Treeview(self.root)
        self.treeview.configure(columns = ("#0", "#1"))
        self.treeview.heading("#0", text = "Id")
        self.treeview.heading("#1", text = "Nombre")
        self.treeview.column("#0", minwidth = 100, width = 100, stretch = False)
        self.treeview.column("#1", minwidth = 200, width = 200, stretch = False)
        self.treeview.place(x = 0, y = 0, height = 350, width = 300)

    #Configuración de los botones
    def __config_buttons_ciudad(self):
        tk.Button(self.root, command = self.__Agregar_C, text="Agregar").place(x = 0, y = 350, width = 100, height = 50)
        tk.Button(self.root, command = self.__Editar_C, text="Editar").place(x = 100, y = 350, width = 100, height = 50)
        tk.Button(self.root, command = self.__Eliminar_C, text="Eliminar").place(x = 200, y = 350, width = 100, height = 50)

    def __Agregar_C(self):
        Add_Ciudad(self)

    def __Editar_C():
        print("Hello")
        #Edit_Ciudad()

    def __Eliminar_C():
        print("Heyo")

class Add_Ciudad:
    #Configuración de la ventana agregar
    def __init__(self, root):
        self.add = tk.Toplevel()
        self.add.geometry('210x90')
        self.add.title("Agregar")
        self.add.resizable(width=0, height=0)
        #Contenido Ventana
        self.__config_labels()
        self.__config_entry()
        self.__config_buttons()

    #Configuración de los labels
    def __config_labels(self):
        tk.Label(self.add ,text = "Nombre: ").place(x = 0, y = 10, width = 100, height = 20)

    #Configuración de las casillas que el usuario ingresa info
    def __config_entry(self):
        self.entry_nombre = tk.Entry(self.add)
        self.entry_nombre.place(x = 100, y = 10, width = 100, height = 20)

    #Configuración de los botones
    def __config_buttons(self):
        tk.Button(self.add, text="Aceptar").place(x = 0, y = 40, width = 105, height = 50)
        tk.Button(self.add, text="Cancelar").place(x = 105, y = 40, width = 105, height = 50)


def main():
    root = ()
    ciudad(root)

if __name__ == "__main__":
    main()
