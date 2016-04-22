from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404

from registry.models import House, Student
from registry.forms import StudentForm


class HomeView(ListView):
    model = House
    queryset = House.objects.order_by('points')
    template_name = 'registry/home.html'


class HouseView(TemplateView):
    template_name = 'registry/house.html'

    def get_context_data(self, **kwargs):
        context = super(HouseView, self).get_context_data(**kwargs)
        house = get_object_or_404(House, pk=kwargs['pk'])
        students = Student.objects.filter(house=house)
        context['house'] = house
        context['students'] = students
        return context


class StudentView(DetailView):
    model = Student
    template_name = 'registry/student.html'


class StudentCreateView(CreateView):
    form_class = StudentForm
    success_url = '/'
    template_name = 'registry/student_form.html'
