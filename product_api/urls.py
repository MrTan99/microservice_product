from django.urls import path, include


from rest_framework import routers
from django.conf.urls import url, include
from product_api.views import ProductAccessView, ProductAccessView1, ProductAccessView2

router = routers.DefaultRouter()
urlpatterns = [
	path("", include(router.urls)),
	path('product-list/', ProductAccessView.as_view()),
	path('product-search/<str:pk>/', ProductAccessView1.as_view()),
	path('product-detail/<str:pk>/', ProductAccessView2.as_view()),
	path('product-create/', ProductAccessView.as_view()),
	path('product-update/<str:pk>/', ProductAccessView.as_view()),
	path('product-delete/<str:pk>/', ProductAccessView.as_view()),
]