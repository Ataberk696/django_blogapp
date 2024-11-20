from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name=_("Name"))
    slug = models.SlugField(null=False, blank=True, unique=True,db_index=True, editable=False)

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Categories")



from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs", null=True, blank=True)
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True, unique=True, db_index=True, editable=False)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)



class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete= models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.blog.title}"






    #Slug alanları aynı gelirse bunu kullanabilirim. 
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #         original_slug = self.slug
    #         counter = 1
    #         while Blog.objects.filter(slug=self.slug).exists():
    #             self.slug = f"{original_slug}-{counter}"
    #             counter += 1
    #     super().save(*args, **kwargs) 


