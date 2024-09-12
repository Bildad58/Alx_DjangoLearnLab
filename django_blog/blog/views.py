from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form.email = request.POST.get('email')

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile.html')         
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})
 #redirect('profile.html')

def login_view(request):
    return render(request, 'blog/login.html')
# redirect('profile.html')

def logout_view(request):
    return redirect(request,'blog/login.html')   

def profile_view(request):  
    return render(request, 'blog/profile.html')


@login_required
def profile(request):
    if request.method == 'POST':
        # Handle profile update
        user = request.user
        user.email = request.POST.get('email')
        user.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('profile')
    return render(request, 'blog/profile.html')




class PostListView(ListView):
    model = Post
    template_name ='blog/post_list.html'
    context_object_name= 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'posts'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name= 'blog/form.html'
    # form_class = PostForm
    fields = ['title', 'content']
     

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/form.html'
    # form_class = PostForm
    fields = ['title', 'content']
    success_url= reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
       
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post-list')

    def delete_post(request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('post_list')