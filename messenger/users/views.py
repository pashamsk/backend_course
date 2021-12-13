from django.http.response import JsonResponse, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.http import require_GET, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics

from django.contrib import auth

from rest_framework import viewsets

from .serializers import UserSerializer, UserAuthSerializer

from .models import User

from tracker.tasks import send_mail_create

from django.core.exceptions import PermissionDenied

from .documents import UserDocument
# from .search import search

import abc

from elasticsearch_dsl import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView


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
        return JsonResponse({'status': '400 BadRequest'})
    return JsonResponse({'status': '200 OK UserCreated'})


@require_POST
def update_user(request):
    try:
        data = request.POST
        up_user = User.objects.get(id=data.get('id'))
        up_user.location = data.get('location')
        up_user.save()
    except ValueError:
        return JsonResponse({'status': '400 BadRequest'})
    except User.DoesNotExist:
        return JsonResponse({'status': '404 UserNotFound'})
    return JsonResponse({'status': '200 OK UserEdited'})


@require_POST
def delete_user(request):
    try:
        data = request.POST
        del_user = User.objects.get(id=data.get('id'))
        del_user.delete()
    except ValueError:
        return JsonResponse({'status': '400 BadRequest'})
    except User.DoesNotExist:
        return JsonResponse({'status': '404 UserNotFound'})
    return JsonResponse({'status': '200 OK UserDeleted'})


# @my_login_required
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
        return JsonResponse({'status': '404 UserNotFound'})
    return JsonResponse({f'user id = {id}': data})


def users(request):
    template = loader.get_template('11.html')
    return HttpResponse(template.render())


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def my_login_required(function):
    def wrapper(self, request, *args, **kw):
        if self.request._user.is_authenticated:
            return function(self, request, *args, **kw)
        else:
            return HttpResponseRedirect('/')  # см дополнения
    return wrapper


class UserAuthViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAuthSerializer

    @my_login_required
    def retrieve(self, request, pk, format=None):
        queryset = User.objects.get(username=request._user)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)

    @my_login_required
    def update(self, request, *args, **kwargs):
        queryset = User.objects.get(username=request._user)
        serializer = UserSerializer(queryset)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @my_login_required
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    @my_login_required
    def destroy(self, request, format=None):
        queryset = User.objects.get(username=request._user)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def create(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail_create.delay(serializer.data['username'], serializer.data['id'], serializer.data['date_joined'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SearchUser(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def get_queryset(self):
#         q = self.request.query_params.get('q')
#         print(q)
#         if q is not None:
#             return search(q)
#         return super().get_queryset()


class PaginatedElasticSearchAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden
        and return a Q() expression."""

    def get(self, request, query):
        try:
            q = self.generate_q_expression(query)
            print(q)
            search = self.document_class.search().query(q)
            response = search.execute()

            print(f'Found {response.hits.total.value} hit(s) for query: "{query}"')

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)


class SearchUser(PaginatedElasticSearchAPIView):
    serializer_class = UserAuthSerializer
    document_class = UserDocument

    def generate_q_expression(self, query):
        print(query)
        return Q('bool',
                 should=[
                     Q('match', username=query),
                     Q('match', id=query),
                     Q('match', location=query),
                 ], minimum_should_match=1)

