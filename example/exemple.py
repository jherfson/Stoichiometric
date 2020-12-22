#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from stoichiometric.stoichiometric import Stoichiometric
import json

__autor__ = 'Micael Rocha de Azevêdo'
__email__ = 'azr.micael@gmail.com'
__version__ = '2020.22.12'
__date__ = 'dez 22, 2020'

print("")
print("CÁLCULO ESTEQUIOMÁTRICO" + 2*"\n")

eq = "Li2CO3 + Nb2O5 -> Li5NbO5 + CO2"

print("Equação fornecida:")
print(eq)

mass = 3

print("")
print("Equação balanceada:")
s = Stoichiometric(eq, mass)

print("...")

result = json.loads(s.print_mass())
print("")
reagentes = {}
produtos = {}
for item, valor in result.items():
    if valor < 0:
        reagentes[str(item).strip()] = str(abs(valor))
    else:
        produtos[str(item).strip()] = str(abs(valor))



print("Reagentes\n")
for r, m in reagentes.items():
    #s = 3*" " + r.ljust(30, ".") + ": " + m.rjust(10)
    s = 3*" " + "{reagente}:{massa} g".format(reagente=r.ljust(30, "."), massa=m.rjust(10))
    print(s)
print("")

print("Produtos\n")
for p, m in produtos.items():
    #s = 3*" " + p.ljust(30, ".") + ": " + m.rjust(10)
    s = 3*" " + "{produto}:{massa} g".format(produto=p.ljust(30, "."), massa=m.rjust(10))
    print(s)
print("")
