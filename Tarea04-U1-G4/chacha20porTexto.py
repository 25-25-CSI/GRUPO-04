import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend
import random
import os

def chacha20_encrypt_decrypt(file_path):
    print(f"\nProcesando archivo: {file_path}")

    start = time.time()
    with open(file_path, 'r', encoding='utf-8') as f:
        plaintext = f.read().encode('utf-8')
    end = time.time()
    print(f"[Etapa 1] Lectura completada en {end - start:.6f} segundos")
    print(f"Número de caracteres de entrada: {len(plaintext)}") 
    

    start = time.time()
     # 256
    key = os.urandom(32) 
    nonce = os.urandom(16)  
    end = time.time()
    print(f"[Etapa 2] Clave generada en {end - start:.6f} segundos")
    print(f"Clave (hex): {key.hex()}")
    print(f"Nonce (hex): {nonce.hex()}")

    start = time.time()
    algorithm = algorithms.ChaCha20(key, nonce)
    cipher = Cipher(algorithm, mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext)
    end = time.time()
    print(f"[Etapa 3] Cifrado completado en {end - start:.6f} segundos")
    print(f"Texto cifrado (hex): {ciphertext[:100].hex()}...")

    start = time.time()
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(ciphertext)
    end = time.time()
    print(f"[Etapa 4] Descifrado completado en {end - start:.6f} segundos")
    print(f"Texto descifrado (inicio): {decrypted_text[:300].decode('utf-8', errors='ignore')}...")  
    print(f"Número de caracteres de salida: {len(decrypted_text)}")


def generar_archivo_texto(file_name, num_palabras):
    """
    Creando archivo de texto ... espere un momento.
    """
    palabras_comunes = [
        "casa", "apartamento", "botella", "azucar", "cielo", "tierra", "azul", "pimiento", "Lorem", "feliz",
        "cansancio", "pelicula", "lento", "especia", "noche", "sol", "mercado", "estrella", "mar", "juego"
    ]
    
    texto = " ".join(random.choice(palabras_comunes) for _ in range(num_palabras))
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(texto)
    print(f"Archivo generado: {file_name} con {num_palabras} palabras.")


if __name__ == "__main__":
    sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000] 
    for s in sizes:
        file_name = f"entrada_{s}_palabras.txt"

        if not os.path.exists(file_name): 
            generar_archivo_texto(file_name, s)
        if os.path.exists(file_name): 
            chacha20_encrypt_decrypt(file_name)
        else:
            print(f"Archivo ya existe: {file_name}. Saltando...")