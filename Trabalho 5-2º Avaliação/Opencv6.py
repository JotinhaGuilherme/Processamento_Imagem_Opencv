# Importação de Biblioteca
import cv2 as cv
import numpy as np

#Importação de imagem
img = cv.imread("cachorro.jpg")
#Inicio da Rotação de imagem
# Obtendo as dimensões da imagem
altura, largura = img.shape[:2]
# Definindo o centro da rotação (no centro da imagem)
centro = (largura // 2, altura // 2)
# Definindo o ângulo de rotação (em graus)
angulo = 45  # Definindo o ângulo de rotação (em graus) nesse caso em 45 graus
escala = 1.0 # Definindo o fator de escala (1.0 significa manter o tamanho original)
matriz_rotacao = cv.getRotationMatrix2D(centro, angulo, escala)# Obtendo a matriz de rotação
imgrotacionada = cv.warpAffine(img, matriz_rotacao, (largura, altura))# Aplicando a rotação à imagem
#Fim da Rotação de imagem

#Inicio da Translação de imagem
altura, largura = img.shape[:2]# Obtendo as dimensões da imagem
# Definindo o deslocamento (dx, dy)
deslocamento_x = 50  # deslocamento para a direita
deslocamento_y = 30  # deslocamento para baixo
matriz_translacao = np.float32([[1, 0, deslocamento_x], [0, 1, deslocamento_y]])# Criando a matriz de translação
imgtransladada = cv.warpAffine(img, matriz_translacao, (largura, altura))# Aplicando a translação à imagem
#Fim da Translação de imagem

#Inicio da tranformação de pespectiva
pontos_originais = np.float32([[50, 50], [300, 50], [50, 300], [300, 300]])# Definindo os pontos de origem (quatro cantos da região a ser transformada)
pontos_destino = np.float32([[10, 100], [280, 30], [30, 400], [290, 300]])# Definindo os pontos de destino (onde você deseja que esses pontos vão)
matriz_perspectiva = cv.getPerspectiveTransform(pontos_originais, pontos_destino)# Calculando a matriz de transformação de perspectiva
imgtransformada = cv.warpPerspective(img, matriz_perspectiva, (img.shape[1], img.shape[0]))# Aplicando a transformação à imagem
#Fim da tranformação de pespectiva

cv.imshow("Imagem Original",img)#mostra imagem original
cv.imshow("Imagem Rotacionada", imgrotacionada)# mostra imageem rotacionada
cv.imshow("Imagem Transladada", imgtransladada)# Exibindo a imagem transladada
cv.imshow("Imagem Tranfomada" , imgtransformada)#mostra imagem Transformada

cv.waitKey(0)#temporizador de app,(0)Quer dizer que qualquer tecla feixa as janelas abertas
cv.destroyAllWindows()#finaliza todas as paginas abertas