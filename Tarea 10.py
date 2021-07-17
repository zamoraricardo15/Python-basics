# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Tarea 1
#Ricardo Zamora Mennigke

#Ejercicio 1
##1. a) >Cual es el resultado?

###1
import math as mt
r=(mt.pi*(5**4))-(mt.sqrt(9))
print(r)

###2
r=mt.fabs(12-17*(2/7)-9)
print(r)

###3
r=mt.factorial(7)
print(r)


###4
r=mt.log(19,5)
print(r)

###5
r=mt.log(5,10)
print(r)

###6
r=(mt.e**0.555457)
print(r)

##1.b) Calcule el valor de x
y=mt.pi
z=4
x=(1+y)/(1+2*(z**2))
print(x)

##1.c) Calcule el valor de x
x=(-90)
y=mt.pi
z=mt.sqrt(x**2+y**2)
print(z)


#Ejercicio 2
##Dado x y y como listas

###Listas
x=[1,-5,31,-1,-9,-1,0,18,90,mt.pi]
y=[1,9,-3,1,-99,-10,2,-11,0,2]
print(x)
print(y)

###Estadisticas de y
import statistics as st
print(st.mean(y))
print(st.pvariance(y))
print(st.pstdev(y))

###Estadisticas de x
print(st.mean(x))
print(st.pvariance(x))
print(st.pstdev(x))

###Correlacion x y y
import numpy as np
print(np.corrcoef(x,y)[0,1])


###Extraer indices del 2 al 7 de x
print(x[2:8])

###Extraer indices del 2 y 7 de y
print(y[2], y[7])

###Extraer ultimos 3 valores de y
print(y[-3:])

###x invertida
print(x[:-11:-1])


#Ejercicio 3
###Tabla de datos en un data frame
import pandas as pd
datos = {'Genero':["M", "F","F", "F","M","F"],
         'Peso': ["76", "67","55","57","87","48"],
         'Edad':["25","23","19","18","56","13"],
         'Nivel Educativo': ["Lic", "Bach", "Bach", "Bach", "Dr", "MSc"]}
tabla = pd.DataFrame(datos)
print(tabla)


#Ejercicio 4
###Tabla de datos en un data frame
datos1 = {'id':["1","2","3","4","5","6","7","8","9","10"],
          'calificacion':["B","C","B","A","A","A","C","B","A","B"],
          'tiempo':["64","85","76","83","81","78","68","82","89","62"]}
tabla1 = pd.DataFrame(datos1)
print(tabla1.info())
print(tabla1)


##Ejercicio 5
###Realice las operaciones dado x

###Indices de vector divididos entre 2 son igual a 45
x = [24,28,29,18,95,97,90,72,87,85,74,9,40]
sumatoria = 0 

for elemento in x:
    elemento = 90
    indice = x.index(elemento)
    elemento = elemento + 1 
print(indice)

###Valor mas alto del vector
indice2 = x.index(max(x))
print(indice2)

###Suma de valores de lista usando for
for elemento in x:
    sumatoria = sumatoria + elemento
print(sumatoria)

###Suma de valores eleveados al cubo usando for
sumat=0
for elemento in x:
    cuadrado = elemento**2
    sumat = sumat + cuadrado
print(sumat)


#Ejercicio 6
###Calcule sumatoria usando sum de v1, v2 y v3, y luego empleando for
v1 = [2,7,6,4,52,-2]
v2 = [7,5,7,0,1,0]
v3 = [2,4,3,5,6, mt.pi]

print(sum(v1))
print(sum(v2))
print(sum(v3))

sumatoria1 = 0 
sumatoria2 = 0 
sumatoria3 = 0 

for elemento in v1:
    sumatoria1 = sumatoria1 + elemento
print(sumatoria1)


for elemento in v2:
    sumatoria2 = sumatoria2 + elemento
print(sumatoria2)


for elemento in v3:
    sumatoria3 = sumatoria3 + elemento
print(sumatoria3)


