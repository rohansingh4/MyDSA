# def josephus(n, k):
#     if n==1:
#         return 1
#     return (josephus(n-1, k) + k-1) % n+1

# # driver code
# if __name__ == "__main__":
#     n, k = 7, 3
#     result = josephus(n, k)
#     print(result)


def josephus_debug(n, k):
    if n == 1:
        print("J(1) = 1")
        return 1

    prev = josephus_debug(n - 1, k)
    curr = (prev + k - 1) % n + 1

    print(f"J({n}) = (J({n-1}) + {k} - 1) % {n} + 1")
    print(f"     = ({prev} + {k} - 1) % {n} + 1")
    print(f"     = {curr}\n")

    return curr


if __name__ == "__main__":
    n = 5
    k = 2
    josephus_debug(n, k)
