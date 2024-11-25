from django.shortcuts import render, redirect, get_object_or_404
from blogapp.decorators import login_required , blog_is_active_required
from .forms import BlogForm,  CommentForm
from blog.models import Blog, Category
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Blog, Category, Comment
from datetime import datetime
from django.utils import timezone
import json


@login_required
def load_filtered_blogs(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        selected_categories = data.get('categories', [])
        start_date = data.get('start_date', None)
        end_date = data.get('end_date', None)
        search_query = data.get('search_query','').strip()
        page = int(data.get('page',1))

        try:
            if start_date:
                start_date = timezone.make_aware(
                    datetime.strptime(start_date.strip(), '%Y-%m-%d'),
                    timezone.get_current_timezone()
                )
            if end_date:
                end_date = timezone.make_aware(
                    datetime.strptime(end_date.strip(), '%Y-%m-%d'),
                    timezone.get_current_timezone()
                )
        except ValueError:
            return JsonResponse({'error': 'Invalid date format'}, status=400)

        blogs = Blog.objects.filter(is_active=True)

        if selected_categories:
            blogs = blogs.filter(category__id__in=selected_categories)
        if start_date:
            blogs = blogs.filter(created_at__gte=start_date)
        if end_date:
            blogs = blogs.filter(created_at__lte=end_date)
        if search_query:
            blogs = blogs.filter(title__icontains=search_query)

        paginator = Paginator(blogs.order_by('-created_at'),10)
        try:
            blogs_page = paginator.page(page)
        except EmptyPage:
            return JsonResponse({'blogs': None})
        

        blogs_html = render_to_string('blog/partials/_blog.html',{'blogs': blogs_page}, request=request)
        return JsonResponse({'blogs': blogs_html})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def blog(request):
    blogs_list = Blog.objects.filter(is_active=True).order_by('-created_at')[0:10]
    context = {
        "blogs": blogs_list,  
        "categories": Category.objects.all(),
    }
    return render(request, "blog/blogs.html", context)


def index(request):
    Blog.objects.all()

    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/index.html", context)


def comments_view(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = blog.comments.all()
    page_number = request.GET.get('page', 1)
    paginator = Paginator(comments, 5)  
    page_obj = paginator.get_page(page_number)
    
    
    comments_html = render_to_string('blog/partials/comments_list.html', {'page_obj': page_obj})
    return JsonResponse({'comments': comments_html})


@login_required
@blog_is_active_required
def blog_details(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = blog.comments.all().order_by('-created_at')
    
    #pagination işlemi 
    paginator = Paginator(comments, 5)  # Sayfada gösterilecek yorum sayısı
    page_number = request.GET.get('page')  # Sayfa numarasını alıyoruz
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blog = blog
            comment.author = request.user
            comment.save()
            return redirect('blog_details', slug=blog.slug)
    else:
        comment_form = CommentForm()

    context = {
        'blog': blog,
        'comments': comments,
        'page_obj': page_obj,
        'comment_form': comment_form
    }
    return render(request, "blog/blog-details.html", context)


@login_required
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  # Oturum açan kullanıcıyı author olarak atıyoruz
            blog.save()
            messages.success(request, 'Blog başarıyla eklendi, onay bekleniyor.')
            return redirect('home')
    else:
        form = BlogForm()
    
    return render(request, 'blog/add_blog.html', {'form': form})

