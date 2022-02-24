from distutils.command import config
from django.shortcuts import render, HttpResponse
import pyrebase
config={
'apiKey': "AIzaSyCzjggEgn1MFChFIgyQ-moe7LcOgOkfoPY",
  'authDomain': "ml-7-bf914.firebaseapp.com",
  'projectId': "ml-7-bf914",
  'storageBucket': "ml-7-bf914.appspot.com",
  'messagingSenderId': "442104626326",
  'appId': "1:442104626326:web:58be149e1b9c55054696b7",
  'measurementId': "G-K8EVRB01ZV"
    
}
firebase =pyrebase.intializeApp(config);

auth= firebase.auth()




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
