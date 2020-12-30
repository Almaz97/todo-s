from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone


class CategoryMptt(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', null=True, related_name='category',
                            on_delete=models.PROTECT)

    def get_full_name(self):
        names = self.get_ancestors(include_self=True).values('name')
        full_name = ' -> '.join(map(lambda x: x['name'], names))
        return full_name

    def get_children(self):
        names = self.get_descendants().values('name')
        children = ' -> '.join(map(lambda x: x['name'], names))
        return children

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class TodoList(models.Model):
    class Meta:
        ordering = ["-created"]

    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=True)
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(CategoryMptt, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()
