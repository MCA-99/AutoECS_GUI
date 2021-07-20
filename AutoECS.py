"""
Import tkinter
@mca 13/07/2021
"""
import os
import ctypes
import tkinter as tk
from tkinter import *
import tkinter.font as font
from tkinter import simpledialog
from tkinter import messagebox

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
menu_frame.pack(side=LEFT, padx=22, pady=20, fill="both")
menu_frame.config(width=500, bg="#282a35", highlightthickness=3, highlightcolor="#37d3ff", highlightbackground="#75D7EC")
# submenu frame
submenu_frame = Frame(menu_frame)
submenu_frame.pack(padx=22, pady=20)
submenu_frame.config(width=1, height=1, bg="#282a35")
submenu_frame.place(x=50, y=275)
# log frame
log_frame = Frame(root)
log_frame.pack(side=RIGHT, padx=22, pady=20, fill="both")
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
# This function put the help title and text when user press the help button
def help_mode():
    output_title.config(state=NORMAL)
    output_title.delete('1.0', END)
    output_title.insert(END, help_title)
    output_title.config(state=DISABLED)
    output.config(state=NORMAL)
    output.delete('1.0', END)
    output.insert(END, "\n\n Este programa simplifica el proceso de BurnIn en los equipos fabricados:\n")
    output.insert(END, "\n » El modo automático pasará por todas las acciones hasta realizar todo el\n", "helptext")
    output.insert(END, "   proceso de forma automatica.\n", "helptext")
    output.insert(END, " » El menú de acciones permite al usuario realizar una acción especifica.\n\n\n\n\n\n", "helptext")
    output.insert(END, " Segun el color en los de las opciones significa una cosa u otra:\n\n")
    output.insert(END, " » Azul:", "normal")
    output.insert(END, " La opcion se puede utilizar con normalidad, no requiere permisos\n")
    output.insert(END, "         de administrador.\n\n")
    output.insert(END, " » Naranja:", "admin")
    output.insert(END, " La opcion requiere permisos de administrador, si no se ha\n")
    output.insert(END, "            ininiciado el programa como administrador es necesario\n")
    output.insert(END, "            reiniciarlo y abrirlo con los permisos correspondientes.\n\n")
    output.insert(END, " » Rojo:", "exit")
    output.insert(END, " Se utiliza para marcar la opcion de volover salir.\n\n")
    output.insert(END, " » Morado:", "help")
    output.insert(END, " Se utiliza para marcar la opcion de ayuda.\n\n\n\n\n\n")
    output.insert(END, " Made by: 𝓜𝓒𝓐\n")
    output.insert(END, " Contact: m.capdet@e-corp.es")    
    output.config(state=DISABLED)
# This function put the log title when user realizes an action
def log_mode():
    output_title.config(state=NORMAL)
    output_title.delete('1.0', END)
    output_title.insert(END, log_title)
    output_title.config(state=DISABLED)
# Create the output_title text widget and configure
output_title = Text(log_frame, fg='#FF5555', bg='#282a35', highlightthickness=3, highlightcolor="#37d3ff", highlightbackground="#75D7EC")
output_title.config(width=80, height=8, cursor="pencil")
output_title.place(x=0, y=0)
# Create the output text widget and configure
output = Text(log_frame, fg='white', bg='#282a35', highlightthickness=3, highlightcolor="#37d3ff", highlightbackground="#75D7EC")
help_mode()
output.config(width=80, height=33, state=DISABLED, cursor="pencil")
output.place(x=0, y=143)
# Define the colors for the output tags
output.tag_config('helptext', foreground="#42E66C")
output.tag_config('normal', foreground="#5473d6")
output.tag_config('admin', foreground="#EFA554")
output.tag_config('exit', foreground="#E64747")
output.tag_config('help', foreground="#9B6BDF")
output.tag_config('success', foreground="#42E66C")
output.tag_config('fail', foreground="#E64747")
output.tag_config('warning', foreground="#EFA554")

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
    activate_sys()
    bit()
    unmap_network_drives()
