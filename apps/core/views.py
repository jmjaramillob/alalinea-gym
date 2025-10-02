from django.shortcuts import render
from .models import Staff, PaymentPlan, Client
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import ClientForm
from django.db.models import Q


def home(request):
    return render(request, 'gym/home.html')


class StaffListView(ListView):
    model = Staff
    template_name = "gym/staff.html"
    context_object_name = "staff"

# REGISTRAR CLIENTE
class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'gym/client_form.html'
    success_url = reverse_lazy('cliente_list')  # Redirige después de guardar

    def form_valid(self, form):

        return super().form_valid(form)

# LISTAR CLIENTE
class ClientListView(ListView):
    model = Client
    template_name = 'gym/client_list.html'
    context_object_name = 'clientes'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(email__icontains=query) |
                Q(phone__icontains=query) |
                Q(address__icontains=query)
            )
        return queryset

# ACTUALIZAR CLIENTE
class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'gym/client_form.html'
    success_url = reverse_lazy('cliente_list')

# ELIMINAR CLIENTE
class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'gym/client_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')

def payment_plans(request):
    plans = PaymentPlan.objects.all()
    return render(request, 'gym/payment_plans.html', {'plans': plans})