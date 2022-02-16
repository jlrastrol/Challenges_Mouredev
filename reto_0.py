'''
 * Reto #0
 * EL FAMOSO "FIZZ BUZZ"
 * Fecha publicación enunciado: 27/12/21
 * Fecha publicación resolución: 03/01/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

for k in range(1,100):
    divisibleEntre3 = k % 3 == 0    
    divisibleEntre5 = k % 5 == 0

    if(divisibleEntre5 & divisibleEntre3):
        print("FizzBuzz")
    elif divisibleEntre3:
        print("Fizz")
    elif divisibleEntre5:
        print("Buzz")
    else:
        print(k)