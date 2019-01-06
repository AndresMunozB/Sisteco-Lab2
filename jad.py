from cesar import Cesar


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
        value = ord(password[3])
        value = int ( (iteration + value) ** (iteration+value) )
        return  value
    
    def generateKeys(self,password):
        self.keys = []
        for i in range(16):
            key = string_to_bit_array(self.cesar.encrypt(password,self.generatePasswordCesar(i,password)))
            self.keys.append(key)
    
    def xor(self, t1, t2):#Apply a xor and return the resulting list
        return [x^y for x,y in zip(t1,t2)]

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

    """def run(self, key, text,action=ENCRYPT, padding=False):
        if len(key) < 8:
            raise "Key Should be 8 bytes long"
        elif len(key) > 8:
            key = key[:8] #If key size is above 8bytes, cut to be 8bytes long
        
        self.password = key
        self.text = text
        self.generateKeys() #Se generan las claves para cada una de las iteraciones.

        result_text = ""
        if action==ENCRYPT:
            
            #print(result_text)

        if action==DECRYPT:
            result_text = self.feistel(8,action,self.text)
            result_text = self.cesar.decrypt(result_text,ord(self.password[4]))
            #print(result_text)
        
        return result_text"""

    def encrypt(self,text,password,size_block):
        self.generateKeys(password)
        result_text = self.cesar.encrypt(text,ord(password[4]))
        result_text = self.feistel(size_block,ENCRYPT,result_text)
        return result_text

    def decrypt(self,text,password,size_block):
        self.generateKeys(password)
        result_text = self.feistel(size_block,DECRYPT,text)
        result_text = self.cesar.decrypt(result_text,ord(password[4]))
        return result_text


    
    
jad = Jad()
textooo = jad.encrypt("hola como estas!","holacomo",2)
print(textooo)
textooo = jad.decrypt(textooo,"holacomo",2)
print(textooo)
#print(jad.keys)