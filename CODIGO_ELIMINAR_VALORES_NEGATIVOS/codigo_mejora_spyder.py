# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 13:59:42 2022

@author: Joseph
"""

import numpy as np
import pandas as pd
import datetime
import matplotlib.dates as dates
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

df = pd.DataFrame()
time = np.loadtxt(r'C:\Users\FABRICIO\Desktop\DATOS_ORIGINALES\PRUEBA_MEDIA\ICA-01032019.efm',
                  delimiter=',', unpack=True,skiprows=0, usecols=[0], dtype=bytes).astype(str)

hourday_h = []
for i in range(len(time)):
    hour = datetime.datetime.strptime(time[i], '%H:%M:%S')
    HH = (hour.strftime('%H'))
    MM = (hour.strftime('%M'))
    SS = (hour.strftime('%S'))
    hourday_h.append(float(HH) + float(MM) / 60. + float(SS) / 3600.)

efm, qq = np.loadtxt(rf'C:\Users\FABRICIO\Desktop\DATOS_ORIGINALES\PRUEBA_MEDIA\ICA-01032019.efm', 
                     delimiter=',', unpack=True,skiprows=0, usecols=[1,2])

df['TIME'] = hourday_h
df['EFM'] = ((efm + 0.083670597) / 4.8953412)*1000

plot_data = df[df['EFM']>0]
x = plot_data.iloc[:,0]
y = plot_data.iloc[:,1]

fig, ax = plt.subplots(1, 1, figsize=(6, 4))
ax.plot(x, y,'r')
plt.subplots_adjust(bottom=0.16, right=0.98)
xtick_labels = [i if i in [i for i in range(0,25,6)] else f" " for i in range(0,25)]
ax.set_xticks(range(0,25,1),xtick_labels)
ax.set_xlim([0,24])
plt.ylim([0,max(y)+20])
ax.set_title('03/01/2019',loc="center" ,y=1.12, pad=-20)
plt.xlabel('Hour [UT]')
plt.ylabel('Electric field [V/m]')
plt.grid()
#pones la ruta de la carpeta donde se desea guardar el plot
plt.savefig(r'C:\Users\FABRICIO\Desktop\DATOS_ORIGINALES\CODIGO_ELIMINAR_VALORES_NEGATIVOS\Spyder',dpi=400)
plt.show()






