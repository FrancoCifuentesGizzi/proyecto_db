import tkinter as tk
from tkinter import ttk
# !!importar la sucursal!!

class empleados:
    #Configuración de la ventana principal
    def __init__(self, root):
        self.root = tk.Toplevel()
        self.root.geometry('900x400')
        self.root.title("Empleados")
        self.root.resizable(width=0, height=0)
        self.root.transient(root)
        self.__config_treeview_empleados()
        self.__config_buttons_empleado()

        self.root.mainloop()

    #Configuración de las tablas y su tamaño
    def __config_treeview_empleados(self):
        self.treeview = ttk.Treeview(self.root)
        self.treeview.configure(columns = ("#0", "#1", "#2", "#3", "#4"))
        self.treeview.heading("#0", text = "Id")
        self.treeview.heading("#1", text = "Nombre")
        self.treeview.heading("#2", text = "Apellido")
        self.treeview.heading("#3", text = "Telefono")
        self.treeview.heading("#4", text = "Sucursal")
        self.treeview.column("#0", minwidth = 100, width = 100, stretch = False)
        self.treeview.column("#1", minwidth = 200, width = 200, stretch = False)
        self.treeview.column("#2", minwidth = 200, width = 200, stretch = False)
        self.treeview.column("#3", minwidth = 200, width = 200, stretch = False)
        self.treeview.column("#4", minwidth = 200, width = 200, stretch = False)
        self.treeview.place(x = 0, y = 0, height = 350, width = 900)

    #Configuración de los botones
    def __config_buttons_empleado(self):
        tk.Button(self.root, command = self.__Agregar_E, text="Agregar").place(x = 0, y = 350, width = 300, height = 50)
        tk.Button(self.root, command = self.__Editar_E, text="Editar").place(x = 300, y = 350, width = 300, height = 50)
        tk.Button(self.root, command = self.__Eliminar_E, text="Eliminar").place(x = 600, y = 350, width = 300, height = 50)

    def __Agregar_E(self):
        Add_Empleado(self)

    def __Editar_E():
        print("Hello")
        #Edit_Empleado()

    def __Eliminar_E():
        print("Heyo")
        #Del_Empleado

class Add_Empleado:
    #Configuración de la ventana agregar
    def __init__(self, root):
        self.add = tk.Toplevel()
        self.add.geometry('210x150')
        self.add.title("Agregar")
        self.add.resizable(width=0, height=0)
        #Contenido Ventana
        self.__config_labels()
        self.__config_entry()
        self.__config_buttons()

    #Configuración de los labels
    def __config_labels(self):
        tk.Label(self.add ,text = "Nombre: ").place(x = 0, y = 10, width = 100, height = 20)
        tk.Label(self.add ,text = "Apellido: ").place(x = 0, y = 30, width = 100, height = 20)
        tk.Label(self.add ,text = "Telefono: ").place(x = 0, y = 50, width = 100, height = 20)
        tk.Label(self.add ,text = "Sucursal: ").place(x = 0, y = 70, width = 100, height = 20)

    #Configuración de las casillas que el usuario ingresa info
    def __config_entry(self):
        self.entry_nombre = tk.Entry(self.add)
        self.entry_nombre.place(x = 100, y = 10, width = 100, height = 20)
        self.entry_apellido = tk.Entry(self.add)
        self.entry_apellido.place(x = 100, y = 30, width = 100, height = 20)
        self.entry_telefono = tk.Entry(self.add)
        self.entry_telefono.place(x = 100, y = 50, width = 100, height = 20)
        self.combobox_sucursal = ttk.Combobox(self.add)
        self.combobox_sucursal.place(x = 100, y = 70, width = 100, height = 20)

    #Configuración de los botones
    def __config_buttons(self):
        tk.Button(self.add, text="Aceptar").place(x = 0, y = 100, width = 105, height = 50)
        tk.Button(self.add, text="Cancelar").place(x = 105, y = 100, width = 105, height = 50)

def main():
    root = ()
    empleados(root)

if __name__ == "__main__":
    main()
