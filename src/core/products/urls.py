from django.urls import include, re_path, path
from rest_framework.routers import DefaultRouter
from . import views

#router = DefaultRouter()
#router.register('products', views.ProductApi)

#urlpatterns = [
#    re_path(r'', include(router.urls))
#]

urlpatterns = [
    path('v1/products/', views.ProductApi.as_view()),
    path('v1/products/<int:id>', views.ProductApi.as_view()),
    path('product-list', views.productList, name='products-list'),
    path('add-product', views.addnew, name='add-product'),
    path('edit-product/<int:id>', views.edit, name='edit-product'),  
    path('update-product/<int:id>', views.update, name='update-product'),  
    path('delete-product/<int:id>', views.destroy, name='delete-product'),  
]