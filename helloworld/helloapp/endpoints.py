from django.conf.urls import include, url
from rest_framework import routers
from .views import ProductViewset, FoodViewset

router = routers.DefaultRouter()
router.register('products', ProductViewset)
router.register('food', FoodViewset)

urlpatterns = [
    url("^", include(router.urls)),
]