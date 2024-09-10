from django.shortcuts import render

# Create your views here.
def set(request):
    data=render(request,'app/set.html')
    data.set_cookies('name','sanchita')
    #data.set_cookie('city','bhopal',httponly=True,)