
def sum_of_n(n):

    if (n == 0):
        return 0
    
    return n + sum_of_n(n-1)


# print sum of first n natural numbers using recursion

if __name__ == "__main__":
    n = 5
    result = sum_of_n(n)
    print(f"Sum of first {n} natural numbers is: {result}")