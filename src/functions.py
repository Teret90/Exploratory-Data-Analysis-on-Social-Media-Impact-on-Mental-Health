import pandas as pd
import os
def cargar_datos(file_path):
    """Carga un archivo CSV desde la ruta proporcionada, manejando errores si no se encuentra."""
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        print(f"El archivo no se encuentra en la ruta: {file_path}")
        return None  
    

def estadisticas_basicas(df):
    """Genera estadísticas descriptivas básicas del DataFrame con info, describe y null values."""
    print("Estadísticas Descriptivas:")
    print(df.describe())  
    print("\nInformación de las columnas:")
    print(df.info())  
    print("\nValores Nulos:")
    print(df.isnull().sum())  