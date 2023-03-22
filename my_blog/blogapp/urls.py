from . import views
from django.urls import path

app_name = 'blogapp'

urlpatterns = [
    path('about', views.AboutView.as_view(), name='about'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new', views.CreatePostView.as_view(), name='create_post'),
    path('post/<int:pk>/edit', views.PostUpdateView.as_view(), name='edit_post'),
    path('delete_post/<int:pk>', views.PostDeleteView.as_view(), name='delete_post'),
    path('drafts', views.DraftListView.as_view(), name='drafts'),
    path('post/<int:pk>/comment', views.add_comment_to_post, name='add_comment'),
    path('comment/<int:pk>/approve/', views.approve_comment, name='approve_comment'),
    path('comment/<int:pk>/remove_comment/', views.remove_comment, name='remove_comment'),
    path('post/<int:pk>/publish', views.post_publish, name='post_publish'),

]

