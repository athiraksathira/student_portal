from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from student.forms import StudentForm
from student.models import Student


class AddStudent(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "add_student.html"
    success_url = reverse_lazy("list")


class ListStudent(ListView):
    model = Student
    template_name = "student_list.html"
    context_object_name = "student"
class Detail(DetailView):
    model=Student
    template_name = "detail.html"
    context_object_name = "student"
    pk_url_kwarg = "id"
class Delete(View):

    def get(self, request, *args, **kwargs):
        qs = Student.objects.get(id=kwargs.get("id"))
        qs.delete()
        return redirect("list")
class Change(UpdateView):
    model = Student
    template_name ="change.html"
    form_class = StudentForm
    success_url = reverse_lazy('list')
    pk_url_kwarg = "id"