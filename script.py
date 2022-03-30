from importlib.resources import path
import pandas as pd 

#Libreria para la manipulacion de datos

#Columnas que quiero leer(Indices parten del numero 0)


def main():
    
    pp = input("# de PP: ")    

    df = leer_archivos()
    df = agregar_filtros(df, pp)
    visualizar_datos(df)
    
    dia = input("Dia: ")
    mes = input("# del mes: ")
    fecha_completa = pd.to_datetime(f'{dia}/{mes}/22', dayfirst=True)
    
    renombrar_columnas(df)
    agregar_columnas(df, fecha_completa)
    df = cambiar_orden_columnas(df) #
    exportar_datos(df, pp, dia)

def leer_archivos():
    print("Leyendo archivo")
    import os
    
    input_cols =[1,7,8,9,12,14,17,19]

    #Pedir al usuario que ingrese el nombre del archivo
    path = "C:\\Users\\jaam2\\OneDrive\\Escritorio\\Automatizacion Python-Hugo\\Input\\"
    filename = input("Ingresar el nombre del archivo: ") + ".xlsx"
    fullpath = os.path.join(path, filename)
    
    df = pd.read_excel(fullpath, #Se pone el nombre del archivo y su extension
                    sheet_name="ResultadosPagosdeInformedeGast", #La hoja que leera del archivo
                    header= 0,
                    usecols=input_cols) #Se indica que con un 0 contiene el titulo de las columnas
    return df

def agregar_filtros(df, pp):
    print("Agregando filtros...")
    #df = df[df["ID Interno Factura"] == "PP-651"]
    df = df[df["Propuesta de Pago Relacionada"]== f"PP-{pp}"] #Probar mañana domingo
    return df
    
def visualizar_datos(df):
    print("Visualizando los primeros 3 registros")
    df_cols = df.columns
    
    for col in df_cols:
        print(df[col].head(3))

def exportar_datos(df, pp, dia):
    #Exportar a la carpeta output
    print("Exportando archivo procesado...")
    
    df.to_csv(f"C:\\Users\\jaam2\\OneDrive\\Escritorio\\Automatizacion Python-Hugo\\Output\\PP-{pp} SV Walmart {dia} Marzo CONT.csv",
            sep = ",", #Separador que queremos
            header= True, #Que se exporte con los headers
            index= False) #Para que la primera columna no sea un autonumerico 

def renombrar_columnas(df):
    print('Cambiando nombres...')
    df.rename(columns={"ID Interno Empleado":"Id interno proveedor"}, inplace = True)
    df.rename(columns={"ID Interno Factura":"Id Interno Factura"}, inplace = True)
    df.rename(columns={"ID Interno CxP":"Id interno cxp"}, inplace = True)
    df.rename(columns={"ID Interno Subsidiaria":"Id Interno Subsidiaria"}, inplace = True)
 

def agregar_columnas(df, fecha_completa):
    rows = df.shape[0]
    
    df.insert(0, "ID interno cuenta pagadora", "724")
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
#print(df.shape) #Mirar las dimensiones del archivo (filas, columnas)
#print(df.columns) #Sirve para ver el nombre de las columnas
#print(df["ID Interno Factura"].head(2))

if __name__ == "__main__":
    main()
    input("\tProceso finalizado. ENTER PARA SALIR")
