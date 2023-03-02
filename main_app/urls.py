from django.urls import path
from . import views

urlpatterns = [
    #  USING AN EMPTY STRING MAKES THIS OUR ROOT ROUTE
    # views.home refers to a view that renders a file
    # the name='home' kwarg gives the route a name
    # naming routes is optional, but best practices
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # cats path
    path('cats/', views.cats_index, name='index'),
]