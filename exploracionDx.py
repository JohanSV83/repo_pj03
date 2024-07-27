import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def Mostrar_Correlacion(df):
  correlation_matrix = df[['Administration','R&D Spend','Marketing Spend','Profit']].corr()
  print(correlation_matrix)
  sns.heatmap(correlation_matrix, annot=True, cmap='Blues')
  return  plt.show()


  def Mostrar_Grafico_Pairplot(df):
    return sns.pairplot(df)
  

  def eliminar_filas_erroneas(df,eliminar_nulos=True,eliminar_duplicados=True,condicion=None):
    if eliminar_nulos:
      df.dropna()
    if eliminar_duplicados:
      df.drop_duplicates()
    if condicion is not None:
      df=condicion(df)

    return df  


