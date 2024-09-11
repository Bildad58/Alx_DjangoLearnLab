from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
    return render(request, 'registration/profile.html')


