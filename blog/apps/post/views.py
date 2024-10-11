from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from apps.post.forms import NewPostForm, UpdatePostForm, CommentForm
from django.urls import reverse, reverse_lazy 
from apps.post.models import Post, PostImage, Comment
from django.conf import settings
from django.shortcuts import get_object_or_404

class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'

class IndexView(ListView):
    model = Post
    template_name = 'templates/index.html'
    context_object_name = 'data'  


class PostCreateView(CreateView):
    model = Post
    form_class = NewPostForm
    template_name = 'post/post_create.html'

    def form_valid(self, form): 
        form.instance.author = self.request.user 
        post = form.save() 
        images = self.request.FILES.getlist('images')

        if images: 
            for image in images: 
                PostImage.objects.create(post=post, image=image) 
            else: 
                PostImage.objects.create(post=post, image=settings.DEFAULT_POST_IMAGE) 
            return super().form_valid(form)
        def get_success_url(self): 
            return reverse('post:post_detail', kwargs={'slug': self.object.slug})

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        # Obtener todas las imágenes activas del post 
        active_images = self.object.images.filter(active=True) 
        
        context['active_images'] = active_images
        context['add_comment_form'] = CommentForm()
        
        # Para editar el comentario

        #toma el id del edit_comment           #este lo mandan por url
        edit_comment_id = self.request.GET.get('edit_comment')

        #si hay id en el comentario, intentamos obtenerlo y lo guarda en la variable
        if edit_comment_id:
            comment = get_object_or_404(Comment, id=edit_comment_id)
             #si no lo encuentra tira el error 404 

            #si el autor del comentario es el mismo que quiere editarlo
            if comment.author == self.request.user:
                context['editing_comment_id'] = comment.id  #se pasa al contexto el id
                context['edit_comment_form'] = CommentForm(instance=comment)    #y valores actual del comentario
            else:
                context['editing_comment_id'] = None    #caso contrario se pasa el None
                context['edit_comment_form'] = None


        return context

class PostUpdateView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'post/post_update.html'

    def get_form_kwargs(self): 
        kwargs = super().get_form_kwargs() 
        kwargs['active_images'] = self.get_object().images.filter(active=True)  
            # Pasamos las imágenes activas 
        return kwargs
    
    def form_valid(self, form): 
        post = form.save(commit=False) 
        active_images = form.active_images 
        keep_any_image_active = False
        # Manejo de las imágenes activas 
        if active_images: 
            for image in active_images: 
                field_name = f"keep_image_{image.id}"
                # Si el checkbox no está marcado, eliminamos la imagen 
                if not form.cleaned_data.get(field_name, True): 
                    image.active = False 
                    image.save()
                else: 
                    keep_any_image_active = True
        # Manejo de las nuevas imágenes subidas 
    
        images = self.request.FILES.getlist('images') 
        if images: 
            for image in images: 
                PostImage.objects.create(post=post, image=image)

        # Si no se desea mantener ninguna imagen activa y no se subieron nuevas imágenes, 
        # se agrega una imagen por defecto 
        if not keep_any_image_active and not images: 
            PostImage.objects.create(post=post, image=settings.DEFAULT_POST_IMAGE)
        post.save()  
        # Guardar el post finalmente 
        return super().form_valid(form)
    
    def get_success_url(self): 
    # El reverse_lazy es para que no se ejecute hasta que se haya guardado el post 
        return reverse_lazy('post:post_detail', kwargs={'slug': self.object.slug})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('post:post_list')

class CommentCreateView(CreateView):
    model = Comment
    form_class =  CommentForm
    template_name = 'post/post_detail.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(slug=self.kwargs['slug'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post:post_detail', kwargs={'slug': self.object.post.slug})

class CommentUpdateView(UpdateView):
    model = Comment
    form_class =  CommentForm
    template_name = 'post/post_detail.html'

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('post:post_detail', kwargs={'slug': self.object.post.slug})

    def test_fun(self):
        comment= self.get_object()
        return comment.author == self.request.user

class CommentDeleteView(DeleteView):
    pass


class AboutView(TemplateView):
    template_name = 'templates/about.html'