from django.conf.urls import include, url
from rest_framework import routers
from .views import ProductViewset

router = routers.DefaultRouter()
router.register('products', ProductViewset)

urlpatterns = [
    url("^", include(router.urls)),
]