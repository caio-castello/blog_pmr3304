from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

# List View
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Detail View
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

# Create View
def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content)
        return redirect('blog:list')
    return render(request, 'blog/post_form.html')

# Edit View
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('blog:detail', id=post.id)
    return render(request, 'blog/post_form.html', {'post': post})

# Delete View
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

