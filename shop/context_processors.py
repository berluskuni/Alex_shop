__author__ = 'berluskuni'
from .models import Category


def categories_processors(request):
    return {'categories': Category.objects.prefetch_related('subcategory').all().order_by('name')}
