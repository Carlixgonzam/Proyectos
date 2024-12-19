import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread("1.jpg")

# Crear un kernel de nitidez
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

# Aplicar el filtro de nitidez
imagen_nitida = cv2.filter2D(imagen, -1, kernel)

# Guardar la imagen resultante
cv2.imwrite("imagen_mejorada.jpg", imagen_nitida)

# Mostrar la imagen
cv2.imshow("Imagen Mejorada", imagen_nitida)
cv2.waitKey(0)
cv2.destroyAllWindows()
