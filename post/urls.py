from django.urls import path,include
from .views import PostList, PostDetail
urlpatterns = [
    path('', PostList.as_view(), name='index'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]