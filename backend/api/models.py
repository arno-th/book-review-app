from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Author(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="authors")

    def __str__(self):
        return self.name    

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    has_full_details = models.BooleanField(default=False)
    
    # These fields will be filled only when a discussion thread is created
    description = models.TextField(null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    cover_image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Comment(models.Model):
    thread = models.ForeignKey(DiscussionThread, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Allows for nested comments (replies)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name="replies")

    def __str__(self):
        return f"Comment by {self.user} on {self.thread.title}"

class DiscussionThread(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="threads")
    title = models.CharField(max_length=255)  # Topic of the discussion
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Thread: {self.title} on {self.book.title}"

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()  # Rating from 1-5, for example
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user} on {self.book.title}"