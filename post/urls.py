from django.urls import path,include
from .views import PostList
urlpatterns = [
    path('', PostList.as_view(), name='index'),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]