from django.contrib import messages
from django.shortcuts import redirect

def login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Bu sayfaya erişmek için öncelikle giriş yapınız.")
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def authenticated_redirect(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "Zaten giriş yaptınız, home sayfasına yönlendiriliyorsunuz.")
            return redirect("home")
        return view_func(request, *args, **kwargs)
    return wrapper
