from cesar import Cesar
from time import time


def string_to_bit_array(text):#Convierte un string a una lista de bits
                                
    array = list()
    for char in text:
        binval = binvalue(char, 8)#Obtiene el valor del char en un byte
        array.extend([int(x) for x in list(binval)]) #Agrega una lista de los bits del char a otra lista
    return array

def bit_array_to_string(array): #Transforma un alista de bits a un string
    res = ''.join([chr(int(y,2)) for y in [''.join([str(x) for x in bytes]) for bytes in  nsplit(array,8)]])   
    return res

def binvalue(val, bitsize): #Retorna el valor binario como string de un largo dado 
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = "0"+binval #Agrega ceros necesarios para cumplir con el largo
    return binval

def nsplit(s, n):#Divide una lista en sublistas de tamaño n
    return [s[k:k+n] for k in range(0, len(s), n)]


ENCRYPT=1
DECRYPT=0

class Jad():
    def __init__(self):
        self.keys = list()
        self.cesar = Cesar()

    def generatePasswordCesar(self, iteration,password):
        value = self.generateValue(password)
        value = int ( (iteration + value) ** (iteration+value) )
        return  value

    def generateValue(self,password):
        value = 0
        for c in password:
            value += ord(c)
        return value

    def generateKeys(self,password):
        self.keys = []
        for i in range(16):
            key = string_to_bit_array(self.cesar.encrypt(password,self.generatePasswordCesar(i,password)))
            self.keys.append(key)
    
    def xor(self, t1, t2):#Apply a xor and return the resulting list
        return [x^y for x,y in zip(t1,t2)]
    
    def addPadding(self,text):
        if(len(text) % 8 == 0):
            return text
        pad_len = 8 - (len(text) % 8)
        for i in range(pad_len):
            text += " "
        return text

    def getValidPassword(self,password):
        if len(password) < 8:
            password = self.addPadding(password)
        elif len(password) > 8:
            password = password[:8] 
        return password

    def feistel(self,size_block,action,text):
        text_blocks = nsplit(text, size_block) #Se divide el texto en bloques de size_block bytes es decir 64 bits      
        result = list()
        for block in text_blocks:#Se aplica el método para cada bloque
            block = string_to_bit_array(block)#Se convierte el bloque a binario 
            g, d = nsplit(block, int(len(block)/2)) #g(IZQUIERDA), d(DERECHA)
            tmp = None
            for i in range(16): #Do the 16 rounds
                if action == ENCRYPT:
                    tmp = self.xor(self.keys[i], d)#Se utiliza la clave Ki para encriptar
                else:
                    tmp = self.xor(self.keys[15-i], d)#Se empieza a desencritar desde la ultima clave
                tmp = self.xor(g, tmp)
                g = d
                d = tmp
            result += d+g
        return  bit_array_to_string(result)

    def encrypt(self,text,password,size_block):
        password = self.getValidPassword(password)
        text = self.addPadding(text)
        self.generateKeys(password)
        result_text = self.cesar.encrypt(text,self.generateValue(password))
        result_text = self.feistel(size_block,ENCRYPT,result_text)
        return result_text

    def decrypt(self,text,password,size_block):
        password = self.getValidPassword(password)
        self.generateKeys(password)
        result_text = self.feistel(size_block,DECRYPT,text)
        result_text = self.cesar.decrypt(result_text,self.generateValue(password))
        result_text.strip()
        return result_text


    

"""
jad = Jad()
size_block = 8
start_time = time()
textooo = jad.encrypt("hola como estas!","holacomo",size_block)
elapsed_time = time() - start_time
print("Elapsed time: %0.10f seconds." % elapsed_time)
print(textooo)
textooo = jad.decrypt(textooo,"holacomo",size_block)
print(textooo)
#print(jad.keys)
"""