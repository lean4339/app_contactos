import sqlite3
from tkinter import ttk
from tkinter import *

class Contactos:
    def __init__(self, window):
        self.win = window
        self.win.title("Contactos")
        self.win.resizable("0","0")

        #Creando el frame 
        frame = LabelFrame(self.win, text="Registra un nuevo contacto")
        frame.grid(row = 0, column = 0, columnspan = 6, pady= 20)
        
        #Input nombre 
        nombre = Label(frame, text="Nombre:")
        nombre.grid(row= 1, column= 0)
        self.nombre = Entry(frame)
        self.nombre.grid(row = 1, column = 1)

        #Input numero 
        numero = Label(frame, text = "Numero:")
        numero.grid(row=2, column=0)
        self.numero= Entry(frame)
        self.numero.grid(row = 2, column = 1)

        #Input email
        email = Label(frame, text = "Email:")
        email.grid(row = 3, column = 0)
        self.email = Entry(frame)
        self.email.grid(row = 3, column = 1)
        
        #Input direccion 
        direccion = Label(frame, text="Dirección:")
        direccion.grid(row= 4, column = 0)
        self.direccion = Entry(frame)
        self.direccion.grid(row=4, column = 1)

        #boton para agregar contacto 
        ttk.Button(frame, text="Agregar contacto").grid(row = 5, column = 0, columnspan= 6, sticky = W + E)

        #Buscar contactos
        buscar = Label(frame, text="Buscar Contacto")
        buscar.grid(row=6, column=0, columnspan = 6, sticky = W + E)
        self.buscar = Entry(frame)
        self.buscar.grid(row=7, column=0, columnspan=6, sticky = W + E)
        ttk.Button(frame, text="Buscar contacto").grid(row=8, column = 0, columnspan = 6, sticky = W + E)

        #Creandoo la tabla de datos
        self.tree = ttk.Treeview( height= 10, columns = [f"#{n}" for n in range(1, 4)])
        self.tree.grid(row =9, column = 0, columnspan = 6, sticky = W + E)
        self.tree.heading("#0", text = "Nombre", anchor = "center")
        self.tree.heading("#1", text = "Numero", anchor = "center")
        self.tree.heading("#2", text = "Email", anchor = "center")
        self.tree.heading("#3", text = "Direccion", anchor = "center")

        #Boton eliminar 
        ttk.Button(text="Eliminar").grid(row="20", column="0", sticky= W + E)

        #Boton enviar mail
        ttk.Button(text="Enviar Email").grid(row="20", column="1", sticky= W + E )

        #Boton enviar mensaje 
        ttk.Button(text="Enviar mensaje").grid(row="20", column = "2", sticky= W + E)

        #Boton ver lista de contactos
        ttk.Button(text="Ver lista de contactos").grid(row="20", column="3", sticky= W + E)

        #Boton editar contactos
        ttk.Button(text="Editar contacto").grid(row="20", column="4", columnspan= 3, sticky = E+ W)




if __name__=="__main__":
    window = Tk()
    app = Contactos(window)
    window.mainloop()

