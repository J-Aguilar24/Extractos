from importlib.resources import path
import pandas as pd
import os

def main():
    
    pp = input("# de PP: ")    

    df = leer_archivos()
    df = agregar_filtros(df, pp)
    
    renombrar_columnas(df)
    agregar_columnas(df)
    
    #Agregar tipo entidad
    try:
        tipo_entidad = df["tipo de entidad"].iloc[0]
        nombre_entidad_acortado = tipo_entidad[3::]
    except Exception: 
        print("NO SE ENCONTRÓ TIPO ENTIDAD...")
        nombre_entidad_acortado = "Vacia"
    
    df = cambiar_orden_columnas(df)
    agregar_cuenta_pagadora(df)
    
    #Recuperando el numero de subsidiaria para incluir en el nombre
    try:
        num_subsidiaria = df["Id Interno Subsidiaria"].iloc[0]
    except Exception: 
        print("ERROR CON PP (No encontrada)")
        num_subsidiaria = 0
        
    if num_subsidiaria > 0 and nombre_entidad_acortado == "Vacia":
        nombre_entidad_acortado = "Walmart"
        
    nombre_estado_cuentas = input("Nombre de estado de cuentas: ")
    #Función que permite colocar automaticamente id externo y fecha
    try:
        idexterno_fecha(df, nombre_estado_cuentas)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {nombre_estado_cuentas}")
        
    #visualizar_datos(df) 
    exportar_datos(df, pp, nombre_entidad_acortado, num_subsidiaria) 

def leer_archivos():
    #print("Leyendo archivo")

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
    #print("Agregando filtros...")
    df = df[df["propuesta de pago relacionada"]== f"PP-{pp}"] 
    return df
    
def visualizar_datos(df):
    print("Visualizando los primeros 3 registros")
    df_cols = df.columns
    
    for col in df_cols:
        print(df[col].head(3))

def exportar_datos(df, pp, nombre_entidad_acortado, num_subsidiaria):
    #Exportar a la carpeta output
    #print("Exportando archivo procesado...")
    try:
        df.to_csv(f"C:\\Users\\jaam2\\OneDrive\\Escritorio\\Automatizacion Python-Hugo\\Output\\PP-{pp} {nombre_entidad_acortado} {num_subsidiaria} CONT.csv",
            sep = ",", #Separador que queremos
            header= True, #Que se exporte con los headers
            index= False,
            encoding='latin1') #Para que la primera columna no sea un autonumerico 
            
    except Exception:
        print("CAMBIANDO FORMATO POR ERROR...")
        df.to_csv(f"C:\\Users\\jaam2\\OneDrive\\Escritorio\\Automatizacion Python-Hugo\\Output\\PP-{pp} {nombre_entidad_acortado} {num_subsidiaria} CONT.csv",
            sep = ",", #Separador que queremos
            header= True, #Que se exporte con los headers
            index= False,
            encoding='utf-8') #Para que la primera columna no sea un autonumerico 
            #latin1
    print("*------------------------------------------------------------------------------------------------------------*")
def renombrar_columnas(df):
    df.rename(columns={"moneda":"Moneda"}, inplace = True)
    df.rename(columns={"nota":"Nota"}, inplace = True)
    df.rename(columns={"monto a pagar":"Monto a Pagar"}, inplace = True)
    df.rename(columns={"propuesta de pago relacionada":"Propuesta de Pago Relacionada"}, inplace = True)
    
    df.rename(columns={"id interno empleado":"Id interno proveedor"}, inplace = True)
    df.rename(columns={"id interno factura":"Id Interno Factura"}, inplace = True)
    df.rename(columns={"id interno cxp":"Id interno cxp"}, inplace = True)
    df.rename(columns={"id interno subsidiaria":"Id Interno Subsidiaria"}, inplace = True)
 

def agregar_columnas(df):
    rows = df.shape[0]
    
    df.insert(0, "ID interno cuenta pagadora", 0) #Solo se crea la columna
    #df.insert(1, "Id interno cxp", "114")
    df.insert(2, "Aprobado", "APROBADO")
    df.insert(5, "ID Externo Pago", "421388340") #Es el mismo numero?
    #df.insert(8, "Id Interno Subsidiaria", "15")
    
    #Info de otras 
    df.insert(9, "Fecha", "")
    df.insert(10, "ID externo", "")
        
def cambiar_orden_columnas(df): 
    
    df = df[["ID interno cuenta pagadora", "Id interno cxp", "Aprobado", "Moneda", "Id interno proveedor",
             "ID Externo Pago", "Nota", "Id Interno Subsidiaria",
             "Fecha", "ID externo", "Monto a Pagar", "Id Interno Factura"]]

    return df

def agregar_cuenta_pagadora(df):
    rows = df.shape[0] 
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

def idexterno_fecha(df, nombre_estado_cuentas):
    #! leer estado de cuenta
    #Buscar archivo
    path = "C:\\Users\\jaam2\\OneDrive\\Escritorio\\Automatizacion Python-Hugo\\Input\\"
    filename = nombre_estado_cuentas + ".xlsx"
    fullpath = os.path.join(path, filename)
    df_estado_cuentas = pd.read_excel(fullpath, header= 0)
    df_estado_cuentas["Valor"] = [float(str(i).replace(",", "")) for i in df_estado_cuentas["Valor"]]

    #! Hacer match con el monto
    rows_df = df.shape[0]
    no_completados = 0
     
    for i in range(rows_df):
        df_estados_filtrado = df_estado_cuentas[df_estado_cuentas["Valor"]== df.iloc[i, 10]]
        monto = df.iloc[i, 10]
        
        #Si exactamente un monto coincide, entonces: 
        if df_estados_filtrado.shape[0] == 1:
            #Cambiando los valores de fecha: 
            df.iat[i, 8] = df_estados_filtrado.iloc[0, 0]
            #Cambiando los valores de referencia:
            df.iat[i, 9] = df_estados_filtrado.iloc[0, 2]
        else:
            print(f"ERROR para el monto: {monto}")
            no_completados = no_completados + 1
            
    completados = rows_df - no_completados 
    print(f"Se completaron id y fecha: {completados} de {rows_df}")                

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
