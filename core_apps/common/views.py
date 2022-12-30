from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'common/about.html')

def contact(request):
    return render(request, 'common/contact.html')


