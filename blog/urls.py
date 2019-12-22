from django.urls import path

from . import views
from . import feeds

urlpatterns = [
  path('', views.IndexView.as_view(), name='blog-index'),
  path('rss/', feeds.BlogFeed(), name='blog-rss'),
  path('<slug>/', views.DetailView.as_view(), name='blog-detail'),
]