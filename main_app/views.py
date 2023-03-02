from django.shortcuts import render
from .models import Cat

# temporary cats for building templates
cats = [
  {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
  {'name': 'Jojo', 'breed': 'calico', 'description': 'mean demo thing', 'age': 2},
]

# Create your views here.
# view functions match URLs to code, like controllers in Express
# define our home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    # just like we passed data to our templates in express
    # we pass data to our templates through our view funcs
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', { 'cats': cats })