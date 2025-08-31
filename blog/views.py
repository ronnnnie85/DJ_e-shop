from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from blog.models import Post


class BlogCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_detail')


