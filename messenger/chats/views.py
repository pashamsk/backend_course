from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.http import require_GET, require_POST, require_safe


def chat_detail(request):
    return JsonResponse({'chat': 'first chat'})
