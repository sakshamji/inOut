from django.urls import path
from . import views

urlpatterns = [
    # path('register/', UserRegisterView.as_view(), name = 'register'),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),
]