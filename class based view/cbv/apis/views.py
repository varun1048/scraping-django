from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
def index(req):
    return render(req,"index.html")

class Ex2(TemplateView):
    template_name = "ex2.html"
    
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['name'] = "varun"
        return context
    