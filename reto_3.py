'''
 * Reto #3
 * ¿ES UN NÚMERO PRIMO?
 * Fecha publicación enunciado: 17/01/22
 * Fecha publicación resolución: 24/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100. 
'''

def isPrime(number):
    if number < 2 :
        return False
    
    for k in range(2,number):
        if(number%k == 0):
            return False
    return True

for i in range (1,100):
    if(isPrime(i)):
        print(i)