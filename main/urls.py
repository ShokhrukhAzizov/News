from .views import *
from django.urls import path

urlpatterns= [
    path('',index_page,name='index_url'),
    path('news/page/<slug:slug>/',news_page,name='news_page_url'),
    path('news/detail/<slug:slug>/', news_detail, name='news_detail_url'),
    path('registration/',register_page,name='register_url'),
    path('login/',login_page,name='log_in_url'),
    path('log/out/page/',log_out_page,name='log_out_page'),
    path('yangilik/qoshish/',create_news,name='create_news'),
    path('like/crete/', like_view, name='like_url'),
]