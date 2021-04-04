from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('diet/', views.diet),
    path('supplements/', views.supplements),
    path('products/', views.products),
    path('plan/', views.plan),
    path('log/', views.log),
    path('accounts/signup/', views.signup, name='signup'),
]

