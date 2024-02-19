import datos
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Función para cifrar usando AES
def encrypt_aes(key, data):
    cipher = AES.new(key, AES.MODE_ECB)
    # Se asegura de que los datos estén rellenados antes del cifrado
    padded_data = pad(data.encode(), AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

# Función para descifrar usando AES
def decrypt_aes(key, encrypted_data):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data)
    # Se elimina el relleno después del descifrado
    unpadded_data = unpad(decrypted_data, AES.block_size)
    return unpadded_data.decode()

# Generar una clave de 16, 24 o 32 bytes (128, 192, 256 bits) aleatoria para AES
key = get_random_bytes(16)  # Por ejemplo, generamos una clave de 16 bytes (128 bits)

# Datos a cifrar
data = datos.obtener_mensaje()

# Cifrado
encrypted_data = encrypt_aes(key, data)
print("Mensaje cifrado:", encrypted_data)

# Descifrado
decrypted_data = decrypt_aes(key, encrypted_data)
print("Mensaje descifrado:", decrypted_data)
