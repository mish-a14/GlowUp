from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Hottie!</h1>')

def diet(request):
  return render(request, 'about.html')

def supplements(request):
  return render(request, 'about.html')

def products(request):
  return render(request, 'about.html')

def plan(request):
  return render(request, 'about.html')

def log(request):
  return render(request, 'about.html')


 # This inherited method is called when a
  # valid cat form is being submitted
def form_valid(self, form):
    # Assign the logged in user (self.request.user)
  form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
  return super().form_valid(form)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)