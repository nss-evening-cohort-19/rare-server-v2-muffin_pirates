from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, User, Category
from rest_framework.decorators import action


class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for posts
    """
    class Meta:
        model = Post
        fields = ('id', 'user', 'category', 'title',
                  'publication_date', 'image_url', 'content')
        depth = 2


class PostView(ViewSet):

    def retrieve(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def list(self, request):
        posts = Post.objects.all()
        user = request.query_params.get('user', None)
        if user is not None:
            posts = posts.filter(user_id=user)
        category = request.query_params.get('category', None)
        if category is not None:
            posts = posts.filter(category_id=category)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):

        user = User.objects.get(pk=request.data["user"])
        category = Category.objects.get(pk=request.data["category"])

        post = Post.objects.create(
            title=request.data["title"],
            publication_date=request.data["publication_date"],
            image_url=request.data["image_url"],
            content=request.data["content"],
            user=user,
            category=category
        )
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def update(self, request, pk):

        post = Post.objects.get(pk=pk)
        post.title = request.data["title"]
        post.publication_date = request.data["publication_date"]
        post.image_url = request.data["image_url"]
        category = Category.objects.get(pk=request.data["category"])
        post.category = category
        post.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
