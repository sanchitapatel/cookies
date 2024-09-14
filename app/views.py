from django.shortcuts import render

# Create your views here.
# def set(request):
#     data=render(request,'set.html')
#     data.set_cookie('name','sanchita')
#     data.set_cookie('city','bhopal',httponly=True,secure=False)
#     #data.set_cookie('name','sanchita',max_age=60*60*24,)
#     return data
# def get(request):
#     print(request.COOKIES)
#     name = request.COOKIES['name']
#     age = request.COOKIES['age']
#     city = request.COOKIES['city']
#     data={
#         'name':'nm',
#         'age':'ag',
#         'city':'city'
#     }
#     return render(request,'app/get.html',{'data':data})
# def delete(request):
#     data =render(request,'app/delete.html')
#     data.delete_cookie('name')
#     data.delete_cookie('age')
#     data.delete_cookie('city')
#     return data
from django.shortcuts import render

# Create your views here.

def set(request):
    data = render(request, 'set.html')
    data.set_cookie('name','Kushagra', max_age= 4*24*60*60, httponly=True,secure=True)
    data.set_cookie('age','24', max_age= 4*24*60*60, httponly=True,secure=True)
    data.set_cookie('city','Bhopal',max_age= 4*24*60*60, httponly=True,secure=False)
    return data

def get(request):
    print(request.COOKIES)
    name = request.COOKIES['name']
    age = request.COOKIES['age']
    city = request.COOKIES['city']
    data={'name': name,
          'age': age,
          'city': city}
    return render(request, 'get.html', data)