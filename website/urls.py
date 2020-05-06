from website.views import IndexTemplateView, FuncionarioListView, FuncionarioUpdateView, FuncionarioCreateView, \
    FuncionarioDeleteView, EquipamentoCreateView, EquipamentoListView, EquipamentoUpdateView, EquipamentoDeleteView

from django.urls import path

app_name = 'website'

urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),

    # GET /funcionario/cadastrar
    path('funcionario/cadastrar', FuncionarioCreateView.as_view(), name="cadastra_funcionario"),

    # GET /funcionarios
    path('funcionarios/', FuncionarioListView.as_view(), name="lista_funcionarios"),

    # GET/POST /funcionario/{pk}
    path('funcionario/<pk>', FuncionarioUpdateView.as_view(), name="atualiza_funcionario"),

    # GET/POST /funcionarios/excluir/{pk}
    path('funcionario/excluir/<pk>', FuncionarioDeleteView.as_view(), name="deleta_funcionario"),

    # GET /equipamento/cadastrar
    path('equipamento/cadastrar', EquipamentoCreateView.as_view(), name="cadastra_equipamento"),

    # GET /equipamento
    path('equipamento/', EquipamentoListView.as_view(), name="lista_equipamentos"),

    # GET/POST /equipamento/{pk}
    path('equipamento/<pk>', EquipamentoUpdateView.as_view(), name="atualiza_equipamento"),

    # GET/POST /equipamento/excluir/{pk}
    path('equipamento/excluir/<pk>', EquipamentoDeleteView.as_view(), name="deleta_equipamento"),
]
