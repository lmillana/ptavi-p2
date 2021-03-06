#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():

    def sum(self, op1, op2):
        return op1 + op2

    def rest(self, op1, op2):
        return op1 - op2

if __name__ == "__main__":

    calculadora = Calculadora()

    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])

    except ValueError:
        sys.exit("Error: Non numerical parameters.")

    if sys.argv[2] == "suma":
        result = calculadora.sum(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calculadora.rest(operando1, operando2)
    else:
        sys.exit("Gramatic Error")

    print(result)
