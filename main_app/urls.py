from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('supplements/', views.supplements),
    path('products/', views.products),
    path('plan/', views.plan),
    path('accounts/signup/', views.signup, name='signup'),


    #this is the user's log show page
    path('log/hair/', views.hair_log),
    path('log/skin/', views.skin_log),

    #these are the paths to get to the forms for the user to enter thier diary input
    path('log/hairdiary/', views.hairdiary),
    path('log/skindiary/', views.skindiary), 

    #this is the user's log' detail page of every log 
    path('log/<int:hair_id>/', views.hair_detail),


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
    path('log/skindiary/create_form/', views.skin_create_form),
    path('log/skindiary/submit_create_form/', views.submit_skin_form),

    #this is the user's log' detail page of every log 
    path('log/<int:skin_id>/', views.skin_detail),

    #update skin diary: edit feature
    path('log/skindiary/<int:s_id>/edit/', views.skin_edit_form),
    #update hair diary step 2: accept form from user
    path('log/skindiary/<int:s_id>/skin_submit_update_form/', views.skin_submit_update_form),

    #delete skin diary
    path('log/skindiary/<int:s_id>/delete/', views.skin_delete),

    #PHOTOS 
   # path('log/<int:hair_id>/add_photo/', views.add_photo, name='add_photo'),
     
]

