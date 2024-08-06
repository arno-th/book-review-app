from django.urls import path
from . import views

urlpatterns = [
    path("authors/", views.AuthorList.as_view(), name="author-list"),
    path("authors/create/", views.AuthorCreate.as_view(), name="author-create"),
    path("authors/delete/<int:pk>/", views.AuthorDelete.as_view(), name="author-delete"),
    path("books/", views.BookList.as_view(), name="book-list"),
    path("books/<int:pk>/", views.BookGet.as_view(), name="book-get"),
    path("books/create/", views.BookCreate.as_view(), name="book-create"),
    path("books/delete/<int:pk>/", views.BookDelete.as_view(), name="book-delete"),
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="note-delete"),
    path("threads/", views.ThreadListCreate.as_view(), name="thread-list"),
    path("threads/delete/<int:pk>/", views.ThreadDelete.as_view(), name="thread-delete"),
    path("reviews/", views.ReviewList.as_view(), name="review-list"),
    path("reviews/<int:pk>/", views.ReviewGet.as_view(), name="review-get"),
    path("reviews/create/", views.ReviewCreate.as_view(), name="review-create"),
    path("reviews/delete/<int:pk>/", views.ReviewDelete.as_view(), name="review-delete"),
]