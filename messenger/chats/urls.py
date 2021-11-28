from django.contrib import admin
from django.urls import path, include
from .views import chat_detail

urlpatterns = [
    path('', chat_detail, name='chat_detail'),
    # path('create_chat/', create_chat, name='create'),
]
