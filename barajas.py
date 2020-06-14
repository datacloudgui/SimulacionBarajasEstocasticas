import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)
    
    return mano

def main(tamano_mano, intentos):
    barajas = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    escalera = 0 #contará el numero de escaleras
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

    probabilidad_escalera = escalera / intentos
    print(f'La probabilidad de obtener una escalera en una mano de {tamano_mano} cartas es {probabilidad_escalera}')

if __name__ == '__main__':
    tamano_mano = int(input('De cuantas barajas (cartas) sera la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))

    main(tamano_mano, intentos)