def FizzBuzz (target):
    for n in range(1, target +1):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0 :
            print("Fizz")
        elif n % 5 == 0 :
            print("Buzz")
    
target = int(input("Qual o valor desejado ? "))
FizzBuzz(target)