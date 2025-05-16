from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogUpdateViews, BlogDetailView, BlogDeleteViews

app_name = BlogConfig.name
urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/update/<int:pk>/', BlogUpdateViews.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>/', BlogDeleteViews.as_view(), name='blog_delete'),
]