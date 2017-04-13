"""
Definition of views.
"""
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Present

class PresentCreate(LoginRequiredMixin, CreateView):
    """
    Create view for new presents

    Require Login
    """
    login_url = '/login/'
    model = Present
    fields = ['name', 'cost', 'url']
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.date_inserted = timezone.now()
        return super(PresentCreate, self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(PresentCreate, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['year'] = timezone.now().year
        context['title'] = 'Aggiungi un regalo'
        return context


class PresentUpdate(LoginRequiredMixin, UpdateView):
    """
    Update view for presents

    Require Login
    """
    login_url = '/login/'
    model = Present
    fields = ['name', 'cost', 'url']

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is None:
            raise AttributeError("Generic detail view %s must be called with "
                                 "either an object pk or a slug."
                                 % self.__class__.__name__)
        obj = get_object_or_404(self.model, pk=pk, owner=self.request.user)
        return obj

    def get_context_data(self, **kwargs):
        context = super(PresentUpdate, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['year'] = timezone.now().year
        context['title'] = 'Aggiorna un regalo'
        return context


class PresentList(LoginRequiredMixin, ListView):
    """
    List view for all presents

    Require Login
    """
    login_url = '/login/'

    model = Present

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(PresentList, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['year'] = timezone.now().year
        context['title'] = 'Lista regali'
        return context

class PresentDetail(LoginRequiredMixin, DetailView):
    """
    List view for all presents

    Require Login
    """

    login_url = '/login/'

    model = Present

    def get_context_data(self, **kwargs):
        context = super(PresentDetail, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['year'] = timezone.now().year
        context['title'] = 'Dettaglio regalo'
        return context

class PresentDelete(LoginRequiredMixin, DeleteView):
    """
    Delete view for presents

    Require Login
    """

    login_url = '/login/'

    model = Present

    success_url = reverse_lazy('user_home')

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is None:
            raise AttributeError("Generic detail view %s must be called with "
                                 "either an object pk or a slug."
                                 % self.__class__.__name__)
        obj = get_object_or_404(self.model, pk=pk, owner=self.request.user)
        return obj

    def get_context_data(self, **kwargs):
        context = super(PresentDelete, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['year'] = timezone.now().year
        context['title'] = 'Cancella Regalo'
        return context
