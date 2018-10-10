from django import forms
from .models import Post, Cadastro


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', )

