from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Post


class PostListView(generic.ListView):
    model = Post


class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog: all")


class PostDetailView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog: all")


class PostDeleteView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog: all")
