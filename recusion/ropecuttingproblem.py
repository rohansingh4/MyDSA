def ropecut(N, A, B, C):
    if (N == 0):
        return 0 
    if(N <= -1):
        return -1
    
    r1 = ropecut(N-A, A, B, C)
    r2 = ropecut(N-B, A, B, C)
    r3 = ropecut(N-C, A, B, C)

    res = max(r1, r2, r3)
    if res == -1:
        return -1
    else :
        return res +1



# driver code
if __name__ == "__main__":
    N, A, B, C = 17, 10, 11, 3
    result = ropecut(N, A, B, C)
    print(result)