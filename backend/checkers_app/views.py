from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    #prints current user login cool!
    print(request.user)
    
    return render(request, 'index.html'   ,{}) #pass data