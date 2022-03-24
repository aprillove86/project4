from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission

from .models import Memo, Tag
from django.contrib.auth import login
from .filters import MemoFilter
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import RolesForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def memos_index(request):
    memos = Memo.objects.filter(user = request.user)
    return render(request, 'memos/index.html', {'memos': memos})



class MemoList(LoginRequiredMixin, ListView):
    model = Memo
    template_name = 'memos/search.html'
    context_object_name = 'memos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MemoFilter(self.request.GET, queryset=self.get_queryset())
        return context

# def memos_detail(request, memos_id):
#     memos = Memo.objects.get(id=memos_id)

#     tag_memos_dont_have = Tag.objects.exclude(id__in = memos.tag.all().values_list('id'))

#     return render(request, 'memos/detail.html', {
#         'memos': memos,
#         'tag': tag_memos_dont_have
#     })

class MemoDetail(LoginRequiredMixin, DetailView):
    model = Memo
    template_name = 'memos/detail.html'

class MemoCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'main_app.add_memo'
    model = Memo
    fields = ('memo_title', 'memo_create_date', 'memo_text')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MemoUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'main_app.change_memo'
    model = Memo
    fields = ('memo_title', 'memo_create_date', 'memo_text')

class MemoDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'main_app.delete_memo'
    model = Memo
    success_url = '/memos/'

@login_required
def assoc_tag(request, memos_id, tag_id):
    Memo.objects.get(id=memos_id).tag.add(tag_id)
    return redirect('memos_detail', memos_id=memos_id)




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
        user_form = UserCreationForm(request.POST)
        roles_form = RolesForm(request.POST)
        # validate form inputs (make sure everything we need is there)
        if user_form.is_valid() and roles_form.is_valid:
            # save the new user to the database
            user = user_form.save()
            role = roles_form.save(commit=False)
            role.user = user
            role.save()
            # log the new user in
            login(request, user)
            # add permissions to admin user
            if user.roles.is_admin:
                user.user_permissions.add(Permission.objects.get(codename='add_memo'))
                user.user_permissions.add(Permission.objects.get(codename='change_memo'))
                user.user_permissions.add(Permission.objects.get(codename='delete_memo'))
            # redirect to the memos index page
            return redirect('memos_index')
        # if form is NOT valid
        else:
            error_message = 'invalid sign up - please try again'
            # redirect to signup page (/accounts/signup) and display error message
    # If GET request
        # render a signup page with a blank user creation form
    user_form = UserCreationForm()
    roles_form = RolesForm()  
    context = {
        'user_form': user_form,
        'error': error_message,
        'roles_form': roles_form
    }    
    return render(request, 'registration/signup.html', context)

class TagCreate(LoginRequiredMixin, CreateView):
    model = Tag
    fields = ('tag_desc',)

class TagUpdate(LoginRequiredMixin, UpdateView):
    model = Tag
    fields = ('tag_desc',)

class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    success_url = '/memos/'

class TagList(LoginRequiredMixin, ListView):
    model = Tag
    template_name = 'tags/index.html'

class TagDetail(LoginRequiredMixin, DetailView):
    model = Tag 
    template_name = 'tags/detail.html'


