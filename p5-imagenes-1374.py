import cv2
# leer la imagen con cv2 = computer vision 
img = cv2.imread('pacheco.webp')
# determiner el tipo de imagen  
print(type(img))
# mostrar pixeles (657, 570, 3)
print(img.shape)
# mostrar imagen en ventana barra de titulo pacheco 1374
cv2.imshow('pacheco 1374', img)
## tiempo de espera 
cv2.waitKey(0)
# destruir todas las ventanas 
cv2.destroyAllWindows()
