# #Statemant
# Se -> if
# Senao, se -> elif 
# Senao -> else
# E -> and 
# Ou -> or
# NAO - not

# #expression
# é feriado?
# é natal?
# é feriado e NAO é natal
# é sabado?
# é domingo?
# é sabado OU é domingo?

# #actions
# #funcao / metodo / instrucao


# PSEUDO CODIGO
import ir, pegar, pedir, tem, comer, ficar 

# Premissas
today = "Segunda"
hora = 15
natal = False
chovendo = True
frio = True
nevando = True
semana = ["segunda", "terca", "quarta", "quinta", "sexta"]
feriados = ["quarta"]
horario_padaria = {
    "semana": 19,
    "fds": 12
}

# Algoritmo
if today in feriados and not natal:
    padaria_aberta = False
elif today not in semana and hora < horario_padaria["fds"]:
    padaria_aberta = True
elif today in semana and hora < horario_padaria["semana"]:
    padaria_aberta = True
else:
    padaria_aberta = False

if padaria_aberta:
    if chovendo and frio or nevando:
        pegar("guarda-chuva")
        pegar("blusa")
        pegar("botas")
    elif chovendo and not frio:
        pegar("gurda-chuvas")
        pegar("agua")
    elif chovendo:
        pegar("guarda-chuva")

    ir("padaria")

    if tem("pao int") and tem("bagete"):
        pedir(6, "pao int")
        pedir(6, "baguete")
    elif tem ("pao int") or tem("baguete"):
        pedir(12, "qualquer um dos 2")
    else:
        pedir(6, "qualquer pao")
else:
    ficar("casa")
    comer("bolacha")