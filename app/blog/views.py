from .models import  post
from django.views import generic

class PostList(generic.ListView):
    queryset = post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class DetailView(generic.DetailView):
     model = post
     template_name = 'post_detail.html'    

