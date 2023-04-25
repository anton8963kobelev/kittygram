from django.urls import path, include

from .views import CatViewSet, OwnerViewSet, LightCatViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cats', CatViewSet)
router.register('owners', OwnerViewSet)
router.register(r'mycats', LightCatViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
