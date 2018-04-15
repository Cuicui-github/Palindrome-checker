
from django.contrib import admin
from django.urls import path
from learn import views as learn_views

urlpatterns = [
    path('isPalindrome/', learn_views.isPalindrome, name='isPalindrome'), 
    path('',learn_views.home, name='home'),
    path('admin/', admin.site.urls),
]
