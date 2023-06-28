from django.urls import path

from apps.files import views

urlpatterns = [
    path('', views.UploadedFilesViewset.as_view({'get': 'list'})),
    path('upload/', views.UpFileView.as_view({'post': 'post'})),
    path('detail/<int:pk>/', views.UploadedFilesViewset.as_view({'get': 'retrieve'})),
    path('latest/', views.UploadedFilesViewset.as_view({'get': 'latest'})),
]
