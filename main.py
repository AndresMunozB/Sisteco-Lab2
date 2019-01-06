#import modulo as m
#m.funcion()
import argparse
 

    

def encrypt(text):
    return text+" fin"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--block", help="Tamaño del bloque", type=int)
    args = parser.parse_args()

    # Aquí procesamos lo que se tiene que hacer con cada argumento
    if args.block:
        print("El tamaño del bloque es: ", args.block)
    texto = input("Introducir texto: ")
    print(texto)
    encryptText = encrypt(texto)
    print(encryptText)




main()

