nombre_archivo="archivo.txt"
# Termina con slash
# Ejemplo:
#   Windows -> "C:\Users\USUARIO\programacion\"
#   Linux -> "/home/USUARIO/programacion/"
ruta_archivo=""

with open(ruta_archivo + nombre_archivo) as f:
    lineas = f.readlines();
    palabras = []
    for linea in lineas:
        palabras += linea.split()

    for palabra in palabras:
        # Reemplace aqui el codigo
        print(palabra)
        # Fin del codigo
