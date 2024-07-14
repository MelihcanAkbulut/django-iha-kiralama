from django.urls import path
from .views import register, login_view, dashboard,logoutUser

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name="dashboard"),
    path('logout/', logoutUser, name="logout"),
]