def isPalindrome(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False
user_response = input("Enter a string:")
string = user_response.replace(" ","")
s=string.lower()
if isPalindrome(s):
    print("Yes")
else:
    print("No")
