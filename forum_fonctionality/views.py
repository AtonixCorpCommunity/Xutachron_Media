from django.shortcuts import render, get_object_or_404
from .models import Category, Thread, Post

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'news/category_list.html', {'categories': categories})

def thread_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    threads = Thread.objects.filter(category=category)
    return render(request, 'news/thread_list.html', {'category': category, 'threads': threads})

def post_list(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    posts = Post.objects.filter(thread=thread)
    return render(request, 'news/post_list.html', {'thread': thread, 'posts': posts})

def post_detail(request, thread_id, post_id):
    post = get_object_or_404(Post, thread_id=thread_id, id=post_id)
    return render(request, 'news/post_detail.html', {'post': post})
