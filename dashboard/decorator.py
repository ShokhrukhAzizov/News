from django.shortcuts import redirect

def staff_required(a):
    def wrapper_func(requset, *args, **kwargs):
        if requset.user.is_staff:
            return a(requset, *args, **kwargs)
        else:
            return redirect('index_url')
    return wrapper_func

def client_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.status==3:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('log_in_url')
    return wrapper_func
