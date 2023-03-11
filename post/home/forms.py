from django import forms
from .models import Post, Comment, Profile

class PostForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'placeholder': 'その気持ち、シェアしましょう'}))
    
    class Meta:
        model = Post
        fields = ['content']
        

class CommentForm(forms.ModelForm):
    body = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'placeholder': 'コメントを入力...'}))
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.post = self.post
        comment.save()

    class Meta:
        model = Comment
        fields = ["body"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']