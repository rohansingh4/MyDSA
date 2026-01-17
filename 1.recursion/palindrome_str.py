def is_palindrome(s):
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True
    # Check first and last characters
    if s[0] != s[-1]:
        return False
    # Recursive case: check the substring without first and last characters
    return is_palindrome(s[1:-1])



# driver code
if __name__ == "__main__":
    s = "121"
    result = is_palindrome(s)
    if result:
        print(f'"{s}" is a palindrome')
    else:
        print(f'"{s}" is not a palindrome')
    # Base case: if the string is empty or has one character

