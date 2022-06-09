from multiprocessing import context
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render

class HomeView(View):
   
   #get es la funcion para las vistas
   #mostrar información
   def get(self, request, *args, **kwargs): 
      context = {}
      return render(request,'index.html',context)
   