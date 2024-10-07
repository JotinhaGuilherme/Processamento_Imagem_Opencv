# Processamento_Imagem_Opencv
# Image Processing with OpenCV

Este repositório contém exemplos de códigos para diversas operações de processamento de imagens usando a biblioteca OpenCV. Abaixo estão as funcionalidades implementadas, com instruções e exemplos para cada uma.

## Funcionalidades

1. **Leitura e Exibição de Imagens**
   - Carregue imagens de diferentes formatos (JPEG, PNG, BMP) utilizando `cv2.imread()`.
   - Exiba imagens carregadas utilizando `cv2.imshow()`.

2. **Pré-processamento de Imagens**
   - Conversão de Cores (RGB para Grayscale, HSV, etc.).
   - Redimensionamento de imagens.
   - Equalização de Histograma para melhorar contraste.

3. **Aplicação de Filtros**
   - Desfoque (Blur).
   - Detecção de Bordas (Canny, Sobel).
   - Filtro Laplaciano.

4. **Detecção de Características**
   - Detecção de Cantos (Harris, Shi-Tomasi).
   - Detecção de Contornos.
   - Pontos de Interesse (SIFT/SURF).

5. **Transformações Geométricas**
   - Rotação e Translação.
   - Transformação de Perspectiva (Homografia).
   - Correção de Distorção.

6. **Operações Morfológicas**
   - Erosão e Dilatação.
   - Segmentação de Objetos.

7. **Segmentação de Imagens**
   - Limiarização (Thresholding).
   - Algoritmo Watershed para segmentação avançada.

## Requisitos

- Python 3.x
- OpenCV

Instale as dependências necessárias executando:

```bash
pip install opencv-python
