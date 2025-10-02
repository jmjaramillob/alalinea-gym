from django.urls import path
from . import views
from .views import ClientCreateView, ClientListView, ClientDeleteView, ClientUpdateView, StaffListView

urlpatterns = [
    path('', views.home, name='home'),
    path('personal/', StaffListView.as_view(), name='staff'),
    path('clientes/registrar/', ClientCreateView.as_view(), name='cliente_create'),
    path('clientes/', ClientListView.as_view(), name='cliente_list'),
    path('clientes/editar/<int:pk>/', ClientUpdateView.as_view(), name='cliente_update'),
    path('clientes/eliminar/<int:pk>/', ClientDeleteView.as_view(), name='cliente_delete'),
    path('payment-plans/', views.payment_plans, name='payment_plans'),
]