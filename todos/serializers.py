from .models import CategoryMptt, TodoList
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMptt
        fields = '__all__'


class CategoryRetrieveSerializer(CategorySerializer):
    class Meta(CategorySerializer.Meta):
        fields = ('id', 'name')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['full_name'] = instance.get_full_name()
        response['sub_categories'] = instance.get_children()
        return response


class GetCategoryInTodoListSerializer(CategorySerializer):
    class Meta(CategorySerializer.Meta):
        fields = ('id', 'name')


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['category'] = GetCategoryInTodoListSerializer(
            instance.category
        ).data
        return response
