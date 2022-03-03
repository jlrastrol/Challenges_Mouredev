import unicodedata
import re

equivalencias = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "CH": "----",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "Ñ": "--.--",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "?": "..--..",
    "'": ".----.",
    "-": "-....-",
    "/": "-..-.",
    "\"": ".-..-.",
    "@": ".--.-.",
    "=": "-...-",
    "!": "-.-.--",
}

def cleanTexto(texto):
    texto = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        unicodedata.normalize( "NFD", texto), 0, re.I
    )
    return unicodedata.normalize( 'NFC', texto)

def caracterAMorse(c):
    if c in equivalencias:
        return equivalencias[c]
    else:
        return c

def morseACaracter(c):
    claves = list(equivalencias.keys())
    valores = list(equivalencias.values())
    if c in equivalencias.values():
        return claves[valores.index(c)]
    else:
        return c

def isMorse(texto):
    for caracter in texto:
        if(caracter != '.' and caracter != '-' and caracter != ' '):
            return False

    return True

def decodificarMorse(texto):

    textSplit = texto.split("  ")
    result = ""
    for caracter in textSplit:
        for caracMor in caracter.split():
            result += morseACaracter(caracMor)

        result += " "
    return result

def codificarMorse(texto):

    textClean = cleanTexto(texto)
    textoUper = textClean.upper()
    result = ""

    for caracter in textoUper:
        carMorse = caracterAMorse(caracter)
        if carMorse == " ":
            carMorse = "  "
        result += carMorse 
    return result


print("Introduzca texto o código morse:")
texto = input()

if(isMorse(texto)):
    print(decodificarMorse(texto))
else:
    print(codificarMorse(texto))


# Pruebas
# Esto es un texto para pasar a morse, gracias Fermín.
# . ... - ---   . ...   ..- -.   - . -..- - ---   .--. .- .-. .-   .--. .- ... .- .-.   .-   -- --- .-. ... . --..--   --. .-. .- -.-. .. .- ... .-.-.-
