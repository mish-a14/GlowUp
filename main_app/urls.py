from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('supplements/', views.supplements),
    path('products/', views.products),
    path('plan/', views.plan),
    path('log/', views.log),
    path('accounts/signup/', views.signup, name='signup'),
    path('log/hairdiary/', views.hairdiary),
    path('log/skindiary/', views.skindiary), 
    path('log/hairdiary/create_form/', views.create_form),
    path('log/hairdiary/submit_create_form/', views.submit_create_form),
]

