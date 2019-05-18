#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 09:14:29 2019

@author: carlosaguirre
"""

print("Hola")

nombre = 'Carlos'
edad = 22

print(nombre)

import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]

tupla_numeros = (1,3)

arreglo_numpy = np.array((1,2,3))

numeros_serie_a = pd.Series(lista_numeros)

numero_serie_b = pd.Series(tupla_numeros)

numero_serie_c = pd.Series(arreglo_numpy)

numeros_serie_d = pd.Series([
        True,
        False,
        12,
        12.21,
        "Asad",
        None,
        (),
        [],
        {"nombre" : "Carlos"}
                ])

numeros_serie_a[0]

lista_ciudades = ["Ambato","Cuenca","Loja","Quito"]

serie_ciudades = pd.Series(lista_ciudades,
                           index=["A","C","L","Q"])

serie_ciudades["Q"]

print(type(serie_ciudades))

valores_ciudad = {
        "Ibarra":9500,
        "Guayaquil":10000,
        "Cuenca":7000,
        "Quito":8000,
        "Loja":3000
        }

serie_valor_ciudad = pd.Series(valores_ciudad)

print(serie_valor_ciudad)

serie_valor_ciudad["Ibarra"]

serie_valor_ciudad[0]

ciudades_menores_5000 = serie_valor_ciudad == 8750

serie_menor_5000 = serie_valor_ciudad[ciudades_menores_5000]

serie_valor_ciudad = serie_valor_ciudad*1.1

serie_valor_ciudad["Quito"] = 8750

print("Lima" in serie_valor_ciudad) #False
print("Loja" in serie_valor_ciudad) #True

np.square(serie_valor_ciudad)
np.sin(serie_valor_ciudad)

ciudades_uno = pd.Series({
            "Quito":1500,
            "Loja":4000,
         })

ciudades_dos = pd.Series({
            "Montañita":1500,
            "Guayaquil":4000,
            "Quito":2000
         })

print(ciudades_uno * ciudades_dos)

randomico = np.random.rand(3)

serie_tres_rand = pd.Series(randomico)


ciudades_uno = pd.Series({
            "Loja":4000,
            "Quito":5000,
            "Manta":70000
         })

ciudades_dos = pd.Series({
            "Montañita":1500,
            "Guayaquil":4000,
            "Quito":2000
         })

#Combinar dos series en una

ciudades_concat = pd.concat([ciudades_uno, ciudades_dos])

ciudades_concat_verify = pd.concat([ciudades_uno, ciudades_dos], verify_integrity=True)

ciudades_append = ciudades_uno.append(ciudades_dos)

ciudades_add = ciudades_uno.add(ciudades_dos)

#Agregar nuevo valor (se combina con el punto anterior)


#Obtener valor máximo
ciudades_uno.max()
pd.Series.max(ciudades_uno)
np.max(ciudades_uno)


#Obtener valor mínimo
ciudades_uno.min()
pd.Series.min(ciudades_uno)
np.min(ciudades_uno)

# Estadísticas (Avg Mean ....)
ciudades_uno.mean()
ciudades_uno.median()
np.average(ciudades_uno)

#Obtener los primeros elementos
ciudades_tres.head(2)

#Obtener los primeros elementos
ciudades_tres.tail(2)

#Ordenar arreglo
ciudades_uno.sort_index()
ciudades_uno.sort_values()

#Ordenar descendente
ciudades_uno.sort_values(ascending=False)

#0 >= 1000      5%
#1000 >= 10000 10%
#10000 >       15%

def calculo(valor):
    if(valor <= 1000):
        return valor * 1.05
    if(valor > 1000 and valor <= 10000):
        return valor * 1.10
    if(valor > 10000):
        return valor * 1.15
    
ciudades_uno.map(calculo)

