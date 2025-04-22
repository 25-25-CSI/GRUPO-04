"""
Algoritmo que realice el cifrado de un mensaje por permutación de filas, teniendo como clave n filas.
Tanto n como el texto del mensaje se ingresan al iniciar el algoritmo. El algoritmo debe controlar 
que el número de caracteres del mensaje (sin espacios), sea menor o igual que n x n. Imprima la matriz
de cifrado, el mensaje original y el mensaje cifrado. Si en la matriz de cifrado sobran espacios para
almacenar los caracteres del mensaje original, estos deben llenarse con "*".
"""

def cifrado_permutacion_filas():
    while True:
        try:
            n = int(input("Ingrese el número de filas (clave): "))
            if n <= 0:
                print("Error: El número de filas debe ser un entero positivo.")
                continue
            break
        except ValueError:
            print("Error: Debe ingresar un número entero positivo.")


    while True:
        mensaje = input("Ingrese el mensaje a cifrar: ").replace(" ", "")
        if not mensaje.isalpha():
            print("Error: El mensaje solo debe contener letras.")
        else:
            break
    
    longitud_maxima = n * n
    
    if len(mensaje) > longitud_maxima:
        print(f"El mensaje es demasiado largo. Máximo permitido: {longitud_maxima} caracteres.")
        return
    
    mensaje += "*" * (longitud_maxima - len(mensaje))
    
    matriz = []
    index = 0
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(mensaje[index])
            index += 1
        matriz.append(fila)
    
    print("\nMatriz de cifrado:")
    for fila in matriz:
        print(" ".join(fila))
    
    orden = list(range(n))
    orden_permutado = orden[::-1] 
    
    matriz_permutada = [matriz[i] for i in orden_permutado]
    

    mensaje_cifrado = "".join("".join(fila) for fila in matriz_permutada)
    
    print("\nMensaje original (sin espacios):", mensaje.replace("*", ""))
    print("Mensaje cifrado:", mensaje_cifrado)

cifrado_permutacion_filas()