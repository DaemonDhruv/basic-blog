from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.
def index(request):
    #return HttpResponse('Hello From Posts :)')
    posts = Posts.objects.all()[:10]
    context = {
        'title': 'Latest posts',
        'posts': posts
    }
    return render(request, 'posts/index.html', context)

def details(request, id):
    posts = Posts.objects.get(id=id)
    context = {
        'post': posts
    }
    return render(request, 'posts/details.html', context)
