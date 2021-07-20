from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from .models import Articles
from django.urls import reverse_lazy
class ArticlesCreateView(LoginRequiredMixin,CreateView):
    model = Articles
    template_name = 'article_new.html'
    fields = ('title','body','Address',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class ArticlesListView(LoginRequiredMixin,ListView):

    model = Articles
    template_name = 'article_list.html'
    login_url = 'login'

class ArticlesDetailView(LoginRequiredMixin,DetailView):
    model = Articles
    template_name = 'article_detail.html'
    login_url = 'login'

class ArticlesUpdateView(LoginRequiredMixin,UpdateView):
    model = Articles
    fields = ('title','body',)
    template_name = 'article_edit.html'
    login_url = 'login'

    def dispatch(self, request,*args,**kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request,*args,**kwargs)
class ArticlesDeleteView(LoginRequiredMixin,DeleteView):
    model = Articles
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def dispatch(self, request,*args,**kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request,*args,**kwargs)
        

    
# Create your views here.
