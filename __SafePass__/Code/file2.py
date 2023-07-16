# Importar librerías necesarias
import tkinter as tk
from tkinter import messagebox
import os
import file3

# Crear toda la ventana de crear / guardar la contraseña
def createWindow():  
    def contraseña_segura():
        file3.createWindow()
    
    def establecer_contraseña():
        ventana = entry1.get()
        contraseña = entry2.get()
    
        if ventana and contraseña:                        
            ruta_carpeta = 'Data/'

            archivo_encontrado = None

            for i in range(1, 41):
                nombre_archivo = f'datos{i}.txt'
                ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
                
                with open(ruta_archivo, 'r') as archivo:
                    primera_linea = archivo.readline().strip()
                    
                    if primera_linea == 'Ventana / app:':
                        archivo_encontrado = nombre_archivo
                        break

            if archivo_encontrado:
                print(f'Escribiendo en : {archivo_encontrado}')
                
                """with open(archivo_encontrado, 'w') as  arch:
                    pass"""
                
                with open(f"Data/{str(archivo_encontrado)}", "w") as file:
                    file.write("Ventana / app: " + ventana + "\n")
                    file.write("Password: " + contraseña)
                    
                file.close()
            else:
                pass
                                        
            entry1.delete(0, tk.END)
            entry2.delete(0, tk.END)
            
            # Mensage de completado correctamente :)
            tk.messagebox.showinfo("Guardar contraseña", "Contraseña guardada correctamente.")
        else:
            # Mensage de error :(
            tk.messagebox.showerror("Error", "Por favor, complete ambos campos.")
    
    # Configurar la ventana 
    contraseña_window = tk.Tk()
    contraseña_window.resizable(0, 0)
    contraseña_window.geometry("500x300")
    contraseña_window.iconbitmap("")
    contraseña_window.title("Guardar contraseña")
    contraseña_window.configure(bg="#CCCCCC")
    
    # Estilo de botón (bordes)
    estilo_boton = {
    "bg": "#B0E0E6", 
    "fg": "black", 
    "bd": 0,
    "relief": "solid",
    "borderwidth": 2,
    "highlightthickness": 0,
    "activebackground": "blue",  
    "activeforeground": "white", 
    "highlightbackground": "white", 
    "highlightcolor": "white"  
    }
    
    # Estilo botón 2 (bordes + color fuerte)
    estilo_boton2 = {
        "bg": "#00BFFF", 
        "fg": "black", 
        "bd": 0, 
        "relief": "solid", 
        "borderwidth": 2, 
        "highlightthickness": 0,
        "activebackground": "blue",  
        "activeforeground": "white", 
        "highlightbackground": "white", 
        "highlightcolor": "white"
    }
    
    # Label "Establecer contraseña"
    label_establecer = tk.Label(contraseña_window, text="Establecer contraseña", font="Helvetica 30")
    label_establecer.pack(pady=15)

    # Crear un frame
    frame = tk.Frame(contraseña_window, padx=20, pady=20)
    frame.pack(pady=10)

    # Label 1 del frame anterior
    label1 = tk.Label(frame, text="Ventana / app")
    label1.grid(row=0, column=0, sticky="w")

    # Entry 1 del frame anterior
    entry1 = tk.Entry(frame)
    entry1.grid(row=0, column=1)

    # Label 2 del frame anterior
    label2 = tk.Label(frame, text="contraseña")
    label2.grid(row=1, column=0, sticky="w")

    # Entry 2 del frame anterior
    entry2_text = tk.StringVar()
    entry2 = tk.Entry(frame, textvariable=entry2_text)
    entry2.grid(row=1, column=1)

    # Botón del frame anterior
    button = tk.Button(frame, text="Guardar", command=establecer_contraseña, **estilo_boton)
    button.grid(row=0, column=2, rowspan=2, padx=(10, 0))

    # Crear otro frame debajo del frame existente
    frame2 = tk.Frame(contraseña_window, padx=20, pady=20)
    frame2.pack(pady=10)

    # Label "Generar contraseña segura"
    label_generar = tk.Label(frame2, text="Generar contraseña segura")
    label_generar.grid(row=0, column=0, sticky="w")

    # Otra etiqueta en el frame2
    label_segura_contra_text = tk.StringVar()
    label_segura_contra = tk.Label(frame2, textvariable=label_segura_contra_text)
    label_segura_contra.grid(row=0, column=1, sticky="w")

    # Botón del frame2
    boton_generar = tk.Button(frame2, text="Generar", command=contraseña_segura, **estilo_boton)
    boton_generar.grid(row=0, column=2, padx=(10, 0))

    # Funciones para el efecto de sombreado
    def on_enter(event):
        event.widget.config(**estilo_boton2)

    def on_leave(event):
        event.widget.config(**estilo_boton)

    # Poner las funciones sombreado cursor a los botones
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    boton_generar.bind("<Enter>", on_enter)
    boton_generar.bind("<Leave>", on_leave)

    # Ejecutar nueva ventana de guardado de contraseña
    contraseña_window.mainloop()