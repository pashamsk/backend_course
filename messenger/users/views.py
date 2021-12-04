from django.http.response import JsonResponse, HttpResponse
from django.template import loader
from django.views.decorators.http import require_GET, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rest_framework import viewsets

from .serializers import UserSerializer

from .models import User


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'home.html')


@require_POST
def create_user(request):
    try:
        data = request.POST
        new_user = User(
            username=data.get('username'),
            password=data.get('password'),
        )
        new_user.save()
    except ValueError:
        return HttpResponse('BadRequest', status=400)
    return HttpResponse('UserCreated', status=201)
    # return HttpResponseRedirect("/")


@require_POST
def update_user(request):
    try:
        data = request.POST
        up_user = User.objects.get(id=data.get('id'))
        up_user.location = data.get('location')
        up_user.save()
    except ValueError:
        return HttpResponse('BadRequest', status=400)
    except User.DoesNotExist:
        return HttpResponse('UserNotFound', status=404)
    return HttpResponse('UserEdited', status=200)


@require_POST
def delete_user(request):
    try:
        data = request.POST
        del_user = User.objects.get(id=data.get('id'))
        del_user.delete()
    except ValueError:
        return HttpResponse('BadRequest', status=400)
    except User.DoesNotExist:
        return HttpResponse('UserNotFound', status=404)
    return HttpResponse('UserDeleted', status=200)


@require_safe
def list_users(request):
    all_users = User.objects.all()
    data = [
        {
            'id': user.id,
            'username': user.username,
        } for user in all_users
    ]
    return JsonResponse({'users': data})


@require_GET
def details(request, id):
    try:
        user = User.objects.get(id=id)
        data = [
            {
                'id': user.id,
                'username': user.username,
                'password': user.password,
            }
        ]
    except User.DoesNotExist:
        return HttpResponse('UserNotFound', status=404)
    return JsonResponse({f'user id = {id}': data})


def users(request):
    template = loader.get_template('11.html')
    return HttpResponse(template.render())


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
