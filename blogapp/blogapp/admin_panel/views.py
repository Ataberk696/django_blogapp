from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from blog.models import User, Blog
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from django.core.paginator import Paginator
# from django.views.decorators.http import require_GET
from blogapp.decorators import superuser_required


@csrf_exempt
def activate_user(request):
    if request.method == "POST":
        user_id = request.POST.get("id")
        user = get_object_or_404(User, id=user_id)
        user.is_active = True
        user.save()
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"})


@csrf_exempt
def deactivate_user(request):
    if request.method == "POST":
        user_id = request.POST.get("id")
        user = get_object_or_404(User, id=user_id)
        user.is_active = False
        user.save()
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"})


def activate_blog(request):
    if request.method == "POST":
        blog_id = request.POST.get("id")
        Blog.objects.filter(id=blog_id).update(is_active=True)
        return JsonResponse({"success": True})

def deactivate_blog(request):
    if request.method == "POST":
        blog_id = request.POST.get("id")
        Blog.objects.filter(id=blog_id).update(is_active=False)
        return JsonResponse({"success": True})
    
def ajax_manage_users(request):
    users = User.objects.all().values('id', 'username', 'email', 'is_active')  
    user_list = list(users)  
    return JsonResponse(user_list, safe=False)  

def ajax_manage_blogs(request):
    blogs = Blog.objects.all().values('id', 'title', 'author__username', 'category__name', 'is_active')
    blog_list = list(blogs)  
    return JsonResponse(blog_list, safe=False)

# @require_GET
# def ajax_test_view(request):
#     data = {'message': 'AJAX çalışıyor!'}
#     return JsonResponse(data)

@login_required
@superuser_required
def manage_users(request):
    users = User.objects.all() 
    return render(request, 'admin_panel/manage_users.html', {'users': users})


@login_required
@superuser_required
def manage_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'admin_panel/manage_blogs.html', {'blogs': blogs})



@login_required
@superuser_required
def approve_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = True
    user.save()
    messages.success(request, f"{user.username} başarıyla onaylandı.")
    return redirect('admin_panel:manage_users')

@login_required
@superuser_required
def inactive_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = False
    user.save()
    messages.warning(request, f"{user.username} inaktif edildi")
    return redirect('admin_panel:manage_users')



@login_required
@superuser_required
def approve_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.is_active = True
    blog.save()
    messages.success(request, f"{blog.title} başarıyla onaylandı.")
    return redirect('admin_panel:manage_blogs')

@login_required
@superuser_required
def inactive_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.is_active = False
    blog.save()
    messages.warning(request, f"{blog.title} inaktif edildi.")
    return redirect('admin_panel:manage_blogs')

#@user_passes_test(superuser_required) -- django içinde bulunan superuser decoratoru, kendim yazmak yerine bunu da kullanabilirsin.

#paginator kullanmama gerek kalmadı datatables kullandığım için
# @login_required
# @superuser_required
# def manage_blogs(request):
#     blogs = Blog.objects.all()
#     paginator = Paginator(blogs, 5) 
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'admin_panel/manage_blogs.html', {'page_obj': page_obj})

#paginator kullanmama gerek kalmadı datatables kullandığım için
# @login_required
# @superuser_required
# def manage_users(request):
#     users_list = User.objects.all() 
#     paginator = Paginator(users_list, 5)  
#     page_number = request.GET.get('page')  
#     page_obj = paginator.get_page(page_number) 

#     return render(request, 'admin_panel/manage_users.html', {'page_obj': page_obj}) 