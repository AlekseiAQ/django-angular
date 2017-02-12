from django.http import HttpResponse
from django.shortcuts import render


def post_create(request):
    return HttpResponse('create')


def post_detail(request):
    context = {
        "title": "Detail"
    }
    return render(request, 'index.html', context)


def post_list(request):
    if request.user.is_authenticated():
        context = {
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
