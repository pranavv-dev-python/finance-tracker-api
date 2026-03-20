from django.urls import path
from rest_framework.permissions import AllowAny
from .views import profile , Registeruser
from rest_framework_simplejwt.views import(
    TokenObtainPairView ,
    TokenRefreshView ,
)

urlpatterns = [
    path("resgister/" , Registeruser.as_view()) ,
    path("profile/" , profile.as_view()) ,
    path("login/" , TokenObtainPairView.as_view() ) ,
    path("token/refresh/" , TokenRefreshView.as_view() ) ,
]

