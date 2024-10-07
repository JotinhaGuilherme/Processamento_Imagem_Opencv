#Biblioteca
import cv2 as cv

#Importação de imagem
img = cv.imread("cachorro.jpg")
#chamando a imagem aplicando o filtro blur,(15,15)Indica o nivel do desfoque
img_blur = cv.blur(img, (15, 15))
#mostra imagem com desfoque
cv.imshow("Imagem com Blur", img_blur)
#Conversão de Cores(parametro necessario para a detecção de bordas)
imgbordas = cv.cvtColor(img, cv.COLOR_BGR2GRAY )
img_bordas = cv.Canny(imgbordas, 100, 200)#chamando a imagem aplicando o filtro de detecção de bordas

cv.imshow("Deteccao de Bordas", img_bordas)#mostra imagem com detecção de bordas
cv.imshow("Imagem Original",img)#mostra imagem original

cv.waitKey(0)#temporizador de app,(0)Quer dizer que qualquer tecla feixa as janelas abertas
cv.destroyAllWindows()#finaliza todas as paginas abertas