def dechiffrement_vigenere(message, cle):
    message_dechiffre = ""
    cle_index = 0
    for caractere in message:
        if caractere.isalpha():
            ascii_offset = ord('A') if caractere.isupper() else ord('a')
            decalage = ord(cle[cle_index]) - ord('A')
            indice_caractere = (ord(caractere) - ascii_offset - decalage) % 26
            caractere_dechiffre = chr(indice_caractere + ascii_offset)
            message_dechiffre += caractere_dechiffre
            cle_index = (cle_index + 1) % len(cle)
        else:
            message_dechiffre += caractere
    return message_dechiffre

# Demande à l'utilisateur de saisir le message chiffré et la clé de déchiffrement
message_chiffre = input("Entrez le message chiffré : ")
cle = input("Entrez la clé de déchiffrement : ")

# Déchiffrement du message saisi par l'utilisateur
message_dechiffre = dechiffrement_vigenere(message_chiffre, cle)

# Affichage du résultat
print("Message chiffré :", message_chiffre)
print("Message déchiffré :", message_dechiffre)













