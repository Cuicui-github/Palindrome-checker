from django.shortcuts import render


# Create your views here.
def home(request):
 #   r = requests.post('http://127.0.0.1:8000/',myText)
    string=isPalindrome("abc")
    return render(request,'home.html',{'string':string})
def isPalindrome(r):
    string = r.replace(" ","")
    test_string=string.lower()
    rev = ''.join(reversed(test_string))
    if (test_string == rev):
        return True
    return False
