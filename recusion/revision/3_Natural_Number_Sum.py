'''
Docstring for recusion.revision.3_Natural_Number_Sum

Input : 3
Output : 6
Explanation : 1 + 2 + 3 = 6

Input : 5
Output : 15
Explanation : 1 + 2 + 3 + 4 + 5 = 15

'''

def calcSum(n):
    if n < 1:
        return 0

    return (n + calcSum(n-1))


n = 3
x = calcSum(n)
print(x)

