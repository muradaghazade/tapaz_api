from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .viewsets import *

app_name = "core"

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('categories', CategoryViewSet, basename='category')
router.register('sub-categories', SubCategoryViewSet, basename='sub-category')
router.register('sub-sub-categories', SubSubCategoryViewSet, basename='sub-sub-category')


urlpatterns = [
    path('', include(router.urls)),
    # path('subsubcategory-by-title/', SubSubCategoryTitleAPIView.as_view(), name='subsubcategory-by-title'),
]