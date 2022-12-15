#Sirve para plotear por carpeta, y calcula:
#Valor a las 0ut, Valor minimo, valor maximo, Media diaria; de cada dia y los exporta en excel.
#Asi existan dias con datos vacios.
import numpy as np
import pandas as pd
import os
from os.path import isfile, join
from pathlib import Path

df = pd.DataFrame()
ruta = r'C:\Users\FABRICIO\Desktop\DATOS_ORIGINALES\2021'
contenido = os.listdir(ruta)
Archivos = [nombre for nombre in contenido if isfile(join(ruta,nombre))]

Valor_0ut = []
Valor_minimo = []
Valor_Maximo = []
Media_diaria = []
for dia in Archivos:
    my_file = Path(rf'C:\Users\FABRICIO\Desktop\DATOS_ORIGINALES\2021\{dia}')
    if os.path.getsize(my_file) > 0:
        efm, qq = np.loadtxt(rf'C:\Users\FABRICIO\Desktop\DATOS_ORIGINALES\2021\{dia}', delimiter=',', unpack=True,skiprows=0, usecols=[1,2])
        y1 = []
        for i in efm:
            calibrado = ((i + 0.083670597) / 4.8953412)*1000
            y1.append(calibrado)
        average = np.mean(y1)  # y1 = calibrated
        Valor_0ut.append(round(y1[0]))
        Valor_minimo.append(round(min(y1)))
        Valor_Maximo.append(round(max(y1)))
        Media_diaria.append(round(average))

    else:
        Valor_0ut.append(" ")
        Valor_minimo.append(" ")
        Valor_Maximo.append(" ")
        Media_diaria.append(" ")

df['Fecha'] = Archivos
df['Valor a las 0 UT'] = Valor_0ut
df['Valor minimo'] = Valor_minimo
df['Valor Maximo'] = Valor_Maximo
df['Media Diaria'] = Media_diaria

df.to_excel(r'C:\Users\FABRICIO\Desktop\DATOS_ORIGINALES\EXCEL_2021_1.xlsx', sheet_name='pag')
