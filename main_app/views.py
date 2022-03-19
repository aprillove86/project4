from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .models import Memo
from django.contrib.auth import login
from .filters import MemoFilter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class MemoList(ListView):
    model = Memo
    template_name = 'memos/index.html'
    context_object_name = 'memos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MemoFilter(self.request.GET, queryset=self.get_queryset())
        return context

class MemoDetail(DetailView):
    model = Memo
    template_name = 'memos/detail.html'

class MemoCreate(CreateView):
    model = Memo
    fields = ('title', 'date')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MemoUpdate(UpdateView):
    model = Memo
    fields = ('title', 'date')

class MemoDelete(DeleteView):
    model = Memo
    success_url = '/memos/'





"""
def posts_index(request):
    posts = Post.objects.filter(user = request.user)
    return render(request, 'posts/index.html', {'posts' : posts})

def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/detail.html',{'post': post})
"""


def signup(request):
    # we'll need this for our context dictionary, in case there are no errors
    error_message = ''
    # check for a POST request (as opposed to a GET request)
    if request.method == 'POST':
        # capture form inputs
        form = UserCreationForm(request.POST)
        # validate form inputs (make sure everything we need is there)
        if form.is_valid():
            # save the new user to the database
            user = form.save()
            # log the new user in
            login(request, user)
            # redirect to the memos index page
            return redirect('memos_index')
        # if form is NOT valid
        else:
            error_message = 'invalid sign up - please try again'
            # redirect to signup page (/accounts/signup) and display error message
    # If GET request
        # render a signup page with a blank user creation form
    form = UserCreationForm()  
    context = {
        'form': form,
        'error': error_message
    }    
    return render(request, 'registration/signup.html', context)

"""
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

