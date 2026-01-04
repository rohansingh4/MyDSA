'''
Docstring for recusion.revision.5_sumOfDigits

Input : 12345
Output : 15

Input : 45632
Output :20

'''

def sumDigits(n):
    if 0 <= n <= 9:
        return n
    return (n%10 + sumDigits(n // 10))

n = 154
print(sumDigits(n))

#time complexity logN