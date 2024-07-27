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
  

  
