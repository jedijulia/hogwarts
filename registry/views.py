from django.views.generic.list import ListView

from registry.models import House


class HomeView(ListView):
    model = House
    queryset = House.objects.order_by('points')
    template_name = 'registry/home.html'
