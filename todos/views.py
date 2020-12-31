from rest_framework.viewsets import ModelViewSet
from .models import CategoryMptt, TodoList
from rest_framework.response import Response
from .serializers import (CategorySerializer, TodoListSerializer,
                          CategoryRetrieveSerializer)
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.conf import settings


class CategoryViewSet(ModelViewSet):
    queryset = CategoryMptt.objects.all()
    serializer_class = CategorySerializer

    @method_decorator(cache_page(settings.CACHE_TIME))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, args, kwargs)

    @method_decorator(cache_page(settings.CACHE_TIME))
    def retrieve(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = CategoryRetrieveSerializer(category)
        return Response(serializer.data)


class TodoListViewSet(ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    @method_decorator(cache_page(settings.CACHE_TIME))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, args, kwargs)

    @method_decorator(cache_page(settings.CACHE_TIME))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, args, kwargs)
