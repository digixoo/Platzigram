# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Django Authentication
from django.contrib.auth import authenticate, login
from django.views.generic import DetailView

# Form
from users.forms import ProfileForm, ProfileSignup

# Model
from django.contrib.auth.models import User
from posts.models import Post

class UserDetailView(LoginRequiredMixin, DetailView):
    """User Detail View"""
    template_name='users/detail.html'
    
    slug_field= 'username'
    slug_url_kwarg='username'
    queryset=User.objects.all()
    context_object_name='user'

    def get_context_data(self, **kwargs):
        """Agrega posts de usuarios al contexto"""
        context = super().get_context_data(**kwargs)
        user= self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context



def login_view(request):
    """Login view"""
    print('login')
    
    if(request.method == 'POST'):
        print('post')
        username = request.POST['username']
        password = request.POST['password']
        print(f'{username}:{password}')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('login sucess')
            return redirect('posts:feed')
            
        else:
            print('not login, sorry ')
            return render(request, 'users/login.html', {'error': 'Usuario y/o contraseña invalido'})
    
    return render(request, 'users/login.html', {})

@login_required
def logout_view(request):
    """logout a user"""
    logout(request)
    return redirect('users:login')

def signup_view(request):
    """sign up view"""
    if request.method=='POST':
        form = ProfileSignup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = ProfileSignup()

    return render(request, 'users/signup.html', {'form': form})

@login_required
def update_profile(request):
    """actualización de los datos de perfil de ususario"""
    profile = request.user.profile

    if request.method=='POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('users:update_profile')
    else:
        form = ProfileForm()

    return render(
        request, 
        'users/update_profile.html',
        {
            'profile': request.user.profile,
            'user': request.user,
            'form': form,
        }
    )