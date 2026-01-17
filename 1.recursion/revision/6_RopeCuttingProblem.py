'''
Docstring for recusion.revision.6_RopeCuttingProblem

Input: 

N = 17, A = 10, B = 11, C = 3 

Output: 3 

Explanation: The maximum cut can be obtain after making 2 cut of length 3 and one cut of length 11. 

Input: N = 10, A = 9, B = 7, C = 11 

Output: -1 

Explanation: It is impossible to make any cut so output will be -1.

'''

def ropeCut(n, a, b, c):
    if n < 0:
        return -1
    if n == 0:
        return 0
    res = max((ropeCut(n-a, a, b, c)),(ropeCut(n-b, a, b, c)),(ropeCut(n-c, a, b, c)))
    if res == -1:
        return -1
    else :
        return res + 1

n, a, b, c = 17, 10, 11, 3
print(ropeCut(n, a, b, c))