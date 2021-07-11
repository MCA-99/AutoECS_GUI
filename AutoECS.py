# Importes
import os
import tkinter as tk
from tkinter import *

# Creamos la intancia de la ventana principal y la configuramos
root = tk.Tk()
root.title("AutoECS")
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='favicon.png'))
root.geometry("1280x720")
root.resizable(False, False)

# Otuput de los comandos ejecutados
title = r"""
 ██       ██████   ██████  
 ██      ██    ██ ██       
 ██      ██    ██ ██   ███ 
 ██      ██    ██ ██    ██ 
 ███████  ██████   ██████

██████████████████████████████████████████████████████████████████████████████████████████"""
output_title = Text(root, bg="white", bd=0, highlightthickness = 0, borderwidth=0, state=NORMAL)
output_title.insert(END, title)
output_title.config(state=DISABLED)
output_title.config(width=90, height=8)
output_title.place(x=550, y=9)

output = Text(root, bg="white", bd=0, highlightthickness = 0, borderwidth=0, state=DISABLED, yscrollcommand=TRUE)
output.config(width=90, height=33)
output.place(x=550, y=148)


# Definimos los colores para los outputs afirmativos/negativos/neutro
output.tag_config('success', foreground="green")
output.tag_config('fail', foreground="red")
output.tag_config('warning', foreground="orange")
output.tag_config('neutral', foreground="purple")

# Modo automatico
def jaja():
    return 0

auto_button = Button(text="Auto", command=jaja)
auto_button.place(x=50, y=50)


# Acciones
def menu_acciones():
    return 0

auto_button = Button(text="Acciones", command=menu_acciones)
auto_button.place(x=50, y=80)

# Salir
auto_button = Button(text="Salir", command=root.destroy)
auto_button.place(x=50, y=680)




################################################################
# TESTIIIN
def jaja():
    output.config(state=NORMAL)
    output.delete('1.0', END)
    output.insert(END, "\n")
    output.insert(END, "Haciendo ping a google:\n")
    command = os.system("ping -c 1 google.es")
    output.insert(END, "\nResultado: ")
    if command == 0:
        output.insert(END, "CORRECTO AFIRMATIVO\n", "success")
    else:
        output.insert(END, "FRACASO TOTAL\n", "fail")
    output.config(state=DISABLED)

a_button = Button(text="test", command=jaja)
a_button.place(x=1, y=1)
################################################################





# Lanza la aplicación
root.mainloop()