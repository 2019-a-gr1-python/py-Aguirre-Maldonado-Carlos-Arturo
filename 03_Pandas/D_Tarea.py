# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 20:53:30 2019

@author: CarlosHP
"""

import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado = '/Users/carlosaguirre/Documents/GitHub/py-Aguirre-Maldonado-Carlos-Arturo/03_Pandas/data/csv/artwork_data.pickle'

df_completo_pickle = pd.read_pickle(path_guardado)

df = df_completo_pickle.iloc[49980:50019,:].copy()

df.to_excel('ejemplo_basico.xlsx')

writer = pd.ExcelWriter('formatoDeber.xlsx', engine = 'xlsxwriter')

############################################################################

artistas_contados = df_completo_pickle['artist'].value_counts()

artistas_contados.to_excel(writer, sheet_name = 'Artistas contados')

hoja_artistas = writer.sheets['Artistas contados']

rango_celdas_artistas = 'B2:B{}'.format(len(artistas_contados.index)+1)

formato = {
        'type':'2_color_scale',
        'min_color':'#35D72F',
        'max_color':'#BB2828'
        }

hoja_artistas.conditional_format(rango_celdas_artistas, formato)

#############################################################################

años_contados = df_completo_pickle['year'].value_counts()

años_contados.to_excel(writer, sheet_name = 'Años Publicacion')

hojas_años_publicacion = writer.sheets['Años Publicacion']

rango_celdas_publicacion = 'B2:B{}'.format(len(años_contados.index)+1)

formato2 = {
        'type':'data_bar',
        'bar_color':'#009DFF'
        }

hojas_años_publicacion.conditional_format(rango_celdas_publicacion, formato2)

#############################################################################

años_adquisicion = df_completo_pickle['acquisitionYear'].value_counts()

años_adquisicion.to_excel(writer, sheet_name = 'Años Adquisicion')

hojas_años_adquisicion = writer.sheets['Años Adquisicion']

rango_celdas_adquirir = 'B2:B{}'.format(len(años_adquisicion.index)+1)

formato3 = {
        'type':'3_color_scale',
        'min_color':'#F9FF00',
        'mid_color':'#00FF43',
        'max_color':'#FF00E2'      
        }

hojas_años_adquisicion.conditional_format(rango_celdas_adquirir, formato3)

#############################################################################

anchura = df_completo_pickle['width'].value_counts()

anchura.to_excel(writer, sheet_name = 'Anchura')

hojas_anchura = writer.sheets['Anchura']

rango_celdas_anchura = 'B2:B{}'.format(len(anchura.index)+1)

formato4 = {
        'type':'icon_set',
        'icon_style': '3_arrows_gray',
        'icons': [{'criteria': '>=', 'type': 'number',     'value': 600.00}]
        }

hojas_anchura.conditional_format(rango_celdas_anchura, formato4)

writer.save()