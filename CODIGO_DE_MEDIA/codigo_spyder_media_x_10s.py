# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 21:07:54 2022

@author: Joseph
"""

import numpy as np
import pandas as pd
import os
from os.path import isfile, join

ruta = r'C:\Users\FABRICIO\Desktop\DATOS_ORIGINALES\DATOS_PARA_MEDIA_2021'
contenido = os.listdir(ruta)
Archivos = [nombre for nombre in contenido if isfile(join(ruta,nombre))]

lista_time = []
lista_efm = []

print("COMENZANDO EL PROCESO")

for dia in Archivos:

    
    time = np.loadtxt(rf'C:\Users\FABRICIO\Desktop\DATOS_ORIGINALES\DATOS_PARA_MEDIA_2021\{dia}',
                  delimiter=',', unpack=True,skiprows=0, usecols=[0], dtype=bytes).astype(str)

    fecha = f'{dia[8:12]}-{dia[4:6]}-{dia[6:8]}'
    
    
    lista_fecha_hora = [f'{fecha} {time[i]}'  for i in range(len(time))]
    lista_time.extend(lista_fecha_hora) 
   
    
    efm, qq = np.loadtxt(rf'C:\Users\FABRICIO\Desktop\DATOS_ORIGINALES\DATOS_PARA_MEDIA_2021\{dia}', 
                         delimiter=',', unpack=True,skiprows=0, usecols=[1,2])
 
    
    y = [((i + 0.083670597) / 4.8953412) * 1000 for i in efm]
    lista_efm.extend(y)


data = {'TIME':lista_time,
        'EFM':lista_efm}

df = pd.DataFrame(data)
df.rename({'EFM': 'Media x \'10s\''}, axis=1, inplace=True)
df['TIME'] = pd.to_datetime(df['TIME'], errors = 'coerce')
df = df.set_index('TIME')

# '10s' 10 segundos, '1h' 1 hora, '1M' 1 mes , '17min' 17 min, '1Y' 1año
media = df.between_time('00:00:00', '23:59:59').resample('10s').mean().dropna(how='all')

df1 = pd.DataFrame(media[0:1000000])
df2 = pd.DataFrame(media[1000000:2000000])
writer = pd.ExcelWriter(r'C:\Users\FABRICIO\Desktop\DATOS_ORIGINALES\EXCEL_MEDIA_X 10s_JUL_NOV_2022.xlsx')
df1.to_excel(writer, sheet_name='Sheet1')
df2.to_excel(writer, sheet_name='Sheet2')


writer.save()

print("TERMINO EL PROCESO")
    
#para cuando tenga filas de max 1 000 000
#media.to_excel(r'C:\Users\FABRICIO\Desktop\DATOS_ORIGINALES\EXCEL_MEDIA_X 10s_JUL_NOV_2022.xlsx', sheet_name='pag')

