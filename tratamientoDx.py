import pandas as pd

#data=pd.read_csv('https://raw.githubusercontent.com/krishnaik06/Multiple-Linear-Regression/master/50_Startups.csv')

def Eliminar_Limpiar_datos(df, metodo='eliminar', axis=0):

    if metodo == 'eliminar':
        df_limpio = df.dropna(axis=axis)
    elif metodo == 'rellenar':
        df_limpio = df.fillna(df.mean() if axis == 0 else df.mode().iloc[0])
    else:
        raise ValueError("El método debe ser 'eliminar' o 'rellenar'.")
    
    return df_limpio

def eliminar_filas_erroneas(df,eliminar_nulos=True,eliminar_duplicados=True,condicion=None):
    if eliminar_nulos:
      df.dropna()
    if eliminar_duplicados:
      df.drop_duplicates()
    if condicion is not None:
      df=condicion(df)

    return df
