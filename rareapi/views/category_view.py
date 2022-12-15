from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models.category import Category

class CategoryView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for a single category
        """
        try:
            categories = Category.objects.get(pk=pk)
            serializer = CategorySerializer(categories)
            return Response(serializer.data)
        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """"Handle GET requests to handle all categories"""
        categories = Category.objects.all()

        category = request.query_params.get('type', None)
        if category is not None:
            category = categories.filter(category_id=category)

        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle create requests for category
        """
        category = Category.objects.create(
                label=request.data["label"],
            )
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a category

        Returns:
            Response -- Empty body with 204 status code
            """

        category = Category.objects.get(pk=pk)
        category.label = request.data["label"]
        category.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """this deletes stuff
        """
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Category
        fields = ('id', 'label')
        depth = 1
