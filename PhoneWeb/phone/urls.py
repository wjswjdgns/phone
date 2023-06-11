from django.urls import path
from . import views

urlpatterns = [
    path('smartphone', views.device, name="device"),
    path('hotdeal', views.hotdeal, name="hotdeal"),
    path('advance', views.advance, name="advance"),
    path('information', views.information, name="information"),
]
