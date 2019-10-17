from django.shortcuts import render
from .models import Thought

# Create your views here.


def index(request):
    thoughts = Thought.objects.all()
    return render(request, 'thoughts/index.html', {'thoughts': thoughts})
