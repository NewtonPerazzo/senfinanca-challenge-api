from django.contrib import admin
from django.urls import include, path
from django.urls import path, include
from rest_framework import routers
from viewsets.viewset import TransactionViewSet
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='SenFinança API')

router = routers.DefaultRouter()
router.register(r'transactions', TransactionViewSet, basename='Transactions')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', schema_view)
]
