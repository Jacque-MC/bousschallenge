from django.urls import path

from apps.files import views

urlpatterns = [
    path('', views.UploadedFilesViewset.as_view({'get': 'list'})),
    path('upload/', views.ReadFileView.as_view({'post': 'post'})),
]
