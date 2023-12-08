import numpy as np
import cv2
from matplotlib import pyplot as plt

def imagenes(img):
    rows, cols = img.shape
    crow, ccol = int(rows/2), int(cols/2)
    mask = np.zeros((rows, cols, 2), np.uint8)  # Asegúrate de tener 2 canales en la máscara
    mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 1
    return mask

def dft_inversa_sin_mascara(img, mask):
    # Calcular la transformada de Fourier y el desplazamiento
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    # Realizar la DFT inversa sin aplicar la máscara
    fshift = dft_shift * mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
    magnitude_spectrum = 20 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

    return img_back, magnitude_spectrum

# Leer las imágenes
img1 = cv2.imread('alaska.jpg', 0)
img2 = cv2.imread('perros2.jpg', 0)
img3 = cv2.imread('perroBN.jpg', 0)

mask1 = imagenes(img1)
mask2 = imagenes(img2)
mask3 = imagenes(img3)

# Realizar la DFT inversa sin aplicar la máscara para cada imagen
img_resultante_sin_mascara1, magnitude_spectrum1 = dft_inversa_sin_mascara(img1, mask1)
img_resultante_sin_mascara2, magnitude_spectrum2 = dft_inversa_sin_mascara(img2, mask2)
img_resultante_sin_mascara3, magnitude_spectrum3 = dft_inversa_sin_mascara(img3, mask3)

# Configurar la ventana de subgráficos
fig, axes = plt.subplots(3, 3, figsize=(10, 8))

# Mostrar las imágenes
axes[0, 0].imshow(img1, cmap='gray')
axes[0, 0].set_title('Imagen de entrada 1'), axes[0, 0].axis('off')

axes[0, 1].imshow(magnitude_spectrum1, cmap='gray')
axes[0, 1].set_title('Espectro de magnitud 1'), axes[0, 1].axis('off')

axes[0, 2].imshow(img_resultante_sin_mascara1, cmap='gray')
axes[0, 2].set_title('DFT Inversa sin Máscara 1'), axes[0, 2].axis('off')

axes[1, 0].imshow(img2, cmap='gray')
axes[1, 0].set_title('Imagen de entrada 2'), axes[1, 0].axis('off')

axes[1, 1].imshow(magnitude_spectrum2, cmap='gray')
axes[1, 1].set_title('Espectro de magnitud 2'), axes[1, 1].axis('off')

axes[1, 2].imshow(img_resultante_sin_mascara2, cmap='gray')
axes[1, 2].set_title('DFT Inversa sin Máscara 2'), axes[1, 2].axis('off')

axes[2, 0].imshow(img3, cmap='gray')
axes[2, 0].set_title('Imagen de entrada 3'), axes[2, 0].axis('off')

axes[2, 1].imshow(magnitude_spectrum3, cmap='gray')
axes[2, 1].set_title('Espectro de magnitud 3'), axes[2, 1].axis('off')

axes[2, 2].imshow(img_resultante_sin_mascara3, cmap='gray')
axes[2, 2].set_title('DFT Inversa sin Máscara 3'), axes[2, 2].axis('off')

plt.show()
