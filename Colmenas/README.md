## Final de Colmenas - 19/05/2021

En este final, la mayor dificultad era tal vez la búsqueda dicotómica con archivos. Lo importante era poder modularizarla en una función como la de la resolución de este repositorio (colmenaExiste), para no tener que hacerla dos veces en los puntos 1 y 2.

Es el típico final que tiene 3 items, donde se incluye una búsqueda y un ordenamiento. No es de los más difíciles, ya que el procedimiento para resolverlo es bastante estándar.

En el punto 3, al no saber la cantidad de colmenas que tenemos por zona, no nos queda otra que hacer algo exhaustivo por cada zona.

Tener en cuenta que, siempre que estemos modificando valores en los registros guardados en archivos, nos conviene tener algún tipo de función "auxiliar" o "helper", para poder posicionarnos en la fila correspondiente, en este caso, el procedure correspondiente se llama posicionarseEnColmena. Estudiar bien cómo funciona esto, ya que es muy probable que entre en la mayoría de los parciales o finales. Nótese que definimos la variable pos que contiene el tell() siempre ANTES del load, no después.