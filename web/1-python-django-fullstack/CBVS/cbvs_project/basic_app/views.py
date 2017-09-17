from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

from . import models


class CBView(View):
    def get(self, request):
        return HttpResponse('CLASS BASED VIEWS')


class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injected'] = 'Injected content'
        return context


class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name', 'principal')


class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name', 'principal', 'location')


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    # template_name = "basic_app/school_list.html"


class SchoolDetailView(DetailView):
    context_object_name = 'school'
    model = models.School
    # template_name = "basic_app/school_detail.html"
