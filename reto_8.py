def binario(number):
    binario = []
    while(number !=0):
        binario.append(number%2)
        number = number//2
    return list(reversed(binario))

print(binario(98))

