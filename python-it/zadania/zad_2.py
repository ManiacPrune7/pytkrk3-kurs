"""
Write a function to check if string has balanced number of parentheses in proper order or not.
Example:
'()()()' -> True
'((()))' -> True
'((()' -> False
')()()(' -> False
'())))(((()' -> False
"""

def check_string(string: str) -> bool:  # True/False
  temp = 0

  for sign in string:
    if sign == '(':
      temp += 1
    else:
      if temp == 0:
        return False
      temp -= 1

  return temp == 0

print(check_string('())))(((()'))  # True
