from django.urls import path
from .views import ArticlesListView,ArticlesUpdateView,ArticlesDetailView,ArticlesDeleteView,ArticlesCreateView
urlpatterns = [
path('', ArticlesListView.as_view(), name='article_list'),
path('<int:pk>/edit',ArticlesUpdateView.as_view(),name='article_edit'),
path('<int:pk>/delete',ArticlesDeleteView.as_view(),name='article_delete'),
path('new/',ArticlesCreateView.as_view(),name='article_new'),
path('<int:pk>/',ArticlesDetailView.as_view(),name='article_detail'),


]