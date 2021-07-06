from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.base import View
from .models import Post
from .forms import PostForm

from fishing.getinfo import siteinfo, getuserinfo



class NewsDetails(View):
    template = 'blog/detail.html'
    def get(self, *args, **kwargs):
        news = get_object_or_404(Post, pk=kwargs['news_id'])
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'news': news})


class NewsNew(View):
    template = 'blog/edit.html'
    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, *args, **kwargs):
        result = PostForm.save_me(self.request)
        if result:
            return redirect('fishing:index')
        else:
            return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'form': result})
    
    def get(self, *args, **kwargs):
        form = PostForm()
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'form': form})


class NewsEdit(View):

    template = 'blog/edit.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        news = get_object_or_404(Post, pk=kwargs['news_id'])
        if news.author == self.request.user:
            result = PostForm.save_me(self.request, news_id=kwargs['news_id'])
            if result:
                return redirect('fishing:index')
            else:
                return render(self.request,
                              self.template,
                              {'fisherman': getuserinfo(self.request),
                               'siteinfo': siteinfo(),
                               'old': True,
                               'news_id': kwargs['news_id'],
                               'form': result})
        return redirect('fishing:index')

    def get(self, *args, **kwargs):
        news = get_object_or_404(Post, pk=kwargs['news_id'])
        form = PostForm(instance=news)
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'old': True,
                       'news_id': kwargs['news_id'],
                       'form': form})

class NewsDelete(View):
    
    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        news = get_object_or_404(Post, pk=kwargs['news_id'])
        if news.author == self.request.user:
            news.delete()
        return redirect('fishing:index')