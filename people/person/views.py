from django.shortcuts import render
from .models import Person
# Create your views here.
from django.views import generic

class PersonListView(generic.ListView):
    model = Person
from django.contrib.auth.mixins import LoginRequiredMixin
class PersonDetailView(LoginRequiredMixin,generic.DetailView):
    model = Person
    def get_queryset(self):
        return Person.objects.filter(django_username=self.request.user)
