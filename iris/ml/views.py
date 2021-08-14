from django.http import request
from django.shortcuts import render

def predict(request):
    return render(request, 'new.html')