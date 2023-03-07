#Librerías

import random
import tkinter as tk
import customtkinter as ctk


class villanous_app(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('blue')
        
        #Funciones para los botones
        def pedir_nombre():
            jugador = self.name_entry.get()
            self.jugadores.append(jugador)
            self.name_entry.delete(0, tk.END)

        def combinar_nombres():
            random.shuffle(self.villanos)
            result = ''
            for i, jugador in enumerate(self.jugadores):
                result += f"{jugador} juega con {self.villanos[i]}\n"
            self.result_label.configure(text=result)
        
        #Creamos las listas iniciales de la app
        self.jugadores = []
        self.villanos = ['Ursula',
            'Capitán Garfio',
            'Príncipe Juan',
            'Reina de Corazones',
            'Jafar',
            'Maléfica',
            'Cruela de Vil',
            'Pete',
            'Madre Gothel']
        
        #Configuramos la ventana inicial
        self.geometry('500x200')
        self.title('Villanous aleatorio')
        self.minsize(300,300)

        #Creamos una cuadrícula de 3x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0,2), weight=1)

        #Añadimos resto de elementos de la app
        self.name_label = ctk.CTkLabel(self, text="Introduce un nombre:")
        self.name_label.grid(row=0, column=0)

        self.name_entry = ctk.CTkEntry(self)
        self.name_entry.grid(row=0, column=1)
        self.name_entry.bind('<Return>', lambda event: pedir_nombre())
                             
        self.add_button = ctk.CTkButton(self, text="Añadir", command=pedir_nombre)
        self.add_button.grid(row=0, column=2)

        self.attach_button = ctk.CTkButton(self, text="Villano", command=combinar_nombres)
        self.attach_button.grid(row=1, column=0, columnspan=3)

        self.result_label = ctk.CTkLabel(self, text="")
        self.result_label.grid(row=2, column=0, columnspan=3, pady=20)

        
    
if __name__ == '__main__':
    app = villanous_app()
    app.mainloop()