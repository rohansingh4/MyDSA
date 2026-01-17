'''
Docstring for recusion.revision.7_generateSubset
Input :  set = "abc"
Output : "". "a", "b", "c", "ab", "ac", "bc", "abc"

Input : set = "abcd"
Output : "" "a" "ab" "abc" "abcd" "abd" "ac" "acd"
         "ad" "b" "bc" "bcd" "bd" "c" "cd" "d"
'''

# driver

def genSubset(s, index, curr):
    if len(s) == index:
        print(f'"{curr}"')
        return
    genSubset(s, index + 1, curr)
    genSubset(s, index + 1, curr + s[index])

if __name__ == "__main__":
    s = "abc"
    # res = genSubset(s, 0, "")
    # print(res)
    genSubset(s, 0, " ")