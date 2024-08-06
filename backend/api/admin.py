from django.contrib import admin
from .models import Note, Book, Author, Thread, Review

models = (Note, Book, Author, Thread, Review)
admin.site.register(models)