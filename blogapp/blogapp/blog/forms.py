from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'category', 'image']


    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        # Tüm inputlara form-control sınıfı ekle
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
