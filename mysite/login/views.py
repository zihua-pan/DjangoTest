from django.shortcuts import render
from .models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def homepage(request):
    context = {}
    context['start'] = "登录"
    if 'username' and 'password' in request.GET:
        username = request.GET['username']
        password = request.GET['password']
        if password == User.objects.get(username=username).password:
                context['username'] = request.GET['username']
                return render(request, 'login/results.html', context)
        else:
                context['wrong'] = "密码错误"
    elif 'username' in request.GET:
        context['wrong'] = "请输入密码"
    else:
        context['wrong'] = "请输入账号"
    return render(request, 'login/homepage.html', context)


def regist(request):
    context = {}
    context['start'] = "注册"
    if 'username' and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            username == User.objects.get(username=username).username
        except User.DoesNotExist:
            context['username'] = username
            new_user = User(username=username, password=password)
            new_user.save()
            return render(request, 'login/results.html', context)
        else:
            context['wrong'] = "账号已存在"
    elif 'username' in request.POST:
        context['wrong'] = "请输入密码"
    else:
        context['wrong'] = "请输入要注册的账号"
    return render(request, 'login/regist.html', context)


def results(request):
    return render(request, 'login/results')
