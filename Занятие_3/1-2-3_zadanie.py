def prime_number():
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("You entered an invalid value!")
            continue
    if number > 1:  
        for i in range(2, number):  
            if (number % i) == 0:  
                print(number, "is not a prime number")  
                print(i, "*", number // i, "=", number) 
                break  
        else:  
            print(number, "is a prime number") 
    else:  
        print(number, "is not a prime number")

def greatest_common_factor():
    while True:
        try:
            a = int(input("Enter first number: "))
            break
        except ValueError:
            print("You entered an invalid value!")
            continue

#Ещё один цикл, чтобы на втором номере не окидывало
#обратно в первый при ошибке, дабы снова не вводить.  
    while True:
        try:
            b = int(input("Enter second number: "))
            break
        except ValueError:
            print("You entered an invalid value!")
            continue
    while b > 0:
        a, b = b, a % b
    print("GCD is", a)

def least_common_multiple():
    while True:
        try:
            a = int(input("Enter first number: ")) 
            break
        except ValueError:
            print("You entered an invalid value!")
            continue
        
    while True:
        try:
            b = int(input("Enter second number: ")) 
            break
        except ValueError:
            print("You entered an invalid value!")
            continue
    max_num = max(a, b)
    while(True):
        if(max_num % a == 0 and max_num % b == 0):
            break
        max_num = max_num + 1
    print(f"The LCM of {a} and {b} is {max_num}")

while True:
    choose = input(
"""
Select operation:
1. Definition of prime numbers
2. Finding the greatest common factor
3. Finding the least common multiple
|||Enter "exit" for leave from program|||
"""        
    )
    if choose == "1":
        print("You have selected operation \"1\"")
        prime_number()
    elif choose == "2":
        print("You have selected operation \"2\"")
        greatest_common_factor()
    elif choose == "3":
        print("You have selected operation \"3\"")
        least_common_multiple()
    elif choose == "exit":
        print("Good Bye!")
        break
    