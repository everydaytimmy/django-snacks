from django.views.generic import (
  TemplateView,
  ListView,
  DetailView,
  UpdateView,
  DeleteView,
  CreateView

)
from .models import Snack
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class HomePageView(TemplateView):
  template_name = 'home.html'

class AboutPageView(TemplateView):
  template_name = 'about.html'

class SnackListView(ListView):
  template_name = 'snack_list.html'
  model = Snack

class SnackDetailView(DetailView):
  template_name = 'snack_detail.html'
  model = Snack

class SnackCreateView(CreateView):
  model = Snack
  template_name = 'snack_create.html'
  fields = ['name', 'description', 'purchaser']

class SnackUpdateView(UpdateView):
  model = Snack
  template_name = 'snack_update.html'
  fields = ['name', 'description', 'purchaser']

class SnackDeleteView(DeleteView):
  model = Snack
  template_name = 'snack_delete.html'
  success_url = reverse_lazy('snack_list')