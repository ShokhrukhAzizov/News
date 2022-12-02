from django.urls import path
from .views import *

urlpatterns = [
    path('user/panel<int:id>/', users_panel, name='user_panel'),
    path('users/news/delete/', users_news_delete, name='users_news_delete'),
    path('user/news/edit/', user_news_edit, name='user_news_edit'),
]