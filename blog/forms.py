from datetime import timezone
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'discription', 'text', 'published_date', 'created_date')
    
    def save_me(request, *args, **kwargs):
        try:
            post = Post.objects.get(id=kwargs['news_id'])
            form = PostForm(request.POST, instance=post)
        except:
            form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return True
        return form
