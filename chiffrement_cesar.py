def chiffrement_cesar(message, decalage):
    message_chiffre = ""
    for caractere in message:
        if caractere.isalpha():
            ascii_offset = ord('A') if caractere.isupper() else ord('a')
            indice_caractere = (ord(caractere) - ascii_offset + decalage) % 30
            caractere_chiffre = chr(indice_caractere + ascii_offset)
            message_chiffre += caractere_chiffre
        else:
            message_chiffre += caractere
    return message_chiffre

message=input("quel est le message chiffrer")
decalage=int(input("quel est le message decalage"))
message_chiffre=chiffrement_cesar(message, decalage)
print("message original: ", message)
print("message chiffre: ", message_chiffre)