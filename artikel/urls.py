from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from .views import (
    ArticleListView, 
    ArticleDetailView, 
    ArticleKategoriListView,
    # ArticleCreateView,
    ArticleManageView,
    ArticleDetailView,
    ArticleDeleteView,
    # ArticleUpdateView,
    )
app_name = 'blog'
urlpatterns = [
    # path('manage/update/<int:pk>',ArticleUpdateView.as_view(), name='update'),
    path('manage/delete/<int:pk>',ArticleDeleteView.as_view(), name='delete'),
    path('manage',ArticleManageView.as_view(), name='manage'),
    # path('create',ArticleCreateView.as_view(), name='create'),
    path('kategori/<str:kategori>/<int:page>', ArticleKategoriListView.as_view(), name='category'),
    path('detail/<slug:slug>', ArticleDetailView.as_view(), name='detail'),
    path('', ArticleListView.as_view(), name='list'),
    path('<int:page>', ArticleListView.as_view(), name='list'),

]