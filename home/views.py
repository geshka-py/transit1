from django.shortcuts import render


def about(request):
    return render(request, 'home/index.html')


def contact(request):
    return render(request, 'home/contact.html')


def index(request):
    return render(request, 'home/index.html')