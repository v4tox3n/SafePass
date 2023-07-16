import time
import shutil

# Animación "[ - ] Cargando..."
def animacion_carga():
    contador = 0
    while contador < 3:
        for i in range(4):
            print("[ ", "\u2699", " ] Cargando " + "." * i, end="\r")
            time.sleep(0.5)
        contador += 1
    
# Hacer print del candado
def candado():
    print(" ")
    print(" ")
    
    print("                                ___________________")
    time.sleep(0.17)
    print("                             //                     \\\\")
    time.sleep(0.17)
    print("                            ||                       ||")
    time.sleep(0.17)
    print("                            ||                       ||")
    time.sleep(0.17)
    print("                            ||                       ||")
    time.sleep(0.17)
    print("                            ||                       ||")
    time.sleep(0.17)
    print("                            ||                       ||")
    time.sleep(0.17)
    print("                            ||                       ||")
    time.sleep(0.17)
    print("                            ||                       ||")
    time.sleep(0.17)
    print("                            ||                       ||")
    time.sleep(0.17)
    print("                            ||                       ||")
    time.sleep(0.17)
    print("                            \\\\______________________//")
    time.sleep(0.17)
    print("                    ___________________________________________")
    time.sleep(0.17)
    print("                  / ___________________________________________ \\")
    time.sleep(0.17)
    print("                 // SafePass                                    \\\\")
    time.sleep(0.17)
    print("                ||                                               ||")
    time.sleep(0.17)
    print("                ||                                               ||")
    time.sleep(0.17)
    print("                ||                                               ||")
    time.sleep(0.17)
    print("                ||                                               ||")
    time.sleep(0.17)
    print("                ||                                               ||")
    time.sleep(0.17)
    print("                ||                                               ||")
    time.sleep(0.17)
    print("                ||                                               ||")
    time.sleep(0.17)
    print("                ||                                               ||")
    time.sleep(0.17)
    print("                ||                                               ||")
    time.sleep(0.17)
    print("                ||                                               ||")
    time.sleep(0.17)
    print("                ||                                               ||")
    time.sleep(0.17)
    print("                ||                                               ||")
    time.sleep(0.17)
    print("                ||                                               ||")
    time.sleep(0.17)
    print("                ||                                               ||")
    time.sleep(0.17)
    print("                \\\\______________________________________________//")
    time.sleep(0.17)
    
    print(" ")
    print(" ")

# Función resetear Aplicación/Data/contraseñas.txt
def contraseñas_reset():
    pass
    """with open("Data/contraseñas.txt", 'w') as file:
        file.truncate(0)"""

# Función resetear todos los datos de Aplicación/Data/
def datos_reset():
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

    def parte1_datos():
        for archivo in archivos:
            with open(archivo, 'w') as arch:
                arch.truncate(0)


    def parte_final_datos():
        for archivo in archivos:
            with open(archivo, 'w') as file:
                file.write("Ventana / app: " + "\n")
                file.write("Password: ")
                
    def borrar_carpeta():
        directory = "Data/"
        shutil.rmtree(directory)

    # Ejecutar función completa
    parte1_datos()
    time.sleep(1)
    parte_final_datos()
    time.sleep(1)
    borrar_carpeta()

# Función de resetear todo
def reseteo():
    animacion_carga()
    candado()
    #contraseñas_reset()
    datos_reset()
    print("[ ", "\u2705", " ] Proceso completado")
    print("\U0001F4BB", "Puedes cerrar esta ventana")
    print("")

# Preguntar si realmente desea resetear todo
def preguntar():
    print("")
    primera_pregunta = input("[ ? ] Deseas resetear todas las contraseñas? (s = si / n = no) : ")

    if primera_pregunta == "s" or primera_pregunta == "S":
        print("[ ", "\u26A0", " ] Se perderan todos los datos guardados, ¿desea continuar?")
        input("Si deseas continuar pulsa 1 vez [enter], si no, pulsa [ctrl + c] y se cancela todo ")
        reseteo()
        
    elif primera_pregunta == "n" or primera_pregunta == "N":
        print("[ ", "\u274C", " ] Operación cancelada")
        print("\U0001F4BB", "Puedes cerrar esta ventana")
        print("")
        
    else:
        print("[ ", "\u274C", " ] Operación cancelada")
        print("\U0001F4BB", "Puedes cerrar esta ventana")
        print("")