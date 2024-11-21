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

def update_status(request):
    if request.method == "POST":
        item_ids = request.POST.getlist('ids[]')  
        item_type = request.POST.get('type')
        action = request.POST.get('action')

        # print(f"Gelen istek - item_type: {item_type}, action: {action}, ids: {item_ids}")

        if item_type == 'user':
            try:
                users = User.objects.filter(id__in=item_ids)  
                is_active_status = True if action == 'activate' else False
                
                for user in users:
                    user.is_active = is_active_status
                    user.save()

                return JsonResponse({'success': True, 'message': f"Kullanıcılar {action} edildi"})
            except User.DoesNotExist:
                return JsonResponse({'success': False, 'message': "Kullanıcılar bulunamadı"})

        elif item_type == 'blog':
            try:
                blogs = Blog.objects.filter(id__in=item_ids)  
                is_active_status = True if action == 'activate' else False
                
                for blog in blogs:
                    blog.is_active = is_active_status
                    blog.save()

                return JsonResponse({'success': True, 'message': f"Bloglar {action} edildi"})
            except Blog.DoesNotExist:
                return JsonResponse({'success': False, 'message': "Bloglar bulunamadı"})

    return JsonResponse({'success': False, 'message': "Geçersiz istek"})

    
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
