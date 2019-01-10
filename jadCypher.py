from jad2 import Jad

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


class JadCypher():
    def __init__(self):
        self.blocks = list()
        self.vi = list()
    def generateBlocks(self,text,size_block):
        self.blocks = []
        blocks = nsplit(text, size_block)
        for block in blocks:
            self.blocks.append(string_to_bit_array(block))
    def initvi(self,size_block):
        self.vi = string_to_bit_array("\x00"*size_block)
    def xor(self, t1, t2):#Apply a xor and return the resulting list
        return [x^y for x,y in zip(t1,t2)]
            
    def encrypt(self,text,password,size_block):
        result = ""
        self.generateBlocks(text,size_block)
        self.initvi(size_block)

        jad = Jad()
        for i in range(len(self.blocks)):
            xor = self.xor(self.vi,self.blocks[i])
            #print(len(xor))
            textXor = bit_array_to_string(xor)
            encryp = jad.encrypt(textXor,password,len(textXor))
            #print(encryp)
            self.vi = string_to_bit_array(encryp)
            result += encryp

            #newtext = self.xor(self.vi,self.blocks[i])
            #textoBlock = bit_array_to_string(newtext)
            #self.vi = jad.encrypt(textoBlock,password,len(textoBlock))
        #print(result)
        return result 

    def decrypt(self,text,password,size_block):
        #print(text)
        result = ""
        self.generateBlocks(text,size_block)
        self.initvi(size_block)
        print(self.vi)
        jad = Jad()
        #print(len(self.blocks))        
        for i in range(len(self.blocks)):
            texto = bit_array_to_string(self.blocks[i])
            decryp = jad.decrypt(texto,password,len(texto))
            #print(decryp)
            plaintext = self.xor(self.vi,string_to_bit_array(decryp))
            self.vi = self.blocks[i]
            
            result += bit_array_to_string(plaintext)
        return result


jadcypher = JadCypher()
texto = jadcypher.encrypt("holacomoestatula","golacomo",8 )
#print("encryptado:", texto)
textodecrypt = jadcypher.decrypt(texto,"golacomo",8)
print("desent: ", textodecrypt)

        

    
