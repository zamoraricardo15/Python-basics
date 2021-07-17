# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 09:07:30 2020

@author: rzamoram
"""

#Tarea 3
#Ricardo Zamora Mennigke

#Ejercicio 1
##Tres atributos A, B, y C (retorna menor cuadrado, mayor cubo, producto tres y suma cosenos)
import math

class Punto:
    def __init__(self, A = 0, B = 0, C = 0): # Constructor
        self.A = A
        self.B = B
        self.C = C
    def cambiar(self, A, B, C): #Cambiar inicial
        self.A = float(A)
        self.B = float(B)
        self.C = float(C)
    def menor_cuadrado(self): #indica el menor y lo estima al cuadrado
        if (self.A <= self.B and self.A <= self.C):
            return((self.A)**2)
        elif self.B <= self.C:
            return((self.B)**2)
        else:
            return((self.C)**2)
    def mayor_cubo(self): #indica el mayor y lo estima al cubo
        if (self.A >= self.B and self.A >= self.C):
            return((self.A)**3)
        elif self.B >= self.C:
            return((self.B)**3)
        else:
            return((self.C)**3)
    def producto_abc(self): #producto de los tres
        productocosenos = (self.A*self.B*self.C)
        return(productocosenos)
    def suma_cosenos(self):  #estimacion de suma cosenos
        sumacosenos = ((math.cos(self.A)) + (math.cos(self.B)) + (math.cos(self.C)))
        return(sumacosenos)
    def __str__(self):
        return "Punto: (%i, %i, %i)" % (self.A,self.B, self.C)
    
Punto1 = Punto(2,3, 4)
Punto2 = Punto(-5,6, 7)
print(Punto1)
print(Punto2)

Punto1.menor_cuadrado()
Punto1.mayor_cubo()
Punto1.producto_abc()
Punto1.suma_cosenos()

Punto2.menor_cuadrado()
Punto2.mayor_cubo()
Punto2.producto_abc()
Punto2.suma_cosenos()

Punto1.cambiar(33, 54, 76)
Punto1.menor_cuadrado()
Punto1.mayor_cubo()
Punto1.producto_abc()
Punto1.suma_cosenos()



#Ejercicio 2
##Sistema de control para linea aerea

##Vuelo
class vuelo:   ##define el vuelo
    def __init__(self, numero = 0, salida = 0, llegada = 0): ##define atributos del vuelo
        self.numero = numero
        self.salida = salida
        self.llegada = llegada
    def info_vuelo(self):  ##arroja informacion del vuelo
        infovuelo = str(self.numero) + ' ' + str(self.salida) + ' ' + str(self.llegada)
        return infovuelo.title()

##Vuelo comercial
class vuelocomercial(vuelo):
    def __init__(self, numero = 0, salida = 0, llegada = 0, pasajeros = None):
        super().__init__(numero, salida, llegada)
        if pasajeros == None:
            self.__pasajeros = []
        else:
            self.__pasajeros = pasajeros
    @property
    def pasajeros(self):
        return self.__lista_pasajeros
    @pasajeros.setter
    def agregar(self, nuevo):
        for pasajero in self.pasajeros:
            if pasajero.codigo == nuevo.codigo:
                return None
        self.__pasajeros.append(nuevo)
    def eliminar(self, codigo):
        for pasajero in self.pasajeros:
            if pasajero.codigo == codigo:
                self.__pasajeros.pop(pasajero)
                return None
    def monto_total_vendido(self):
        monto = 0
        for pasajero in self.pasajeros:
            monto = monto + pasajero.preciototal()
        return monto
    def __str__(self):
        s = f"{super().__str__()}\nMonto Vendido:{self.monto_total_vendido()}"
        s = s + "\n" + " Pasajeros ".center(25, '*') + "\n"
        for pasajero in self.lista_pasajeros:
            s = s + "*" * 25 +"\n" + str(pasajero) + "\n"
        return s

##Vuelo local (USA)
class vuelo_local(vuelocomercial):
    def __init__(self, numero, salida, llegada, pasajeros):
        super().__init__(numero, salida, llegada, pasajeros)
        self.minimo_pasajeros = 1
    @property
    def pasajeros_minimos(self):
        return (self.pasajeros_minimos)
    def __str__(self):
        minimo = super().__str__() + "\n" + self.pasajeros_minimos()
        return minimo


##Vuelo internacional
class vuelo_internacional(vuelocomercial):
    def __init__ (self, numero, salida, llegada, pasajeros, pasajeros_minimos):
        super().__init__(numero, salida, llegada, pasajeros, pasajeros_minimos)
        self.pais_destino = 'CANADA'
    @property
    def pais_destino(self):
        return (self.pais_destino)
    def __str__(self):
        pais = super().__str__() + "\n" + self.pais_destino()
        return pais

##Vuelo carga
class vuelo_carga(vuelo):
    def __init__(self, numero, salida, llegada):
        super().__init__(numero, salida, llegada)
        self.carga = 1
    @property
    def carga_maxima(self):
        return (self.carga_maxima)
    def __str__(self):
        cargamaxima = super().__str__() + "\n" + self.carga_maxima
        return cargamaxima

##Pasajero
class pasajero(object):
    def __init__(self, codigo, nombre, precio, impuesto, pagototal):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__impuesto = impuesto
        self.__pagototal = pagototal 
    @property
    def codigo(self):
        return str(self.__codigo)
    @property
    def nombre (self):
        return str(self.__nombre)
    @property
    def precio(self):
        return str(self.__precio)
    @property
    def impuesto(self):
        return str(self.__impuesto)
    @property
    def pagototal(self):
        return str(self.__pagototal)
    @codigo.setter
    def codigo(self, nuevo_codigo):
        self.__codigo  = nuevo_codigo
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    @precio.setter
    def precio (self, nuevo_precio):
        self.__precio = nuevo_precio
    @impuesto.setter
    def impuesto (self, nuevo_impuesto):
        self.__impuesto = nuevo_impuesto
    @pagototal.setter
    def pagototal (self, nuevo_pagototal):
        self.__pagototal = nuevo_pagototal 
    def preciototal(self):
        if  nofrecuente.__primervuelo == True:
            return (float(self.precio) + float(self.impuesto) * float(self.precio)) * - 0.05 + (float(self.precio) + float(self.impuesto) * float(self.precio))
        else: 
            return (float(self.precio) + float(self.impuesto) * float(self.precio)) * - 0.20 + (float(self.precio) + float(self.impuesto) * float(self.precio))
    def __str__(self):
        return (self.preciototal)

##Pasajero frecuente
class frecuente(pasajero):
    def __init__(self, codigo, nombre, precio, impuesto, pagototal, puntos):
        super().__init__(codigo, nombre, precio, impuesto, pagototal)
        self.__puntos = puntos
    @property
    def puntos(self):
        return str(self.__puntos)
    @puntos.setter
    def puntos(self, nuevospuntos):
        self.__puntos = nuevospuntos
    def __str__(self):
        return (self.puntos)

##Pasajero no frecuente
class nofrecuente (pasajero):
    def __init__(self, codigo, nombre, precio, impuesto, pagototal, primervuelo):
        super().__init__(codigo, nombre, precio, impuesto, pagototal)
        self.__primervuelo = primervuelo
    @property
    def primervuelo(self):
        return str(self.__primervuelo)
    @primervuelo.setter
    def primervuelo(self, nuevo_primervuelo):
        self.__primervuelo = nuevo_primervuelo
    def __str__(self):
        return (self.primervuelo) 


vuelo1 = vuelo(3, 16, 20)
vuelo1.info_vuelo()


#Ejercicio 3
##class mi DF() vista en clase
import os
import pandas as pd
pasada = os.getcwd()
os.chdir("C:/Users/rzamoram/Documents/Machine Learning/Programacion en Python/Clase 3")
os.getcwd()
ejemplo10 = pd.read_csv("Tarea 3_Ricardo_Zamora_Mennigke.csv", delimiter = ';', decimal = ",", header = 0, index_col = 0)
print(ejemplo10)
data = pd.DataFrame(ejemplo10)
import pandas as pd
import numpy as np

class mi_DF():
    def __init__(self, DF = pd.DataFrame()):
        self.__num_filas = DF.shape[0]
        self.__num_columnas = DF.shape[1]
        self.__DF = DF
    @property
    def num_filas(self):
        return self.__num_filas
    @property
    def num_columnas(self):
        return self.__num_columnas
    @property
    def DF(self):
        return self.__DF  
    def valores(self):
        divisibles3 = 0
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                if self.DF.iloc[i,j] % 2 == 0:
                    divisibles3 = divisibles3+1
        return {'Divisibles entre 3' : divisibles3}
    def DF_diccionario(self, nc):
        cor = np.corrcoef(self.DF.iloc[:,nc])
        cov = np.cov(self.DF.iloc[:,nc])
        return {'Correlacion': cor, 'Covarianza': cov}


#datos = mi_DF(pd.DataFrame(data))
datos = mi_DF(pd.DataFrame([[4,1,-3],[2,4.4,0],[-5,9,198],[2,4,-5]]))
print(datos.DF)

print(datos.valores())
print(datos.DF_diccionario(1))


#Ejercicio 4
##clase denominada Analisis que tiene como atributo una matriz numerica tipo numpy
class Analisis():
    def __init__(self, data = np.matrix([])):
        self.__M = data
        self.__filas = data.shape[0]
        self.__columnas = data.shape[1]
    @property
    def matriz(self):
        return self.__matriz
    @property
    def filas(self):
        return self.__filas
    @property
    def columnas(self):
        return self.__columnas
    def as_data_frame(self): ##matriz en data frame
        return pd.DataFrame(self.M)
    def des_estandar(self):  ##desviacion estandar
        return self.as_data_frame().std()
    def media(self): ##media
        return self.as_data_frame().mean()
    def mediana(self): ##mediana
        return self.as_data_frame().median()
    def maximo(self): ##maximo
        return self.as_data_frame().max()
    def encontar(self):
        return self.as_data_frame().where()

datos = Analisis(np.array(pd.DataFrame([[4,1,-3],[2,4.4,0],[-5,9,198],[2,4,-5]])))
print(Analisis)


