from importlib.resources import path
from pydoc import doc
import pandas as pd 

input_cols =["ID Interno Factura", "ID Interno Empleado", 
             "ID Interno CxP", "ID Interno Subsidiaria",
             "Moneda", "Nota", "Monto a Pagar", "Propuesta de Pago Relacionada"]
columnas_minusculas =["id interno factura", "id interno empleado", 
                      "id interno cxp", "id interno subsidiaria",
                      "moneda", "nota", "monto a pagar", "propuesta de pago relacionada"]

"""
for i in range(len(input_cols)):
    input_cols[i] = input_cols[i].lower()
"""
documento = r"C:\Users\jaam2\OneDrive\Escritorio\Automatizacion Python-Hugo\Input\Carga pt1.xlsx"
df = pd.read_excel(documento)

