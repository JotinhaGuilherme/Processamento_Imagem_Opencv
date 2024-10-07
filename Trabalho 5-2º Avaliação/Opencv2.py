#Biblioteca
import cv2 as cv

#Importação de imagem
img = cv.imread("cachorro.jpg")
#Conversão de Cores
imgcores = cv.cvtColor(img, cv.COLOR_BGR2GRAY )
#redimencionamento de imagem
imgRedimencionada = cv.resize(imgcores, (600, 600))
# Equalização de Histograma
img_equalizada = cv.equalizeHist(imgRedimencionada)

# #Saída da Conversão de cores
cv.imshow("Imagem Original",imgcores)#mostra imagem
# #Saída da redimencionamento
cv.imshow("Imagem Redimencionada",imgRedimencionada)#mostra imagem
# Saída da imagem equalizada
cv.imshow("Imagem Equalizada", img_equalizada)
cv.waitKey(0)#temporizador de app,(0)Quer dizer que qualquer tecla feixa as janelas abertas
cv.destroyAllWindows()#finaliza todas as paginas abertas

