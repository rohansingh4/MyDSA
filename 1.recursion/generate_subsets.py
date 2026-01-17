"""

Input :  set = "abc"
Output : "". "a", "b", "c", "ab", "ac", "bc", "abc"

Input : set = "abcd"
Output : "" "a" "ab" "abc" "abcd" "abd" "ac" "acd"
         "ad" "b" "bc" "bcd" "bd" "c" "cd" "d"

"""


def subsets(s, index, current):
    if index == len(s):
        print(f'"{current}"')
        return
    
    subsets(s, index + 1, current)
    subsets(s, index + 1, current + s[index])

if __name__ == "__main__":
    s = "abc"
    subsets(s, 0, "")

# def subsets(s, index, current):
#     # Base case: processed entire string
#     if index == len(s):
#         print(f'"{current}"')
#         return

#     # Choice 1: exclude current character
#     subsets(s, index + 1, current)

#     # Choice 2: include current character
#     subsets(s, index + 1, current + s[index])


# # Driver code
# s = "abc"
# subsets(s, 0, "")
