from django.shortcuts import redirect, render
from main.models import *

def users_panel(request,id):
    user = User.objects.get(id=id)
    news = News.objects.filter(author=request.user).count()
    newses = News.objects.filter(author=request.user)
    category = Category.objects.all()   
    
    context = {
        'news':news,
        'user':user,
        'newses':newses,
        'category':category
    }

    return render(request,'users_dashboard/user_panel.html',context)

def users_news_delete(request):
    id = request.POST['id']
    news = News.objects.get(id=id)
    news.delete()
    return redirect('user_panel',news.author.id)

def user_news_edit(request):
    name = request.POST['name']
    body = request.POST['body']
    image = request.POST['load']
    id = request.POST['id']
    category_select = request.POST['categoriya']
    category = Category.objects.get(id=category_select)
    news = News.objects.get(id=id)
    news.title=name
    news.body=body
    news.image=image
    news.category=category
    news.save()
    
    return redirect('user_panel',news.author.id)