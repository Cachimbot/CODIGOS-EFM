#sirve para plotear por año, asi exista archivos .efm vacios en la carpeta
import pandas as pd
import os
from os.path import isfile, join
from pathlib import Path
import numpy as np
import datetime
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

df = pd.DataFrame()
ruta = r'C:\Users\FABRICIO\Desktop\DATOS_ORIGINALES\2021'
contenido = os.listdir(ruta)
Archivos = [nombre for nombre in contenido if isfile(join(ruta,nombre))]

for dia in Archivos:
    my_file = Path(rf'C:\Users\FABRICIO\Desktop\DATOS_ORIGINALES\2021\{dia}')
    if os.path.getsize(my_file) > 0:
        time = np.loadtxt(fr'C:\Users\FABRICIO\Desktop\DATOS_ORIGINALES\2021\{dia}', delimiter=',', unpack=True,skiprows=0, usecols=[0], dtype=bytes).astype(str)
        hourday_h = []
        for i in range(len(time)):
            hour = datetime.datetime.strptime(time[i], '%H:%M:%S')
            HH = (hour.strftime('%H'))
            MM = (hour.strftime('%M'))
            SS = (hour.strftime('%S'))
            hourday_h.append(float(HH) + float(MM) / 60. + float(SS) / 3600.)

        efm, qq = np.loadtxt(fr'C:\Users\FABRICIO\Desktop\DATOS_ORIGINALES\2021\{dia}', delimiter=',', unpack=True,skiprows=0, usecols=[1, 2])
        y = [((i + 0.083670597) / 4.8953412) * 1000 for i in efm]
        fig, ax = plt.subplots(1, 1, figsize=(6, 4))
        ax.plot(hourday_h, y, 'g')
        plt.subplots_adjust(left=0.095, bottom=0.16, right=0.98)
        #plt.legend(loc="upper left")
        plt.xticks(range(0, 25), [f'{i:02}' for i in range(25)], rotation=0)
        ax.set_xlim([0, 24])
        ax.set_title(f'{dia}',loc="center" ,y=1.12, pad=-20)
        plt.xlabel('Hour [UT]')
        plt.ylabel('Electric field [V/m]')
        plt.grid()
        plt.savefig(rf'C:\Users\FABRICIO\Desktop\DATOS_ORIGINALES\Imagenes_2022\{dia[0:12]}.jpg', dpi=400)
        plt.close(fig)
        #plt.show()

    else:
        continue

