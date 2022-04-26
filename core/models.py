from django.db import models
from .common import slugify


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField('Description')
    price = models.DecimalField('Price',max_digits=6, decimal_places=2)
    is_new = models.BooleanField(default=False)
    is_verified_by_admin = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    sub_category = models.ForeignKey('SubCategory', on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    sub_sub_category = models.ForeignKey('SubSubCategory', on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Mehsul'
        verbose_name_plural = 'Mehsullar'


class Image(models.Model):
    image = models.ImageField('Image',upload_to='images/', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True, related_name='images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Shekil'
        verbose_name_plural = 'Shekiller'

    def __str__(self):
        return self.product.title


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    icon = models.ImageField('Image',upload_to='icons/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'
        ordering = ['title']


class SubCategory(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Alt kateqoriya"
        verbose_name_plural = "Alt kateqoriyalar"
        ordering = ['title']

    def save(self, *args, **kwargs):
        super(SubCategory, self).save(*args, **kwargs)
        self.slug = slugify(self.title)
        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class SubSubCategory(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='sub_sub_categories', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Alt Alt kateqoriya"
        verbose_name_plural = "Alt Alt kateqoriyalar"
        ordering = ['title']

    def save(self, *args, **kwargs):
        super(SubSubCategory, self).save(*args, **kwargs)
        self.slug = slugify(self.title)
        super(SubSubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.title