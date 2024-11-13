from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Blog, Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'category', 'image']
        labels = {
            'title': _('Title'),
            'description': _('Description'),
            'category': _('Category'),
            'image': _('Image'),
        }
        help_texts = {
            'title': _('Enter the title of the blog.'),
            'description': _('Provide a detailed description of the blog.'),
            'category': _('Select a category for the blog.'),
            'image': _('Upload an image for the blog.'),
        }


    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        # Tüm inputlara form-control sınıfı ekle
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 6,
                'cols': 80,  
                'placeholder': _('Yorumunuzu buraya yazın...'),
                'class': 'form-control',  
                'style': 'width: 100%; resize: vertical;' 
            })
        }

        labels = {
            'content' : ''
        }