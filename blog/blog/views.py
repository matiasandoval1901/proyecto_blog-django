from django.views.generic import TemplateView, ListView
from apps.post.models import Post

class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self): 
        return Post.objects.all().order_by('-creation_date')  
                                # ordenar por fecha de creación

class AboutView(TemplateView):
    template_name = 'about.html'
