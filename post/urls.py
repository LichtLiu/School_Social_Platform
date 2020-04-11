from django.urls import path,include
from .views import PostList, PostDetail, PostCreate, userprofile
urlpatterns = [
    path('user_profile/',include([
        path('', userprofile, name='personal_home_page')
    ])),
    path('',include([
        path('', PostList.as_view(), name='index'),
        path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    ])),

    path('post/',include([
        path('post_create/', PostCreate.as_view(), name='post_create'),

    ])),
    
]