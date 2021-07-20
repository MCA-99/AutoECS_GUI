"""
Import tkinter
@mca 13/07/2021
"""
import os
import tkinter as tk
from tkinter import *
import tkinter.font as font

"""
This section create the instance of the main window and configure it
@mca 13/07/2021
"""
root = tk.Tk()
root.title("AutoECS")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='favicon.png'))
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
menu_frame.config(width=500, bg="#282a35", highlightthickness=3, highlightcolor="#37d3ff", highlightbackground="#75D7EC")
# submenu frame
submenu_frame = Frame(menu_frame)
submenu_frame.pack(padx=20, pady=20)
submenu_frame.config(width=1, height=1, bg="#282a35")
submenu_frame.place(x=50, y=280)
# log frame
log_frame = Frame(root)
log_frame.pack(side=RIGHT, padx=20, pady=20, fill="both")
log_frame.config(width=650, bg="#1d1f26")

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





 Made by: 𝓜𝓒𝓐
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
output_title = Text(log_frame, fg='#FF5555', bg='#282a35', highlightthickness=3, highlightcolor="#37d3ff", highlightbackground="#75D7EC")
output_title.config(width=79, height=8, cursor="pencil")
output_title.place(x=0, y=0)
# Create the output text widget and configure
output = Text(log_frame, fg='white', bg='#282a35', highlightthickness=3, highlightcolor="#37d3ff", highlightbackground="#75D7EC")
help_mode()
output.config(width=79, height=31, state=DISABLED, cursor="pencil")
output.place(x=0, y=143)
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
    map_network_drives()
    update_sys_time()
    open_device_manager()
    open_disk_manager()
    update_sys()
    bit()
    activate_sys()
    unmap_network_drives()
# Create a button to call the auto mode function
auto_icon = PhotoImage(file="auto.png")
auto_font = font.Font(family="Verdana", size=16)
auto_button = Button(menu_frame, text="Modo Automático", image=auto_icon, compound=LEFT, font=auto_font, command=auto)
auto_button.pack(padx=50, pady=25)
auto_button.config(width=425, height=85, cursor="center_ptr", bg="#42E66C", highlightthickness=0, activebackground='#50FA7B')

"""
This section create a button to call a function that goes through all actions automatically
@mca 13/07/2021
"""
# This function shows or hide all the actions that the user can perform
def actions_menu():
    submenu_frame_width = submenu_frame.winfo_width()
    if submenu_frame_width == 1:
        submenu_frame.config(width=450, height=300)
    if submenu_frame_width == 450:
        submenu_frame.config(width=1, height=1)
# Create a button to call the actions menu function
actions_menu_button_icon = PhotoImage(file="actions.png")
actions_menu_button_font = font.Font(family="Verdana", size=16)
actions_menu_button = Button(menu_frame, text="Acciones", image=actions_menu_button_icon, compound=LEFT, font=actions_menu_button_font ,command=actions_menu)
actions_menu_button.pack(padx=50, pady=25)
actions_menu_button.config(width=425, height=85, cursor="center_ptr", bg="#EFA554", highlightthickness=0, activebackground='#FFB86C')

"""
This section create a button to call a function that map network drives
@mca 16/07/2021
"""
# This function map network drives
def map_network_drives():
    log_mode()
    output.config(state=NORMAL)
    output.delete('1.0', END)
    output.insert(END, "\n")
    output.insert(END, " Mapeando unidades de red...\n")
    try:
        command1 = os.system("net use X: \\\\MASTERS\\drivers /persistent:no")
        command2 = os.system("net use Z: \\\\MASTERS\\informes /persistent:no")
        if (command1 | command2) == 0:
            output.insert(END, "\n ######## COMPLETADO ########", "success")
        elif (command1 | command2) != 0:
             raise Exception()
    except:
        output.insert(END, "\n No se puede conectar con el servidor, o las unidades ya estan mapeadas...", "fail")
#Create a button to call map_network_drives
map_network_drives_button = Button(submenu_frame, text="Mapear unidades", command=map_network_drives)
map_network_drives_button.config(width=20, height=2, bg="#5473d6", highlightthickness=0, activebackground='#788ed6', cursor="center_ptr")
map_network_drives_button.place(x=20, y=12)

"""
This section create a button to call a function that unmap network drives
@mca 16/07/2021
"""
# This function umap network drives
def unmap_network_drives():
    log_mode()
    output.config(state=NORMAL)
    output.delete('1.0', END)
    output.insert(END, "\n")
    output.insert(END, " Desmapeando unidades de red...\n")
    try:
        command = os.system("net use * /delete /y")
        if command == 0:
            output.insert(END, "\n ######## COMPLETADO ########", "success")
        elif command != 0:
            raise Exception()
    except:
        output.insert(END, "\n No se puede desmapear las unidades de red...", "fail")
#Create a button to call map_network_drives
unmap_network_drives_button = Button(submenu_frame, text="Desmapear unidades", command=unmap_network_drives)
unmap_network_drives_button.config(width=20, height=2, bg="#5473d6", highlightthickness=0, activebackground='#788ed6', cursor="center_ptr")
unmap_network_drives_button.place(x=20, y=68)

