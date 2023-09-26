
def fib(a:int):
    list_fib = [1,1]
    for i in range(2,a):
        list_fib.append(list_fib[i-1]+list_fib[i-2])
    return list_fib
print(fib(9))