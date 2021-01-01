from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views


router = routers.SimpleRouter()

router.register('categories', views.CategoryViewSet, 'categories')
router.register('todos', views.TodoListViewSet, 'todos')

urlpatterns = [
    path('v1/', include(router.urls))
]