from itertools import permutations

"""
Algoritmo que escriba todas las permutaciones posibles de una palabra de longitud n 
SIN espacios (Anagrama). La palabra se ingresa al iniciar el algoritmo. El algoritmo 
debe mostrar el número total de permutaciones y las 10 primeras ordenadas alfabéticamente.
"""

def generar_permutaciones(palabra):
    palabra = palabra.strip()
    if not palabra.isalpha():
        print("Error: La palabra solo debe contener letras.")
        return

    permutaciones = sorted(set([''.join(p) for p in permutations(palabra)]))
    total = len(permutaciones)
    
    print(f"Palabra ingresada: {palabra}")
    print(f"Total de permutaciones: {total}")
    print("Primeras 10 permutaciones ordenadas alfabéticamente:")
    for p in permutaciones[:10]:
        print(p)

# Ejemplo de uso
entrada = input("Ingrese una palabra sin espacios: ")
generar_permutaciones(entrada)