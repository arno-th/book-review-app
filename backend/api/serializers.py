from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Author, Book, Note, Thread, Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "created_at", "name"]
        extra_kwargs = {"created_at": {"read_only": True}}

class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='name', queryset=Author.objects.all())
    class Meta:
        model = Book
        fields = ["id", "created_at", "title", "description", "isbn", "author"]
        extra_kwargs = {
            "created_at": {"read_only": True},
        }

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "created_at", "title", "content", "author", "book"]
        extra_kwargs = {
            "created_at": {"read_only": True},
            "author": {"read_only": True},
        }

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ["id", "created_at", "content", "author", "note"]
        extra_kwargs = {
            "created_at": {"read_only": True},
            "author": {"read_only": True},
            "note": {"read_only": True},
        }

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    book = serializers.SlugRelatedField(slug_field='title', queryset=Book.objects.all())

    class Meta:
        model = Review
        fields = ["id", "created_at", "author", "book", "rating", "content"]
        extra_kwargs = {
            "created_at": {"read_only": True},
            # "author": {"read_only": True},
            # "book": {"read_only": True},
        }