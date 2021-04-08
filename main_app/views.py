from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import ListView, DetailView


import uuid
import boto3
from .models import HairDiary, SkinDiary, Hair_Photo, Skin_Photo, Pill, Routine, Products

# Add these "constant" variables below the imports
S3_BASE_URL = 'https://s3-accesspoint.ca-central-1.amazonaws.com/'
BUCKET = 'glowup'


S3_BASE_URL = 'https://s3.ca-central-1.amazonaws.com/'
BUCKET = 'glowup'

# Define the home view


def home(request):
    return render(request, 'home.html')


# SUPPLEMENTS FORM STUFF
def supplements(request):
    pill = Pill.objects.filter(user=request.user)
    return render(request, 'supplements.html', {'pill': pill})


def supplements_form(request):
    return render(request, 'add_supplements.html')


def submit_form(request):
    Pill.objects.create(
        Name=request.POST['name'],
        Price=request.POST['price'],
        user=request.user,
    )
    return redirect('/supplements/')


def supplements_delete(request, p_id):
    p = Pill.objects.get(id=p_id)
    p.delete()
    return redirect('/supplements/')


# PRODUCTS FORM


def products(request):
    products = Products.objects.filter(user=request.user)
    return render(request, 'products.html', {'products': products})


def products_add(request):
    return render(request, 'products_form.html')


def products_submit(request):
    Products.objects.create(
        Name=request.POST['name'],
        Brand=request.POST['brand'],
        Price=request.POST['price'],
        user=request.user,
    )
    return redirect('/products/')


def products_delete(request, p_id):
    p = Products.objects.get(id=p_id)
    p.delete()
    return redirect('/products/')


def plan(request):
    return render(request, 'about.html')


@login_required
def hair_log(request):
    hair = HairDiary.objects.filter(user=request.user).order_by('-Date')
    return render(request, 'hair_log.html', {'hair': hair})


@login_required
def skin_log(request):
    skin = SkinDiary.objects.filter(user=request.user).order_by('-Date')
    return render(request, 'skin_log.html', {'skin': skin})


@login_required
def hair_detail(request, hair_id):
    hair = HairDiary.objects.get(id=hair_id)
    return render(request, 'log_detail.html', {'hair': hair})


@login_required
def skin_detail(request, skin_id):
    skin = SkinDiary.objects.get(id=skin_id)
    return render(request, 'skin_log_detail.html', {'skin': skin})


def hairdiary(request):
    return render(request, 'diary.html')


def skindiary(request):
    return render(request, 'diary.html')


# page to add log that displays both HairDiary and Skin Diary buttons
def add_hair_log(request):
    return render(request, 'create_form.html')


def add_skin_log(request):
    return render(request, 'create_form.html')


# HAIR DIARY FORM
@login_required
def create_form(request):
    return render(request, 'create_form.html')

# hair diary create


@login_required
def submit_create_form(request):
    HairDiary.objects.create(
        Log=request.POST['log'],
        Date=request.POST['date'],
        Water=request.POST['water'],
        Product=request.POST['product'],
        Morning=request.POST['morning'],
        Night=request.POST['night'],
        Supplements=request.POST['supplements'],
        user=request.user,
    )
    return redirect('/log/hair/')


# hair diary delete
def delete(request, h_id):
    h = HairDiary.objects.get(id=h_id)
    h.delete()
    return redirect('/log/hair/')

# hair diary edit


def edit_form(request, h_id):
    # get the particular hair post i'm editing by id
    h = HairDiary.objects.get(id=h_id)
    return render(request, 'edit_form.html', {'h': h})

# hair diary submit of update form after user has made edit


def submit_update_form(request, h_id):
    this_entry = HairDiary.objects.get(id=h_id)
    this_entry.Log = request.POST['log']
    this_entry.Date = request.POST['date']
    this_entry.Water = request.POST['water']
    this_entry.Product = request.POST['product']
    this_entry.Morning = request.POST['morning']
    this_entry.Night = request.POST['night']
    this_entry.Supplements = request.POST['supplements']
    this_entry.save()
    print(this_entry)
    return redirect('/log/hair/')


# hair diary submit of update form after user has made edit


@login_required
def submit_update_form(request, h_id):
    this_entry = HairDiary.objects.get(id=h_id)
    this_entry.Log = request.POST['log']
    this_entry.Date = request.POST['date']
    this_entry.Water = request.POST['water']
    this_entry.Product = request.POST['product']
    this_entry.Morning = request.POST['morning']
    this_entry.Night = request.POST['night']
    this_entry.save()
    print(this_entry)
    return redirect('/log/hair/')


# skin Diary FORM
def skin_create_form(request):
    return render(request, 'skin_create_form.html')

# skin diary create


@login_required
def submit_skin_form(request):
    SkinDiary.objects.create(
        Log=request.POST['log'],
        Date=request.POST['date'],
        Water=request.POST['water'],
        Product=request.POST['product'],
        Morning=request.POST['morning'],
        Night=request.POST['night'],
        Supplements=request.POST['supplements'],
        user=request.user,
    )
    return redirect('/log/skin/')


def skin_edit_form(request, s_id):
    # get the particular hair post i'm editing by id
    s = SkinDiary.objects.get(id=s_id)
    return render(request, 'skin_edit_form.html', {'s': s})

# skin diary update


def skin_edit_form(request, s_id):
    s = SkinDiary.objects.get(id=s_id)
    return render(request, 'skin_edit_form.html', {'s': s})


def skin_submit_update_form(request, s_id):
    this_entry = SkinDiary.objects.get(id=s_id)
    this_entry.Log = request.POST['log']
    this_entry.Date = request.POST['date']
    this_entry.Water = request.POST['water']
    this_entry.Product = request.POST['product']
    this_entry.Morning = request.POST['morning']
    this_entry.Night = request.POST['night']
    this_entry.Supplements = request.POST['supplements']
    this_entry.save()
    return redirect('/log/skin/')

# skin diary delete


def skin_delete(request, s_id):
    s = SkinDiary.objects.get(id=s_id)
    s.delete()
    return redirect('/log/skin/')


@login_required
def skin_submit_update_form(request, s_id):
    this_entry = SkinDiary.objects.get(id=s_id)
    this_entry.Log = request.POST['log']
    this_entry.Date = request.POST['date']
    this_entry.Water = request.POST['water']
    this_entry.Product = request.POST['product']
    this_entry.Morning = request.POST['morning']
    this_entry.Night = request.POST['night']
    this_entry.save()
    return redirect('/log/skin/')
# skin diary delete
# note: i have already imported both of the models at the top!


# PHOTOS STUFF

def add_hair_photo(request, hair_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
    try:
        s3.upload_fileobj(photo_file, BUCKET, key)
        url = f"{S3_BASE_URL}{BUCKET}/{key}"
        photo = Hair_Photo.objects.create(
            url=url, hair=HairDiary.objects.get(id=hair_id))
        photo.save()
    except:
        print('An error occurred uploading file to S3')
    return redirect('/log/hair/', hair_id=hair_id)


def add_skin_photo(request, skin_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
    try:
        s3.upload_fileobj(photo_file, BUCKET, key)
        url = f"{S3_BASE_URL}{BUCKET}/{key}"
        photo = Skin_Photo.objects.create(
            url=url, skin=SkinDiary.objects.get(id=skin_id))
        photo.save()
    except:
        print('An error occurred uploading file to S3')
    return redirect('/log/skin/', skin_id=skin_id)


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
