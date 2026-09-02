from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import SignUpForm
from .models import Post

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

# PROTECTED: only logged-in users can see the list of posts
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    login_url = '/login/' # where to send anonymous users

# PROTECTED: only logged-in users can create a post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('post_list')
    login_url = '/login/'

    def form_valid(self, form):
        # automatically set the author to the logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)
