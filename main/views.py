from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from time import gmtime, strftime


def PagenatorPage(List, num, request):
    paginator = Paginator(List, num)
    pages = request.GET.get('page')
    try:
        list = paginator.page(pages)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list


def index_page(request):
    showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    categorys = Category.objects.all()
    top_news = News.objects.all()[:3]
    top_news_id = []
    for i in top_news:
        top_news_id.append(i.id)
    news = News.objects.exclude(id__in=top_news_id)

    query = request.GET.get('name')
    if query is not None and query != '':
        news = News.objects.filter(Q(title__icontains=query))
    context = {
        'showtime':showtime,
        'categorys':categorys,
        'top_news':top_news,
        'news':PagenatorPage(news, 3, request)
    }
    return render(request,'index.html',context)

def news_page(request,slug):
    showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    categoryia = Category.objects.all()
    category = Category.objects.get(slug=slug)
    news = News.objects.filter(category=category)
    
    context = {
        'category':category,
        'news':news,
        'categoryia':categoryia,
        'showtime':showtime
    }
    return render(request,'news.html',context)

def news_detail(request,slug):
    user = request.user
    new_get = News.objects.get(slug=slug)
    like = Like.objects.filter(news=new_get).count()
    # try:
    #     views = Views.objects.get(news=new_get)
    #     views.quantity +=1
    #     views.save()
    # except:
    #     views = Views.objects.create(
    #         news=new_get,
    #         quantity=1
    #     ) 
    #     views = views.count()
    context = {
        'new_get':new_get,
        'like':like,
        'user':user
        # 'views':views
    }
    return render(request,'news_detail.html',context)


def register_page(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        raqam = request.POST['raqam']
        parol = request.POST['parol']
        parol2 = request.POST['parol2']
        if parol == parol2:
            try:
                User.objects.create_user(
                    username=username,
                    email=email,
                    phone=raqam,
                    password=parol
                )
                messages.success(request,"Ro'yaxtdan o'tdingiz")
                return redirect('log_in_url')
            except:
                messages.error(request,'Bunday foydalanuvchi bor')
                return redirect('register_url')
        else:
            messages.error(request,'Parol bir xil emas')
    return render(request,'registration.html')

def login_page(request):
    if request.method=='POST':
        try:
            username = request.POST['name']
            password = request.POST['parol']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('index_url')
        except:
            messages.error(request,"Username yoki parol no'tog'ri terilgan")
            return redirect('log_in_url')
    return render(request,'login.html')

def log_out_page(request):
    logout(request)
    return redirect('index_url')


@login_required
def create_news(request):
    category = Category.objects.all()
    user = request.user
    if request.method == 'POST':
        title = request.POST['name']
        body = request.POST['news']
        image = request.FILES['load']
        category_id = request.POST['category']
        category_post = Category.objects.get(id=category_id)
        News.objects.create(
            author=user,
            title=title,
            category=category_post,
            body=body,
            image=image,
            slug=title

        )
        messages.success(request, 'Muoffaqiyatli amalga oshirildi')
    context = {
        'category':category,
        'user':user,
       
    }
    return render(request,'create_news.html',context)

@login_required
def like_view(request):
    news_id = request.POST['news_id']
    news = News.objects.get(id=news_id)
    try:
        Like.objects.get(user=request.user, news=news)
    except:
        Like.objects.create(
            user = request.user,
            news = news
        )
    return redirect('news_detail_url', news.slug)