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


class UserViewSet(viewsets.ReadOnlyModelViewSet):  # Only allow reading data (no updates)
    """
    A viewset for viewing users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Require authentication to view users


class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing books.
    """
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.get_object().has_full_details:
            return BookDetailSerializer
        return BookBasicSerializer

    # Custom action to fetch full book details (when a discussion thread is created)
    @action(detail=True, methods=['get'])
    def fetch_details(self, request, pk=None):
        book = self.get_object()
        if not book.has_full_details:
            # Call your external API function here to fetch and update details
            # Example: fetch_full_book_details(book)
            book.has_full_details = True
            book.save()
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)

class ReviewViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing reviews.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

class DiscussionThreadViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing discussion threads.
    """
    queryset = DiscussionThread.objects.all()
    serializer_class = DiscussionThreadSerializer
    permission_classes = [IsAuthenticated]  # Adjust permissions as needed

class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing comments.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]  # Adjust permissions as needed

