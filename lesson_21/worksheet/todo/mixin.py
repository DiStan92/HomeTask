from django.db import models

class DateTimeMixin:
    date_create = models.DateTimeField(auto_now_add=True)
