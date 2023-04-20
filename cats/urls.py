from django.urls import path, include

from .views import CatViewSet, OwnerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
