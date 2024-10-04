from django.shortcuts import render
from .models import Student,Summary

def display_data(request):
    records = Summary.objects.all()
    return render(request, 'interview/data.html', {'records': records})
