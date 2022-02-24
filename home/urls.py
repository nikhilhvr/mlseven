
from django.urls import path, include
from home import views

urlpatterns = [
    path ("", views.home, name='home'),
    path ('about', views.about, name='about' ),
    path ('books', views.books, name='books' ),
    path ('documentation', views.documentation, name='documentation' ),
    path ('course', views.course, name='course'),
    path ('community', views.community, name='community' )
    
]
