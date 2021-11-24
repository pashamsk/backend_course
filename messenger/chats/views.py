from django.shortcuts import render
from django.http.response import JsonResponse

def chat_detail(request):
    return JsonResponse({'chat': 'first chat'})
