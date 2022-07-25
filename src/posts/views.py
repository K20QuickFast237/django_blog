from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from posts.models import BlogPost


# Create your views here.


class BlogHome(ListView):
    model = BlogPost   # Pour afficher tous les articles
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter(published=True)

@method_decorator(login_required, name='dispatch')
class BlogPostCreate(CreateView):
    model = BlogPost 
    fields = ['title', 'content']
    template_name = 'posts/blogpost_create.html'
    context_object_name = 'form'


@method_decorator(login_required, name='dispatch')
class BlogPostUpdate(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'published',]
    template_name = 'posts/blogpost_edit.html'


class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = 'post'


@method_decorator(login_required, name='dispatch')
class BlogpostDelete(DeleteView):
    model = BlogPost
    context_object_name = 'post'
    success_url = reverse_lazy('posts:home')