import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""Daniel Lozano Simanca"""

"""Punto 1"""
aleatoria = np.random.randint(10, size=1200000).reshape((4,4,5,15000))
print(aleatoria.shape)

"""Punto 2 y 3"""
copia = aleatoria[:,:,:,0].copy()
print(f'\n\n{copia}')
print(f'Shape: {copia.shape}')
print(f'Size: {copia.size}')
