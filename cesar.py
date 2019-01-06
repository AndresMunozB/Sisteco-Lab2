



class Cesar():
    def __init__(self):
        self.password = None
        self.text = None
        self.alphabet = ['!', ',', 'l', "'", 'T', 'B', 'F', '0', 'u', 'j', 'z', 'b', 'A', '#', 'n', '@', 'm', 'L', 'g', '[', '4', 'R', 'a', '|', 'v', 'c', 'U', ';', '~', 'S', '9', '5', 'o', 'k', ')', ' ', 'C', '+', '&', 'q', 'M', 'i', 'Q', '>', 'X', '/', '7', 'J', '-', 'E', 'H', 'w', 'V', 'K', '$', 't', '{', 'Y', '*', '%', 'e', '<', '}', '`', 'G', 'r', 'd', 's', '1', 'I', '=', 'W', '?', '_', ':', '^', '2', '3', '8', '6', '(', 'y', '.', 'Z', '\\', 'p', '"', 'D', 'O', 'N', 'x', ']', 'h', 'P', 'f']
    
    def decrypt(self):
        result = ""
        for c in self.text:
            result += self.alphabet[(self.alphabet.index(c) - self.password) % len(self.alphabet)]
        return result

    def encrypt(self):
        result = ""
        for c in self.text:
            result += self.alphabet[(self.alphabet.index(c) + self.password) % len(self.alphabet)]
        return result
    
    
"""   
cesar = Cesar()
cesar.password = 20
cesar.text = "hola como EStas!"

encriptado = cesar.encrypt()
print (encriptado)
cesar.text = encriptado
desencriptado = cesar.decrypt()
print (desencriptado)
"""