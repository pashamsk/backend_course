from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from users.views import UserViewSet, login, home, UserAuthViewSet, SearchUser


router = DefaultRouter()
router.register(r'api/admin/users', UserViewSet, basename='users')
router.register(r'api/users', UserAuthViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chats/', include('chats.urls')),
    path('users/', include('users.urls')),
    path('login/', login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social_auth/', include('social_django.urls', namespace='social')),
    path('', home, name='home'),
    # path('api/search/', SearchUser.as_view()),
    path('search/', include('users.urls')),
    # path('search_chats/', include('chats.urls')),
    # path('api/auth/', include('rest_framework_social_oauth2.urls')),
    # path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]

urlpatterns = format_suffix_patterns(urlpatterns)  # ?
urlpatterns += router.urls
