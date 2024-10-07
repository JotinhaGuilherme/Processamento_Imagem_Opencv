# Importação de Biblioteca
import cv2 as cv

#Importação de imagem
img = cv.imread("cachorro.jpg")
imgcores = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# Inicio da aplicação da Erosão
elemento_estruturante = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))# Elemento retangular de 5x5 pixels
imgerodida = cv.erode(imgcores, elemento_estruturante, iterations=1)# Aplicando a erosão
# Fim da aplicação da Erosão

# Inicio da Dilatação
elemento_estruturante = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))  # Elemento retangular de 5x5 pixels
imgdilatada = cv.dilate(imgcores, elemento_estruturante, iterations=1)# Aplicando a dilatação
# Fim da Dilatação


# Encontrar contornos
contornos, _ = cv.findContours(imgcores, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
imgcontornos = img# Desenhar contornos na imagem original
cv.drawContours(imgcontornos, contornos, -1, (0, 255, 0), 3)  # Contornos em verde

cv.imshow("Imagem Original",img)#mostra imagem original
cv.imshow("Imagem Binária Original", imgcores)#mostra imagem em preto e branco
cv.imshow("Imagem Erodida", imgerodida)#mostra imagem Erodida
cv.imshow("Imagem Dilatada", imgdilatada)#mostra imagem Dilatada
cv.imshow("Segmentação de objetos", imgcontornos)#mostra imagem com segmentacao de contornos

cv.waitKey(0)#temporizador de app,(0)Quer dizer que qualquer tecla feixa as janelas abertas
cv.destroyAllWindows()#finaliza todas as paginas abertas