from asyncore import read
from importlib.resources import path
import pandas as pd 
import os

datos = pd.read_excel(r"C:\Users\jaam2\OneDrive\Escritorio\Automatizacion Python-Hugo\Faltante\Walmart Faltante.xlsx")
datos_faltantes = pd.DataFrame(datos)

valor = [71.34, 1434.68, 7]

#id_externo = datos_faltantes[datos_faltantes["Monto"] == valor]["Id externo"]
#fecha = datos_faltantes[datos_faltantes["Monto"] == valor]["Fecha"]

for i in datos_faltantes:
    print(i)
    """
    
    if datos_faltantes["Monto"][i] == valor[i]:
        #datos_faltantes["Monto"][i]
        #print(datos_faltantes["Monto"][i])
        print("Concuerda")
        
    else:
        print("No concuerda")
     """

#print(datos_faltantes.shape[1])

#df.iloc[0] = ('Josy', 'Clarae', 'Female')
#print(datos_faltantes["Monto"])
# print(datos_faltantes.shape)

