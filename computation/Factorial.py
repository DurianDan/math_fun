def factorial(n:int):
    if n == 0 or n == 1:
        return 1
    elif n < 0 :
        return "negative integer factorials are undefined"
    else:
        return n*factorial(n-1)

print(factorial(10))