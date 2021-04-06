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



@login_required
def log(request):
  hair = HairDiary.objects.all()
  hair = HairDiary.objects.filter(user = request.user)
  #hair = request.user.hair_set.all()
  return render(request, 'log.html', { 'hair': hair })


@login_required
def hair_detail(request, hair_id):
  hair = HairDiary.objects.get(id=hair_id)
  print(hair)
  print(request)
  return render(request, 'hair_log_detail.html', { 'hair': hair})




def hairdiary(request):
  return render(request, 'diary.html')

def skindiary(request):
  return render(request, 'diary.html')

#page to add log that displays both HairDiary and Skin Diary buttons
def add_log(request):
  return render(request, 'add_log.html')


#HAIR DIARY FORM 
#@login_required
def create_form(request):
  return render(request, 'create_form.html')

#hair diary create
@login_required
def submit_create_form(request):
  HairDiary.objects.create(
    Log=request.POST['log'],
    Date=request.POST['date'],
    user=request.user,
  )
  return redirect('/log')


#hair diary delete 
def delete(request, h_id):
  h = HairDiary.objects.get(id=h_id)
  h.delete()
  return redirect('/log')

#hair diary edit 
def edit_form(request, h_id):
  return
#hair diary update
def update(request, h_id):
  return
 



#skin Diary FORM 
#skin diary create
#skin diary update
#skin diary delete 
#note: i have already imported both of the models at the top! 





#LOG IN STUFF


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