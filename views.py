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
        string2=r+": Yes"
    else:
        string2=r+": No"
    f=open('/Users/weihe/django_projects/zqxt_tmpl/learn/history.txt','a')
    f.write(string2+';')
    f.close()
    f=open('/Users/weihe/django_projects/zqxt_tmpl/learn/history.txt','r')
    string=f.read()
    return render(request,'home.html',{'string':string})
    f.close()
