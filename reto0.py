
for k in range(0,100):
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