num = int(input("Enter number: "))

def factorial_value(num):
    factorial = 1

    if num == 0:
        return factorial
    else:
        for i in range(1,num+1):
            factorial = factorial*i
        return factorial


print(factorial_value(5))