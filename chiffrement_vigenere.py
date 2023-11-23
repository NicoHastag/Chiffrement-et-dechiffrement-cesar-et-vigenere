def chiffrement_vigenere(message, cle):
    message_chiffre = ""
    cle_index = 0
    for caractere in message:
        if caractere.isalpha():
            ascii_offset = ord('A') if caractere.isupper() else ord('a')
            decalage = ord(cle[cle_index]) - ord('A')
            indice_caractere = (ord(caractere) - ascii_offset + decalage) % 26
            caractere_chiffre = chr(indice_caractere + ascii_offset)
            message_chiffre += caractere_chiffre
            cle_index = (cle_index + 1) % len(cle)
        else:
            message_chiffre += caractere
    return message_chiffre

# Demande à l'utilisateur de saisir le message et la clé de chiffrement
message = input("Entrez le message à chiffrer : ")
cle = input("Entrez la clé de chiffrement : ")

# Chiffrement du message saisi par l'utilisateur
message_chiffre = chiffrement_vigenere(message, cle)

# Affichage du résultat
print("Message chiffré :", message_chiffre)