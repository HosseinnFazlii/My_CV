
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index_view(request):
    context = {'name':'Hossein', 'lastname': 'Fazli'}
               
    return render(request,'index.html',context)
