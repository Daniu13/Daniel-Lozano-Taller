import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sci

"""Daniel Lozano Simanca"""

"""Punto 1"""
aleatoria = np.random.randint(10, size=1200000).reshape((2,8,5,15000))
print(aleatoria.shape)

"""Punto 2 y 3"""
copia = aleatoria[:,:,:,0].copy()
print(f'\n\n{copia}')
print(f'Shape: {copia.shape}')
print(f'Size: {copia.size}')
print(f'Dim: {copia.ndim}')

"""Punto 4"""
copia2d = copia.reshape((4,4,5))[:,:,0].copy()
print(copia2d)
print(copia2d.shape)

"""Punto 5"""
def zu_pandas(array):
   df = pd.DataFrame(array, columns=["c0", "c1", "c2", "c3"])
   return df
df = zu_pandas(copia2d)
print(f'\n\n{df}')

"""Punto 6"""
def cargar(archivo):
    if archivo.endswith(".mat"):
        datos = sci.loadmat(archivo)
    elif archivo.endswith(".csv"):
        datos = pd.read_csv(archivo)
    return datos

"""Punto 7"""
def operaciones(array, tipo):
    if tipo == 1:
        pass
    elif tipo == 2:
        pass
    elif tipo == 3:
        pass
    elif tipo == 4:
        pass
    elif tipo == 5:
        pass
    elif tipo == 6:
        pass
    elif tipo == 7:
        pass