from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.views import ProductDocumentViewSet

router = DefaultRouter()
router.register('products', ProductDocumentViewSet, 'products')

urlpatterns = [
    path('', include(router.urls)),
]
