#!/usr/bin/env python3
"""Calculadora infix.]

Funcionamento:

[operacao] [n1] [n2]

Operacaoes:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
opracao: sum 
n1: 5
n2: 4
9

Os resultados serao salvos em 'infixcalc.log'

"""

__version__ = "0.1.0"

import os
from datetime import datetime
import sys   #pegar os argumentos
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# nossa instancia
log = logging.Logger("logs.py", log_level)

# level
ch = logging.StreamHandler()
ch.setLevel(log_level)

# formatacao
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l%(lineno)d f:%(filename)s: %(message)s '
)
ch.setFormatter(fmt)

# destino
log.addHandler(ch)

arguments = sys.argv[1:]

if not arguments:
    operation = input("Operacao:")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [operation, n1, n2]

elif len(arguments) != 3:
    print("Numero de argumentos invalidos")
    print("ex: 'sum 5 5'")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print("Operaco invalida")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Numero invalido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)
try:
    n1, n2 = validated_nums
except ValueError as e:
    print(str(e))
    sys.exit(1)


if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2 

print(f"O resultado é {result}") 

path = "/"
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymus')

print(f"O resultado é {result}")

try:
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp} - {user} - {operation},{n1},{n2} = {result}\n")
except PermissionError as e:
    log.error((e))
    #print(str(e))
    sys.exit(1)

#print(f"{operation},{n1},{n2} = {result}", file=open(filepath, "a"))

