from django.shortcuts import render, redirect
from .forms import BlogForm
from blog.models import Blog, Category
from django.contrib.auth import authenticate, login
from blogapp.decorators import login_required
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/index.html", context)

@login_required
def blog(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)

@login_required
def blog_details(request, slug):

    blog = Blog.objects.get(slug=slug)
    
    return render(request, "blog/blog-details.html", {
        'blog': blog
    })

@login_required
def blogs_by_category(request, slug):
    context = {
        #"blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        "blogs": Blog.objects.filter(is_active=True, category__slug=slug),
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

