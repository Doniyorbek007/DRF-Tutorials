# from django.shortcuts import render
# from django.http import HttpResponse 
# from .models import *

# # Create your views here.
# def index(req):
#     # todo = Todo.objects.all()
#     data = {'key':'value'}
#     return 

#______________________________

from rest_framework import generics

from .models import *
from .serializers import