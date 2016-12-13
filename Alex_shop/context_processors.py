__author__ = 'berluskuni'
from .settings import PORTAL_URL


def shop_processors(request):
    return {'PORTAL_URL': PORTAL_URL}

