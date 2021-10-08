from django.shortcuts import render

# Create your views here.
def post_list(request): # render 메서드를 호출, blog/post_list.html을 보여줌
    return render(request, 'blog/post_list.html', {})