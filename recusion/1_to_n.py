def func(n):
    if (n < 1):
        return
    func(n-1)
    print(n)


# driver code
if __name__ == "__main__":
    n = 5
    func(n)