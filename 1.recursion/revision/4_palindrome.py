'''
Docstring for recusion.revision.4_palindrome

Input : malayalam
Output : Yes
Reverse of malayalam is also
malayalam.

Input : max
Output : No
Reverse of max is not max. 

'''

def palin(s):
  if len(s) == 0:
    return True
  if len(s) == 1:
    return True
  if s[0] == s[-1]:
    return palin(s[1:-1])
  else :
    return False  

s = "aba"
print(palin(s))