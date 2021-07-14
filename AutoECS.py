"""
Import tkinter
@mca 13/07/2021
"""
import os
import tkinter as tk
from tkinter import *

"""
This section create the instance of the main window and configure it
@mca 13/07/2021
"""
root = tk.Tk()
root.title("AutoECS")
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='favicon.png'))
root.geometry("1280x720")
root.config(bg="#1d1f26")
root.resizable(0,0)

"""
This section create the frames where the elements will go
@mca 13/07/2021
"""
# menu frame
menu_frame = Frame(root)
menu_frame.pack(side=LEFT, padx=20, pady=20, fill="both")
menu_frame.config(width="500", bg="#282a35")
# submenu frame
submenu_frame = Frame(menu_frame)
#submenu_frame.pack(side=LEFT, padx=20, pady=20, fill="both")
submenu_frame.config(width="10", bg="red")
# log frame
log_frame = Frame(root)
log_frame.pack(side=RIGHT, padx=20, pady=20, fill="both")
log_frame.config(width="650")

"""
This section creates two text widgets to simulate the output of a terminal
@mca 13/07/2021
"""
# ASCII art
help_title = r"""
            █████╗ ██╗   ██╗████████╗ ██████╗ ███████╗ ██████╗███████╗
           ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔════╝██╔════╝██╔════╝
           ███████║██║   ██║   ██║   ██║   ██║█████╗  ██║     ███████╗
           ██╔══██║██║   ██║   ██║   ██║   ██║██╔══╝  ██║     ╚════██║
           ██║  ██║╚██████╔╝   ██║   ╚██████╔╝███████╗╚██████╗███████║
           ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝╚══════╝
"""
log_title = r"""
 ██╗      ██████╗  ██████╗ 
 ██║     ██╔═══██╗██╔════╝ 
 ██║     ██║   ██║██║  ███╗
 ██║     ██║   ██║██║   ██║
 ███████╗╚██████╔╝╚██████╔╝
 ╚══════╝ ╚═════╝  ╚═════╝ 
"""
# Help text
help = r"""
Este programa simplifica el proceso de BurnIn en los equipos fabricados:

»El modo automático pasará por todas las acciones hasta realizar todo el
proceso de forma automatica.
»El menú de acciones permite al usuario realizar una acción especifica.




Segun el color en los de las opciones significa una cosa u otra:

»Azul: La opcion se puede utilizar con normalidad, no requiere permisos
       de administrador.

»Naranja: La opcion requiere permisos de administrador, si no se ha 
          ininiciado el programa como administrador es necesario 
          reiniciarlo y abrirlo con los permisos correspondientes.

»Rojo: Se utiliza para marcar la opcion de volover atras, o en caso de
       error.

»Morado: Se utiliza para marcar la opcion de ayuda.





Made by: MCA
Contact: m.capdet@e-corp.es
"""
# This function put the help title and text when user press the help button
def help_mode():
    output_title.config(state=NORMAL)
    output_title.delete('1.0', END)
    output_title.insert(END, help_title)
    output_title.config(state=DISABLED)
    output.config(state=NORMAL)
    output.delete('1.0', END)
    output.insert(END, help)
    output.config(state=DISABLED)
# This function put the log title when user realizes an action
def log_mode():
    output_title.config(state=NORMAL)
    output_title.delete('1.0', END)
    output_title.insert(END, log_title)
    output_title.config(state=DISABLED)
# Create the output_title text widget and configure
output_title = Text(log_frame, fg='#37d3ff', bg='#282a35', bd=10, highlightthickness=4, highlightcolor="#37d3ff", highlightbackground="#37d3ff", borderwidth=4)
output_title.config(width=79, height=8, cursor="pencil")
output_title.place(x=0, y=0)
# Create the output text widget and configure
output = Text(log_frame, fg='white', bg='#282a35', bd=10, highlightthickness=4, highlightcolor="#37d3ff", highlightbackground="#37d3ff", borderwidth=4)
help_mode()
output.config(width=79, height=31, state=DISABLED, cursor="pencil")
output.place(x=0, y=137)
# Define the colors for the affirmative / negative / neutral outputs
output.tag_config('success', foreground="green")
output.tag_config('fail', foreground="red")
output.tag_config('warning', foreground="orange")
output.tag_config('neutral', foreground="purple")

"""
This section create a button to call a function that goes through all actions automatically
@mca 13/07/2021
"""
# This function goes through all actions automatically
def auto():
    return 0
# Create a button to call the auto mode function
auto_button = Button(menu_frame, text="Modo Automático", command=auto)
auto_button.pack(padx=50, pady=25)
auto_button.config(width=53, height=5, cursor="gumby")

"""
This section create a button to call a function that goes through all actions automatically
@mca 13/07/2021
"""
# This function shows all the actions that the user can perform
def actions_menu():
    return 0
# Create a button to call the actions menu function
actions_menu_button = Button(menu_frame, text="Acciones", command=actions_menu)
actions_menu_button.pack(padx=50, pady=25)
actions_menu_button.config(width=53, height=5, cursor="spider")

"""
This section create a button to show the help in the output
@mca 13/07/2021
"""
# Create a button to show the help in the output
help_button = Button(menu_frame, text="Ayuda", command=help_mode)
help_button.pack()
help_button.config(width=23, height=3, cursor="question_arrow")
help_button.place(x=50, y=590)

"""
This section create a button to exit the program
@mca 13/07/2021
"""
# Create a button to exit the program
exit_button = Button(menu_frame, text="Salir", command=root.destroy)
exit_button.pack()
exit_button.config(width=23, height=3, cursor="X_cursor")
exit_button.place(x=290, y=590)








################################################################
# TESTIIIN
def jaja():
    # Cambia el titulo del log
    log_mode()
    # Cambia el contenido del log
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
a_button = Button(root, text="test", command=jaja)
a_button.place(x=1, y=1)
################################################################




# Launch the app
root.mainloop()
