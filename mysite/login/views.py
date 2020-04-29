from django.shortcuts import render
from .models import User

# Create your views here.
def homepage(request):
    context = {}
    if User.username and  
