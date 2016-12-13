# coding=utf-8

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

    def __unicode__(self):
        return u'Категория: %s' % self.name

    def get_absolute_url(self):
        return reverse('shop:product_category', kwargs={'slug': self.slug})


class SubCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    categories = models.ForeignKey(Category, related_name='subcategory')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = u'Под Категория'
        verbose_name_plural = u'Под Категории'

    def __unicode__(self):
        return u'Категория: %s' % self.name

    def get_absolute_url(self):
        return reverse('shop:product_subcategory', kwargs={'slug': self.slug, 'category_slug': self.categories.slug})


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', verbose_name=u'Категория')
    subcategory = models.ForeignKey(SubCategory, related_name='product', verbose_name=u'Подкатегория', blank=True,
                                    default='')
    name = models.CharField(max_length=200, db_index=True, verbose_name=u'Название')
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True, verbose_name=u'Изображения товара')
    description = models.TextField(blank=True, verbose_name=u'Описание товара')
    color = models.CharField(max_length=40, verbose_name=u'Цвет', blank=True, default='')
    size = models.CharField(max_length=10, verbose_name=u'Размер', blank=True, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'Цена товара')
    stock = models.PositiveIntegerField(verbose_name=u'На складе')
    available = models.BooleanField(default=True, verbose_name=u'Доступен')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __unicode__(self):
        return u'Товар: %s' % self.name

    def get_absolute_url(self):
        return reverse('shop:product_items', kwargs={'slug': self.slug, 'pk': self.pk,
                                                     'subcategory_slug': self.subcategory.slug})


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True, verbose_name=u'Изображения товара')
    product = models.ForeignKey(Product, related_name='product', verbose_name=u'Название продукта')

    def __unicode__(self):
        return self.product.name