"""
Algoritmo que realice el cifrado de un mensaje por permutación de columnas, teniendo
como clave n columnas. Tanto n como el texto del mensaje se ingresan al iniciar el
algoritmo. El algoritmo debe controlar que el número de caracteres del mensaje
(sin espacios), sea menor o igual que n x n. Imprima la matriz de cifrado, el mensaje
original y el mensaje cifrado.  Si en la matriz de cifrado sobran espacios para
almacenar los caracteres del mensaje original, estos deben llenarse con "*".
"""
def cifrado_columnas(mensaje, n):
    mensaje = mensaje.replace(" ", "")
    if not mensaje.isalpha():
        print("Error: El mensaje solo debe contener letras.")
        return
    
    if n <= 0:
        print("Error: El número de columnas debe ser un entero positivo.")
        return
    

    longitud = len(mensaje)
    tamaño = n * n

    if longitud > tamaño:
        print("El mensaje es muy largo para la matriz.")
        return

    mensaje += '*' * (tamaño - longitud)
    matriz = [list(mensaje[i * n:(i + 1) * n]) for i in range(n)]

    print("Matriz de cifrado:")
    for fila in matriz:
        print(' '.join(fila))

    cifrado = ''.join([matriz[i][j] for j in range(n) for i in range(n)])

    print("Mensaje original:", mensaje)
    print("Mensaje cifrado:", cifrado)

while True:
    mensaje = input("Ingrese el mensaje: ")
    if not mensaje.isalpha():
        print("Error: El mensaje solo debe contener letras.")
        continue
    break

while True:
    try:
        n = int(input("Ingrese el número de columnas: "))
        if n <= 0:
            print("Error: El número de columnas debe ser un entero positivo.")
            continue
        break
    except ValueError:
        print("Error: Debe ingresar un número entero positivo.")

cifrado_columnas(mensaje, n)