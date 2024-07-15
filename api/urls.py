from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import SimpleRouter

app_name = "api"
urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('list/', CarList.as_view(), name="car_list"),
]

router = SimpleRouter()
router.register("", CarViewSet, basename="car")
urlpatterns += router.urls