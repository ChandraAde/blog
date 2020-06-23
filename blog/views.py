from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView
from artikel.models import Artikel
# from artikel.views import ArtikelPerKategori

# class HomeBlogView(TemplateView,ArtikelPerKategori):
#     template_name = 'index.html'

#     def get_context_data(self):
#         querysets = self.get_latest_artikel()
#         context = {
#             'latest_list':querysets
#         }
#         return context

class HomeListView(ListView):
    model = Artikel
    rang = range(0, 1)
    template_name = 'index.html'
    context_object_name = 'latest_list'
    extra_context = {
        'range':rang,
    }
    ordering = ['-published']
    paginate_by = 6
    
    def get_context_data(self,*args,**kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list':kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(*args,**kwargs)