from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
# получается здесь использовали словарь для posts, чтобы иметь возможность
# обращения к нему по ключу 'posts'(а не по индексу, как это было бы для списка)
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
