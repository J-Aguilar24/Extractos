from importlib.resources import path
import pandas as pd 

#Libreria para la manipulacion de datos

#Columnas que quiero leer(Indices parten del numero 0)


def main():
    
    pp = input("# de PP: ")    

    df = leer_archivos()
    df = agregar_filtros(df, pp)
    
    
    dia = input("Dia: ")
    mes = input("# del mes: ")
    fecha_completa = pd.to_datetime(f'{dia}/{mes}/22', dayfirst=True)
    
    renombrar_columnas(df)
    agregar_columnas(df, fecha_completa)
    df = cambiar_orden_columnas(df)
    agregar_cuenta_pagadora(df)
    visualizar_datos(df) 
    exportar_datos(df, pp, dia, mes) 

def leer_archivos():
    print("Leyendo archivo")
    import os
    #nombre_hoja = input("Escribe el nombre de la hoja: ")

    #Pedir al usuario que ingrese el nombre del archivo
    path = "C:\\Users\\jaam2\\OneDrive\\Escritorio\\Automatizacion Python-Hugo\\Input\\"
    filename = input("Ingresar el nombre del archivo: ") + ".xlsx"
    fullpath = os.path.join(path, filename)
    
    df = pd.read_excel(fullpath, #Se pone el nombre del archivo y su extension
                    #sheet_name= nombre_hoja, #La hoja que leera del archivo #
                    header= 0) #Se indica que con un 0 contiene el titulo de las columnas
    for i in range(len(df.columns.values)):
        df.columns.values[i] = df.columns.values[i].lower()
        if df.columns.values[i] == "id interno proveedor":
            df.rename(columns={"id interno proveedor":"id interno empleado"}, inplace = True) #Cambiar a id interno empleado

    return df

def agregar_filtros(df, pp):
    print("Agregando filtros...")
    df = df[df["propuesta de pago relacionada"]== f"PP-{pp}"] 
    return df
    
def visualizar_datos(df):
    print("Visualizando los primeros 3 registros")
    df_cols = df.columns
    
    for col in df_cols:
        print(df[col].head(3))

def exportar_datos(df, pp, dia, mes):
    #Exportar a la carpeta output
    print("Exportando archivo procesado...")
    
    df.to_csv(f"C:\\Users\\jaam2\\OneDrive\\Escritorio\\Automatizacion Python-Hugo\\Output\\PP-{pp} {dia}{mes} CONT.csv",
            sep = ",", #Separador que queremos
            header= True, #Que se exporte con los headers
            index= False,
            encoding='utf-8') #Para que la primera columna no sea un autonumerico 
            #latin1
def renombrar_columnas(df):
    print('Cambiando nombres...')

    df.rename(columns={"moneda":"Moneda"}, inplace = True)
    df.rename(columns={"nota":"Nota"}, inplace = True)
    df.rename(columns={"monto a pagar":"Monto a Pagar"}, inplace = True)
    df.rename(columns={"propuesta de pago relacionada":"Propuesta de Pago Relacionada"}, inplace = True)
    #
    df.rename(columns={"id interno empleado":"Id interno proveedor"}, inplace = True)
    df.rename(columns={"id interno factura":"Id Interno Factura"}, inplace = True)
    df.rename(columns={"id interno cxp":"Id interno cxp"}, inplace = True)
    df.rename(columns={"id interno subsidiaria":"Id Interno Subsidiaria"}, inplace = True)
 

def agregar_columnas(df, fecha_completa):
    rows = df.shape[0]
    
    df.insert(0, "ID interno cuenta pagadora", 0) #Solo se crea la columna
    #df.insert(1, "Id interno cxp", "114")
    df.insert(2, "Aprobado", "APROBADO")
    df.insert(5, "ID Externo Pago", "421388340") #Es el mismo numero?
    #df.insert(8, "Id Interno Subsidiaria", "15")
    
    #Info de otras 
    df.insert(9, "Fecha", fecha_completa)
    df.insert(10, "ID externo", "")
        
def cambiar_orden_columnas(df): 
    
    df = df[["ID interno cuenta pagadora", "Id interno cxp", "Aprobado", "Moneda", "Id interno proveedor",
             "ID Externo Pago", "Nota", "Id Interno Subsidiaria",
             "Fecha", "ID externo", "Monto a Pagar", "Id Interno Factura"]]

    return df

def agregar_cuenta_pagadora(df):
    rows = df.shape[0] # == 3
    for i in range(rows):
        if df.iloc[i, 3] == "US Dollar" and df.iloc[i, 7] == 15: # SV
            df.iat[i,0] = 724
        elif df.iloc[i, 3] == "Quetzal GTQ" and df.iloc[i, 7] == 26: # GT
            df.iat[i, 0] = 727
        elif df.iloc[i, 3] == "US Dollar" and df.iloc[i, 7] == 26: # GT
            df.iat[i, 0] = 990
        elif df.iloc[i, 3] == "Lempira HNL" and df.iloc[i, 7] == 24: # HN
            df.iat[i, 0] = 713
        elif df.iloc[i, 3] == "US Dollar" and df.iloc[i, 7] == 24: # HN
            df.iat[i, 0] = 992
        elif df.iloc[i, 3] == "Cordoba NIO" and df.iloc[i, 7] == 25: # NI
            df.iat[i, 0] = 1077
        elif df.iloc[i, 3] == "US Dollar" and df.iloc[i, 7] == 25: # NI
            df.iat[i, 0] = 1078
        elif df.iloc[i, 3] == "Peso Dominicano DOP" and df.iloc[i, 7] == 27: # RD
            df.iat[i, 0] = 730
        elif df.iloc[i, 3] == "US Dollar" and df.iloc[i, 7] == 27: # RD
            df.iat[i, 0] = 993
        elif df.iloc[i, 3] == "Dólar Jamaiquino JMD" and df.iloc[i, 7] == 32: # RD  #AFECTA TILDE?
            df.iat[i, 0] = 1485
        elif df.iloc[i, 3] == "US Dollar" and df.iloc[i, 7] == 32: # RD
            df.iat[i, 0] = 1487
        else:
            df.iat[i, 0] = 0
        
                
        #print(df.iloc[i, 3]) #Moneda
        #print(df.iloc[i, 7]) # Id interno sub
    

#print(df.shape) #Mirar las dimensiones del archivo (filas, columnas)
#print(df.columns) #Sirve para ver el nombre de las columnas
#print(df["ID Interno Factura"].head(2))

if __name__ == "__main__":
    numero_pp = int(input("Cuantas PP quieres cargar? "))
    i = 0
    while i < numero_pp:
        main()
        i = i+1
    input("\tProceso finalizado. ENTER PARA SALIR")
