'''
Docstring for recusion.revision.1_n_to_1

Input: N = 10
Output: 10 9 8 7 6 5 4 3 2 1
Input: N = 7
Output: 7 6 5 4 3 2 1

'''
def printDesc(n):
    if n < 1:
        return
    
    print(n)
    printDesc(n-1)   

# driver
if __name__ == "__main__":
    n = 10
    printDesc(n)
