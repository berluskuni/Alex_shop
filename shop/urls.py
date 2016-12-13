__author__ = 'berluskuni'
from django.conf.urls import url
from .views import product_list, BaseProductsList, BaseProductDetailView


urlpatterns = [
    url(r'^$', product_list, name="home"),
    url(r'^(?P<slug>[-\w]+)/$', product_list, name='product_category'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/$', BaseProductsList.as_view(), name='product_subcategory'),
    url(r'^(?P<subcategory_slug>[-\w]+)/(?P<slug>[-\w]+)/(?P<pk>[-\d]+)/$', BaseProductDetailView.as_view(),
        name='product_items'),

]

from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
