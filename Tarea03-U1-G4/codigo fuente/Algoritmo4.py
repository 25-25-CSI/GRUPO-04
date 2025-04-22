"""
Algoritmo que realice el cifrado de una cadena de caracteres mediante un método de sustitución
Monoalfabético de desplazamiento n caracteres a la derecha. Tanto la palabra como el valor de n 
se ingresan al iniciar el algoritmo. El algoritmo debe mostrar el alfabeto original, el alfabeto 
cifrado, la cadena de caracteres ingresada y su resultado.
"""

def cifrado_desplazamiento(texto, n):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    texto = texto.upper()

    alfabeto_cifrado = alfabeto[n % 26:] + alfabeto[:n % 26]
    sustitucion = {original: cifrada for original, cifrada in zip(alfabeto, alfabeto_cifrado)}

    resultado = ''
    for letra in texto:
        if letra in sustitucion:
            resultado += sustitucion[letra]
        else:
            resultado += letra

    print("Alfabeto original: ", alfabeto)
    print("Alfabeto cifrado : ", alfabeto_cifrado)
    print("Texto original   : ", texto)
    print("Texto cifrado    : ", resultado)

# Ejemplo de uso
while True:
    mensaje = input("Ingrese la cadena a cifrar: ")
    if not mensaje.isalpha():
        print("Error: El texto solo debe contener letras.")
        continue
    break

while True:
    try:
        n = int(input("Ingrese el valor de desplazamiento: "))
        if n <= 0:
            print("Error: El valor de desplazamiento debe ser un entero positivo.")
            continue
        break
    except ValueError:
        print("Error: Debe ingresar un número entero positivo.")

cifrado_desplazamiento(mensaje, n)