from django.urls import path, include
from rest_framework.routers import DefaultRouter

from musics.views import MusicModelViewSet

router = DefaultRouter()
router.register(r'music', MusicModelViewSet, basename='music')

urlpatterns = [
    path('', include(router.urls)),
]
