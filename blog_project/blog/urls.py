from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='list'),
    path('post/<int:id>/', views.post_detail, name='detail'),
    path('post/new/', views.post_create, name='create'),
    path('post/<int:id>/edit/', views.post_edit, name='edit'),
    path('post/<int:id>/delete/', views.post_delete, name='delete'),
]
