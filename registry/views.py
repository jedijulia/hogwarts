from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404

from registry.models import House, Student
from registry.forms import StudentForm, PointForm


class HomeView(ListView):
    model = House
    queryset = House.objects.order_by('points')
    template_name = 'registry/home.html'


class HouseView(TemplateView):
    form_class = PointForm
    template_name = 'registry/house.html'

    def get_context_data(self, **kwargs):
        context = super(HouseView, self).get_context_data(**kwargs)
        house = get_object_or_404(House, pk=kwargs['pk'])
        students = Student.objects.filter(house=house)
        context['house'] = house
        context['students'] = students
        context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        house = get_object_or_404(House, pk=kwargs['pk'])
        form = self.form_class(request.POST)
        if form.is_valid():
            house.points += form.cleaned_data['points']
            house.save()
        return redirect('house-detail', house.pk)


class StudentView(DetailView):
    model = Student
    template_name = 'registry/student.html'


class StudentCreateView(CreateView):
    form_class = StudentForm
    success_url = '/'
    template_name = 'registry/student_form.html'
