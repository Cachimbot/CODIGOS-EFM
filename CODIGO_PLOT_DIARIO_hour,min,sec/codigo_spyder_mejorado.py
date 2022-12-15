# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:14:53 2022

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

hourday_h_m_s = []
for i in range(len(time)):
    hour = datetime.datetime.strptime(time[i],'%H:%M:%S')
    hourday_h_m_s.append(hour)

efm, qq = np.loadtxt(rf'C:\Users\FABRICIO\Desktop\DATOS_ORIGINALES\PRUEBA_MEDIA\ICA-01032019.efm', 
                     delimiter=',', unpack=True,skiprows=0, usecols=[1,2])

df['TIME'] = hourday_h_m_s
df['EFM'] = ((efm + 0.083670597) / 4.8953412)*1000

fig,ax = plt.subplots(1,1, figsize=(8,6))
ax.plot(df['TIME'], df['EFM'],'r')
plt.subplots_adjust(bottom=0.16, right=0.98)
plt.xticks(plt.gca().xaxis.set_major_formatter(dates.DateFormatter("%H:%M:%S")),rotation=90)
ax.set_xlim(min(hourday_h_m_s), max(hourday_h_m_s))
ax.set_title('03/01/2019',loc="center" ,y=1.1, pad=-22,fontsize=16)
plt.xlabel('Hour [UT]')
plt.ylabel('Electric field [V/m]')
plt.grid()
plt.savefig(r'C:\Users\FABRICIO\Desktop\DATOS_ORIGINALES\CODIGO_PLOT_DIARIO_hour,min,sec\Spyder.png',dpi=400)
plt.show()





