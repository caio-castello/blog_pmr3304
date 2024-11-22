from django.urls import path
from .views import (
    post_list,
    post_detail,
    post_create,
    post_edit,
    post_delete,
)

app_name = 'blog'

urlpatterns = [
    path('', post_list.as_view(), name='list'),
    path('post/<int:pk>/', post_detail.as_view(), name='detail'),
    path('post/new/', post_create.as_view(), name='create'),
    path('post/<int:pk>/edit/', post_edit.as_view(), name='edit'),
    path('post/<int:pk>/delete/', post_delete.as_view(), name='delete'),
]
