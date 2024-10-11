from django.urls import path
import apps.post.views as view

app_name = 'post'

urlpatterns = [
    path('', view.IndexView.as_view(), name="index"),
    path('about/', view.AboutView.as_view(), name="about"),
    path('posts/', view.PostListView.as_view(), name="post_list"),
    path('posts/create', view.PostCreateView.as_view(), name="post_create"),
    path('posts/<slug:slug>/', view.PostDetailView.as_view(), name="post_detail"),
    path('posts/<slug:slug>/update', view.PostUpdateView.as_view(), name="post_update"),
    path('posts/<slug:slug>/delete', view.PostDeleteView.as_view(), name="post_delete"),
    path('posts/<slug:slug>/comments/create', view.CommentCreateView.as_view(), name="comment_create"),
    path('comments/<uuid:pk>/update', view.CommentUpdateView.as_view(), name="comment_update"),
    path('comments/<uuid:pk>/delete', view.CommentDeleteView.as_view(), name="comment_delete"),
]
