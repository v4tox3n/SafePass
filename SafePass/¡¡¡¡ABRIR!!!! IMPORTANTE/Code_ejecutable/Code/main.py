# Importar librerías / módulos necesarios
from tkinter import messagebox
import shutil
import os
import time

# Main function
def transportarLnk():
    # Copiar acceso directo al Desktop
    ruta_inicial = "Aplicación/Code/dist/SafePass.lnk"
    ruta_final = os.path.join(os.path.expanduser("~"), "Desktop", "SafePass.lnk")
    shutil.copy(ruta_inicial, ruta_final)
    
    # Sumar 7 segs
    time.sleep(6.5)
    
    # Mostrar ventana operación completada correctamente
    messagebox.showinfo("Instalación completada", "¡Instalación completada correctamente!")