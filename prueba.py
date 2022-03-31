from importlib.resources import path
import pandas as pd 

input_cols =["ID Interno Factura", "ID Interno Empleado", "ID Interno CxP", "ID Interno Subsidiaria",
             "Moneda", "Nota", "Monto a Pagar", "Propuesta de Pago Relacionada"]

df = pd.read_excel(r"C:\Users\jaam2\OneDrive\Escritorio\Automatizacion Python-Hugo\Input\PP-632.xlsx",
                usecols=input_cols) #Se indica que con un 0 contiene el titulo de las columnas

df.insert(0, "ID interno cuenta pagadora", "0")
"""
for mon in  df["Moneda"]:
    if mon == "Quetzal GTQ":
        print("ES QUETZAL")
    else:
        print("NO ES")
"""
"""
for id in df["ID Interno Subsidiaria"]:
    print(id)
"""
"""
for mon in  df["Moneda"]:
    for id in df["ID Interno Subsidiaria"]:
        if mon == "US Dollar" and id == 15:
            df["Id Interno Factura"] = 
            print(df) #Cambiar a tipo numero
        elif mon == "Quetzal GTQ" and id == 26:
            pass
        elif mon == "US Dollar" and id == 26:
            pass
        elif mon == "US Dollar" and id == 15:
            pass
        elif mon == "US Dollar" and id == 15:
            pass
"""

for i in range(len(df)):
    if df["Moneda"][i] == "US Dollar" and df["ID Interno Subsidiaria"][i] == 15:
        df.at[i,  'ID interno cuenta pagadora'] = 724
    elif df["Moneda"][i] == "Quetzal GTQ" and df["ID Interno Subsidiaria"][i] == 26:
        df.at[i,  'ID interno cuenta pagadora'] = 727

                        
print(df)

#print(df["Moneda"]=="Quetzal GTQ")
"""
for mon in  df["Moneda"]:
    for id in df["ID Interno Subsidiaria"]:
        if mon == "US Dollar" and id == 15:
            df["ID interno cuenta pagadora"] = 724
            print(df["ID interno cuenta pagadora"])
"""
#for i in range(len(df)):