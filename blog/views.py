from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Category
from .forms import PostForm

class post_list(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class post_detail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class post_create(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:list')

class post_edit(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:list')

class post_delete(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:list')

class comment_create(CreateView):
    model = Comment
    fields = ['text']
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, id=post_id)
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        post_id = self.kwargs['post_id']
        return reverse('blog:detail', kwargs={'pk': post_id})

class category_list(ListView):
    model = Category
    template_name = 'blog/category_list.html'
    context_object_name = 'categories'

class category_detail(DetailView):
    model = Category
    template_name = 'blog/category_detail.html'
    context_object_name = 'category'

    def get_queryset(self):
        """
        Garante que a categoria será carregada com seus posts.
        """
        return Category.objects.prefetch_related('posts').all()
