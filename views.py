from django.shortcuts import render
 
# Create your views here.
def home(request):
    
    return render(request,'home.html')
def isPalindrome(request):
    
    r=request.GET['input_string']
    string1 = r.replace(" ","")
    test_string=string1.lower()
    rev = ''.join(reversed(test_string))
    if (test_string == rev):
        string=r+":Yes"
    else:
        string=r+"No"
    return render(request,'home.html',{'string':string})
