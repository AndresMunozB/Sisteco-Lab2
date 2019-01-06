import random
listanueva = ['!', ',', 'l', "'", 'T', 'B', 'F', '0', 'u', 'j', 'z', 'b', 'A', '#', 'n', '@', 'm', 'L', 'g', '[', '4', 'R', 'a', '|', 'v', 'c', 'U', ';', '~', 'S', '9', '5', 'o', 'k', ')', ' ', 'C', '+', '&', 'q', 'M', 'i', 'Q', '>', 'X', '/', '7', 'J', '-', 'E', 'H', 'w', 'V', 'K', '$', 't', '{', 'Y', '*', '%', 'e', '<', '}', '`', 'G', 'r', 'd', 's', '1', 'I', '=', 'W', '?', '_', ':', '^', '2', '3', '8', '6', '(', 'y', '.', 'Z', '\\', 'p', '"', 'D', 'O', 'N', 'x', ']', 'h', 'P', 'f']
archivo = open("alfabeto.txt")
alfabeto = list()
for linea in archivo:
    lista = linea.strip().split(" ") 
    alfabeto.append(lista[1])
    print (lista)
alfabeto[0] = ' '
random.shuffle(alfabeto)
print(alfabeto)
print(listanueva)
archivo.close()

