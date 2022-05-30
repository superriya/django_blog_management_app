from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('blog/<int:pk>', views.blog_detail, name='blog_detail'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('create_post', views.create_post, name='create_post'),
    path('create_category', views.create_category, name='create_category'),
    path('category/<int:pk>', views.show_category, name='show_category'),
    path('tag/<slug:slug>/', views.tagged, name='tagged'),
    path('search-blog', views.search_blog, name='search_blog'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)