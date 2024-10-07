# Impprtação da Biblioteca Opencv
import cv2 as cv

#Importação de imagem
img = cv.imread("cachorro.jpg")
#Conversão de Cores
imgcores = cv.cvtColor(img, cv.COLOR_BGR2GRAY )
ret, thresh = cv.threshold(imgcores, 127, 255, cv.THRESH_BINARY)
# Identificação dos contornos usando a função findContours
contornos, hierarquia = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# Desenho dos contornos na imagem original
img_contornos = img.copy()
cv.drawContours(img_contornos, contornos, -1, (0, 255, 0), 2)  # Desenha os contornos em verde
# Inicializa o detector SIFT
sift = cv.SIFT_create()
# Detecta os keypoints (pontos de interesse) e calcula os descritores
keypoints, descriptors = sift.detectAndCompute(imgcores, None)
imgsift = cv.drawKeypoints(img.copy(), keypoints, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv.imshow('Imagem com SIFT', imgsift)#mostra imagem em SIFT
cv.imshow("Imagem com Contornos", img_contornos)#mostra imagem com contornos
cv.imshow("Imagem Binarizada",imgcores)#mostra imagem em preto e branco

cv.imshow("Imagem Original",img)#mostra imagem original
cv.waitKey(0)#temporizador de app,(0)Quer dizer que qualquer tecla feixa as janelas abertas
cv.destroyAllWindows()#finaliza todas as paginas abertas