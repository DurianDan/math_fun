'''
This function check if a number is a prime number
Idea:
step 1: take square root of the number
step 2: divide the number by any num that are smaller than the square root
if there's a number (smaller than square root) that the number can divide => is prime
'''
from math import sqrt
first_primes = [1,2,3,5,7,11,13,17,19]
def check_prime(num):
    sqrt_num = sqrt(num)
    if num in first_primes: return True
    if str(sqrt_num).split(".")[1] == "0":
        return False
    else:
        if sqrt_num < 23:
            for i in first_primes:
                if i<  sqrt_num and num//i == 0:
                    return False
            return True
        else:
            for i in range(1,int(str(sqrt_num).split(".")[0])):
                if check_prime(i) and num//i == 0:
                    return False
            return True

if __name__ == "__main__":
    print(check_prime(29))

    