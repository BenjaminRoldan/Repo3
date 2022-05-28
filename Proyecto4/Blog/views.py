from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from Usuarios.decorators import personal_permitido
from django.utils.decorators import method_decorator

def render_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})

@method_decorator(login_required(login_url='Login'), name='dispatch')
@method_decorator(personal_permitido(cargo_permitido=['Preceptor']), name='dispatch')
class add_post(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = '/AppZero/'

@method_decorator(login_required(login_url='Login'), name='dispatch')
@method_decorator(personal_permitido(cargo_permitido=['Preceptor']), name='dispatch')
class delete_post(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = '/AppZero/'

@method_decorator(login_required(login_url='Login'), name='dispatch')
@method_decorator(personal_permitido(cargo_permitido=['Preceptor']), name='dispatch')
class update_post(UpdateView):
    model = Post
    template_name = 'update_post.html'
    success_url = '/AppZero/'
    fields = '__all__'