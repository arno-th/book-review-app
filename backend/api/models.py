from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Author(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    isbn = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.RESTRICT, related_name="books")

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title

class Thread(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="threads")
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name="threads")

    def __str__(self):
        return f"{self.author}: {self.content[:10]}"

class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    content = models.TextField()

    def __str__(self):
        return f"{self.author}: {self.content[:10]}"