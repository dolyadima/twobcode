from django.shortcuts import render
from apps.authentication.models import User


def users(request):
    return render(request, 'userlist/users.html', {
        'title': 'User List',
        'page_active': 'users',
        'users': User.objects.all().order_by("id"),
        'req_user': request.user,
    })


def user_detail(request, pk):
    user_detail = User.objects.filter(id=pk).first()
    id_not_found = True if user_detail is None else False
    return render(request, 'userlist/user_detail.html', {
        'title': 'User Detail',
        'page_active': 'users',
        'id_not_found': id_not_found,
        'pk': pk,
        'user_detail': user_detail,
        'req_user': request.user,
    })


def user_delete(request, pk):
    user_delete = User.objects.filter(id=pk).first()
    id_not_found = True if user_delete is None else False
    if not id_not_found:
        user_delete.delete()
    return render(request, 'userlist/user_delete.html', {
        'title': 'User Delete',
        'page_active': 'users',
        'id_not_found': id_not_found,
        'pk': pk,
        'user_delete': user_delete,
        'req_user': request.user,
    })
