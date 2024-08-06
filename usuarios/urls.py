from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views  
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path(
        "usuarios/",
        views.UsuarioListCreateView.as_view(),
        name='usuario-list-create' 
    ),
     path(
        'usuarios/<int:pk>/', 
        views.UsuarioRetrieveUpdateDestroyView.as_view(),
         name='usuario-retrieve-update-destroy'
         ),
    path(
        "login/",
        TokenObtainPairView.as_view(),
        name='token_obtain_pair' 
    ),
    path(
        "login/refresh/",
        TokenRefreshView.as_view(),
        name='token_refresh' 
    ),
]

