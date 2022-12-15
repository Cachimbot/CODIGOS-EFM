#Joseph
#Plot diario sirve para ver las curvas en horas no pudiendo observar detallamente
# los minutos y segundos.
import numpy as np
import datetime
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#======================================================
# Reading efm time
time = np.loadtxt(r'C:\Users\FABRICIO\Desktop\Python\Datos_C_E_MEJORADO\ENERO\DIA1\ICA-09132022.efm',
                  delimiter=',', unpack=True,skiprows=0, usecols=[0], dtype=bytes).astype(str)

hourday_h = []   # sirve para plotear solo horas, se elije ejecutar el bloque 2
for i in range(len(time)):
    hour = datetime.datetime.strptime(time[i], '%H:%M:%S')
    HH = (hour.strftime('%H'))
    MM = (hour.strftime('%M'))
    SS = (hour.strftime('%S'))
    hourday_h.append(float(HH) + float(MM) / 60. + float(SS) / 3600.)
#======================================================


#======================================================
# Reading efm data
efm, qq = np.loadtxt(r'C:\Users\FABRICIO\Desktop\Python\Datos_C_E_MEJORADO\ENERO\DIA1\ICA-09132022.efm',
                     delimiter=',', unpack=True,skiprows=0, usecols=[1,2])
#======================================================


#======================================================
# Calibracion del eje y
y = [((i + 0.083670597) / 4.8953412) * 1000 for i in efm]
print(y)
#======================================================


#======================================================
#Plotting and legend
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
ax.plot(hourday_h, y, 'b')
plt.subplots_adjust(bottom=0.16, right=0.98)
#======================================================

#======================================================
# Estableciendo eje x
xtick_labels = [i if i in [i for i in range(0,25,2)] else f" " for i in range(0,25)]
ax.set_xticks(range(0,25,1),xtick_labels)
ax.set_xlim([0,24])
#======================================================

#======================================================
#Definiendo titulo,nombres de ejes, guarda archivo.
ax.set_title('13/09/2022',loc="center" ,y=1.12, pad=-20)
plt.xlabel('Hour [UT]')
plt.ylabel('Electric field [V/m]')
plt.grid()
# pones la ruta de la carpeta donde se desea guardar el plot
plt.savefig(r'C:\Users\FABRICIO\Desktop\DATOS_ORIGINALES\CODIGO_PLOT_DIARIO_hour\Prueba_plot_diario.png',dpi=400)
plt.show()
#======================================================

#======================================================
#Saving file
plt.savefig('plot_efm.eps')
#======================================================
