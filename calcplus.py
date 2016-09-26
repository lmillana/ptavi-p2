#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import calcoo 

mifichero = open('fichero.csv')

lineas = mifichero.readlines()

if __name__ == "__main__":

    calcplus = calcoohija.CalculadoraHija()
    for linea in lineas:
        #lista = linea[:-1].split(',')
        
        operation = linea.split(',')[0]
        numbers = linea.split(',')[1:] 
        result = int(numbers[0]) #inicializamos el resultado al primero de la lista.
        
        if operation == "suma":
            for i in range(1, len(numbers)):
                result = calcplus.sum(result, int(numbers[i]))
        elif operation == "resta":
            for i in range(1, len(numbers)):
                result = calcplus.rest(result, int(numbers[i]))
        elif operation == "multiplica":
            for i in range(1, len(numbers)):
                result = calcplus.mult(result, int(numbers[i]))
        elif operation == "divide":
            for i in range(1, len(numbers)):
                if int(numbers[i]) == "0":
                    sys.exit("Error.Divide by zero.")
                else:
                    result = calcplus.div(result, int(numbers[i]))
        else:
            sys.exit("Gramatical Error.Try again.")
        print(result)

""" El resultado empieza en el primer elemento de la lista, la posicion cero.
Por eso hacemos que el rango empiece en la posicion uno, para no repetirlos."""

    


