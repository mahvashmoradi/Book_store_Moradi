from django.db import models
from django.db.models import Count

class CategoriesManager(models.Manager):
    def empty(self):
        return self.annotate(c=Count('category')).filter(c=0)

    def full(self):
        return self.annotate(c=Count('category')).filter(c__gt=0)