from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, JsonResponse
from .models import *
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    keyboard = request.POST.get("keyboard")
    if keyboard:
        articles = Article.objects.filter(title__icontains=keyboard)
    else:
        articles = Article.objects.all()
    return render(request, "index.html", locals())


def about(request):
    return render_to_response("about.html")


def listpic(request):
    return render_to_response("listpic.html")


def newslistpic(request):
    t = request.GET.get("type")
    if t:
        ty = type.objects.filter(name=t).first()
        authors = ty.author_set.all()
        articles = Article.objects.none()
        for a in authors:
            articles1 = a.article_set.all()
            articles = articles | articles1
    else:
        articles = Article.objects.all()

    paginator_obj = Paginator(articles, 6)
    id = request.GET.get("id")

    page_obj = paginator_obj.get_page(id)

    return render_to_response("newslistpic.html", locals())


def test(request):
    return HttpResponse("hello world")


def add(request):
    for i in range(1, 100):
        article = Article()
        article.title = "title" + str(i)
        article.author_id = 1
        article.content = "content%s" % i
        article.description = "description%s" % i
        article.save()

    return HttpResponse("add")


def article(request):
    id = request.GET.get("id")

    ar = Article.objects.filter(id=id).first()
    ar.click = ar.click + 1
    ar.save()
    return render(request, "article.html", locals())


def register(request):
    msg = ""
    if request.method == "POST":
        name = request.POST.get("form-username")
        pwd = request.POST.get("form-password")
        if name != "":
            user = User()
            user.username = name
            user.password = pwd
            if not User.objects.filter(username=name).exists():
                user.save()
                msg = "注册成功"
            else:
                msg = "用户名已存在"
        else:
            msg = "用户名不能为空"

    return render(request, "register.html", locals())


def register_ajax(request):
    return render(request, "register_ajax.html")


def ajax_get(request):
    username = request.GET.get("username")
    print(username)
    res = {"code": 10000, "msg": ""}
    if username == "":
        res = {"code": 10001, "msg": "用户名不能为空"}
    elif User.objects.filter(username=username).exists():
        res = {"code": 10002, "msg": "用户名已存在"}
    else:
        res = {"code": 10000, "msg": "ok"}
    return JsonResponse(res)


def ajax_post(request):
    res = {"code": 10000, "msg": ""}
    username = request.POST.get("username")
    pwd = request.POST.get("pwd")
    try:
        User.objects.create(username=username, password=pwd)
        res = {"code": 10000, "msg": "注册成功"}
    except:
        res = {"code": 10000, "msg": "注册失败"}
    return JsonResponse(res)


def authors(request):
    id = request.GET.get("id")
    a = author.objects.filter(id=id).first()

    return render(request, "author.html", locals())
