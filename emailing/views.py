from django.shortcuts import render, redirect
from django.core.mail import send_mail
from main.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def send_message(request):
    if request.method == 'POST':
        name = request.POST['name']
        send_email = request.POST['email']
        subject = request.POST['subject']
        send_mail(
                subject=name,
                message=subject,
                from_email=send_email,
                recipient_list=['tuneeechi939@gmail.com'],
        )
    return render(request,'emailing/send_msg.html')


def password_reset(request):
    user = request.user
    if request.method=='POST':
        pass_reset = request.POST['pass1']    
        pass_reset2 = request.POST['pass2']
        if pass_reset==pass_reset2:
            user.set_password(pass_reset)
            # user.password=pass_reset
            user.save()
            usr = authenticate(username=user.username,password=pass_reset)
            login(request,usr)
            messages.success(request,'Ozgardi')
            return redirect('index_url')
        else:
            messages.error(request,'bir xil emas')

    return render(request,'emailing/reset_password.html')            


def contact_us(request):
    user = request.user
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        body = request.POST['body']
        send_mail(
            subject=name,
            from_email=email,
            message=body,
            recipient_list=['tuneeechi939@gmail.com']
        )

    return render(request,'emailing/contact_us.html')