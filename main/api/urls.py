from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# urlpatterns = [
#     path('', views.post_list, name='post_list'),
#     path('create/', views.post_create, name='post_create'),
    
#     path('<int:pk>', views.post, name='post'),
#     path('update_post/<int:pk>', views.post, name='update_post'),
#     path('delete_post/<int:pk>', views.post, name='delete_post'),
# ]

# format_suffix_patterns
urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:pk>', views.post, name='post'),
]

urlpatterns = format_suffix_patterns(urlpatterns)