#Ejercicio 7
###Construya un diccionario x resumen
x = [24,28,29,18,95,97,90,72,87,85,74,9,40,91,87,92,-3]
resumen = {"Media":st.mean(x), "Moda":st.mode(x),"Maximo":max(x),"Minimo":min(x)}
print(resumen)


#Ejercicio 8
###Efectue la operacion entre matrices
M = np.matrix([[9,3,4],[1,3,-1]])
N = np.matrix([[91,-3],[1,8],[-4,5]])
A = M + 31*N.T
print(A)


#Ejercicio 9
###Cargue en un data frame el archivo
import os
pasada = os.getcwd()
os.chdir("C:/Users/rzamoram/Documents/Programacion en Python/Clase 1")
os.getcwd()
ejemplo = pd.read_csv("EjemploAlgoritmosRecomendacion.csv", delimiter = ';', decimal = ",",
                      header = 0, index_col = 0)
print(ejemplo)
data = pd.DataFrame(ejemplo)

###Dimensiones de la tabla
print(data)
print(data.shape)

###Primeras 3 columnas usando []
print(data[["VelocidadEntrega","Precio"]])

###Primeras 3 columnas usando iloc
print(data.iloc[:,0:2])

###Primeras 3 columnas usando loc
print(data.loc[:,["VelocidadEntrega","Precio"]])

###info de los datos
print(data.info())

###Media para todas las variables
print(data.describe(include = [np.number]))
print(ejemplo.mean())


#Ejercicio 10
###Cargue en un data frame el archivo
ejemplo1 = pd.read_csv("SAheart.csv", delimiter = ';', decimal = ".", header = 0, index_col = 0)
print(ejemplo1)
data1 = pd.DataFrame(ejemplo1)
print(data1)

###Dimensiones de la tabla
print(data1.shape)

###Primeras 4 columnas usando []
print(data1[["tobacco","ldl", "adiposity"]])

###Primeras 4 columnas usando iloc
print(data1.iloc[:,0:3])

###Primeras 3 columnas usando loc
print(data1.loc[:,["tobacco","ldl", "adiposity"]])

###info de los datos
print(data1.info())

###Suma de variables cuantitativas
data2 = data1.describe(include = [np.number])
print(data2.sum())



#Ejercicio 11
###Suma de numeros enteros elevados al cubo del 1 al 100
sumato1 = 0
for elemento in range(0,101):
    cuadrado = elemento**2
    sumato1 = sumato1 + cuadrado
print(sumato1)


#Ejercicio 12
###Sumatoria de numeros comprendidos entre el 1 y el n
sumato2 = 0
n=200

for elemento in range(1,n+1):
    sumato2 = sumato2 + elemento
print(sumato2)


#Ejercicio 13
###Sumatoria de numeros pares comprendidos entre el 1 y el n
sumato3 = 0
n=15

for elemento in range(2,n+1,2):
    sumato3 = sumato3 + elemento
print(sumato3)


#Ejercicio 14
###Sumatoria de numeros multiplos de 5 comprendidos entre el 1 y el n
sumato4 = 0
n=15 

for elemento in range(5,n+1,5):
    sumato4 = sumato4 + elemento
print(sumato4)
 

#Ejercicio 15
###Calcule la traza de la matriz
import numpy as np
A = np.matrix([[9,3,4],[1,0,-1],[4,12,-2]])

tam_filas, tam_columnas = A.shape
sumas_por_fila = []
suma = 0

for indice_fila in range(tam_filas):
    for indice_columna in range(tam_columnas):
        if [indice_fila] == [indice_columna]:
            suma = suma +  A[indice_fila, indice_columna]
            sumas_por_fila.append(suma)
            suma = 0
    
sum(sumas_por_fila)


#Ejercicio 16
###Obtenga el centro de la matriz
A = np.matrix([[1,1,1,1],[1,9,9,1],[1,9,9,1],[1,1,1,1]])
print(A[1:3,1:3])


