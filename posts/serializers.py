from rest_framework import serializers

from .models import Post

"""The serializer not only transforms data into JSON, it can also specify
which fields to include or exclude. In our case, we will include the id field
Django automatically adds to database models but we will exclude the updated_at
field by not including it in our fields."""


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created_at",
        )
        model = Post
