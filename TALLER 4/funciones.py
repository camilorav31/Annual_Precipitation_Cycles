import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

#@title BOXPLOT ENCOORDENADAS POLARES

def graficar_boxplot_polar(datos, nombre_columna, variable, unidades):
    meses = {12: 'Ene', 11: 'Feb', 10: 'Mar', 9: 'Abr', 8: 'May', 7: 'Jun',
             6: 'Jul', 5: 'Ago', 4: 'Sep', 3: 'Oct', 2: 'Nov', 1: 'Dic'}

    media_mensual = datos.groupby('Month')[[nombre_columna]].mean()
    datos_por_mes = [datos[datos['Month'] == mes][nombre_columna].values for mes in media_mensual.index]

    angulo_inicio = np.pi / 6
    angulo_final = 2 * np.pi

    angulos = np.linspace(angulo_inicio, angulo_final, len(media_mensual.index), endpoint=True)
    radios = media_mensual[nombre_columna].tolist()

    plt.figure(figsize=(10, 10))
    ax = plt.subplot(111, polar=True)

    # Añadir barras que representan la media
    bars = ax.bar(angulos, radios, width=0.4, color='skyblue', edgecolor='black', alpha=0.7)


    # Configuración del boxplot
    boxprops = dict(linewidth=2, color='black')
    whiskerprops = dict(linestyle='-', linewidth=1.5, color='black')
    medianprops = dict(linestyle='-', linewidth=2.5, color='red')

    ax.boxplot(datos_por_mes, positions=angulos, widths=0.25, patch_artist=True,
               boxprops=dict(facecolor='blue'), whiskerprops=whiskerprops, medianprops=medianprops,whis=[0,100])

    min_value = min([item for sublist in datos_por_mes for item in sublist])
    lower_limit = np.floor(min_value)  # Redondeado al número entero inferior más cercano

    ax.set_ylim(lower_limit, max(radios) * 2.2)

    ax.set_xticks(angulos)
    ax.set_xticklabels([meses[mes] for mes in reversed(media_mensual.index)])

    ax.set_theta_offset(np.pi / 2 - np.pi / 6)
    ax.set_rlabel_position(30)

    plt.title(f'Ciclo anual de {variable} en [{unidades}]')

    media_handle = Patch(color='skyblue', label='Media')
    variabilidad_handle = Patch(color='blue', label='IQR')
    mediana_handle = Line2D([0], [0], color='red', linewidth=2.5, linestyle='-', label='Mediana')

    plt.legend(handles=[media_handle, variabilidad_handle, mediana_handle], loc='upper right')
    plt.show()

# ENSO 

def ensofuc(datos, nombre_columna, variable, unidades, enso):
    meses = {12: 'Ene', 11: 'Feb', 10: 'Mar', 9: 'Abr', 8: 'May', 7: 'Jun',
             6: 'Jul', 5: 'Ago', 4: 'Sep', 3: 'Oct', 2: 'Nov', 1: 'Dic'}

    media_mensual = datos.groupby('Month')[[nombre_columna]].mean()
    datos_por_mes = [datos[datos['Month'] == mes][nombre_columna].values for mes in media_mensual.index]

    angulo_inicio = np.pi / 6
    angulo_final = 2 * np.pi

    angulos = np.linspace(angulo_inicio, angulo_final, 12, endpoint=True)
    radios = media_mensual[nombre_columna].tolist()

    plt.figure(figsize=(10, 10))
    ax = plt.subplot(111, polar=True)

    # Añadir barras que representan la media
    bars = ax.bar(angulos, radios, width=0.4, color='skyblue', edgecolor='black', alpha=0.7)
    media_handle = Patch(color='skyblue', label='Media')
    min_value = min([item for sublist in datos_por_mes for item in sublist])
    lower_limit = np.floor(min_value)  # Redondeado al número entero inferior más cercano

    ax.set_ylim(lower_limit, max(radios) * 2.2)

    ax.set_xticks(angulos)
    ax.set_xticklabels([meses[mes] for mes in reversed(media_mensual.index)])

    ax.set_theta_offset(np.pi / 2 - np.pi / 6)
    ax.set_rlabel_position(30)

    plt.title(f'Efecto del ENSO sobre el Ciclo anual de {variable} en [{unidades}]')

    # Graficar las líneas de las variables nino, nina, neut
    angulos_enso = np.linspace(angulo_inicio, angulo_final, 12, endpoint=True)

    ax.plot(angulos_enso, enso['nino'], color='red', label='Niño')
    ax.plot(angulos_enso, enso['nina'], color='blue', label='Niña')
    ax.plot(angulos_enso, enso['neut'], color='black', label='Neutral')

    nino_handle = Line2D([0], [0], color='red', linewidth=2.5, linestyle='-', label='El Niño')
    nina_handle = Line2D([0], [0], color='blue', linewidth=2.5, linestyle='-', label='La Niña')
    neutro_handle = Line2D([0], [0], color='black', linewidth=2.5, linestyle='-', label='Neutro')
    
    plt.legend(handles=[media_handle,nino_handle,nina_handle,neutro_handle], loc='upper right')
    plt.show()