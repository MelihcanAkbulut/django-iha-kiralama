from django.urls import include, re_path, path
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('rent/', views.RentApi.as_view()),
    path('rent/<int:id>', views.RentApi.as_view()),
    path('add-rent', views.addRent, name='add-rent'),
    path('rent-list', views.rentList,name='rent-list'),
    path('edit-rent/<int:id>', views.edit, name='edit-rent'),  
    path('update-rent/<int:id>', views.update, name='update-rent'),  
    path('delete-rent/<int:id>', views.destroy, name='delete-rent'),  
]