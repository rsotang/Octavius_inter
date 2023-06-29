import numpy as np 
import matplotlib.pyplot as plt
from scipy import ndimage 


# Configurar las opciones de impresión.
# 'threshold' es el número total de elementos de la matriz a partir del cual NumPy empezará a truncar la salida.
np.set_printoptions(threshold=np.inf)


matriz = np.loadtxt('myData.txt', delimiter='\t')
og_matriz= matriz

#Primero interpolamos en el eje de las filas
for i in range(matriz.shape[0]):
    # Obtener los índices de los valores no cero y los cero.
    indices_no_cero = np.nonzero(matriz[i])[0]
    indices_cero = np.where(matriz[i] == 0)[0]
    
    # Solo interpolar si la fila tiene al menos un valor no cero y un cero.
    if indices_no_cero.size > 0 and indices_cero.size > 0:
        # Interpolar los valores cero.
        valores_interpolados = np.interp(indices_cero, indices_no_cero, matriz[i][indices_no_cero])
        
        # Reemplazar los ceros en la matriz con los valores interpolados.
        matriz[i][indices_cero] = valores_interpolados


plt.figure(figsize=(10, 10))  # Crear una figura de 10x10 pulgadas.
plt.imshow(matriz, cmap='gray')  # Mostrar la matriz como una imagen en escala de grises.
plt.colorbar()  # Mostrar una barra de colores que mapea los colores a los valores de la matriz.
plt.savefig('interp_x.png', dpi=300)
#plt.show()  # Mostrar la figura.

################################################################
#Interpolamos en el eje y
################################################################

matriz = og_matriz.T

#Primero interpolamos en el eje de las filas
for i in range(matriz.shape[0]):
    # Obtener los índices de los valores no cero y los cero.
    indices_no_cero = np.nonzero(matriz[i])[0]
    indices_cero = np.where(matriz[i] == 0)[0]
    
    # Solo interpolar si la fila tiene al menos un valor no cero y un cero.
    if indices_no_cero.size > 0 and indices_cero.size > 0:
        # Interpolar los valores cero.
        valores_interpolados = np.interp(indices_cero, indices_no_cero, matriz[i][indices_no_cero])
        
        # Reemplazar los ceros en la matriz con los valores interpolados.
        matriz[i][indices_cero] = valores_interpolados


plt.figure(figsize=(10, 10))  
plt.imshow(matriz, cmap='gray')  
plt.colorbar()  
plt.savefig('interp_y.png', dpi=300)

##############################################################
#Convolucionamos
##############################################################

matriz = og_matriz
# Crear un kernel de 3x3 para promediar los píxeles circundantes.
kernel = np.full((3, 3), 1/9)

# Aplicar la convolución.
matriz = ndimage.convolve(matriz, kernel, mode='constant', cval=np.nan)

# Reemplazar los valores NaN originales.
matriz[np.isnan(matriz)] = matriz[np.isnan(matriz)]

plt.figure(figsize=(10, 10))  
plt.imshow(matriz, cmap='gray')  
plt.colorbar()  
plt.savefig('interp_conv.png', dpi=300)

####################################
#Ahora hay que convertir las matrices en txt
#y adaptar el profiler to mephysto para convertir las matrices en archivos que se pueda comer el mephysto o 
#el veriqaaaaaaaa