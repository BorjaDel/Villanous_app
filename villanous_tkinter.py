#Librerías

import random
import tkinter as tk


#Variables

nombres = []
villanos = ['Ursula',
            'Capitán Garfio',
            'Príncipe Juan',
            'Reina de Corazones',
            'Jafar',
            'Maléfica',
            'Cruela de Vil',
            'Pete',
            'Madre Gothel']


#Funciones a asignar a los botones

def pedir_nombre():
    nombre = name_entry.get()
    nombres.append(nombre)
    name_entry.delete(0, tk.END)

def combinar_nombres():
    random.shuffle(villanos)
    result = ''
    for i, nombre in enumerate(nombres):
        result += f"{nombre} juega con {villanos[i]}\n"
    result_label.config(text=result)


#Creación de la interfaz

root = tk.Tk()
root.title("Tu villano aleatorio")

name_label = tk.Label(root, text="Introduce un nombre:")
name_label.grid(row=0, column=0)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

add_button = tk.Button(root, text="Añadir", command=pedir_nombre)
add_button.grid(row=0, column=2)

attach_button = tk.Button(root, text="Seleccionar villano", command=combinar_nombres)
attach_button.grid(row=1, column=0, columnspan=3)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=3)

root.mainloop()