"""
This section create a button to call a function that update system time
@mca 16/07/2021
"""
# This function update system time
def update_sys_time():
    log_mode()
    output.config(state=NORMAL)
    output.delete('1.0', END)
    output.insert(END, "\n")
    output.insert(END, " Actualizando la Hora del Sistema...\n")
    try:
        try:
            output.insert(END, "\n Comprobando si el servicio de tiempo esta iniciado...", "warning")
            command1 = os.system("net start w32time")
            if command1 == 0:
                pass
            else:
                raise Exception()
        except:
            output.insert(END, "\n No se puede comprobar si el servicio de tiempo se puede iniciar...", "fail")
        try:
            output.insert(END, "\n Sincronizando hora con el servidor time.windows.com...", "warning")
            command2 = os.system("w32tm /resync")
            if command2 == 0:
                pass
            else:
                raise Exception()
        except:
            output.insert(END, "\n No se puede sincronizar la hora con el servidor...", "fail")

        if (command1 | command2) == 0:
            output.insert(END, "\n\n ######## COMPLETADO ########", "success")
        elif (command1 | command2) != 0:
             raise Exception()
    except:
        output.insert(END, "\n\n No se puede actualizar la hora del sistema", "fail")
#Create a button to call map_network_drives
update_sys_time_button = Button(submenu_frame, text="Actualizar Hora", command=update_sys_time)
update_sys_time_button.config(width=20, height=2, bg="#EFA554", highlightthickness=0, activebackground='#FFB86C', cursor="center_ptr")
update_sys_time_button.place(x=20, y=124)

"""
This section create a button to call a function that open install system updates
@mca 16/07/2021
"""
# This function call wumpt to update system
def update_sys():
    log_mode()
    output.config(state=NORMAL)
    output.delete('1.0', END)
    output.insert(END, "\n")
    output.insert(END, " Actualizando el sistema...\n")
#Create a button to call map_network_drives
update_sys_button = Button(submenu_frame, text="Actualizar el sistema", command=update_sys)
update_sys_button.config(width=20, height=2, bg="#5473d6", highlightthickness=0, activebackground='#788ed6', cursor="center_ptr")
update_sys_button.place(x=20, y=180)

"""
This section create a button to call a function that open device manager
@mca 16/07/2021
"""
# This function open the activation wizard
def activate_sys():
    log_mode()
    output.config(state=NORMAL)
    output.delete('1.0', END)
    output.insert(END, "\n")
    output.insert(END, " ACTIVAR EL SISTEMA\n")
#Create a button to call map_network_drives
activate_sys_button = Button(submenu_frame, text="Activar el sistema", command=activate_sys)
activate_sys_button.config(width=20, height=2, bg="#5473d6", highlightthickness=0, activebackground='#788ed6', cursor="center_ptr")
activate_sys_button.place(x=20, y=236)

"""
This section create a button to call a function that open device manager
@mca 16/07/2021
"""
# This function open the device manager in order to install drivers if necessary
def open_device_manager():
    log_mode()
    output.config(state=NORMAL)
    output.delete('1.0', END)
    output.insert(END, "\n")
    output.insert(END, " INSTALAR DRIVERS\n")
#Create a button to call map_network_drives
open_device_manager_button = Button(submenu_frame, text="Instalar Drivers", command=open_device_manager)
open_device_manager_button.config(width=20, height=2, bg="#5473d6", highlightthickness=0, activebackground='#788ed6', cursor="center_ptr")
open_device_manager_button.place(x=240, y=12)

"""
This section create a button to call a function that open disk manager
@mca 16/07/2021
"""
# This function open the disk manager
def open_disk_manager():
    log_mode()
    output.config(state=NORMAL)
    output.delete('1.0', END)
    output.insert(END, "\n")
    output.insert(END, " COMRPOBAR PARTICIONES\n")
#Create a button to call map_network_drives
open_disk_manager_button = Button(submenu_frame, text="Comprobar particiones", command=open_disk_manager)
open_disk_manager_button.config(width=20, height=2, bg="#5473d6", highlightthickness=0, activebackground='#788ed6', cursor="center_ptr")
open_disk_manager_button.place(x=240, y=68)

"""
This section create a button to call a function that open BIT
@mca 16/07/2021
"""
# This function open the BIT
def bit():
    log_mode()
    output.config(state=NORMAL)
    output.delete('1.0', END)
    output.insert(END, "\n")
    output.insert(END, " BIT\n")
#Create a button to call map_network_drives
bit_button = Button(submenu_frame, text="BurnInTest", command=bit)
bit_button.config(width=20, height=2, bg="#5473d6", highlightthickness=0, activebackground='#788ed6', cursor="center_ptr")
bit_button.place(x=240, y=124)

"""
This section create a button to show the help in the output
@mca 13/07/2021
"""
# Create a button to show the help in the output
help_button_icon = PhotoImage(file="help.png")
help_button_font = font.Font(family="Verdana", size=16)
help_button = Button(menu_frame, text="Ayuda", command=help_mode)
help_button.pack()
help_button.config(width=184, height=52, cursor="question_arrow", bg="#9B6BDF", highlightthickness=0, activebackground='#BD93F9', font=help_button_font, compound=LEFT, image=help_button_icon)
help_button.place(x=50, y=590)

"""
This section create a button to exit the program
@mca 13/07/2021
"""
# Create a button to exit the program
exit_button_icon = PhotoImage(file="exit.png")
exit_button_font = font.Font(family="Verdana", size=16)
exit_button = Button(menu_frame, text="Salir", command=root.destroy)
exit_button.pack()
exit_button.config(width=184, height=52, cursor="X_cursor", bg="#E64747", highlightthickness=0, activebackground='#FF5555', font=exit_button_font, compound=LEFT, image=exit_button_icon)
exit_button.place(x=290, y=590)

# Launch the app
root.mainloop()
