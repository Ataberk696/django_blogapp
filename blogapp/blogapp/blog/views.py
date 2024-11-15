from django.shortcuts import render, redirect, get_object_or_404
from blogapp.decorators import login_required , blog_is_active_required
from .forms import BlogForm,  CommentForm
from blog.models import Blog, Category
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Blog, Category, Comment

# from django.http import JsonResponse
# from django.views.decorators.http import require_GET

# @require_GET
# def ajax_test_view(request):
#     data = {'message': 'AJAX çalışıyor!'}
#     return JsonResponse(data)

# Create your views here.


def index(request):
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
def blog(request):
    blogs_list = Blog.objects.filter(is_active=True)  
    paginator = Paginator(blogs_list, 200)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,  
        "categories": Category.objects.all(),
    }
    return render(request, "blog/blogs.html", context)

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
def filter_blogs(request):
    blogs = Blog.objects.all()

    selected_categories = request.GET.getlist('categories[]')

    if selected_categories:
        if isinstance(selected_categories[0], str) and ',' in selected_categories[0]:
            selected_categories = selected_categories[0].split(',')
        
        selected_categories = [int(category_id) for category_id in selected_categories if category_id.isdigit()]

        if selected_categories:
            blogs = blogs.filter(category__id__in=selected_categories)

    elif not selected_categories:
        blogs = Blog.objects.all()

    # HTML içeriğini render et ve JSON ile döndür
    html = render_to_string('blog/partials/_blog.html', {'blogs': blogs}, request=request)
    return JsonResponse({'html': html})








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

