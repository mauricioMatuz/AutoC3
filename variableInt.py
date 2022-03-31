import sys


gramatica0 = ["nombre", "=", "tipoDato", ";"]
nombre = ["letra", "nombre", "|", "letra"]
letra = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
LETRAs = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "Z",
]
tipoDato = ["int", "(L)"]
l = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

variableEjemplo = "x = int() ;"
variableEjemplo1 = "suma = int () ;"
variableEjemplo2 = "Arbol = int (25) ;"

bandera = True
nombreBool = False
tipoDatoBool = False
letraBool = False
lBool = False

tieneIgual = False
tieneNombre = False
tieneTipo = False
tieneParen = False
tieneComa = False
tieneDato = False
noTieneDato = False
error = False

gramatica0 = gramatica0[::-1]
nombre = nombre[::-1]
tipoDato = tipoDato[::-1]
l = l[::-1]

variableSplit = variableEjemplo1.split(" ")
variableSplit = variableSplit[::-1]
guardarPos = []

i = 0
j = 0
x = 0
y = 0
z = 0

while bandera:
    try:
        finPila = gramatica0.pop()
    except:
        break
    evaluar = variableSplit.pop()
    if finPila == "nombre":
        nombreBool = True
        tieneNombre = True
    else:
        error = True
    if finPila == "=" and evaluar == "=":
        tieneIgual = True
    else:
        error = True
    if finPila == ";" and evaluar == ";":
        tieneComa = True
    else:
        error = True
    if finPila == "tipoDato":
        tipoDatoBool = True
        nombreBool = False
        for i in range(len(tipoDato)):
            gramatica0.append(tipoDato[i])
        finPila = gramatica0.pop()
    else:
        error = True
    if finPila == "(L)":
        lBool = True
    else:
        error = True
    if nombreBool:
        while j < len(variableSplit[0]):
            if variableSplit[0][j].islower():
                for i in range(len(letra)):
                    if letra[i] == variableSplit[0][j]:
                        tieneNombre = True
            else:
                error = True
            if variableSplit[0][j].isupper:
                for i in range(len(LETRAs)):
                    if LETRAs[i] == variableSplit[0][j]:
                        tieneNombre = True
            else:
                error = True
            j = j + 1
    if tipoDatoBool:
        palabra = ""
        while x < 3:
            palabra = palabra + evaluar[x]
            if palabra == finPila:
                tieneTipo = True
            else:
                error = True
            x += 1
    if lBool:
        x = 0
        while y < len(evaluar):
            if evaluar[y] == "(":
                while x < len(l):
                    if z == len(evaluar):
                        z = 0
                    if evaluar[z] == l[x]:
                        tieneDato = True
                    else:
                        noTieneDato = True
                    x += 1
                    z += 1
            else:
                error = True
            if evaluar[y] == ")":
                tieneParen = True
            else:
                error = True
            y += 1
    i = i + 1

todoOk = False

if tieneIgual and tieneNombre and tieneTipo and tieneParen and tieneComa:
    if tieneDato or noTieneDato:
        print("TODO SIRVE, CREACION DE VARIABLE INT OK")
else:
    print("FUE FALSO")

# tieneIgual and tieneNombre and tieneTipo and tieneParen and tieneComa and tieneDato or noTieneDato