# Create a button to call the auto mode function
auto_icon = PhotoImage(file="auto.png")
auto_font = font.Font(family="Verdana", size=16)
auto_button = Button(menu_frame, text="Modo Automático", image=auto_icon, compound=LEFT, font=auto_font, command=auto)
auto_button.pack(padx=50, pady=25)
auto_button.config(width=425, height=85, cursor="hand1", bg="#42E66C", highlightthickness=0, activebackground='#50FA7B')

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
actions_submenu_button_font = font.Font(family="Verdana", size=9)
actions_menu_button_font = font.Font(family="Verdana", size=16)
actions_menu_button = Button(menu_frame, text=" Acciones", image=actions_menu_button_icon, compound=LEFT, font=actions_menu_button_font ,command=actions_menu)
actions_menu_button.pack(padx=50, pady=25)
actions_menu_button.config(width=425, height=85, cursor="hand1", bg="#EFA554", highlightthickness=0, activebackground='#FFB86C')

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
        output.insert(END, "\n Conectando con x:\\\\Masters\drivers\\", "warning")
        command1 = os.system('net use X: \\\\MASTERS\\drivers /persistent:no')
        if command1 == 0:
            output.insert(END, "\n » OK!", "success")
            pass
        else:
            raise Exception()
    except:
        output.insert(END, "\n » No se puede conectar con \\\\Masters\drivers\\ o la unidad ya esta mapeada", "fail")
    try:
        output.insert(END, "\n Conectando con z:\\\\Masters\informes\\", "warning")
        command2 = os.system('net use Z: \\\\MASTERS\\informes /persistent:no')
        if command2 == 0:
            output.insert(END, "\n » OK!", "success")
            pass
        else:
            raise Exception()
    except:
        output.insert(END, "\n » No se puede conectar con \\\\Masters\informes\\ o la unidad ya esta mapeada", "fail")

    if command1 == 0 & command2 == 0:
        output.insert(END, "\n\n ######## COMPLETADO ########", "success")
    else:
        output.insert(END, "\n\n ######## COMPLETADO ########", "fail")

#Create a button to call map_network_drives
map_network_drives_button = Button(submenu_frame, text="Mapear unidades", command=map_network_drives)
map_network_drives_button.config(width=22, height=3, bg="#5473d6", highlightthickness=0, activebackground='#788ed6', cursor="hand1", font=actions_submenu_button_font)
map_network_drives_button.place(x=22, y=0)

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
        command = os.system('net use * /delete /y')
        if command == 0:
            output.insert(END, "\n » OK!", "success")
            output.insert(END, "\n\n ######## COMPLETADO ########", "success")
        elif command != 0:
            raise Exception()
    except:
        output.insert(END, "\n » No se puede desmapear las unidades de red", "fail")
        output.insert(END, "\n\n ######## COMPLETADO ########", "fail")
#Create a button to call map_network_drives
unmap_network_drives_button = Button(submenu_frame, text="Desmapear unidades", command=unmap_network_drives)
unmap_network_drives_button.config(width=22, height=3, bg="#5473d6", highlightthickness=0, activebackground='#788ed6', cursor="hand1", font=actions_submenu_button_font)
unmap_network_drives_button.place(x=22, y=63)

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
        output.insert(END, "\n Comprobando si el servicio de tiempo esta iniciado...", "warning")
        command1 = os.system('net start w32time')
        if command1 == 0:
            output.insert(END, "\n » OK!", "success")
            pass
        else:
            raise Exception()
    except:
        output.insert(END, "\n » El servicio ya esta iniciado o no se puede iniciar", "fail")
    try:
        output.insert(END, "\n Sincronizando hora con el servidor time.windows.com...", "warning")
        command2 = os.system('w32tm /resync')
        if command2 == 0:
            output.insert(END, "\n » OK!", "success")
            pass
        else:
            raise Exception()
    except:
        output.insert(END, "\n » No se puede sincronizar la hora con el servidor...", "fail")

    if command1 == 0 & command2 == 0:
        output.insert(END, "\n\n ######## COMPLETADO ########", "success")
    else:
        output.insert(END, "\n\n ######## COMPLETADO ########", "fail")

