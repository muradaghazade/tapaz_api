from rest_framework import serializers
from .models import *
from drf_extra_fields.fields import Base64ImageField
from drf_writable_nested.serializers import WritableNestedModelSerializer


class ImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    class Meta:
        model = Image
        fields = ('id', 'image', 'created_at', 'updated_at' )


class ProductSerializer(WritableNestedModelSerializer):
    images = ImageSerializer(many=True, required=False)
    
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'images', 'is_new', 'is_verified_by_admin', 'category', 'sub_category', 'sub_sub_category', 'created_at', 'updated_at')


class SubSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSubCategory
        fields = ('id', 'title', 'icon', 'created_at', 'updated_at')


class SubCategorySerializer(serializers.ModelSerializer):
    sub_sub_categories = SubSubCategorySerializer(many=True, required=False)
    class Meta:
        model = SubCategory
        fields = ('id', 'title', 'icon', 'created_at', 'updated_at', 'sub_sub_categories')


class CategorySerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True, required=False)
    class Meta:
        model = Category
        fields = ('id', 'title', 'icon', 'created_at', 'updated_at', 'sub_categories', 'category_reklam')