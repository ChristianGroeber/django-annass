from django.shortcuts import render
from .models import BlogEntry

# Create your views here.


def index(request):
    blogentries = BlogEntry.objects.filter(active=True)
    return render(request, 'blog/index.html', {'blogentries': blogentries})


def view_post(request, post_id):
    post = BlogEntry.objects.get(pk=post_id, active=True)
    return render(request, 'blog/post.html', {'post': post})
