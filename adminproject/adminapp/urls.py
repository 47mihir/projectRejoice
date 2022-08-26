from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_login, name='login'),
    path('insert', views.user_form, name ='insert' ),
    path('<int:id>/', views.user_form, name ='update'),
    path('list', views.user_list, name = 'list'),
    path('delete/<int:id>/',views.user_delete,name='delete'),
    path('logout',views.user_logout, name='logout'),
]