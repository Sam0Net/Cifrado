import datos
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Función para cifrar usando Triple DES
def encrypt_des3(key, data):
    cipher = DES3.new(key, DES3.MODE_ECB)
    # Se asegura de que los datos estén rellenados antes del cifrado
    padded_data = pad(data.encode(), DES3.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

# Función para descifrar usando Triple DES
def decrypt_des3(key, encrypted_data):
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data)
    # Se elimina el relleno después del descifrado
    unpadded_data = unpad(decrypted_data, DES3.block_size)
    return unpadded_data.decode()

# Generar una clave de 24 bytes (192 bits) aleatoria para Triple DES
key = get_random_bytes(24)

# Datos a cifrar
data = datos.obtener_mensaje()

# Cifrado
encrypted_data = encrypt_des3(key, data)
print("Mensaje cifrado:", encrypted_data)

# Descifrado
decrypted_data = decrypt_des3(key, encrypted_data)
print("Mensaje descifrado:", decrypted_data)

