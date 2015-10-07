#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import calcoo
import calcoohija
import csv


if __name__ == "__main__":
    calchija = calcoohija.CalculadoraHija()
    with open(sys.argv[1]) as fichero:
        reader = csv.reader(fichero)
        for ListaNums in reader:

            Operacion = ListaNums.pop(0)

            if Operacion == 'suma':
                suma = calchija.plus(int(ListaNums[0]), int(ListaNums[1]))
                for numero in ListaNums[2:]:
                    suma = calchija.plus(suma, int(numero))
                print(suma)

            elif Operacion == 'resta':
                resta = calchija.minus(int(ListaNums[0]), int(ListaNums[1]))
                for numero in ListaNums[2:]:
                    resta = calchija.minus(resta, int(numero))
                print(resta)

            elif Operacion == 'multiplica':
                multi = calchija.multi(int(ListaNums[0]), int(ListaNums[1]))
                for numero in ListaNums[2:]:
                    multi = calchija.multi(multi, int(numero))
                print(multi)

            elif Operacion == 'divide':
                div = calchija.div(int(ListaNums[0]), int(ListaNums[1]))
                for numero in ListaNums[2:]:
                    div = calchija.div(div, int(numero))
                    print(div)
