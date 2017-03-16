import sys
import string
import functools

teste = "thiago.rodrigues.magalhaes.txt"

teste = teste.split(".")

del teste[len(teste) - 1]

string = ""
print(string.join(teste))