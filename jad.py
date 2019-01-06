from cesar import Cesar
from time import time


def string_to_bit_array(text):#Convert a string into a list of bits
    array = list()
    for char in text:
        binval = binvalue(char, 8)#Get the char value on one byte
        array.extend([int(x) for x in list(binval)]) #Add the bits to the final list
    return array

def bit_array_to_string(array): #Recreate the string from the bit array
    res = ''.join([chr(int(y,2)) for y in [''.join([str(x) for x in bytes]) for bytes in  nsplit(array,8)]])   
    return res

def binvalue(val, bitsize): #Return the binary value as a string of the given size 
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = "0"+binval #Add as many 0 as needed to get the wanted size
    return binval

def nsplit(s, n):#Split a list into sublists of size "n"
    return [s[k:k+n] for k in range(0, len(s), n)]


ENCRYPT=1
DECRYPT=0

class Jad():
    def __init__(self):
        self.password = None
        self.text = None
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

        text_blocks = nsplit(text, size_block) #Se divide el texto en bloques de 8 bytes es decir 64 bits
        #print(text_blocks)
        
        result = list()
        for block in text_blocks:#Se aplica el método para cada bloque
            block = string_to_bit_array(block)#Se convierte el bloque a binario 
            g, d = nsplit(block, int(len(block)/2)) #g(LEFT), d(RIGHT)

            tmp = None
            for i in range(16): #Do the 16 rounds
                if action == ENCRYPT:
                    tmp = self.xor(self.keys[i], d)#If encrypt use Ki
                else:
                    tmp = self.xor(self.keys[15-i], d)#If decrypt start by the last key
                tmp = self.xor(g, tmp)
                g = d
                d = tmp
            result += d+g
        return  bit_array_to_string(result)


    def encrypt(self,text,password,size_block):
        password = self.getValidPassword(password)
        self.generateKeys(password)
        result_text = self.cesar.encrypt(text,self.generateValue(password))
        result_text = self.feistel(size_block,ENCRYPT,result_text)
        return result_text

    def decrypt(self,text,password,size_block):
        password = self.getValidPassword(password)
        self.generateKeys(password)
        result_text = self.feistel(size_block,DECRYPT,text)
        result_text = self.cesar.decrypt(result_text,self.generateValue(password))
        return result_text


    


jad = Jad()
size_block = 1
start_time = time()
textooo = jad.encrypt(jad.addPadding("hola como estas"),"holacomo",size_block)
elapsed_time = time() - start_time
print("Elapsed time: %0.10f seconds." % elapsed_time)
print(textooo)
textooo = jad.decrypt(textooo,"holacomo",size_block).strip()
print(textooo)
#print(jad.keys)