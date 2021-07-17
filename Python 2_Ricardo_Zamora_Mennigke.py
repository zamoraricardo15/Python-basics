# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 14:51:46 2020

@author: rzamoram
"""

#Tarea 2
#Ricardo Zamora Mennigke

#Ejercicio 1
##Dos valores, determinar el mayor

valor1 = float(input("Digite un número: "))
valor2 = float(input("Digite otro número: "))

def mayor_dos_valores(valor1, valor2):
    if valor1 > valor2:
        return("\nEl número " + str(valor1) + " es el mayor de ambos numeros.")
    elif valor1 < valor2:
        return("\nEl número " + str(valor2) + " es el mayor de ambos numeros.")
    else:
        return("Ambos numeros son iguales.")
print(mayor_dos_valores(valor1, valor2))

#Ejercicio 2
##Tres valores, determinar el mayor

A = float(input("Digite un número A: "))
B = float(input("Digite un número B: "))
C = float(input("Digite un número C: "))

def mayor_tres_valores(A,B,C):
    if A > B and A > C:
        return("\nEl número A, " + str(A) + " es el mayor de los tres numeros.")
    elif B > C:
        return("\nEl número B, " + str(B) + " es el mayor de los tres numeros.")
    else:
        return("\nEl número C, " + str(C) + " es el mayor de los tres numeros.")
print(mayor_tres_valores(A,B,C))
    

#Ejercicio 3
##Tres valores, producto de los tres
def producto_tres_valores(A,B,C):
    import math as mt
    while True:
        A = input("Digite un número A: ")
        B = input("Digite un número B: ")
        C = input("Digite un número C: ")
        try:
            A = float(A)
            B = float(B)
            C = float(C)
            return(mt.fabs(A*B*C))
        except ValueError:
            return(0)
            
print("El producto es ", producto_tres_valores(A,B,C))
print("A = ",type(A), ", B = ", type(B), ", C = ", type(C))


#Ejercicio 4
##Sumatoria al cubo de 1 a n

n = int(input("Digite un número entero mayor a 0: "))

def suma_cubos(n):
    if n <= 0:
        print("No digitaste un numero mayor a 0.")
    else:
        suma = 0
        numero = 1
        while numero <= n:
            suma = (numero**3) + suma
            numero = numero + 1
        return(suma)

print(suma_cubos(n))


#Ejercicio 5  
##Sumatoria multiplos de 3 al cubo de 1 a n
n = int(input("Digite un número entero: "))

def suma_multiplos3(n):
    sumato = 0
    for elemento in range(0,n+1,3):
           sumato = sumato + elemento
    return(sumato)
       
print(suma_multiplos3(n))

#Ejercicio 6
##Costo de llamada telefonica
t = int(input("Indique la cantidad de minutos que duro la llamada: "))

def telefono(t):
    if t < 5:
        return("El costo de la llamada es $0,4 dolares.")
    else:
        t1 = 0.4 + (t-1)/4
        return("El costo de la llamada es $" + str(t1) + " dolares.")
print(telefono(t))    
        
#Ejercicio 7
##Porcentaje valores menores de x
import math as mt
reales = [mt.pi, -3, 5, 4, 89, 127, 267, -236, 364, 457, -234]
x = float(input("Indique un numero real x: "))

def porcentaje_x(reales, x):
    elementos = 0
    for real in reales:
        if real < x:
            elementos = elementos + 1
    porcentaje =  elementos / len(reales) * 100
    return porcentaje
print(porcentaje_x(reales, x))
    
#Ejercicio 8 
##Vector v de tamano n
n = int(input("Indique un numero natural n: "))

def vector_vk_n(n):
    if n == 1:
        return[2]
    else:
        vk = vector_vk_n(n-1)
        vk.append(((vk[-1])/3) + mt.pi)
        return(vk)

print(vector_vk_n(n))
    

#Ejercicio 9
##Traza de matriz A
import numpy as np
A = np.matrix([[9,3,4],[1,3,-1],[4,12,-2]])

def suma_filas(A):
    tam_filas, tam_columnas = A.shape
    sumas_por_fila = []
    suma = 0
    for indice_fila in range(tam_filas):
        for indice_columna in range(tam_columnas):
            if [indice_fila] == [indice_columna]:
                suma = suma +  A[indice_fila, indice_columna]
                sumas_por_fila.append(suma)
                suma = 0 
    return(sum(sumas_por_fila))
print(suma_filas(A))


#Ejercicio 10
##Valores divisibles entre 2 de un dataframe
import os
import pandas as pd
pasada = os.getcwd()
os.chdir("C:/Users/rzamoram/Documents/Machine Learning/Programacion en Python/Clase 2")
os.getcwd()
ejemplo10 = pd.read_csv("ejemplo_estudiantes.csv", delimiter = ';', decimal = ",",
                      header = 0, index_col = 0)
print(ejemplo10)
data = pd.DataFrame(ejemplo10)

def valores_divisibles2(data):
    n, m = data.shape
    divisibles = 0
    for i in range(n):
        for j in range(m):
            if data.iloc[i,j] % 2 ==0: 
                divisibles = divisibles+1
                
    return{'Divisibles entre 2' : divisibles}
    
valores_divisibles2(data)


#Ejercicio 11
##Valores columnas, covarianza y correlacion de un dataframe
print(data)
encabezado = ['nombre', 'Matematicas', 'Ciencias', 'Espanol', 'Historia', 'EdFisica']
datos = [['Lucia ', 7.0, 6.5, 9.2, 8.6, 8.0],
          ['Pedro ', 7.5, 9.4, 7.3, 7.0, 7.0],
          ['Ines  ', 7.6, 9.2, 8.0, 8.0, 7.5],
          ['Luis  ', 5.0, 6.5, 6.5, 7.0, 9.0],
          ['Andres', 6.0, 6.0, 7.8, 8.9, 7.3],
          ['Ana   ', 7.8, 9.6, 7.7, 8.0, 6.5],
          ['Carlos', 6.3, 6.4, 8.2, 9.0, 7.2],
          ['Jose  ', 7.9, 9.7, 7.5, 8.0, 6.0],
          ['Sonia ', 6.0, 6.0, 6.5, 5.5, 8.7],
          ['Maria ', 6.8, 7.2, 8.7, 9.0, 7.0]]
import pandas as pd
import numpy as np
df = pd.DataFrame(columns=encabezado, data=datos)
df.set_index('nombre', inplace=True)
y = df['Matematicas']
x = df['Ciencias']

def DF_diccionario(x, y):
    correlacion = np.corrcoef(x, y)[0,1]
    covarianza = np.cov(x, y)[0,1]
    return {'Variable x': x, 'Variable y': y, 'Correlacion': correlacion, 'Covarianza': covarianza}
print(DF_diccionario(x, y))