"""
Algoritmo que realice el cifrado de una cadena de caracteres mediante un
método de sustitución Polialfabético de Vigenére. La cadena se ingresa al
iniciar el algoritmo. El algoritmo debe mostrar la cadena de caracteres
ingresada, la clave de cifrado y la cadena de caracteres cifrada.
"""

def imprimir_matriz_vigenere(alfabeto):
    print("Matriz de Vigenére:")
    encabezado = "  | " + " ".join(alfabeto)
    print(encabezado)
    print("-" * len(encabezado))
    for i in range(len(alfabeto)):
        fila = alfabeto[i:] + alfabeto[:i]
        print(f"{alfabeto[i]} | " + " ".join(fila))
    print("")

def cifrado_vigenere(mensaje, clave):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mensaje = mensaje.upper().replace(" ", "")
    clave = clave.upper().replace(" ", "")

    clave_repetida = (clave * (len(mensaje) // len(clave) + 1))[:len(mensaje)]

    cifrado = ''
    for i in range(len(mensaje)):
        if mensaje[i] in alfabeto:
            m = alfabeto.index(mensaje[i])
            k = alfabeto.index(clave_repetida[i])
            cifrado += alfabeto[(m + k) % 26]
        else:
            cifrado += mensaje[i]

    imprimir_matriz_vigenere(alfabeto)
    print("Mensaje original : ", mensaje)
    print("Clave repetida   : ", clave_repetida)
    print("Mensaje cifrado  : ", cifrado)


# Validación para el mensaje
while True:
    mensaje = input("Ingrese el mensaje a cifrar: ")
    if not mensaje.isalpha():
        print("Error: El mensaje solo debe contener letras.")
        continue
    break

# Validación para la clave
while True:
    clave = input("Ingrese la clave: ")
    if not clave.isalpha():
        print("Error: La clave solo debe contener letras.")
        continue
    break

cifrado_vigenere(mensaje, clave)