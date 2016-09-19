#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def plus(op1, op2):
    """ Function to sum the operands """
    return op1 + op2

def minus(op1, op2):
    """ Function to substract the operands """
    return op1 - op2

def mult(op1, op2):
	 """ Function to multiply the operands """
    return op1 * op2

def div(op1, op2)
	 """ Function to divide the operands """
    return op1/op2

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1]) #Pasamos a int porque si sumamos como string, nos daria 23
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = minus(operando1, operando2)
	 elif sys.argv[2] == "multiplica":
        result = mult(operando1, operando2)
    elif sys.argv[2] == "divide":
        if op2 == "0":
            sys.exit("Division entre cero")
        else:
            result = div(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar,restar, multiplicar o dividir.')

    print(result)
