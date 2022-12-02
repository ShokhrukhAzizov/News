from django.urls import path
from .views import *

urlpatterns = [
    path('manage_panel/',manage_panel,name='manage_panel'),
    path('category_manage/',category_manage,name='category_manage'),
    path('category_edit',category_edit,name='category_edit_url'),
    path('category_delete',category_delete,name='category_delete_url'),
    path('category_add',category_add,name='category_add_url'),
    path('news_manage/',news_manage,name='news_manage'),
    path('news_add/',news_add,name='news_add'),
    path('news/delete/',news_delete,name='news_delete'),
    path('news/edit/',news_edit,name='news_edit'),
    path('user/list',users_list,name='user_list'),
    path('user/delete/',user_delete,name='user_delete'),
    
]