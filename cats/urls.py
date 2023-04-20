from django.urls import path

from .views import CatList, CatDetail


urlpatterns = [
    path('cats/', CatList.as_view()),
    path('cats/<int:pk>/', CatDetail.as_view()),
]