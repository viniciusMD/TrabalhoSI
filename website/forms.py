from helloworld.models import Funcionario, Equipamento
from django import forms


# FORMULÁRIO DE INCLUSÃO DE FUNCIONÁRIOS
# -------------------------------------------

class InsereFuncionarioForm(forms.ModelForm):

    chefe = forms.BooleanField(
        label='Chefe?',
        required=False,
    )

    biografia = forms.CharField(
        label='Biografia',
        required=False,
        widget=forms.Textarea
    )

    class Meta:
        # Modelo base
        model = Funcionario

        # Campos que estarão no form
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'tempo_de_servico',
            'remuneracao'
        ]

# FORMULÁRIO DE INCLUSÃO DE EQUIPAMENTOS
# -------------------------------------------
class InsereEquipamentoForm(forms.ModelForm):

    class Meta:
        # Modelo base
        model = Equipamento

        # Campos que estarão no form
        fields = [
            'nome',
            'codigo',
            'modelo',
            'quantidade',
            'valor',
        ]