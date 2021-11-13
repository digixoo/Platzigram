"""Posts views."""

# Django
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Model
from posts.models import Post

# Form
from posts.forms import PostForm

# Utilities
from datetime import datetime


posts2 = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

@login_required
def list_posts(request):
    """List existing posts."""
    db_posts = list(Post.objects.all())
    posts = []
    for post in db_posts:
        temp = {
            'title': post.title,
            'user': {
                'username': post.user.username,
                'name': f'{post.user.first_name} {post.user.last_name}',
                'picture': post.user.profile.picture.url
            },
            'timestamp': post.created.strftime('%b %dth, %Y - %H:%M hrs'),
            'photo': post.photo.url,
        }
        posts.append(temp)
    print(posts)
    return render(request, 'posts/feed.html', {'posts': posts})

@login_required
def create_post(request):
    """Create new post view"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()

    return render(
        request=request, 
        template_name='posts/new.html', 
        context={
            'form':form, 
            'user': request.user, 
            'profile': request.user.profile,
            }
        )
    