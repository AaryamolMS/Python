def is_palindrome(n):
   return str(n) == ''.join(reversed(str(n)))
n=input("Enter a input: ")
result=is_palindrome(n)
if result:
  print("The number is a palindrome!")
else:
  print("The number is not a palindrome.")
  
  
  
   
