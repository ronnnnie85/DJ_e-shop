from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blog.forms import PostForm
from blog.models import Post


class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    context_object_name = 'post'
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('blog:post', kwargs={'pk': self.object.pk})

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    context_object_name = 'post'
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('blog:post', kwargs={'pk': self.object.pk})

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        obj = self.get_object()
        obj.number_of_views += 1
        obj.save(update_fields=['number_of_views'])
        return response

class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/posts_list.html'

    def get_queryset(self):
        return Post.objects.filter(publicated=True)


class BlogDeleteView(DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:posts_list')