from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
# view imports
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import CreateView


from braces.views import LoginRequiredMixin

from .models import *
from .forms import *
# Create your views here.

class OrderView(LoginRequiredMixin, ListView):
    context_object_name = 'specialorders'
    template_name = 'orders.html'
    queryset = SpecialOrder.objects.all()

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context['specialorders'] = SpecialOrder.objects.all()
        context['bulkorders'] = BulkOrder.objects.all()
        # And so on for more models
        return context


class SpecialOrdersView(LoginRequiredMixin, ListView):
    model = SpecialOrder
    slug_field = "SpecialOrder"
    slug_url_kwarg = "SpecialOrder"


class BulkOrdersView(LoginRequiredMixin, ListView):
    model = BulkOrder
    slug_field = "BulkOrder"
    slug_url_kwarg = "BulkOrder"


class SpecialOrderUpdateView(LoginRequiredMixin, UpdateView):

    form_class = SpecialOrderForm

    model = SpecialOrder

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')


class BulkOrderUpdateView(LoginRequiredMixin, UpdateView):

    form_class = BulkOrderForm

    # we already imported User in the view code above, remember?
    model = BulkOrder

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')


class SpecialOrderCreateView(LoginRequiredMixin, CreateView):

    form_class = CreateSpecialOrderForm
    template_name_suffix = '_create_form'
    model = SpecialOrder
    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')


class BulkOrderCreateView(LoginRequiredMixin, CreateView):

    form_class = CreateBulkOrderForm
    template_name_suffix = '_create_form'
    model = BulkOrder

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')

class reports(LoginRequiredMixin, ListView,):
    context_object_name = 'specialorders'
    template_name = 'AlamoParkway/reports.html'
    queryset = SpecialOrder.objects.all()

    def get_context_data(self, **kwargs):
        context = super(reports, self).get_context_data(**kwargs)
        context['specialorders'] = SpecialOrder.objects.all()
        context['bulkorders'] = BulkOrder.objects.all()
        # And so on for more models
        return context