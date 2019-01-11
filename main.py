#import modulo as m
#m.funcion()
from jadCypher import JadCypher
import time
import matplotlib.pyplot as plt

def encryptFile(inputName,outputName,password,size_block):
    jad = JadCypher()
    inputFile = open(inputName,"r")
    outputFile = open(outputName, "w")
    text = ""
    for line in inputFile:
        text += line
    stringOutput = jad.encrypt(text,password,size_block)
    outputFile.write(stringOutput)
    inputFile.close()
    outputFile.close()

def decryptFile(inputName,outputName,password,size_block):
    jad = JadCypher()
    inputFile = open(inputName,"r")
    outputFile = open(outputName, "w")
    text = ""
    for line in inputFile:
        text += line
    stringOutput = jad.decrypt(text,password,size_block)
    outputFile.write(stringOutput)
    inputFile.close()
    outputFile.close()

def printMenu():
    print("    MENU\n")
    print("1) Cambiar tamaño del bloque.")
    print("2) Cambiar contraseña.")
    print("3) Encriptar archivo.")
    print("4) Desencriptar archivo.")
    print("5) Salir")

def main():
    
    size_block = 8
    password = "holacomo"
    menu = ""
    print("NOTA: Tamaño del bloque por defecto: 8 ")
    print("      Contraseña por defecto: 'holacomo' \n\n")
    while(True):
        printMenu()
        menu = input("Ingresa una opción: ")
        if(menu == '1'):
            try:
                size_block = int(input("Ingrese el tamaño del bloque: "))
            except:
                print("Error al ingresar el tamaño del bloque.")
        elif (menu == '2'):
            try:
                password = input("Ingrese la contraseña: ")
            except:
                print("Error al ingresar el la contraseña.")
        elif (menu == '3'):
            try:
                inputName = input("Ingrese el nombre del archivo de entrada: ")
                outputName = input("Ingrese el nombre del archivo de salida: ")
                """start_time = time.time()
                encryptFile(inputName,outputName,password,size_block)
                exec_time = (time.time() - start_time)
                throughput = size_block/(time.time() - start_time)
                print("Time: ", exec_time)
                print("Throughput: ", throughput)"""
                #sizeBloques = [1,2,4,8,16,32]
                sizeBloques = []
                tiempos = []
                throughputs = []
                for i in range(1,32):
                    sizeBloques.append(i)
                for size in sizeBloques:
                    start_time = time.time()
                    encryptFile(inputName,outputName,password,size)
                    exec_time = (time.time() - start_time)
                    throughput = size/(time.time() - start_time)
                    tiempos.append(exec_time)
                    throughputs.append(throughput)
                    print("Tiempo de cifrado (tamaño " + str(size) + "): %s segundos" % exec_time)
                    print("Throughput (tamaño " + str(size) + "): %s" % throughput)
                graficar("","Tamaño del bloque [Bytes]", "Tiempo [s]", sizeBloques, tiempos)
                graficar("","Tamaño del bloque [Bytes]", "Throughput", sizeBloques, throughputs)
                 
            except:
                print("Error al encriptar, intente nuevamente.")
        elif (menu == '4'):
            try:
                inputName = input("Ingrese el nombre del archivo de entrada: ")
                outputName = input("Ingrese el nombre del archivo de salida: ")
                decryptFile(inputName,outputName,password,size_block)
            except:
                print("Error al desencriptar, intente nuevamente.")
        elif (menu == '5'):
            break

def graficar(title,xlabel,ylabel,x,y):
	print("Mostrando grafico...")
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.plot(x,y,"-")
	plt.show()





main()

