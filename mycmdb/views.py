from django.shortcuts import render
from django.shortcuts import HttpResponse
from mycmdb import models



# Create your views here.

def index(request):
    return HttpResponse('Hello,World!')


# def index2(request):
#     return render(request,'index.html')

# def index2(request):
#     myit = models.Zclist.objects.get(id=2)
#     return render(request, 'index.html', {
#         'myit':myit,

def index2(request):
    myits = models.Zclist.objects.all()
    return render(request, 'index.html', {
         'myits': myits,
    })

