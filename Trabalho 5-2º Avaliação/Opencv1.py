# Importação de Biblioteca
import cv2 as cv

#Importação de imagem
img = cv.imread("cachorro.jpg")

cv.imshow("Imagem Original",img)#mostra imagem original
cv.waitKey(0)#temporizador de app,(0)Quer dizer que qualquer tecla feixa as janelas abertas
cv.destroyAllWindows()#finaliza todas as paginas abertas