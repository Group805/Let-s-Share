from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'blog/home.html')

def blogs(request):
    return render(request, 'blog/blogs.html')

def contact(request):
    return render(request, 'blog/contact.html')

def login(request):
    return render(request, 'blog/login.html')

def submit(request):
    return render(request, 'blog/thanks.html')


