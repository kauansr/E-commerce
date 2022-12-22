from django.contrib import admin
from .models import Produto, Variacao

# Exibe 1 campo em branco para cadastrar mais variacoes


class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1

# Mostra quais filtros voce quer editar quando entrar em produto no caso a variacaoinline


class Produtoadmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao_curta',
                    'get_preco_formatado', 'get_preco_promocional_formatado']
    inlines = [
        VariacaoInline
    ]


admin.site.register(Produto, Produtoadmin)
admin.site.register(Variacao)
