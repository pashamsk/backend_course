from django.urls import path
from users.views import create_user, list_users, user_details, users

urlpatterns = [
    path('', users, name='render'),
    path('create_user/', create_user, name='create'),
    path('list_users/', list_users, name='list'),
    path('user_details/', user_details, name='details'),
]
