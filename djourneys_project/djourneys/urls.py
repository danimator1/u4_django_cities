from django.urls import path
from . import views

urlpatterns = [
    path('cities/', views.CityList.as_view(), name='city-list-api'),
    path('cities/<int:pk>/', views.CityDetail.as_view(), name='city-detail-api'),
    path('attractions/', views.AttractionList.as_view(), name='attraction-list-api'),
    path('attractions/<int:pk>/', views.AttractionDetail.as_view(), name='attraction-detail-api'),
    path('reviews/', views.ReviewList.as_view(), name='review-list-api'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail-api'),
]
