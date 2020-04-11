from django.shortcuts import render, reverse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User
from .models import Post
from .forms import PostCreateForm



# List all of the posts on index.html
class PostList(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'index.html'
    context_object_name = 'blog_posts'

# List all personal posts
@login_required
def userprofile(request):
    user = request.user
    user_posts = Post.objects.filter(author=user).order_by('-pub_date')
    template_name = 'post/personal_post_list.html'
    context = {
        'user_posts':user_posts,
        'user':user,
    }
    return render(request, template_name, context)


# Display the specific post and post's comments
class PostDetail(DetailView):
    model = Post
    template_name = 'post/post_detail.html'

# let user create post
@method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    model = Post
    template_name = 'post/post_create.html'
    form_class = PostCreateForm
    context_object_name = 'post'

    def form_valid(self,form):
        post = form.save(commit=False)
        post.author = self.request.user
        return super(PostCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('index')




