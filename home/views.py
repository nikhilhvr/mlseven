from django.shortcuts import render, HttpResponse

def home (request):
    return render(request, 'index.html')

def about (request):
    return HttpResponse("This is the about page")

def books (request):
    return render(request, 'books.html')

def documentation (request):
    return render(request, 'documentation.html')

def course (request):
    return render(request, 'course.html')
    
    # return HttpResponse("This is the contact page")

def community (request):
    return render(request, 'community.html')
    

# Create your views here.
