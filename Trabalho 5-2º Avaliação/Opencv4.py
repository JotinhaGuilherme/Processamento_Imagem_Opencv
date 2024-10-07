# Importação da Biblioteca
import cv2 as cv
import numpy as np

# Importação de imagem
img = cv.imread("cachorro.jpg")

# Conversão para escala de cinza
img_cores = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detecção de cantos usando o método Shi-Tomasi
cantos = cv.goodFeaturesToTrack(img_cores, maxCorners=100, qualityLevel=0.01, minDistance=10)

# Converte as coordenadas dos cantos para inteiros
cantos = np.int64(cantos)

# Faz uma cópia da imagem original para desenhar os cantos
img_com_cantos = img.copy()

# Desenha círculos nos cantos detectados na cópia da imagem
for corner in cantos:
    x, y = corner.ravel()
    cv.circle(img_com_cantos, (x, y), 5, (0, 255, 0), -1)  # Desenha círculos verdes nos cantos detectados

cv.imshow("Imagem Original", img)# Exibição da imagem original
cv.imshow("Imagem com Cantos Detectados", img_com_cantos)# Exibição da imagem com cantos detectados

cv.waitKey(0)# Temporizador de app (0 significa que qualquer tecla fecha as janelas abertas)
cv.destroyAllWindows()# Finaliza todas as janelas abertas
