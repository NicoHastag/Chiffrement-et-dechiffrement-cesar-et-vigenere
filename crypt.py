from PIL import Image
from cryptography.fernet import Fernet

# Ouvrir l'image
image = Image.open("1.jpg")

# Obtenir les données binaires de l'image
image_data = image.tobytes()

# Générer une clé de chiffrement
key = Fernet.generate_key()

# Créer un objet Fernet avec la clé générée
cipher_suite = Fernet(key)

# Chiffrer les données de l'image
encrypted_data = cipher_suite.encrypt(image_data)

# Fermer l'image
image.close()

# Enregistrer les données chiffrées dans un nouveau fichier
with open("image_encrypted.bin", "wb") as file:
    file.write(encrypted_data)

# Enregistrer la clé de chiffrement dans un fichier pour une utilisation ultérieure
with open("encryption_key.key", "wb") as file:
    file.write(key)