from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response


from .serializers import CatSerializer, OwnerSerializer, CatListSerializer
from .models import Cat, Owner


class CreateRetrieveDeleteViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin, viewsets.GenericViewSet):
    # В теле класса никакой код не нужен! Пустячок, а приятно.
    pass


class LightCatViewSet(CreateRetrieveDeleteViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    @action(detail=False, url_path='recent-white-cats')
    def recent_white_cats(self, request):
        # Нужны только последние пять котиков белого цвета
        cats = Cat.objects.filter(color='Белый').order_by('-birth_year')[:5]
        # Передадим queryset cats сериализатору 
        # и разрешим работу со списком объектов
        serializer = self.get_serializer(cats, many=True)
        return Response(serializer.data)
    
    def get_serializer_class(self):
        # Если запрошенное действие (action) — получение списка объектов ('list')
        if self.action == 'list':
            # ...то применяем CatListSerializer
            return CatListSerializer
        # А если запрошенное действие — не 'list', применяем CatSerializer
        return CatSerializer



class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer 



