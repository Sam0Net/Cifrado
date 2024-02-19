import datos
from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Función para cifrar usando Blowfish
def encrypt_blowfish(key, data):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    # Se asegura de que los datos estén rellenados antes del cifrado
    padded_data = pad(data.encode(), Blowfish.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

# Función para descifrar usando Blowfish
def decrypt_blowfish(key, encrypted_data):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data)
    # Se elimina el relleno después del descifrado
    unpadded_data = unpad(decrypted_data, Blowfish.block_size)
    return unpadded_data.decode()

# Generar una clave de 16 bytes (128 bits) aleatoria para Blowfish
key = get_random_bytes(16)

# Datos a cifrar
data = datos.obtener_mensaje()

# Cifrado
encrypted_data = encrypt_blowfish(key, data)
print("Mensaje cifrado:", encrypted_data)

# Descifrado
decrypted_data = decrypt_blowfish(key, encrypted_data)
print("Mensaje descifrado:", decrypted_data)

