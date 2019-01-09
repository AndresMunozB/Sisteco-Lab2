from jad import Jad

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
    def generateBlocks(self,text,size_block):
        blocks = nsplit(text, size_block)
        for block in blocks:
            self.blocks.append(string_to_bit_array(block))
    def encrypt(self,text,password,size_block):
        result = ""
        self.generateBlocks(text,size_block)
        jad = Jad()
        textoBlock = bit_array_to_string(self.blocks[0])
        result += jad.encrypt(textoBlock,password,len(textoBlock))
        for i in range(len(1,self.blocks)):
            
            textoBlock = bit_array_to_string(self.blocks[i])
            result += jad.encrypt(textoBlock,password,len(textoBlock))

        


        

    
