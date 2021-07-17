# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
##Tarea 1
##Ricardo Zamora Mennigke

#Ejercicio 1
##1. a) >Cual es el resultado?

#1
import math as mt
r=(mt.pi*(5**4))-(mt.sqrt(9))
print(r)

#2
r=mt.fabs(12-17*(2/7)-9)
print(r)

#3
r=mt.factorial(7)
print(r)


#4
r=mt.log(19,5)
print(r)

#5
r=mt.log(5,10)
print(r)

#6
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
##Listas
x=[1,-5,31,-1,-9,-1,0,18,90,mt.pi]
y=[1,9,-3,1,-99,-10,2,-11,0,2]

import statistics as st
st.mean(y)
st.pvariance(y)
st.pstdev(y)

st.mean(x)
st.pvariance(x)
st.pstdev(x)

import numpy as np
print(np.corrcoef(x,y)[0,1])

print(x[2:7])
print(y[2], y[7])
print(y[-3:])
print(x[::-1])
