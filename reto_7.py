'''
 * Reto #7
 * CONTANDO PALABRAS
 * Fecha publicación enunciado: 14/02/22
 * Fecha publicación resolución: 21/02/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
'''
import re

def countWords(text):
    arrayText = re.sub(r'[^\w\s]','',text.lower()).split(" ")
    dictWords = {}
    for word in arrayText:
        if(dictWords.get(word) != None):
            dictWords[word] = dictWords[word]+1 
        else:
            dictWords[word] = 1
        
    return dictWords

text = "Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas."
print(countWords(text))