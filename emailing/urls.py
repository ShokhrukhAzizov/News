from django.urls import path
from emailing.views import *

urlpatterns = [
    path('send/msg/',send_message,name='send_msg'),
    path('contact/',contact_us,name='contact_us'),
    path('password/reset/',password_reset,name='password_reset')
]