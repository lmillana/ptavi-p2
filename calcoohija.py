#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

import calcoo

class CalculadoraHija(calcoo.Calculadora):

    def mult(self, op1, op2):
        return op1 * op2

    def div(self, op1 ,op2):
        return op1 / op2

if __name__ == "__main__":

    calculadorahija = CalculadoraHija()
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters.")

    if sys.argv[2] == "suma":
        result = calculadorahija.sum(operando1,operando2)
    elif sys.argv[2] == "resta":
        result = calculadorahija.rest(operando1,operando2)
    elif sys.argv[2] == "multiplica":
        result = calculadorahija.mult(operando1,operando2)
    elif sys.argv[2] == "divide":
        if sys.argv[3] == "0":
            sys.exit("Error.Divide by zero.")
        else:
            result = calculadorahija.div(operando1,operando2)
    else:
        sys.exit("Gramatical Error.Try again.")

    print(result)
