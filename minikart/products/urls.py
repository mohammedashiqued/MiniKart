
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('home_page',views.index,name='index'),
    path('product_list', views.list_product,name='list_product'),
    path('product_des', views.product_details,name='product_details'),
       
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)