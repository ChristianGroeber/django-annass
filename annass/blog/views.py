from django.shortcuts import render
from .models import BlogEntry

# Create your views here.


def index(request):
    blogentries = BlogEntry.objects.all()
    return render(request, 'blog/index.html', {'blogentries': blogentries})
