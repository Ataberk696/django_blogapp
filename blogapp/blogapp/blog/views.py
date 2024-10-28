from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from blog.models import Blog, Category
from blogapp.decorators import login_required , blog_is_active_required
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/index.html", context)

@login_required
def blog(request):
    blogs_list = Blog.objects.filter(is_active=True)  
    paginator = Paginator(blogs_list, 5)  
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
    blog = Blog.objects.get(slug=slug)
    #blog = get_object_or_404(Blog, slug=slug)
    return render(request, "blog/blog-details.html", {
        'blog': blog
    })

@login_required
def blogs_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    blogs = Blog.objects.filter(is_active=True, category=category)
    
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, "blog/blogs.html", context)


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

