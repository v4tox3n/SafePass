# Importar librerías necesarias
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import file2
import file4
import os

# Configuración y creación de la ventana
root = tk.Tk()
root.resizable(0, 0)
root.geometry("500x300")
root.iconbitmap("")
root.title("")
root.configure(bg="white")

# Funciones del script
def guardar_contraseña(event): 
    file2.createWindow()
    
# Mensages menú desplegable
def opcion1():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[0])

    file4.createWindow()


def opcion2():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[1])

    file4.createWindow()


def opcion3():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[2])

    file4.createWindow()


def opcion4():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[3])

    file4.createWindow()


def opcion5():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[4])

    file4.createWindow()


def opcion6():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[5])

    file4.createWindow()


def opcion7():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[6])

    file4.createWindow()


def opcion8():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[7])

    file4.createWindow()


def opcion9():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[8])

    file4.createWindow()


def opcion10():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[9])

    file4.createWindow()


def opcion11():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[10])

    file4.createWindow()


def opcion12():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[11])

    file4.createWindow()


def opcion13():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[12])

    file4.createWindow()


def opcion14():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[13])

    file4.createWindow()


def opcion15():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[14])

    file4.createWindow()


def opcion16():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[15])

    file4.createWindow()


def opcion17():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[16])

    file4.createWindow()


def opcion18():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[17])

    file4.createWindow()


def opcion19():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[18])

    file4.createWindow()


def opcion20():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[19])

    file4.createWindow()


def opcion21():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[20])

    file4.createWindow()


def opcion22():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[21])

    file4.createWindow()


def opcion23():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[22])

    file4.createWindow()


def opcion24():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[23])

    file4.createWindow()


def opcion25():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[24])

    file4.createWindow()


def opcion26():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[25])

    file4.createWindow()


def opcion27():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[26])

    file4.createWindow()


def opcion28():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[27])

    file4.createWindow()


def opcion29():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[28])

    file4.createWindow()


def opcion30():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[29])

    file4.createWindow()


def opcion31():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[30])

    file4.createWindow()


def opcion32():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[31])

    file4.createWindow()


def opcion33():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[32])

    file4.createWindow()


def opcion34():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[33])

    file4.createWindow()


def opcion35():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[34])

    file4.createWindow()


def opcion36():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[35])

    file4.createWindow()


def opcion37():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[36])

    file4.createWindow()


def opcion38():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[37])

    file4.createWindow()


def opcion39():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[38])

    file4.createWindow()


def opcion40():
    with open("Data/contraseñas.txt", 'w') as file:
        file.write(contras[39])

    file4.createWindow()

        
# Label título ventana "SafePass"
def aumentar_tamaño(event):
    label_titulo.config(font="Helvetica 35 bold", bg="gray")

def disminuir_tamaño(event):
    label_titulo.config(font="Helvetica 30", bg="#CCCCCC")
    
label_titulo = tk.Label(root, text="SafePass", fg="black", font="Helvetica 30", bg="#CCCCCC", cursor="hand2")
label_titulo.pack(pady=15)
label_titulo.bind("<Button-1>", guardar_contraseña)

label_titulo.bind("<Enter>", aumentar_tamaño)
label_titulo.bind("<Leave>", disminuir_tamaño)

# Crear el frame
frame = tk.Frame(root, bg="white")
frame.pack(pady=30)

# Label de frame
label_frame = tk.Label(frame, text="Selecciona la contraseña que quieres ver: ", fg="black", bg="white", font="Hevetica 12")
label_frame.pack(pady=5)

