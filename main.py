#import modulo as m
#m.funcion()


def encrypt(text):
    return text+" fin"

def main():
    texto = input("Introducir texto: ")
    print(texto)
    encryptText = encrypt(texto)
    print(encryptText)




main()

