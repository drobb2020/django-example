from django.shortcuts import render
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
    return render(request, 'post.html', context)
