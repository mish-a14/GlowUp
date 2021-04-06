from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('supplements/', views.supplements),
    path('products/', views.products),
    path('plan/', views.plan),
    path('accounts/signup/', views.signup, name='signup'),


    #this is the user's log show page
    path('log/', views.log),

    #these are the paths to get to the forms for the user to enter thier diary input
    path('log/hairdiary/', views.hairdiary),
    path('log/skindiary/', views.skindiary), 

    #this is the user's log' detail page of every log 
    path('log/<int:hair_id>/', views.hair_detail),

    #path for adding a log for either hair or skin form
    path('log/addlog/', views.add_log),

    #create forms for hair diary
    path('log/hairdiary/create_form/', views.create_form),
    path('log/hairdiary/submit_create_form/', views.submit_create_form),
   
    #delete hair diary
    path('log/<int:h_id>/delete/', views.delete),

    #update hair diary step 1: deliver form to user
    path('log/<int:h_id>/edit/', views.edit_form),
    #update hair diary step 2: accept form from user
    path('log/<int:h_id>/hairdiary/submit_update_form/', views.submit_update_form),


    #create forms for skin diary
    #create skin diary 
    #update skin diary 
    #delete skin diary

    #PHOTOS 
   # path('log/<int:hair_id>/add_photo/', views.add_photo, name='add_photo'),
     
]

