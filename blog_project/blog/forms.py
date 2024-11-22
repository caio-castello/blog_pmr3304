from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
            queryset=Category.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=False,
            label="Categorias",
        )

    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']
        labels = {
            'title': 'Título',
            'content': 'Conteúdo',
            'categories': 'Categorias',
        }
