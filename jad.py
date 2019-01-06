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

    def generatePasswordCesar(self, iteration):
        value = ord(self.password[3])
        value = int ( (iteration + 10) ** (iteration+5) )
        return  value
    def generateKeys(self):
        self.keys = []
        
        for i in range(16):
            self.cesar.text = self.password
            self.cesar.password = self.generatePasswordCesar(i)
            key = string_to_bit_array(self.cesar.encrypt())
            self.keys.append(key)
    def xor(self, t1, t2):#Apply a xor and return the resulting list
        #print(t1,t2)
        #print("")
        return [x^y for x,y in zip(t1,t2)]
    
    def run(self, key, text,action=ENCRYPT, padding=False):
        if len(key) < 8:
            raise "Key Should be 8 bytes long"
        elif len(key) > 8:
            key = key[:8] #If key size is above 8bytes, cut to be 8bytes long
        
        self.password = key
        self.text = text
        self.generateKeys() #Se generan las claves para cada una de las iteraciones.
        text_blocks = nsplit(self.text, 8) #Se divide el texto en bloques de 8 bytes es decir 64 bits
        
        if action==ENCRYPT:
            self.cesar.password = ord(self.password[4])
            for i in range(len(text_blocks)):
                self.cesar.text = text_blocks[i]
                text_blocks[i] = self.cesar.encrypt()
                
        print(text_blocks)
        result = list()
        for block in text_blocks:#Se aplica el método para cada bloque
            block = string_to_bit_array(block)#Se convierte el bloque a binario 
            g, d = nsplit(block, 32) #g(LEFT), d(RIGHT)

            tmp = None
            for i in range(16): #Do the 16 rounds
                if action == ENCRYPT:
                    tmp = self.xor(self.keys[i], d)#If encrypt use Ki
                else:
                    tmp = self.xor(self.keys[15-i], d)#If decrypt start by the last key
                g = d
                d = tmp
            result += d+g
        
        final_res = bit_array_to_string(result)
        print(final_res)
        if action==DECRYPT:
            text_blocks = nsplit(final_res, 8) #Se divide el texto en bloques de 8 bytes es decir 64 bits
            print(text_blocks)
            final_res = ""
            self.cesar.password = self.password[4]
            for block in text_blocks:
                self.cesar.text = block
                final_res += self.cesar.decrypt()
                
        return final_res 

    
    

jad = Jad()
jad.password = "holacomo"
jad.text = "hola como estas!"
jad.generateKeys()
textooo = jad.run("holacomo","hola como estas!",ENCRYPT)
print(textooo)
textooo = jad.run("holacomo",textooo,DECRYPT)
#print(textooo)
#print(jad.keys)