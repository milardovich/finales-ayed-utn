## Final Boleto Bus - 02/05/2013

La dificultad de este final estaba en tener que cargar en un arreglo la información guardada previamente en el archivo. En mi caso, lo pensé como 2 arreglos auxiliares distintos (dataAux y metricasAux). En el arreglo dataAux, lo que guardo es la información para cada día del mes elegido, tal como viene en el archivo. En el arreglo metricasAux se guardan las cantidades de boletos y el monto vendidos por cada empresa.

Decidí simplificar el enunciado, y que sólo existan 3 números de colectivos, ya que sino no había forma de asociar todos los números de colectivos con cada empresa sin tener información duplicada. En caso de querer seguir con el enunciado original, vamos a tener que buscar de manera exhaustiva qué colectivos pertenecen a cada empresa.