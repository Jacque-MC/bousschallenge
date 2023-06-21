from django.urls import path
from apps.entries import views

urlpatterns = [
    path('', views.FileEntryView.as_view({'get': 'list'})),
    path('detail/<int:pk>/', views.FileEntryView.as_view({'get': 'retrieve'})),
]
