from django.urls import path, include
from .views import (
    post_list,
    post_detail,
    post_create,
    post_edit,
    post_delete,
    comment_create,
    category_list,
    category_detail,
)

app_name = 'blog'

urlpatterns = [
    path('', post_list.as_view(), name='list'),
    path('post/<int:pk>/', post_detail.as_view(), name='detail'),
    path('post/new/', post_create.as_view(), name='create'),
    path('post/<int:pk>/edit/', post_edit.as_view(), name='edit'),
    path('post/<int:pk>/delete/', post_delete.as_view(), name='delete'),
    path('post/<int:post_id>/comment/', comment_create.as_view(), name='add_comment'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('category_list/', category_list.as_view(), name='category_list'),
    path('category_detail/<int:pk>/', category_detail.as_view(), name='category_detail'),
]
