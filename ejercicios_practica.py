#!/usr/bin/env python
'''
Numpy [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import numpy as np
from numpy import random

def ej1():
    
    '''
    Empecemos a jugar con las listas y su métodos, el objetivo
    es realizar el código lo más simple, ordenado y limpio posible,
    no utilizar bucles donde no haga falta, no "re inventar" una función
    que ya dispongamos de Python. El objetivo es:

    1) Generar una lista 3 numéros aleatorios con random (pueden repetirse),
       que estén comprendidos entre 1 y 10 inclusive
       (NOTA: utilizar comprension de listas a pesar de poder hacerlo
        con un método de la librería random)
        
    2) Luego de generar la lista sumar los números y ver si el resultado
       de la suma es menor o igual a 21
       a) Si el número es menor o igual a 21 se imprime en pantalla
          la suma y los números recoletados
       b) Si el número es mayor a 21 se debe tirar la lista y volver
          a generar una nueva, repetir este proceso hasta cumplir la
        condicion "a"

    Realizar este proceso iterativo hasta cumplir el objetivo
    '''
    
    numeros = []
    print('Comenzamos a divertirnos!')
    for k in range(100):
        numeros = [random.randint(1, 10) for x in range(3)]
        suma = sum(numeros)
        if suma <= 21:
            print(suma, '\n', numeros)
            break

    


def ej2():
    print('Comenzamos a ponernos serios!')

    '''
    Dado una lista de nombres de personas "nombres" se desea
    obtener una nueva lista filtrada que llamaremos "nombres_filtrados"
    La lista se debe filtrar por comprensión de listas utilizando la
    lista "padron" como parámetro.
    La lista filtrada sodo deberá tener aquellos nombres que empiecen
    con alguna de las letras aceptadas en el "padron".
    '''

    padron = ['A', 'E', 'J', 'T']

    nombres = ['Tamara', 'Marcelo', 'Martin', 'Juan', 'Alberto', 'Exequiel',
               'Alejandro', 'Leonel', 'Antonio', 'Omar', 'Antonia', 'Amalia',
               'Daniela', 'Sofia', 'Celeste', 'Ramon', 'Jorgelina', 'Anabela']

    # Se espera obtener:
    # ['Tamara', 'Juan', 'Alberto'......]
    nombres_filtrados = []
    for l in padron:
        nombres_filtrados_l = [x for x in nombres if x[0] == l]
        for i in nombres_filtrados_l:
            nombres_filtrados.append(i)
    print(nombres_filtrados)
    #inovetip: El código resuelve el enunciado pero no aprovecha la
    #compresión de listas. En el apunte vas a ver un ejemplo de "filtro"
    #útil para estos casos


def ej3():
    print("Un poco de Numpy!")
    # Ejercicio de funciones
    # Se desea calcular los valores de salida de
    # una función senoidal, dado "X" como el conjunto
    # de valores que deben someter a la función "sin"

    # Conjunto de valores "X" en un array
    x = np.arange(0, 2*np.pi, 0.1)

    # Utilizar la función np.sin para someter cada valor de "X",
    # obtenga el array "y_nump" que tenga los resultados
    # NO utilizar comprensión de listas, solo utilice la
    # funcion de numpy "np.sin"

    # y_nump =

    # Conjunto de valores "X" en una lista
    x = list(np.arange(0, 2*np.pi, 0.1))

    # Utilizar comprensión de listas para obtener la lista
    # "y_list" que tenga todos los valores obtenidos como resultado
    # de someter cada valor de "X" a la función math.sin

    # y_list =
    y_list = np.sin(x) #Inovetip: este es el resultado de y_nump :D
    print(y_list)
    # Inovetip:la idea es que utilices las dos funciones "np.sin" y math.sin
    #para obtener el mismo resultado, y comparar el código

    # Este es un ejemplo práctico de cuando es útil usar numpy,
    # basicamente siempre que deseen utilizar una función matemática
    # que esté definida en numpy NO necesitaran un bucle o comprensión
    # de listas para obtener el resultado de un monton de datos a la vez.


def ej4():
    print("Acercamiento al uso de datos relacionales")
    # Transformar variable numéricas en categóricas
    # Se dispone del siguiente diccionario que traduce el número ID
    # de un producto en su nombre, por ejemplo:
    # NOTA: Esta información bien podría ser una tabla SQL: id | producto
    producto = {
                556070: 'Auto',
                704060: 'Moto',
                42135: 'Celular',
                1264: 'Bicicleta',
                905045: 'Computadora',
                }

    lista_compra_id = [556070, 905045, 42135, 5674, 704060, 1264, 42135, 3654]

    # Crear una nueva lista "lista_compra_productos" que transforme la lista
    # de realizada por "ID" de producto en lista por "nombre" producto
    # Iterar sobre la lista "lista_compra_id" para generar la nueva
    # En cada iteración acceder al diccionario para traducir el ID.
    # NOTA: Tener en cuenta que puede haber códigos (IDs) que
    # no esten registrados en el sistema, en esos casos se debe
    # almacenar en la lista la palabra 'NaN', para ello puede hacer uso
    # de condicionales PERO recomendamos leer atentamente el método "get"
    # de diccionarios que tiene un parametro configurable respecto
    # que sucede sino encuentra la "key" en el diccionario.

    lista_compra_nombre = []
    for i in lista_compra_id:
        lista = producto.get(i,'NaN')
        lista_compra_nombre.append(lista)
    print(lista_compra_nombre)
    # Inovetip: tenes que lograr lo mismo pero utilizando 
    # compresión de listas :D

def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Black jack! [o algo parecido :)]

    El objetivo es realizar una aproximación al juego de black jack,
    el objetivo es generar una lista de 2 números aleatorios
    entre 1 al 10 inclusive, y mostrar los "números" al usuario.
    El usuario debe indicar al sistema si desea sacar más
    números para sumarlo a la lista o no sacar más
    A medida que el usuario vaya sacando números aleatorios que se suman
    a su lista se debe ir mostrando en pantalla la suma total
    de los números hasta el momento.
    Cuando el usuario no desee sacar más números o cuando el usuario
    haya superado los 21 (como la suma de todos) se termina la jugada
    y se presenta el resultado en pantalla

    BONUS Track: Realizar las modificaciones necesarias para que jueguen
    dos jugadores y compitan para ver quien sacá la suma de números
    más cercanos a 21 sin pasarse!
    '''
    print('\n')
    lista_a = [random.randint(1,10) for x in range(2)]
    lista_b = [random.randint(1,10) for x in range(2)]
    suma_a = sum(lista_a)
    suma_b = sum(lista_b)
    print('Jugador "A" sus cartas son:', lista_a, 'y suman:', suma_a)
    print('Jugador "B" sus cartas son:', lista_b, 'y suman:', suma_b)
    while suma_a < 21:
        print('Sus cartas', lista_a, 'suman:', suma_a)
        print('Jugagor "A" desea sacar otra carta?\n')
        x = str(input('Si desea otra carta "s", si no desea mas cartas "n" \n'))
        if x == 's':
            numero = [random.randint(1, 10)]
            lista_a.append(numero[0])
            suma_a = sum(lista_a)
            print('Sus cartas son', lista_a, 'y suman:', suma_a)
        elif x == 'n':
            print('Sus cartas son:', lista_a, 'y suman:', suma_a)
            break
        elif x != 's' and x != 'n':
            print('Ingrese una opcion valida')

    while suma_b < 21:
        print('Sus cartas', lista_b, 'Suman:', suma_b)
        print('Jugador"B" desea sacar otra carta?\n')
        x = str(input('Si desea otra carta "s", si no desea mas cartas "n" \n'))
        if x == 's':
            numero = [random.randint(1, 10)]
            lista_b.append(numero[0])
            suma_b = sum(lista_b)
            print('Sus cartas son', lista_b, 'y suman:', suma_b)
        elif x == 'n':
            print('Sus cartas son:', lista_b, 'y suman:', suma_b)
            break
        elif x != 's' and x != 'n':
            print('Ingrese una opcion valida')

    if suma_a > suma_b and suma_a <= 21:
        print('Jugador "A" con', suma_a, 'puntos gano la partida')
    elif suma_a < suma_b and suma_b <= 21:
        print('Jugador "B" con', suma_b, 'puntos gano la partida')
    elif suma_a > 21 and suma_b > 21:
        print('Ambos jugadores perdieron la partida')
    print('Finalizo la partida')

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
