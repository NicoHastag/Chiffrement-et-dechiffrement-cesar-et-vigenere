from PIL import Image
from cryptography.fernet import Fernet

# Ouvrir le fichier de clé de chiffrement
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

# Créer un objet Fernet avec la clé
cipher_suite = Fernet(key)

# Lire les données chiffrées à partir du fichier
with open("image_encrypted.bin", "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

# Déchiffrer les données
decrypted_data = cipher_suite.decrypt(encrypted_data)

# Créer une image à partir des données déchiffrées
image = Image.frombytes("RGB", Image.size, decrypted_data)

# Afficher ou enregistrer l'image déchiffrée
image.show()
# image.save("image_decrypted.jpg")