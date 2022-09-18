from django.db import models
from .mixin import DateTimeMixin

__all__ = {'TodoListItem'}

class TodoListItem(models.Model, DateTimeMixin):
    content = models.CharField(max_length=255)
    is_important = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk} - {self.content}'

    def __repr__(self):
        return self.pk, self.content

    class Meta:
        ordering = ['is_important']
        verbose_name = 'task'
        verbose_name_plural = 'tasks'