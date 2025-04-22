"""
Algoritmo que realice el cifrado de una cadena de caracteres utilizando la
siguiente tabla de cifrado:

| * | A | S | D | F | G |
| Q | a | b | c | d | e |
| W | f | g | h | i | j |
| E | k | l | m | n | o |
| R | p | q | r | s | t |
| T | u | v | x | y | z |

La cadena de caracteres se ingresa al iniciar el programa. Si algún caracter
del texto no existe en la matriz, coloque "**". Imprima la matriz de cifrado,
el mensaje original y el mensaje cifrado.
"""

def crear_matriz():
    filas = ['Q', 'W', 'E', 'R', 'T']
    columnas = ['A', 'S', 'D', 'F', 'G']
    letras = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) != 'w']

    matriz = {}
    index = 0
    for f in filas:
        for c in columnas:
            if index < len(letras):
                matriz[letras[index]] = f + c
                index += 1
    return matriz

def cifrar_mensaje(mensaje, matriz):
    mensaje = mensaje.lower()
    cifrado = ''
    for c in mensaje:
        cifrado += matriz.get(c, '**')  # "**" si el caracter no está en la matriz
    return cifrado

def imprimir_matriz():
    filas = ['Q', 'W', 'E', 'R', 'T']
    columnas = ['A', 'S', 'D', 'F', 'G']
    letras = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) != 'w']

    print("    ", end="")
    for c in columnas:
        print(f" {c} ", end="")
    print()

    index = 0
    for f in filas:
        print(f" {f} ", end="")
        for c in columnas:
            if index < len(letras):
                print(f" {letras[index]} ", end="")
                index += 1
            else:
                print("   ", end="")
        print()

# Ejecución
matriz = crear_matriz()
imprimir_matriz()

while True:
    mensaje = input("\nIngrese el mensaje a cifrar: ")
    if not mensaje.isalpha():
        print("Error: El mensaje solo debe contener letras.")
        continue
    break

cifrado = cifrar_mensaje(mensaje, matriz)

print("\nMensaje original : ", mensaje)
print("Mensaje cifrado  : ", cifrado)
