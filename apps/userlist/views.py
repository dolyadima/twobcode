from django.shortcuts import render
from apps.authentication.models import User


def users(request):
    return render(request, 'userlist/users.html', {
        'title': 'User List',
        'page_active': 'users',
        'users': User.objects.all().order_by("id"),
        'user': request.user,
    })


def user_detail(request, pk):
    user_d = User.objects.filter(id=pk).first()
    id_not_found = True if user_d is None else False
    return render(request, 'userlist/user_detail.html', {
        'title': 'User Detail',
        'page_active': 'users',
        'id_not_found': id_not_found,
        'pk': pk,
        'user_d': user_d,
        'user': request.user,
    })
