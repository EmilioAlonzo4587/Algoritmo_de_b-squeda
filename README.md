Este código en Python demuestra la diferencia en eficiencia entre dos algoritmos de búsqueda: búsqueda lineal y búsqueda binaria.  Crea una lista de 100,000 usuarios, cada uno con un ID, nombre y edad.  Luego, permite al usuario ingresar un ID para buscar.

El código implementa dos funciones de búsqueda:

lineal_search: Revisa cada usuario en la lista uno por uno hasta encontrar el ID buscado. Es simple pero lento para listas grandes.
binary_search: Funciona solo en listas ordenadas. Divide repetidamente la lista por la mitad, descartando la mitad donde no puede estar el ID buscado. Es mucho más rápido que la búsqueda lineal para listas grandes.
El código mide el tiempo que tarda cada función en encontrar el ID ingresado por el usuario y muestra los resultados.  También imprime la información del usuario encontrado (si lo encuentra).  La principal ventaja de la búsqueda binaria se evidencia en la comparación de tiempos, especialmente notable al trabajar con grandes cantidades de datos.  El código ordena la lista de usuarios por ID antes de realizar la búsqueda binaria, ya que este algoritmo requiere que la lista esté ordenada.

Link de video: https://drive.google.com/drive/folders/1wA6jWbaKAtUO8nf9pW9H6iVWQ9Q4m0_5?usp=sharing