from django.urls import path
from . import views

app_name = 'userlist'
urlpatterns = [
    path('', views.users, name='users'),
    path('user_detail/<int:pk>/', views.user_detail, name='user_detail'),
    path('user_delete/<int:pk>/', views.user_delete, name='user_delete'),
]
