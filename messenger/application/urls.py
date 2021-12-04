from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from users.views import UserViewSet


router = DefaultRouter()
router.register(r'api/users', UserViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chats/', include('chats.urls')),
    path('users/', include('users.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)  # ?
urlpatterns += router.urls
