#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:36:48 2019

@author: carlosaguirre
"""

import numpy as np
import pandas as pd

arr_rand = np.random.randint(0,10,6).reshape(2,3)

df = pd.DataFrame(arr_rand,
                  columns=['Estatura (cm)', 'Peso (gr)', 'Edad (anios)'],
                  index=['Adrian','Vicente']
                  )

df2 = pd.DataFrame(arr_rand)

df2.columns = ['Estatura (cm)', 'Peso (gr)', 'Edad (anios)']

df3 = pd.DataFrame(arr_rand)


df3[0] # NO ES EL ÍNDICE

df2['Estatura (cm)'] #ES EL NOMBRE DE LA COLUMNA

type(df2['Estatura (cm)'])

df2['Estatura (cm)'][0]

df['Edad (anios)']['Adrian']