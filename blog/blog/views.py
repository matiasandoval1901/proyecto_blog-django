from django.views.generic import TemplateView, ListView
from apps.post.models import Post
from django.shortcuts import render 

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

def not_found_view(request, exception): 
    return render(request, 'errors/error_not_found.html', status=404)

def internal_error_view(request): 
    return render(request, 'errors/error_internal.html', status=500)

def forbidden_view(request, exception): 
    return render(request, 'errors/error_forbidden.html', status=403)

