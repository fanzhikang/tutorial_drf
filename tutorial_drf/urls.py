from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets.views import PostViewSet,TagViewSet, UserViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('tags', TagViewSet)
router.register('users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
