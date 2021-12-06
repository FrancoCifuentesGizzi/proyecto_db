import tkinter as tk
from tkinter import ttk

# !!importar la bodega!!

class sucursal:
    #Configuración de la ventana principal
    def __init__(self, root, db):

        self.db = db
        self.data = []

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
        self.llenar_treeview_sucursal ()
        self.root.after ( 0, self.llenar_treeview_sucursal )

    #Configuración de los botones
    def __config_buttons_sucursal(self):
        tk.Button(self.root, command = self.__Agregar_S, text="Agregar sucursal").place(x = 0, y = 350, width = 366, height = 50)
        tk.Button(self.root, command = self.__Editar_S, text="Modificar datos").place(x = 366, y = 350, width = 366, height = 50)
        tk.Button(self.root, command = self.__Eliminar_S, text="Eliminar sucursal").place(x = 732, y = 350, width = 366, height = 50)

    def llenar_treeview_sucursal(self):
        sql = """select id_sucursal, nombre_suc, direccion_suc, telefono_suc, ciudad.nombre_ciu, bodega.nombre_bod 
           from sucursal join ciudad on sucursal.ciudad_id_ciudad = ciudad.id_ciudad 
           join bodega on sucursal.bodega_id_bodega = bodega.id_bodega"""
        data = self.db.run_select ( sql )

        if (data != self.data):
            self.treeview.delete ( *self.treeview.get_children () )  # Elimina todos los rows del treeview
            for i in data:
                self.treeview.insert ( "", "end", text=i[0],
                                       values=(i[1], i[2], i[3], i[4], i[5]), iid=i[0] )
            self.data = data


    def __Agregar_S(self):
        Add_Sucursal(self.db, self)

    def __Editar_S():
        if (self.treeview.focus () != ""):
            sql = "select id_bodega, nombre_bod, direccion_bod, telefono_bod, ciudad.nombre_ciu from bodega " \
                  "join ciudad on bodega.ciudad_id_ciudad = ciudad.id_ciudad where id_bodega = %(id_bodega)s"
            row_data = self.db.run_select_filter ( sql, {"id_bodega": self.treeview.focus ()} )[0]
            editar_bodega ( self.db, self, row_data )


    def __Eliminar_S():
        print("Heyo")
        #Del_Empleado

class Add_Sucursal:
    #Configuración de la ventana agregar
    def __init__(self, db, padre):
        self.padre = padre
        self.db = db

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
        self.combociudad = ttk.Combobox(self.add)
        self.combociudad.place(x = 100, y = 70, width = 100, height = 20)
        self.combociudad["values"], self.ids = self.__fill_combo_ciudad ()
        self.combobodega = ttk.Combobox(self.add)
        self.combobodega.place(x = 100, y = 90, width = 100, height = 20)
        self.combobodega["values"], self.ids = self.__fill_combo_bodega ()

        #Configuración de los botones
    def __config_buttons(self):
        tk.Button(self.add, text="Aceptar",
                  command = self.__insertar).place(x = 55, y = 120, width = 105, height = 30)

    def __fill_combo_ciudad(self):
        sql = "select id_ciudad, nombre_ciu from ciudad"
        self.data = self.db.run_select ( sql )
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def __fill_combo_bodega(self):
        sql = "select id_bodega, nombre_bod from bodega"
        self.data = self.db.run_select ( sql )
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def __insertar(self):  # Insercion en la base de datos.
        sql = """insert sucursal (nombre_suc, direccion_suc, telefono_suc, ciudad_id_ciudad, bodega_id_bodega ) 
            values (%(nombre_suc)s, %(direccion_suc)s, %(telefono_suc)s, %(ciudad_id_ciudad)s, %(bodega_id_bodega)s);"""
        self.db.run_sql ( sql, {"nombre_suc": self.entry_nombre.get (),
                                "direccion_suc": self.entry_direccion.get (),
                                "telefono_suc": self.entry_telefono.get (),
                                "ciudad_id_ciudad": self.ids[self.combociudad.current ()],
                                "bodega_id_bodega": self.ids[self.combobodega.current ()]} )
        self.add.destroy ()
        self.padre.llenar_treeview_sucursal ()


class editar_sucursal:  # Clase para modificar
    def __init__(self, db, padre, row_data):
        self.padre = padre
        self.db = db
        self.row_data = row_data
        self.insert_datos = tk.Toplevel ()
        self.config_window ()
        self.__config_label ()
        self.__config_entry ()
        self.__config_button ()

    def config_window(self):  # Configuración de la ventana.
        self.insert_datos.geometry ( '250x260' )
        self.insert_datos.title ( "Editar datos" )
        self.insert_datos.resizable ( width=0, height=0 )


    def __config_label(self):
        tk.Label ( self.insert_datos, text= "Modificar " + (self.row_data[1]) ).place ( x=5, y=10, width=250, height=20 )
        tk.Label ( self.insert_datos, text="Nombre: " ).place ( x=0, y=30, width=100, height=20 )
        tk.Label ( self.insert_datos, text="Direccion: " ).place ( x=0, y=60, width=100, height=20 )
        tk.Label ( self.insert_datos, text="Telefono: " ).place ( x=0, y=90, width=100, height=20 )
        tk.Label ( self.insert_datos, text="Ciudad: " ).place ( x=0, y=120, width=100, height=20 )

        # Configuración de las casillas que el usuario ingresa info

    def __config_entry(self):
        self.entry_nombre = tk.Entry(self.insert_datos)
        self.entry_nombre.place(x = 100, y = 30, width = 100, height = 20)
        self.entry_direccion = tk.Entry(self.insert_datos)
        self.entry_direccion.place(x = 100, y = 60, width = 100, height = 20)
        self.entry_telefono = tk.Entry(self.insert_datos)
        self.entry_telefono.place(x = 100, y = 90, width = 100, height = 20)
        self.combo = ttk.Combobox(self.insert_datos)
        self.combo.place(x = 100, y = 120, width = 100, height = 20)
        self.combo["values"], self.ids = self.fill_combo ()
        self.entry_nombre.insert ( 0, self.row_data[1] )
        self.entry_direccion.insert ( 0, self.row_data[2] )
        self.entry_telefono.insert ( 0, self.row_data[3] )
        self.combo.insert ( 0, self.row_data[4] )

        # Configuración de los botones

    def __config_button(self):
        tk.Button ( self.insert_datos, text="Aceptar",
                    command=self.modificar ).place ( x=55, y=160, width=105, height=25 )

    def modificar(self):  # Insercion en la base de datos.
        sql = """update bodega set nombre_bod = %(nombre_bod)s, direccion_bod = %(direccion_bod)s, 
                telefono_bod = %(telefono_bod)s, ciudad_id_ciudad = %(id_ciudad)s
                where id_bodega = %(id_bodega)s"""
        self.db.run_sql ( sql, {"nombre_bod": self.entry_nombre.get (),
                                "direccion_bod": self.entry_direccion.get (),
                                "telefono_bod": self.entry_telefono.get (),
                                "id_ciudad": self.ids[self.combo.current ()],
                                "id_bodega": self.row_data[0]} )
        self.insert_datos.destroy ()
        self.padre.llenar_treeview_bodega ()

    def fill_combo(self):  #
        sql = "select id_ciudad, nombre_ciu from ciudad"
        self.data = self.db.run_select ( sql )
        return [i[1] for i in self.data], [i[0] for i in self.data]
