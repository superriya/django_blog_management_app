from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Category, Comment

#categories added dynamically
choices = Category.objects.all().values_list('name', 'name')
choices_list = []
for item in choices:
    choices_list.append(item)


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'description', 'category', 'tags']
        
        widgets = {
            'category': forms.Select(choices=choices_list),
            'tags': forms.TextInput
                           (attrs={'data-role':'tagsinput'})
        }
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']