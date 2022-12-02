from django.shortcuts import redirect, render
from main.models import Category,News,User
from .decorator import staff_required

@staff_required
def manage_panel(request):
    categorys = Category.objects.all().count()
    news = News.objects.filter(is_active=True).count()
    news_inactive = News.objects.filter(is_active=False).count()
    users = User.objects.all().count()
    admin = request.user
    context = {
        'categorys':categorys,
        'news':news,
        'news_inactive':news_inactive,
        'users':users,
        'admin':admin
    }

    return render(request,'dashboard/dash_index.html',context)

@staff_required
def category_manage(request):
    category = Category.objects.all().count()
    categorys = Category.objects.all()
    admin = request.user
    context = {
        'category':category,
        'categorys':categorys,
        'admin':admin
    }

    return render(request,'dashboard/dash_category.html',context)

@staff_required
def category_add(request):
    name = request.POST['name']
    Category.objects.create(
        title=name,
        slug=name
    )
    return redirect('category_manage')

@staff_required
def category_edit(request):
    name = request.POST['name']
    id = request.POST['id']
    category = Category.objects.get(id=id)
    category.title=name
    category.save()
    return redirect('category_manage')

@staff_required
def category_delete(request):
    id = request.POST['id']
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('category_manage')

@staff_required
def news_manage(request):
    categorys = Category.objects.all()
    news = News.objects.all().count()
    newses = News.objects.all
    user = User.objects.all()
    admin = request.user

    context = {
        'categorys':categorys,
        'news':news,
        'newses':newses,
        'user':user,
        'admin':admin
    }
    return render(request,'dashboard/dash_news.html',context)
    
@staff_required
def news_add(request):
    name = request.POST['theme']
    body = request.POST['body']
    image = request.POST['image']
    categoriya_select = request.POST['categoriya']
    user_select = request.POST['user_list']
    category = Category.objects.get(id=categoriya_select)
    user = User.objects.get(id=user_select)
    News.objects.create(
        title=name,
        body=body,
        image=image,
        category=category,
        slug=name,
        author=user
    )
    return redirect('news_manage')

@staff_required
def news_delete(request):
    id = request.POST['id']
    news = News.objects.get(id=id)
    news.delete()
    return redirect('news_manage')

@staff_required
def news_edit(request):
    name = request.POST['nom']
    body = request.POST['yangilik']
    image = request.FILES.get('rasm')
    id = request.POST['id']
    categoriya_select = request.POST['categoriya']
    news = News.objects.get(id=id)
    category = Category.objects.get(id=categoriya_select)
    news.title=name
    news.body=body
    news.image=image
    news.category=category
    
    if image is not None:
        news.image = image
    news.save()

    return redirect('news_manage')

@staff_required
def users_list(request):
    my_dict = {}
    for user in User.objects.all():
        news_quantity = News.objects.filter(author=user).count()
        my_dict[user] = news_quantity
    user_count = User.objects.all().count()
    admin = request.user
    context = {
        'user_count':user_count,
        'my_dict':my_dict,
        'admin':admin
    }
    return render(request, 'dashboard/user_list.html',context)



@staff_required
def user_delete(request):
    id = request.POST['id']
    user = User.objects.get(id=id)
    user.delete()
    return redirect('user_list')

  