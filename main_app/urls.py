from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),

    #AM ROUTINE
    path('morning/routine/', views.morning_routine),
    path('morning/routine/add/form/', views.morning_routine_add),
    path('morning/routine/submit/', views.morning_routine_submit),







    #PM ROUTINE
    path('evening/routine/', views.evening_routine),
    path('evening/routine/add/form/', views.evening_routine_add),
    path('evening/routine/submit/', views.evening_routine_submit),




    # SUPPLEMENTS PATH
    path('supplements/', views.supplements),  # this is the index page
    path('supplements/add/form/', views.supplements_form),
    path('supplements/submit_form/', views.submit_form),
    path('supplements/<int:p_id>/delete/', views.supplements_delete),


    # PRODUCTS PATH
    path('products/', views.products),
    path('products/add/form/', views.products_add),
    path('products/submit/', views.products_submit),
    path('products/<int:p_id>/delete/', views.products_delete),


    # this is the user's log show page
    path('log/hair/', views.hair_log),
    path('log/skin/', views.skin_log),

    # these are the paths to get to the forms for the user to enter thier diary input
    path('log/hairdiary/', views.hairdiary),
    path('log/skindiary/', views.skindiary),

    # this is the user's log' detail page of every log
    path('log/hair/<int:hair_id>/', views.hair_detail),


    # create forms for hair diary
    path('log/hairdiary/create_form/', views.create_form),
    path('log/hairdiary/submit_create_form/', views.submit_create_form),

    # delete hair diary
    path('log/<int:hair_id>/delete/', views.delete),

    # update hair diary step 1: deliver form to user
    path('log/<int:hair_id>/edit/', views.edit_form),
    # update hair diary step 2: accept form from user
    path('log/<int:h_id>/hairdiary/submit_update_form/', views.submit_update_form),




    # create forms for skin diary
    path('log/skindiary/create_form/', views.skin_create_form),
    path('log/skindiary/submit_create_form/', views.submit_skin_form),

    # this is the user's log' detail page of every log
    path('log/skin/<int:skin_id>/', views.skin_detail),

    # update skin diary: edit feature
    path('log/skindiary/<int:s_id>/edit/', views.skin_edit_form),
    # update hair diary step 2: accept form from user
    path('log/skindiary/<int:s_id>/skin_submit_update_form/',
         views.skin_submit_update_form),

    # delete skin diary
    path('log/skindiary/<int:skin_id>/delete/', views.skin_delete),


    # PHOTO PATHS
    path('log/hair/<int:hair_id>/add_hair_photo/',
         views.add_hair_photo, name='add_hair_photo'),
    path('log/skin/<int:skin_id>/add_skin_photo/',
         views.add_skin_photo, name='add_skin_photo'),
]
