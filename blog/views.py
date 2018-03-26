from audioop import reverse

from django.shortcuts import render, redirect
from .models import Post, About, Comment, Tag
from datetime import datetime
from django.utils import timezone
from .forms import CommentForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=datetime.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_content(request, **kwargs):
    post = Post.objects.get(id=kwargs['post_id'])
    tegs = Tag.objects.filter(post=post.id)
    comments = Comment.objects.filter(post_id=post.id)
    return render(request, 'blog/post_content.html', {'post':post, 'comments':comments,'tegs':tegs})

def about(request):
    about = About.objects.first()
    return render(request, 'blog/about.html', {'about':about})

def commet(request, **kwargs):
    form = CommentForm
    comment = Comment.objects.all()
    if(request.method== 'POST'):
        name = request.POST['name']
        text = request.POST['text']
        comment_date = timezone.now()
        post_id = kwargs.get('post_id')
        ekle = Comment(name=name, text=text, comment_date=comment_date, post_id=post_id)
        ekle.save()

    return redirect(request.META.get('HTTP_REFERER', '/'))
def tag(request, **kwargs):
    post = Post.objects.filter(tags__id=kwargs.get('tags_id'))
    return render(request, 'blog/post_list.html', {'posts':post})