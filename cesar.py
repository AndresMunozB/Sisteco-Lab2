



class Cesar():
    def __init__(self):

        self.alphabet = ['!', ',', 'l', "'", 'T', 'B', 'F', '0', 'u', 'j', 'z', 'b', 'A', '#', 'n', '@', 'm', 'L', 'g', '[', '4', 'R', 'a', '|', 'v', 'c', 'U', ';', '~', 'S', '9', '5', 'o', 'k', ')', ' ', 'C', '+', '&', 'q', 'M', 'i', 'Q', '>', 'X', '/', '7', 'J', '-', 'E', 'H', 'w', 'V', 'K', '$', 't', '{', 'Y', '*', '%', 'e', '<', '}', '`', 'G', 'r', 'd', 's', '1', 'I', '=', 'W', '?', '_', ':', '^', '2', '3', '8', '6', '(', 'y', '.', 'Z', '\\', 'p', '"', 'D', 'O', 'N', 'x', ']', 'h', 'P', 'f']
    
    def decrypt(self,text, password):
        result = ""
        for c in text:
            result += self.alphabet[(self.alphabet.index(c) - password) % len(self.alphabet)]
        return result

    def encrypt(self,text, password):
        result = ""
        for c in text:
            result += self.alphabet[(self.alphabet.index(c) + password) % len(self.alphabet)]
        return result
    
    
"""
cesar = Cesar()
encriptado = cesar.encrypt("hola como EStas!", 20)
print (encriptado)
desencriptado = cesar.decrypt(encriptado,20)
print (desencriptado)
"""