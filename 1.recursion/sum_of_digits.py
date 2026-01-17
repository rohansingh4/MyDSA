# recursive funciton
def sum_of_digits(n):
    if  0<= n <= 9:
        return n
    return n%10 + sum_of_digits(n//10)

# driver code
if __name__ == "__main__":
    n = 1234
    sum = sum_of_digits(n)
    print(f"Sum of digits of {n} is: {sum}")