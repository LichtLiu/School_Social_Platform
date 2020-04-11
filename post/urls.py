from django.urls import path,include
from .views import PostList, PostDetail, PostCreate
urlpatterns = [
    path('',include([
        path('', PostList.as_view(), name='index'),
        path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    ])),

    path('post/',include([
        path('post_create/', PostCreate.as_view(), name='post_create'),

    ])),
    
]