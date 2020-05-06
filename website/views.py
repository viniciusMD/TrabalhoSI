from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from helloworld.models import Funcionario, Equipamento
from website.forms import InsereFuncionarioForm, InsereEquipamentoForm


# PÁGINA PRINCIPAL
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"


# LISTA DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioListView(ListView):
    template_name = "website/funcionario/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"


# CADASTRAMENTO DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioCreateView(CreateView):
    template_name = "website/funcionario/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("website:lista_funcionarios")


# ATUALIZAÇÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioUpdateView(UpdateView):
    template_name = "website/funcionario/atualiza.html"
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionarios")


# EXCLUSÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioDeleteView(DeleteView):
    template_name = "website/funcionario/exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionarios")

# LISTA DE EQUIPAMENTOS
# ----------------------------------------------

class EquipamentoListView(ListView):
    template_name = "website/equipamento/lista.html"
    model = Equipamento
    context_object_name = "equipamentos"

# CADASTRAMENTO DE EQUIPAMENTOS
# ----------------------------------------------

class EquipamentoCreateView(CreateView):
    template_name = "website/equipamento/cria.html"
    model = Equipamento
    form_class = InsereEquipamentoForm
    success_url = reverse_lazy("website:lista_equipamentos")


# ATUALIZAÇÃO DE EQUIPAMENTOS
# ----------------------------------------------

class EquipamentoUpdateView(UpdateView):
    template_name = "website/equipamento/atualiza.html"
    model = Equipamento
    fields = '__all__'
    context_object_name = 'equipamentos'
    success_url = reverse_lazy("website:lista_equipamentos")


# EXCLUSÃO DE EQUIPAMENTOS
# ----------------------------------------------

class EquipamentoDeleteView(DeleteView):
    template_name = "website/equipamento/exclui.html"
    model = Equipamento
    context_object_name = 'equipamentos'
    success_url = reverse_lazy("website:lista_equipamentos")