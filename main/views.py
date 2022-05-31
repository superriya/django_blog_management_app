from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import RegisterForm, PostForm, CategoryForm, CommentForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from .models import Post, Category, Comment
from taggit.models import Tag
import urllib.parse

# @login_required(login_url='/login')
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    # show latest_post
    latest_posts = Post.objects.all().order_by('-created_at')[:4]
    # show all tags
    tags = Tag.objects.all()
    # show most-common tags
    common_tags = Post.tags.most_common()[:4]
    categories = Category.objects.all()
    context = {
        "posts": posts, 
        "categories": categories, 
        "latest_posts": latest_posts, 
        "tags": tags,
        "common_tags": common_tags
    }
    if request.method == 'POST':
        post_id = request.POST.get("post-id")
        print(f"Post Deleted for id {post_id}")
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()
    return render(request, 'main/home.html', context)

def tagged(request, slug):
    # show latest_post
    latest_posts = Post.objects.all().order_by('-created_at')[:4]
    # show all tags
    tags = Tag.objects.all()
    # show most-common tags
    common_tags = Post.tags.most_common()[:4]
    tag = get_object_or_404(Tag, slug=slug)
    # Filter post by tag name
    posts = Post.objects.filter(tags=tag)
    context = {
        "posts": posts, 
        "latest_posts": latest_posts, 
        "tag": tag,
        "tags": tags,
        "common_tags": common_tags
    }
    return render(request, 'main/home.html', context)

#category by name
def category_view(request, cats):
    print(urllib.parse.unquote(cats))
    # category_post = Post.objects.filter(category__icontains=urllib.parse.unquote(cats))
    # return render(request, 'main/categories.html', {"cats": urllib.parse.unquote(cats), "category_post": category_post})
    pass

# Show blogs belongs to perticular category
def show_category(request, pk):
    latest_posts = Post.objects.all().order_by('-created_at')[:4]
    # show all tags
    tags = Tag.objects.all()
    # show most-common tags
    common_tags = Post.tags.most_common()[:4]
    cats = Category.objects.all()
    categories = Category.objects.get(id=pk)
    category_post = Post.objects.filter(category = categories).order_by('-created_at') 
    context = {
        "categories": categories, 
        "category_post": category_post, 
        "cats": cats, 
        "latest_posts": latest_posts, 
        "tags": tags,  
        "common_tags": common_tags
    }
    return render(request, 'main/show_categories.html', context)
    
# redirect to indivisual blog with having id
def blog_detail(request, pk):
    #if used filter method then for loop is required in blog_detail
    # posts = Post.objects.filter(id=pk) 
    
    # if used get_object_or_404 method then in blog_detail template, you don't need a for loop; As you are just passing one post to the template:
    # post = get_object_or_404(Post, id=pk)
    # get_object_or_404 shortcut method supports queryset 
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            # return redirect('blog_detail', pk=post.id)
            return redirect(reverse('blog_detail', kwargs={'pk': post.id}) + '#comment-section')
            # return redirect('/home')``
    else:
        form = CommentForm()
    return render(request, 'main/blog_detail.html', {"post": post, "form": form})


# Redirect on single blog with having url(slug)
# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, 'main/post_detail.html', {"post": post})

#search by input field
def search_blog(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        posts = Post.objects.filter(title__icontains=searched).order_by('-created_at') 
        return render(request, 'search/search_blog.html', {"searched": searched, "posts": posts})
    else:
        return render(request, 'search/search_blog.html', {})
    
    
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
        
    else:
        form = RegisterForm()
        
    return render(request, 'registration/sign_up.html', {"form": form})

@login_required(login_url='/login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # important - to save tags add form.save_m2m() function
            form.save_m2m()
            return redirect('/home')
    else:
        form = PostForm()
    return render(request, 'main/create_post.html', {"form": form})

@login_required(login_url='/login')
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('/home')
    else:
        form = CategoryForm()
    return render(request, 'main/create_category.html', {"form": form})

        
        
            