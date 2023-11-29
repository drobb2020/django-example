from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
)

from .forms import PostCreateForm, PostUpdateForm
from .models import Author, Post


def index(request):
    context = {}
    return render(request, 'index.html', context)


def blog(request):
    posts = Post.objects.all().order_by('-date')
    context = {'posts': posts}
    return render(request, 'blog.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)


def faq(request):
    context = {}
    return render(request, 'faq.html', context)


def profile(request):
    author = Author.objects.all().first()
    context = {'author': author}
    return render(request, 'profile.html', context)


def post(request, id):
    post = Post.objects.get(id=id)
    context = {'post': post}
    return render(request, 'core/post_single.html', context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "core/post_create.html"
    form_class = PostCreateForm


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "core/post_update.html"
    form_class = PostUpdateForm


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog")
