from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    )
from .models import Artikel
from django.shortcuts import get_object_or_404
# Create your views here.
# class ArticleUpdateView(UpdateView):
#     model = Artikel
#     form_class = ArtikelForm
#     template_name = 'artikel/article_create.html'
#     extra_context = {
#         'page_title':'Update Article',
#         'button':'Update'
#         }

class ArticleDeleteView(DeleteView):
    model = Artikel
    template_name = 'artikel/article_delete_notif.html'
    success_url = reverse_lazy('artikel:manage')

class ArticleManageView(ListView):
    model = Artikel
    template_name = 'artikel/article_manage.html'
    context_object_name = 'article'
    ordering = ['-published']

# class ArticleCreateView(CreateView):
#     form_class = ArtikelForm
#     template_name = 'article/article_create.html'

#     def get_context_data(self):
#         context = {
#             'page_title':'Create Article',
#             'button':'Tambah',
#             'form':self.form_class
#         }
#         return context

# class ArtikelPerKategori():
#     model = Article
#     context_object_name = 'latest_list'
#     # def get_latest_artikel(self):
#     #     kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
#     #     queryset = []
#     #     for kategori in kategori_list:
#     #         artikel = self.model.objects.values_list(kategori=kategori).latest('published')
#     #         queryset.append(artikel)
#     #     return queryset

class ArticleKategoriListView(ListView):
    model = Artikel
    template_name = 'artikel/article_category_list.html'
    context_object_name = 'article_list'
    ordering = ['-published']
    paginate_by = 3

    def get_queryset(self):
        self.queryset = self.model.objects.filter(kategori=self.kwargs['kategori'])
        print(self.queryset)
        return super().get_queryset()

    def get_context_data(self,*args,**kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list':kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(*args,**kwargs)

class ArticleListView(ListView):
    model = Artikel
    template_name = 'artikel/article_list.html'
    context_object_name = 'article_list'
    ordering = ['-published']
    paginate_by = 3
    
    def get_context_data(self,*args,**kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list':kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(*args,**kwargs)

class ArticleDetailView(DetailView):
    model = Artikel
    template_name = 'artikel/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self,*args,**kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list':kategori_list})

        artikel_serupa = self.model.objects.filter(kategori=self.object.kategori).exclude(id=self.object.id)
        self.kwargs.update({'artikel_serupa':artikel_serupa})
        kwargs = self.kwargs
        return super().get_context_data(*args,**kwargs)