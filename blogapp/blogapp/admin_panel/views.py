from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from blog.models import Blog
from django.contrib import messages
from django.core.paginator import Paginator

from blogapp.decorators import superuser_required

@login_required
@superuser_required
def manage_users(request):
    users_list = User.objects.all() 
    paginator = Paginator(users_list, 5)  
    page_number = request.GET.get('page')  # sayfa numarasını al
    page_obj = paginator.get_page(page_number)  # Sayfayı al

    return render(request, 'admin_panel/manage_users.html', {'page_obj': page_obj}) 


@login_required
@superuser_required
def manage_blogs(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin_panel/manage_blogs.html', {'page_obj': page_obj})




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