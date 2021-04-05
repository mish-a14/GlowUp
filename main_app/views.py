from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import ListView, DetailView

from .models import HairDiary, SkinDiary

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Define the home view
def home(request):
  return render(request, 'home.html')

def supplements(request):
  return render(request, 'about.html')

def products(request):
  return render(request, 'about.html')

def plan(request):
  return render(request, 'about.html')



#@login_required
def log(request):
  return render(request, 'log.html')


def hairdiary(request):
  return render(request, 'diary.html')

def skindiary(request):
  return render(request, 'diary.html')

#@login_required
def create_form(request):
  return render(request, 'create_form.html')

@login_required
def submit_create_form(request):
  HairDiary.objects.create(
    Log=request.POST['log'],
    Date=request.POST['date'],
    user=request.user,
  )
  return redirect('/log')



 



def form_valid(self, form):
  form.instance.user = self.request.user 
  return super().form_valid(form)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)