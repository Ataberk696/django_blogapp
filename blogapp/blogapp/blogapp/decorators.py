from django.contrib import messages
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

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


def superuser_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, "Bu sayfaya yalnızca yönetici erişebilir.")
            return redirect('home') 
    return _wrapped_view

# def admin_required(view_func):
#     def _wrapped_view(request, *args, **kwargs):
#         if not request.user.is_authenticated or not request.user.is_superuser:
#             raise PermissionDenied("Bu sayfaya yalnızca admin erişebilir.")
#         return view_func(request, *args, **kwargs)
#     return _wrapped_view