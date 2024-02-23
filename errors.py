#!/usr/bin/env python3

import sys
import os

#LBYL - Look Before You Leap

#EAFP  - Easy to ASK Forgiveness than permission
# (É mais facil pedir perdao do que permissao)

# try:
#     raise ValueError("Ocorreu um erro")
# except Exception as e:
#     print(str(e))



try:
    names = open("names.txt").readlines() #FileNotFoundError
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    # TODO: Usar retray
else:
    print("Success!!!")
finally:
    print("Execute isso sempre!")

try:
    print(names[2])
except:
    print("[Error] Missing name in the list.")
    sys.exit(1)