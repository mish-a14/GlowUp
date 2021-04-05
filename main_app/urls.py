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

    path('log/<int:hair_id>/', views.hair_detail,),

    #create forms for hair diary
    path('log/hairdiary/create_form/', views.create_form),
    path('log/hairdiary/submit_create_form/', views.submit_create_form),
    #delete hair diary
    #update hair diary



    #create forms for skin diary
    #create skin diary 
    #update skin diary 
    #delete skin diary
]

