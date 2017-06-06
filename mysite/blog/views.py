from django.shortcuts import render
from django.models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView, CreateView,UpdateView, DeleteView)
# Create your views here.

# The view of the "about" page
class AboutView(TemplateView):
    template_name = 'about.html'

# The view of the "post list" page
class PostListView(ListView):
    model = Post

    # Get the query list of Post lists with descending order.
    def get_queryset(self):
        return Post.objects.filter(published_date__lte = timezome.now()).order_by('-published_date')

# the view of detail
class PostDetailView(DetailView):
    model = Post

# the view of Create a post
class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

# the view of updating a view
class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

# the view of deleting a posts
class PostDeleteView(LoginRequiredMixin, DetailView):
    model = Post
    success_url = reverse_lazy('post_list')

# the view of drafts (unposted posts)
class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by('created_date')
