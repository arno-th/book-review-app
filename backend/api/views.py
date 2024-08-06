from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Author, Book, Note, Thread, Review
from .serializers import (
    UserSerializer,
    AuthorSerializer,
    BookSerializer,
    NoteSerializer,
    ThreadSerializer,
    ReviewSerializer
)

#################################################################
# Users
#################################################################

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

#################################################################
# Authors
#################################################################

class AuthorList(generics.ListAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()

class AuthorCreate(generics.CreateAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()

    def perform_create(self, serializer: AuthorSerializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

class AuthorDelete(generics.DestroyAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Author.objects.all()
        else:
            return Author.objects.none()

#################################################################
# Books
#################################################################

class BookList(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()

class BookGet(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()

class BookCreate(generics.CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()

    def perform_create(self, serializer: BookSerializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

class BookDelete(generics.DestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Book.objects.all()
        else:
            return Book.objects.none()

#################################################################
# Notes
#################################################################
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer: NoteSerializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

#################################################################
# Threads
#################################################################
class ThreadListCreate(generics.ListCreateAPIView):
    serializer_class = ThreadSerializer
    permission_classes = [IsAuthenticated]
    queryset = Thread.objects.all()

    def perform_create(self, serializer: ThreadSerializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class ThreadDelete(generics.DestroyAPIView):
    serializer_class = ThreadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Thread.objects.filter(author=user)

#################################################################
# Reviews
#################################################################

class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()

class ReviewGet(generics.RetrieveAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()

    def perform_create(self, serializer: ReviewSerializer):
        if serializer.is_valid():
            print("test", self.request)
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
            print("test", self.request)

class ReviewDelete(generics.DestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Review.objects.all()
        else:
            return Review.objects.none()