# Función para ejecutar la opción seleccionada
def ejecutar_opcion():
    seleccion = opcion_var.get()
    if seleccion == opciones[0]:
        opcion1()
         
    elif seleccion == opciones[1]:
        opcion2()
        
    elif seleccion == opciones[2]:
        opcion3()
        
    elif seleccion == opciones[3]:
        opcion4()
        
    elif seleccion == opciones[4]:
        opcion5()
        
    elif seleccion == opciones[5]:
        opcion6()
        
    elif seleccion == opciones[6]:
        opcion7()
        
    elif seleccion == opciones[7]:
        opcion8()
        
    elif seleccion == opciones[8]:
        opcion9()
        
    elif seleccion == opciones[9]:
        opcion10()
        
    elif seleccion == opciones[10]:
        opcion11()
        
    elif seleccion == opciones[11]:
        opcion12()
        
    elif seleccion == opciones[12]:
        opcion13()
        
    elif seleccion == opciones[13]:
        opcion14()
        
    elif seleccion == opciones[14]:
        opcion15()
        
    elif seleccion == opciones[15]:
        opcion16()
        
    elif seleccion == opciones[16]:
        opcion17()
        
    elif seleccion == opciones[17]:
        opcion18()
        
    elif seleccion == opciones[18]:
        opcion19()
        
    elif seleccion == opciones[19]:
        opcion20()
        
    elif seleccion == opciones[20]:
        opcion21()
        
    elif seleccion == opciones[21]:
        opcion22()
        
    elif seleccion == opciones[22]:
        opcion23()
        
    elif seleccion == opciones[23]:
        opcion24()
        
    elif seleccion == opciones[24]:
        opcion25()
        
    elif seleccion == opciones[25]:
        opcion26()
        
    elif seleccion == opciones[26]:
        opcion27()
        
    elif seleccion == opciones[27]:
        opcion28()
        
    elif seleccion == opciones[28]:
        opcion29()
        
    elif seleccion == opciones[29]:
        opcion30()
        
    elif seleccion == opciones[30]:
        opcion31()
        
    elif seleccion == opciones[31]:
        opcion32()
        
    elif seleccion == opciones[32]:
        opcion33()
        
    elif seleccion == opciones[33]:
        opcion34()
        
    elif seleccion == opciones[34]:
        opcion35()
        
    elif seleccion == opciones[35]:
        opcion36()
        
    elif seleccion == opciones[36]:
        opcion37()
        
    elif seleccion == opciones[37]:
        opcion38()
        
    elif seleccion == opciones[38]:
        opcion39()
        
    elif seleccion == opciones[39]:
        opcion40()
        

# Función de resetear todo
def resetear_aplicacion():
    import resetear_todo as reset
    reset.reseteo()
    
    messagebox.showinfo("Reseteo de la aplicación", "Se ha borrado toda la información de SafePass, cierra la ventana y vuelve a abrirla para ver los cambios.")
    root.destroy()

# Menú desplegable en la parte inferior del frame
archivos = ["Data/datos1.txt", "Data/datos2.txt", "Data/datos3.txt", "Data/datos4.txt",
            "Data/datos5.txt", "Data/datos6.txt", "Data/datos7.txt", "Data/datos8.txt",
            "Data/datos9.txt", "Data/datos10.txt", "Data/datos11.txt", "Data/datos12.txt",
            "Data/datos13.txt", "Data/datos14.txt", "Data/datos15.txt", "Data/datos16.txt",
            "Data/datos17.txt", "Data/datos18.txt", "Data/datos19.txt", "Data/datos20.txt",
            "Data/datos21.txt", "Data/datos22.txt", "Data/datos23.txt", "Data/datos24.txt",
            "Data/datos25.txt", "Data/datos26.txt", "Data/datos27.txt", "Data/datos28.txt",
            "Data/datos29.txt", "Data/datos30.txt", "Data/datos31.txt", "Data/datos32.txt",
            "Data/datos33.txt", "Data/datos34.txt", "Data/datos35.txt", "Data/datos36.txt",
            "Data/datos37.txt", "Data/datos38.txt", "Data/datos39.txt", "Data/datos40.txt"]


# Crear carpeta "Data" si no existe
if not os.path.exists("Data"):
    os.makedirs("Data")
    
datos_globales = archivos[39]

# Crear los 40 archivos de datos.txt si no existen
if os.path.exists(datos_globales):
    pass

elif not os.path.exists(datos_globales):
    for i in range(1, 41):
        datos_nombre = f"Data/datos{i}.txt"
        with open(datos_nombre, "w") as files:
            files.write("Ventana / app: " + "\n")
            files.write("Password: ")
            
with open("Data/contraseñas.txt", 'w') as contras:
    contras.write("")

opcion_var = tk.StringVar()

opciones = ["--------"]

for archivo in archivos:
    with open(archivo, 'r') as file:
        primera_linea = file.readline().strip()
        partes = primera_linea.split("Ventana / app:")
        ventana_app = partes[1]
        
        # ......... Añadir código para eliminar opciones[0]
        
        opciones.append(ventana_app)

opciones.pop(0)

opcion_menu = tk.OptionMenu(frame, opcion_var, *opciones)
opcion_menu.pack(pady=10)

# Botón para ejecutar la opción seleccionada
boton_ejecutar = tk.Button(frame, text="Confirmar", command=ejecutar_opcion)
boton_ejecutar.pack(pady=10)

# Botón de resetear todo el programa
boton_reset = tk.Button(root, text="Resetear", command=resetear_aplicacion)
boton_reset.pack(pady=10, padx=10, side="left")

# Leer solo la contraseña de cada archivo
contras = []

for archivo in archivos:
    with open(archivo) as f:
        username = f.readline()
        password = f.readline().replace("Password: ", "")        
        contras.append(password)

# Ejecutar ventana "root"
root.mainloop()