from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import *
# Create your views here.

def index(request):
    tasks = Task.objects.all() #get all elements
    return render(request,'main/index.html',{'tasks':tasks})

def about(request):
    return HttpResponse("<h2>about LANDU</h2>")


  
# upload image function 
def hotel_image_view(request): 
  
    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = HotelForm() 
    return render(request, 'main/image_form.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfully uploaded')     
