# from rest_framework.generics import ListAPIView
from django.core.exceptions import ObjectDoesNotExist

# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from main.models import Post
from .serializers import PostSerializer


# class PostListAPIView(ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer  #serializer_class is a inbuilt attribute in ListAPIView


# @api_view(['GET']) # this is without serializer
# def post_list(request):
#     posts = Post.objects.all() #complex data
#     post_python = list(posts.values()) #python dictionary data
#     return JsonResponse({
#         'posts': post_python
#     })
    

# Serializer is converting complex data into json 
# Get method for getting all posts and Post method for creating new post
@api_view(['GET', 'POST'])
def post_list(request, format=None):
    if request.method == 'GET':
        posts = Post.objects.all()
        posts_serializer = PostSerializer(posts, many=True)
        return Response(posts_serializer.data)

    elif request.method == 'POST':
        post_serializer = PostSerializer(data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def post(request, pk, format=None): #this pk parameter came from urls.py where <int:pk>
    # below try/except exeptions are publicly accessible
    try:
        post = Post.objects.get(id=pk) # id is came from models.py (post unique id)
    except ObjectDoesNotExist:
        return Response({"Message": "Given id does not exists in our record!"}, status=status.HTTP_404_NOT_FOUND)
    
    # Get post by unique id 
    if request.method == 'GET':
        post_serializer = PostSerializer(post)
        return Response(post_serializer.data)
      
    # Update method  
    elif request.method == 'PUT':
        post_serializer = PostSerializer(post, data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data)
        else:
            return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete method
    elif request.method == 'DELETE':
        try:
            post.delete()
            return Response({"Message": "Post is successfully deleted!"}, status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"Message": "Given id does not exists in our record!"}, status=status.HTTP_404_NOT_FOUND)