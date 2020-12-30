from rest_framework.viewsets import ModelViewSet
from .models import CategoryMptt, TodoList
from rest_framework.response import Response
from .serializers import (CategorySerializer, TodoListSerializer,
                          CategoryRetrieveSerializer)


class CategoryViewSet(ModelViewSet):
    queryset = CategoryMptt.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = CategoryRetrieveSerializer(category)
        return Response(serializer.data)


class TodoListViewSet(ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