#Create a button to call map_network_drives
update_sys_time_button = Button(submenu_frame, text="Actualizar Hora", command=update_sys_time)
update_sys_time_button.config(width=22, height=3, bg="#EFA554", highlightthickness=0, activebackground='#FFB86C', cursor="hand1", font=actions_submenu_button_font)
update_sys_time_button.place(x=22, y=124)

"""
This section create a button to call a function that open install system updates
@mca 16/07/2021
"""
# This function moves WUMT into pc and open to update system
def update_sys():
    log_mode()
    output.config(state=NORMAL)
    output.delete('1.0', END)
    output.insert(END, "\n")
    output.insert(END, " Actualizando el sistema...\n")
    try:
        output.insert(END, "\n Moviendo WUMT al equipo...", "warning")
        command1 = os.system('copy ""X:\\programas\\wumt.exe"" "".""')
        if command1 == 0:
            output.insert(END, "\n » OK!", "success")
            pass
        else:
            raise Exception()
    except:
        output.insert(END, "\n » No se ha podido mover el WUMT al equipo", "fail")
    try:
        output.insert(END, "\n Abriendo WUMT...", "warning")
        command2 = os.system('wumt.exe')
        if command2 == 0:
            output.insert(END, "\n » OK!", "success")
            pass
        else:
            raise Exception()
    except:
        output.insert(END, "\n » No se puede abrir el WUMT", "fail")
    try:
        output.insert(END, "\n Limpiando...", "warning")
        command3 = os.system('del ""wumt.exe""')
        if command3 == 0:
            output.insert(END, "\n » OK!", "success")
            pass
        else:
            raise Exception()
    except:
        output.insert(END, "\n » No se ha podido efectuar la limpieza", "fail")

    if command1 == 0 & command2 == 0 & command3 == 0:
        output.insert(END, "\n\n ######## COMPLETADO ########", "success")
    else:
        output.insert(END, "\n\n ######## COMPLETADO ########", "fail")

#Create a button to call map_network_drives
update_sys_button = Button(submenu_frame, text="Actualizar el sistema", command=update_sys)
update_sys_button.config(width=22, height=3, bg="#EFA554", highlightthickness=0, activebackground='#FFB86C', cursor="hand1", font=actions_submenu_button_font)
update_sys_button.place(x=22, y=185)

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
    output.insert(END, " Abriendo la ventana de activación del sistema...\n")
    try:
        command = os.system('start ms-settings:activation')
        if command == 0:
            output.insert(END, "\n » OK!", "success")
            output.insert(END, "\n\n ######## COMPLETADO ########", "success")
        elif command != 0:
            raise Exception()
    except:
        output.insert(END, "\n » No se ha podido abrir la ventana de activación del sistema", "fail")
        output.insert(END, "\n\n ######## COMPLETADO ########", "fail")
#Create a button to call map_network_drives
activate_sys_button = Button(submenu_frame, text="Activar el sistema", command=activate_sys)
activate_sys_button.config(width=22, height=3, bg="#5473d6", highlightthickness=0, activebackground='#788ed6', cursor="hand1", font=actions_submenu_button_font)
activate_sys_button.place(x=22, y=246)

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
    output.insert(END, " Abriendo el administrador de dispositivos...\n")
    try:
        command = os.system('devmgmt.msc')
        if command == 0:
            output.insert(END, "\n » OK!", "success")
            output.insert(END, "\n\n ######## COMPLETADO ########", "success")
        elif command != 0:
            raise Exception()
    except:
        output.insert(END, "\n » No se ha podido abrir el administrador de dispositivos", "fail")
        output.insert(END, "\n\n ######## COMPLETADO ########", "fail")
