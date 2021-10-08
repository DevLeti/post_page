from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request): # render 메서드를 호출, blog/post_list.html을 보여줌
    posts = Post.objects.filter(published_date__lte=timezone.now().order_by('published_date'))
    return render(request, 'blog/post_list.html', {'posts': posts})