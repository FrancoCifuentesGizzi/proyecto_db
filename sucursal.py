import tkinter as tk
from tkinter import ttk
# !!importar la ciudad!!
# !!importar la bodega!!

class sucursal:
    #Configuración de la ventana principal
    def __init__(self, root):
        self.root = tk.Toplevel()
        self.root.geometry('1100x400')
        self.root.title("Sucursales")
        self.root.resizable(width=0, height=0)
        self.root.transient(root)
        self.__config_treeview_sucursales()
        self.__config_buttons_sucursal()

        self.root.mainloop()

    #Configuración de las tablas y su tamaño
    def __config_treeview_sucursales(self):
        self.treeview = ttk.Treeview(self.root)
        self.treeview.configure(columns = ("#0", "#1", "#2", "#3", "#4", "#5"))
        self.treeview.heading("#0", text = "Id")
        self.treeview.heading("#1", text = "Nombre")
        self.treeview.heading("#2", text = "Direccion")
        self.treeview.heading("#3", text = "Telefono")
        self.treeview.heading("#4", text = "Ciudad")
        self.treeview.heading("#5", text = "Bodega")
        self.treeview.column("#0", minwidth = 100, width = 100, stretch = False)
        self.treeview.column("#1", minwidth = 200, width = 200, stretch = False)
        self.treeview.column("#2", minwidth = 200, width = 200, stretch = False)
        self.treeview.column("#3", minwidth = 200, width = 200, stretch = False)
        self.treeview.column("#4", minwidth = 200, width = 200, stretch = False)
        self.treeview.column("#5", minwidth = 200, width = 200, stretch = False)
        self.treeview.place(x = 0, y = 0, height = 350, width = 1100)

    #Configuración de los botones
    def __config_buttons_sucursal(self):
        tk.Button(self.root, command = self.__Agregar_S, text="Agregar").place(x = 0, y = 350, width = 366, height = 50)
        tk.Button(self.root, command = self.__Editar_S, text="Editar").place(x = 366, y = 350, width = 366, height = 50)
        tk.Button(self.root, command = self.__Eliminar_S, text="Eliminar").place(x = 732, y = 350, width = 366, height = 50)

    def __Agregar_S(self):
        Add_Sucursal(self)

    def __Editar_S():
        print("Hello")
        #Edit_Empleado()

    def __Eliminar_S():
        print("Heyo")
        #Del_Empleado

class Add_Sucursal:
    #Configuración de la ventana agregar
    def __init__(self, root):
        self.add = tk.Toplevel()
        self.add.geometry('210x170')
        self.add.title("Agregar")
        self.add.resizable(width=0, height=0)
        #Contenido Ventana
        self.__config_labels()
        self.__config_entry()
        self.__config_buttons()

    #Configuración de los labels
    def __config_labels(self):
        tk.Label(self.add ,text = "Nombre: ").place(x = 0, y = 10, width = 100, height = 20)
        tk.Label(self.add ,text = "Direccion: ").place(x = 0, y = 30, width = 100, height = 20)
        tk.Label(self.add ,text = "Telefono: ").place(x = 0, y = 50, width = 100, height = 20)
        tk.Label(self.add ,text = "Ciudad: ").place(x = 0, y = 70, width = 100, height = 20)
        tk.Label(self.add ,text = "Bodega: ").place(x = 0, y = 90, width = 100, height = 20)

    #Configuración de las casillas que el usuario ingresa info
    def __config_entry(self):
        self.entry_nombre = tk.Entry(self.add)
        self.entry_nombre.place(x = 100, y = 10, width = 100, height = 20)
        self.entry_direccion = tk.Entry(self.add)
        self.entry_direccion.place(x = 100, y = 30, width = 100, height = 20)
        self.entry_telefono = tk.Entry(self.add)
        self.entry_telefono.place(x = 100, y = 50, width = 100, height = 20)
        self.combobox_ciudad = ttk.Combobox(self.add)
        self.combobox_ciudad.place(x = 100, y = 70, width = 100, height = 20)
        self.combobox_bodega = ttk.Combobox(self.add)
        self.combobox_bodega.place(x = 100, y = 90, width = 100, height = 20)

        #Configuración de los botones
    def __config_buttons(self):
        tk.Button(self.add, text="Aceptar").place(x = 0, y = 120, width = 105, height = 50)
        tk.Button(self.add, text="Cancelar").place(x = 105, y = 120, width = 105, height = 50)


def main():
    root = ()
    sucursal(root)

if __name__ == "__main__":
    main()
