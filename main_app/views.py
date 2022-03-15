"""
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



def about(request):
    return render(request, 'about.html') 

def home(request):
    return render(request)

def posts_index(request):
    posts = Post.objects.filter(user = request.user)
    return render(request, 'posts/index.html', {'posts' : posts})

def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/detail.html',{'post': post})

def signup(request):
    error_message = ''
    if request.method "Post":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'invalid sign-up, please try again'
    form = UserCreationForm()
    context = { 'form': form, 'error_message': error_message }
    return render(request, 'registration/signup.html', context)

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('')

class PostDelete(DeleteView):
    model = Post
    success_url = '/posts'

# Create your views here.
"""
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello')

