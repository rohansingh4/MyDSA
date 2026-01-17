def func(n):
    print(n)
    if(n <= 1):
        return
    
    func(n-1)



# driver code
if __name__ == "__main__":
    n = 5
    func(n)