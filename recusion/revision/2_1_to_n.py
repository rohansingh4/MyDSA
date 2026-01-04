'''
Docstring for recusion.revision.2_1_to_n

Input: N = 10 
Output: 1 2 3 4 5 6 7 8 9 10
Input: N = 7 
Output: 1 2 3 4 5 6 7

'''
def printAsc(n):
    if n < 1:
        return 
    printAsc(n-1)
    print(n)

n = 7
printAsc(n)

# Time Complexity O(n), Space Complexity O(n)