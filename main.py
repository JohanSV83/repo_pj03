import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import exploracionDx  as explo
import tratamientoDx as tr


data=pd.read_csv('https://raw.githubusercontent.com/krishnaik06/Multiple-Linear-Regression/master/50_Startups.csv')

opcion=input("ingresa opcion 1 para ver correlacion de variables\ningresa opcion 2 para eliminar columnas erroneas\ningresa opcion 3 para ver pairplot\ningresa opcion 4 ver grafico pairplot")
def menu():
    if opcion=='1':
      explo.Mostrar_Correlacion(data)
    elif opcion=='2':
      tr.Eliminar_Limpiar_datos(data)

    elif opcion=='3':
      tr.eliminar_filas_erroneas(data)  
      
    elif opcion=='4':
      explo.Mostrar_Grafico_Pairplot(data) 


menu()

  
              

  


