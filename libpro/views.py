from libpro.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# def home(request):
#     return render(request, 'home.html', {})



class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class PostDetailsView(DetailView):
    model = Post
    template_name = 'post_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