#Create a button to call map_network_drives
open_device_manager_button = Button(submenu_frame, text="Instalar Drivers", command=open_device_manager)
open_device_manager_button.config(width=22, height=3, bg="#5473d6", highlightthickness=0, activebackground='#788ed6', cursor="hand1", font=actions_submenu_button_font)
open_device_manager_button.place(x=222, y=0)

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
    output.insert(END, " Abriendo el gestor de particiones...\n")
    try:
        command = os.system('diskmgmt.msc')
        if command == 0:
            output.insert(END, "\n » OK!", "success")
            output.insert(END, "\n\n ######## COMPLETADO ########", "success")
        elif command != 0:
            raise Exception()
    except:
        output.insert(END, "\n » No se ha podido abrir el gestor de particiones", "fail")
        output.insert(END, "\n\n ######## COMPLETADO ########", "fail")
#Create a button to call map_network_drives
open_disk_manager_button = Button(submenu_frame, text="Comprobar particiones", command=open_disk_manager)
open_disk_manager_button.config(width=22, height=3, bg="#5473d6", highlightthickness=0, activebackground='#788ed6', cursor="hand1", font=actions_submenu_button_font)
open_disk_manager_button.place(x=222, y=63)

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
    output.insert(END, " Abriendo BurnInTest...\n")
    try:
        output.insert(END, "\n Moviendo BIT al equipo...", "warning")
        command1 = os.system('Xcopy /E /I /Y ""X:\\programas\\BurnInTest"" ""BurnInTest""')
        if command1 == 0:
            output.insert(END, "\n » OK!", "success")
            pass
        else:
            raise Exception()
    except:
        output.insert(END, "\n » No se ha podido mover el BIT al equipo", "fail")
    try:
        output.insert(END, "\n Abriendo el BIT...", "warning")
        command2 = os.system('.\\BurninTest\\bit.exe /c .\\BurninTest\\config.bitcfg /r""')
        if command2 == 0:
            output.insert(END, "\n » OK!", "success")
            pass
        else:
            raise Exception()
    except:
        output.insert(END, "\n » No se ha podido abrir el BIT", "fail")
    try:
        output.insert(END, "\n Renombrando el informe...", "warning")
        if command2 == 0:
            num_serie = simpledialog.askstring(title="Numero de Seria", prompt="Introduce el numero de serie del equipo:")
        command3 = os.system('MOVE c:\informe.htm c:\"' + num_serie + '".htm')
        if command3 == 0:
            output.insert(END, "\n » OK!", "success")
            pass
        else:
            raise Exception()
    except:
        output.insert(END, "\n » No se ha cambiar el nombre al informe", "fail")
    try:
        output.insert(END, "\n Moviendo el informe a z:\\\\Masters\informes\\...", "warning")
        command4 = os.system('move "'+num_serie+'".htm Z:')
        if command4 == 0:
            output.insert(END, "\n » OK!", "success")
            pass
        else:
            raise Exception()
    except:
        output.insert(END, "\n » No se ha podido mover el informe a z:\\\\Masters\informes\\", "fail")
    try:
        output.insert(END, "\n Limpiando...", "warning")
        command5 = os.system('rmdir /Q /S ""BurnInTest""')
        if command5 == 0:
            output.insert(END, "\n » OK!", "success")
            pass
        else:
            raise Exception()
    except:
        output.insert(END, "\n » No se ha podido efectuar la limpieza", "fail")
    
    if command1 == 0 & command2 == 0 & command3 == 0 & command4 == 0 & command5 == 0:
        output.insert(END, "\n\n ######## COMPLETADO ########", "success")
    else:
        output.insert(END, "\n\n ######## COMPLETADO ########", "fail")

#Create a button to call map_network_drives
bit_button = Button(submenu_frame, text="BurnInTest", command=bit)
bit_button.config(width=22, height=3, bg="#EFA554", highlightthickness=0, activebackground='#FFB86C', cursor="hand1", font=actions_submenu_button_font)
bit_button.place(x=222, y=124)

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

"""
This section check if the programm run as admin
@mca 20/07/2021
"""
def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

if isAdmin():
    pass
else:
    messagebox.showinfo("¡AVISO!","No has iniciado el programa con permisos de adminitrador, puede que algunas funciones no se ejecuten correctamente.")

"""
This section create the instance of the main window and configure it
@mca 13/07/2021
"""

# Launch the app
root.mainloop()