from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post


def post_create(request):
    return HttpResponse('create')


def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, 'post_detail.html', context)


def post_list(request):
    queryset = Post.objects.all()
    if request.user.is_authenticated():
        context = {
            "object_list": queryset,
            "title": "My User List"
        }
    else:
        context = {
            "title": "List"
        }

    return render(request, 'index.html', context)


def post_update(request):
    return HttpResponse('update')


def post_delete(request):
    return HttpResponse('request')
