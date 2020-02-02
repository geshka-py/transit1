from django.shortcuts import render

def index(requests):
    return render(request, 'gallery/index.html')

def delete(requests):
    return render(request, 'gallery/delete.html')

def add_img(requests):
    return render(request, 'gallery/add_img.html')
