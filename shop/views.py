# coding=utf-8
from django.shortcuts import render
from models import Category, Product, SubCategory, ProductImage
# Create your views here.
from django.views import generic


def product_list(request):
    return render(request, 'home.html')


class BaseProductsList(generic.ListView):

    context_object_name = 'products'
    template_name = 'product.html'

    def get_ordering(self):
        name, ordering = self.order.split('-')
        if ordering == 'desc':
            ord_name = '-' + name
            return ord_name
        return name

    def get(self, request, **kwargs):
        self.paginate_by = self.request.GET.get('show', 4)
        self.order = self.request.GET.get('sort', 'name-asc')
        self.color = self.request.GET.get('color', None)
        self.size = self.request.GET.get('size', None)
        self.price = self.request.GET.get('price', None)
        return super(BaseProductsList, self).get(request, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BaseProductsList, self).get_context_data()
        context['subcategory'] = SubCategory.objects.get(slug=self.kwargs['slug'])
        context['order'] = self.order
        context['size'] = self.size
        context['price'] = self.price
        context['color'] = self.color
        return context

    def get_queryset(self):
        if self.color and self.size and self.price == 'lte':
            qs = Product.objects.filter(color=self.color, size=self.size, price__lte='300')\
                .order_by(self.get_ordering())
            return qs
        elif self.color and self.size and self.price == 'gte':
            qs = Product.objects.filter(color=self.color, size=self.size, price__gte='300')\
                .order_by(self.get_ordering())
            return qs
        elif self.color and self.size and self.price is None:
            qs = Product.objects.filter(color=self.color, size=self.size).order_by(self.get_ordering())
            return qs
        elif self.size and self.price == 'gte' and self.color is None:
            qs = Product.objects.filter(size=self.size, price__gte='300')\
                .order_by(self.get_ordering())
            return qs
        elif self.size and self.price == 'lte' and self.color is None:
            qs = Product.objects.filter(size=self.size, price__lte='300')\
                .order_by(self.get_ordering())
            return qs
        elif self.color and self.price == 'gte' and self.size is None:
            qs = Product.objects.filter(color=self.color, price__gte='300')\
                .order_by(self.get_ordering())
            return qs
        elif self.color and self.price == 'lte' and self.size is None:
            qs = Product.objects.filter(color=self.color, price__lte='300')\
                .order_by(self.get_ordering())
            return qs
        elif self.price == 'gte' and self.size is None and self.color is None:
            qs = Product.objects.filter(price__gte='300')\
                .order_by(self.get_ordering())
            return qs
        elif self.price == 'lte' and self.size is None and self.color is None:
            qs = Product.objects.filter(price__lte='300')\
                .order_by(self.get_ordering())
            return qs
        elif self.color and self.price is None and self.size is None:
            qs = Product.objects.filter(color=self.color)\
                .order_by(self.get_ordering())
            return qs
        elif self.size and self.price is None and self.color is None:
            qs = Product.objects.filter(size=self.size)\
                .order_by(self.get_ordering())
            return qs
        else:
            qs = Product.objects.all().order_by(self.get_ordering())
            return qs


class BaseProductDetailView(generic.DetailView):
    template_name = 'product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(BaseProductDetailView, self).get_context_data()
        context['category_product'] = self.kwargs['subcategory_slug']
        context['category'] = SubCategory.objects.get(slug=self.kwargs['subcategory_slug']).categories
        context['product_images'] = ProductImage.objects.filter(product=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return Product.objects.filter(pk=self.kwargs['pk'])




