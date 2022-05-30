from rest_framework.serializers import ModelSerializer

from main.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'excerpt',
            'description',
            'category',
        ]   
        
"""

    data = {
        "title": "new post by supriya", 
        "excerpt": "This is my favourite post", 
        "description": "This is new and unique post created by supriya sontakke"
    }
    
    new_item = PostSerializer(data = data)
    if new_item.is_valid():
        new_item.save()
    else:
        print(new_item.errors)
"""