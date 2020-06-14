# SimulacionBarajasEstocasticas
Hola!

En este tutorial te comparto como resolví el reto de nuestro profesor David Aroesti de Platzi en su [Clase simulación Barajas](https://platzi.com/clases/1835-programacion-estocastica/26443-simulacion-de-barajas/) en el modulo de simulaciones de Montecarlo, del curso Programación Dinámica y Estocástica con Python

**Recuerda que el reto es:**
- Encontrar la probabilidad de encontrar una corrida (o escalera) de 5 barajas (cartas).

En el link de la clase puedes encontrar el código completo, en este tutorial explicare las modificaciones.

En este caso incluí escaleras en los limites del mazo Ejemplo: jota, reina, rey, As y 1.

Antes de iniciar te recuerdo:

- Se realiza la creación de la baraja
- Se obtienen **n=intentos** numero de manos

En nuestro caso cada mano es de 5 cartas.

Por tanto el problema es revisar **n=intentos** manos en busca de escaleras, cada mano puede tener diferentes cartas del vector definido **VALORES**

```
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']
```

**Nota las mayúsculas, pues este vector es importante a lo largo del tutorial**

El código escrito reutiliza el **ciclo for** que recorre el numero de manos, donde en se define **valores** (minúscula), el cual almacenará solo los valores de las cartas en la mano (en este caso 5 cartas). Te dejo esa parte inicial del código a continuación para que recuerdes:

```
    escalera = 0 #contará el numero de escaleras
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])
```
Ahora sí, lo primero que haremos es buscar el indice (la posición en la lista) en **VALORES** que corresponde con la primer carta de nuestra mano **valores[0]**:

```
primer_index= VALORES.index(valores[0])
```

**Ej:** Si nuestra mano es 3, 6, 4, 2 y 5 (Notar que es una escalera en desorden)
primer_index = 2, que es la posición del 3 en el vector **VALORES**

**Y acá esta el truco de mi propuesta**, una vez identificada la primera carta buscare las cartas en orden ascendente y descendente desde la primera carta e iré contando en dos variables **ascendente** y **descendente**

Haremos el ejercicio con el ejemplo que di anteriormente para que lo veamos mejor:
**Ej:** 3, 6, 4, 2 y 5

El **for** recorre desde la segunda carta hasta el final (en este caso 4 veces, debido al numero de cartas por cada mano), recuerda que nuestra primera carta es 3, cuya posición la tenemos en **primer_index**:

1. Buscaré si esta la carta 2 ó la carta 4.
como están las dos cartas, entonces ascendente=1, descendente =1

2. Buscaré si esta la carta As ó la carta 5
como esta solo el 5, entonces: ascendente=2, descendente=1

3. Buscaré si esta la carta rey ó la carta 6
como esta solo el 6, entonces: ascendente=3, descendente=1

4. Buscaré si esta la carta reina ó la carta 7
como no está ninguna, entonces: ascendente=3, descendente=1

Finalmente, recuerda que la primera carta por definición esta ordenada (es solo una), entonces validamos la escalera cuando:
`ascendente+descendente+1 == tamano_mano`
Para el ejemplo anterior: **3+1+1==5** es verdadero! entonces tenemos una escalera.

Ahora si miremos el código, luego del código te explicare dos casos que se deben tener en cuenta para poder aplicar el algoritmo previamente explicado:
- El caso que me permita recorrer la lista de forma continua (pasar del rey al As o viceversa).
- El caso de validar si la carta ascendente o descendente esta en la mano

```
for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        primer_index= VALORES.index(valores[0])
        ascentente=0 #Numero de cartas en orden ascendente desde la primera
        descendente=0 #Numero de cartas en orden descendente desde la primera
        for i in range(1,tamano_mano): #Recorro desde la segunda a la última carta
            #Calculo el indice de la siguiente y anterior carta en el mazo
            #Con el if valido que siempre este entre 0 y 12     
            siguiente=(primer_index+i if (primer_index+i)<13 else primer_index+i-12)
            anterior=(primer_index-i if (primer_index-i)>=0 else primer_index-i+12)
            #Si se encuentra la carta anterior o siguiente sumo a las cartas en orden
            if (valores.count(VALORES[siguiente]))==1:
                ascentente += 1
            elif (valores.count(VALORES[anterior]))==1:
                descendente += 1
            else:
                break
        #Valido si el numero de cartas ascendente + el descendente + 1 (la primera carta)
        #es igual al numero de cartas en la mano 
        if (ascentente+descendente+1)==tamano_mano:
            escalera +=1
```

No te alarmes, es más sencillo de lo que parece!

Vamos a explorar los dos casos:

1.  Recorrer la lista de forma continua (pasar del rey al As o viceversa).

Recuerda que tenemos la lista **VALORES** la cual esta ordenada y tenemos el indice de la primera carta en **primer_index**, entonces se puede recorrer el arreglo **VALORES** aumentando y disminuyendo el indice (denominados **siguiente y anterior**) en cada ciclo for que recorre las 4 cartas. Pero:
El problema es que si queremos pasar del rey al As el aumento en algunos casos nos puede generar indices mayores a 12 y menores a 0, para esto coloque un if, sin embargo, por compresión en el código use los [Condicionales ternarios](https://www.pythoncentral.io/one-line-if-statement-in-python-ternary-conditional-operator/), puedes revisar en detalle en el link, estos consisten en un if-else en una sola linea.

```
<expression1> if <condition> else <expression2>
```
En nuestro caso una de las condiciones es:

```
siguiente=(primer_index+i if (primer_index+i)<13 else primer_index+i-12)
```
De esta forma aseguramos que el valor no sea mayor a 12.
Recuerda que **i** es el indice del for, por lo cual **i** tomara valores desde 1 hasta 4.

Te dejo la sentencia del indice anterior para que lo revises, recuerda que siempre puedes apoyarte del **print**

2. Validar si la carta ascendente o descendente **esta** en la mano

Ahora que ya podemos recorrer el arreglo **VALORES** sin que se rompa nuestro programa, vamos a verificar si las cartas anteriores o siguientes están en la mano (las 5 cartas que tenemos), para esto usé la función **count** que tienen las listas, la cual nos devuelve el numero de veces que esta un elemento en una lista. Para esto:
Buscaremos el número de veces que esta la carta siguiente ó anterior **(VALORES[siguiente])** dentro de la lista que tiene nuestra mano **(valores)**.
Teniendo en cuenta que solo queremos que este **una sola vez**, lo cual se realiza de la siguiente forma:

```
if (valores.count(VALORES[siguiente]))==1:
                ascentente += 1
            elif (valores.count(VALORES[anterior]))==1:
                descendente += 1
            else:
                break
```
Por último hacemos la validación final de **ascendente+descendente+1=tamano_mano** para contar si esa mano es una escalera o no y calculamos su probabilidad tal como lo hace el profe David en su código.

Espero te haya sido de utilidad este tutorial, déjame en los comentarios que te pareció o si quieres que detalle alguno de los otros ejercicios de la clase o de la escuela de Data Science

y recuerda
**Nunca pares de aprender**