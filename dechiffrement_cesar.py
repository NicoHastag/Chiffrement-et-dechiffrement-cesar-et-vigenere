def dechiffrement_cesar(message, decalage):
    message_dechiffre = ""
    for caractere in message:
        if caractere.isalpha():
            ascii_offset = ord('A') if caractere.isupper() else ord('a')
            indice_caractere = (ord(caractere) - ascii_offset - decalage) % 26
            caractere_dechiffre = chr(indice_caractere + ascii_offset)
            message_dechiffre += caractere_dechiffre
        else:
            message_dechiffre += caractere
    return message_dechiffre

message_chiffre = input("Quel est le message chiffré ? ")
decalage = int(input("Quel est le décalage de chiffrement ? "))

message_dechiffre = dechiffrement_cesar(message_chiffre, decalage)

print("Message chiffré :", message_chiffre)
print("Message déchiffré :", message_dechiffre)