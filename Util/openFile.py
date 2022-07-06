import os

def openFile(path):
    try:
        print("Leyendo archivo...")
        archivo = open(path)
        dataSet = []
        for linea in archivo:
            datos = linea.strip().split(",")
            dataSet.append(datos)
        archivo.close()
        print("Archivo leído con éxito.")
        return dataSet
    except IOError as e:
        print("El archivo no existe. {}".format(e))