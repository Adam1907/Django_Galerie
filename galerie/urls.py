from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('paintings/', views.PaintingListView.as_view(), name='paintings'),
    path('paintings/<int:pk>/', views.PaintingDetailView.as_view(), name='painting_detail'),
]