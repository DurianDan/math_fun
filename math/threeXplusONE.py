#https://www.youtube.com/watch?v=094y1Z2wpJg
#Youtube video titled: "The Simplest Math Problem No One Can Solve - Collatz Conjecture"

#Below function is based on the above math problem 
#and i think it can be used to generate hash key.

def threeXplusONE(n:int,step_num=[]):
    '''input: n ()    starting integer that greater than 0
              step_num      number after each operation(step)
       output: the list of all the number that it has calculated'''
    step_num.append(n)
    if n == 0:
        return "the first integer must be greater than 0"
    if n == 1:
        return step_num,len(step_num)
    if (n%2) == 0:
        n= int(n/2)
        return threeXplusONE(n,step_num=step_num)
    if (n%2) > 0 :
        n= 3*n+1
        return threeXplusONE(n,step_num=step_num)

if __name__ == "__main__":
    '''NOTICE: i think this test will break your CPU if u dont interupt the executor :))'''
    for i in range(1,2^99999999999):
        print(i,"   ",threeXplusONE(i)[1])


        