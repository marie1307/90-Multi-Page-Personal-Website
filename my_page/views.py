from django.shortcuts import render, redirect
from django.http import HttpResponse

my_list = ["My page", "My content", "My contacts list"]

def home(request):
    return HttpResponse ("Welcome to EU")

def about(request):
    return render(request, 'my_page/about.html')


def contact(request):
    return render(request, 'my_page/contact.html')
