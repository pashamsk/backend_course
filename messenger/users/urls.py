from django.urls import path
from .views import create_user, list_users, users, details, update_user, delete_user #search_user
from .views import SearchUser

urlpatterns = [
    path('', users, name='render'),
    path('create_user/', create_user, name='create'),
    path('list_users/', list_users, name='list'),
    path('<int:id>/', details, name='details'),
    path('update_user/', update_user),
    path('delete_user/', delete_user),
    path('user/<str:query>/', SearchUser.as_view()),
    # path('search/', search_user),
]
