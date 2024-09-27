from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='book')
router.register(r'reviews', views.ReviewViewSet, basename='review')
router.register(r'threads', views.DiscussionThreadViewSet, basename='thread')
router.register(r'comments', views.CommentViewSet, basename='comment')
router.register(r'users', views.UserViewSet, basename='user')  # Optional: if you have a custom UserViewSet

urlpatterns = [
    path('', include(router.urls)),  # Include all the registered routes
    path('auth/', include('djoser.urls')),  # Djoser auth endpoints
    path('auth/', include('djoser.urls.authtoken')),  # Djoser token auth endpoints
]