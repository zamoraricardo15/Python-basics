# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:51:58 2020

@author: rzamoram
"""

#Tarea 4
#Ricardo Zamora Mennigke


#Ejercicio 1
##Programa de Factura
from abc import  ABCMeta, abstractmethod

class Base(metaclass = ABCMeta):
    @abstractmethod
    def __str__(self):
        pass    
    @abstractmethod
    def Captura(self):
        pass

class App:
    def __init__(self):
        self.__lista = list()
    def __menu(self):
        print(" ==================================================== ")
        print(" [1] Insertar Factura")
        print(" [2] Insertar Credito")
        print(" [3] Insertar Contado")
        print(" [4] Ver la Lista")
        print(" [5] Borrar la Lista")
        print(" [6] Salir")
        print(" ==================================================== ")
        return input("> ")
    def __mostrarLista(self):
        print("\n"*50)
        #os.system('Clear') #os.system('cls') #en windows
        for i in range(len(self.__lista)):
            print(self.__lista[i])
            print(15 * "*" + "\n")
    def principal(self):
        respuesta = ""
        while respuesta != "7":
            respuesta = self.__menu()
            if respuesta == "1":
                self.__lista.append(self.__lec.LeeDatosFactura())
            elif respuesta == "2":
                self.__lista.append(self.__lec.LeeDatosCredito())
            elif respuesta == "3":
                self.__lista.append(self.__lec.LeeDatosContado())
            elif respuesta == "4":
                self.__mostrarLista()
                input("Digite cualquier tecla para continuar")
            elif respuesta == "5":
                self.__lista.clear()

prueba = App()
prueba.principal()


class Factura(Base):
    def __init__(self, pimpuesto = 0):
        self.__pimpuesto = pimpuesto
        self.__listaCompra = []
    @property
    def pimpuesto(self):
        return self.__pimpuesto
    @pimpuesto.setter
    def pimpuesto(self, porcentajenuevo):
        self.__pimpuesto = porcentajenuevo
    def agregarcompra (self, nueva_compra):
        self.listaCompra.append(nueva_compra)
    def eliminarcompra(self, codigo):
        for i in range(len(self.__listaCompra)):
            if codigo == self.__listaCompra[i].codigo:
                del self.__listaCompra[i]
    def montototal (self, mcompra):
        return sum(mcompra)
    def total_pagar (self):
       sumatotal = (self.montototal + (self.pimpuesto * self.montototal) - (self.pimpuesto * self.montototal)) 
       return sumatotal
    def menu (self):
       self.pimpuesto = float(input("Indique impuesto porcentual: "))
    def __str__(self):
       return "Porcentaje de impuesto asignado: %sumatotal\nmonto total: %i\ntotal por pagar: %i" % (self.pimpuesto, self.montototal, self.total_pagar)




#Ejercicio 2
##Sistema de control para linea aerea

##Vuelo
class Base2(metaclass = ABCMeta):
    @abstractmethod
    def __str__(self):
        pass    
    @abstractmethod
    def Captura2(self):
        pass

class App:
    def __init__(self):
        self.__lista = list()
    def __menu2(self):
        print(" ==================================================== ")
        print(" [1] Insertar Vuelo")
        print(" [2] Insertar Vuelo comercial")
        print(" [3] Insertar pasajero")
        print(" [4] Insertar vuelo carga")
        print(" [5] Ver la Lista")
        print(" [6] Borrar la Lista")
        print(" [7] Salir")
        print(" ==================================================== ")
        return input("> ")
    def __mostrarLista(self):
        print("\n"*50)
        for i in range(len(self.__lista)):
            print(self.__lista[i])
            print(15 * "*" + "\n")
    def principal(self):
        respuesta = ""
        while respuesta != "7":
            respuesta = self.__menu2()
            if respuesta == "1":
                self.__lista.append(self.__lec.LeeDatosvuelo())
            elif respuesta == "2":
                self.__lista.append(self.__lec.LeeDatosvuelocomercial())
            elif respuesta == "3":
                self.__lista.append(self.__lec.LeeDatospasajero())
            elif respuesta == "4":
                self.__lista.append(self.__lec.LeeDatosvuelocarga())
            elif respuesta == "5":
                self.__mostrarLista()
                input("Digite cualquier tecla para continuar")
            elif respuesta == "6":
                self.__lista.clear()

prueba = App()
prueba.principal()

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



#Ejercicio Optativo
##Sistema de control para supermercado

from abc import  ABCMeta, abstractmethod

class Base3(metaclass = ABCMeta):
    @abstractmethod
    def __str__(self):
        pass    
    @abstractmethod
    def Captura2(self):
        pass

class App:
    def __init__(self):
        self.__lista = list()
    def __menu2(self):
        print(" ==================================================== ")
        print(" [1] Insertar producto perecedero")
        print(" [2] Insertar producto no perecedero")
        print(" [3] Insertar cliente")
        print(" [4] Ver Lista productos")
        print(" [5] Ver la Lista de clientes")
        print(" [6] Borrar la Lista")
        print(" [7] Salir")
        print(" ==================================================== ")
        return input("> ")
    def __mostrarLista(self):
        print("\n"*50)
        for i in range(len(self.__lista)):
            print(self.__lista[i])
            print(15 * "*" + "\n")
    def principal(self):
        respuesta = ""
        while respuesta != "7":
            respuesta = self.__menu2()
            if respuesta == "1":
                self.__lista.append(self.__lec.LeeDatosperecedero())
            elif respuesta == "2":
                self.__lista.append(self.__lec.LeeDatosnoperecedero())
            elif respuesta == "3":
                self.__lista.append(self.__lec.LeeDatoscliente())
            elif respuesta == "4":
                self.__lista.append(self.__lec.LeeDatoslistaproductos())
            elif respuesta == "5":
                self.__mostrarLista()
                input("Digite cualquier tecla para continuar")
            elif respuesta == "6":
                self.__lista.clear()

prueba = App()
prueba.principal()

class producto:   ##define el producto
    def __init__(self, codproducto = 0, nombreprod = 0, precio = 0): ##define atributos del producto
        self.codproducto = codproducto
        self.nombreprod = nombreprod
        self.precio = precio
    def info_producto(self):  ##arroja informacion del producto
        infoproducto = str(self.codproducto) + ' ' + str(self.nombreprod) + ' ' + str(self.precio)
        return infoproducto.title()
    
    
##Pasajero percedero
class percedero(pesoneto = 0, vencimiento = 0, precioventa = 0):
    def __init__(self, codigo, nombre, precio, pesoneto, vencimiento, precioventa):
        super().__init__(codigo, nombre, precio, pesoneto, vencimiento)
        self.__precioventa = precioventa
    @property
    def precioventa(self):
        return str(self.__precioventa = (self.precio * 1.40))
    @precioventa.setter
    def __str__(self):
        return (self.precioventa)

##Pasajero no percedero
class nopercedero (pais, precioventano):
    def __init__(self, codigo, nombre, precio, pais, precioventano):
        super().__init__(codigo, nombre, precio)
        self.__primerproducto = primerproducto
    @property
    def primerproducto(self):
        return str(self.__primerproducto)
    @primerproducto.setter
    def primerproducto(self, nuevo_primerproducto):
        self.__primerproducto = nuevo_primerproducto
    def precioventano(self):
        return str(self.__precioventano = (self.precio * 1.15))
    def __str__(self):
        return (self.primerproducto) 
