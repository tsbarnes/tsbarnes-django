from django.urls import path

from . import views

urlpatterns = [
  path('', views.IndexView.as_view(), name='portfolio-index'),
  path('<slug>/', views.DetailView.as_view(), name='portfolio-detail'),
]