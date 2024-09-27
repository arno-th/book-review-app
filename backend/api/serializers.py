from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Book, DiscussionThread, Comment, Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "firstname", "lastname"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class BookBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn']

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'description', 'publication_date', 'cover_image_url']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Show the username of the commenter
    
    class Meta:
        model = Comment
        fields = ['id', 'thread', 'user', 'comment_text', 'created_at', 'parent_comment']
        read_only_fields = ['created_at']


class DiscussionThreadSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()  # Show username instead of just ID
    
    class Meta:
        model = DiscussionThread
        fields = ['id', 'book', 'title', 'created_by', 'created_at']
        read_only_fields = ['created_at']


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Display the user's name instead of just their ID
    
    class Meta:
        model = Review
        fields = ['id', 'book', 'user', 'rating', 'review_text', 'created_at']
        read_only_fields = ['created_at']
