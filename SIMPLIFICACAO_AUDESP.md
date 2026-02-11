# ✅ Simplificação do Sistema AUDESP

## 🎯 Mudanças Realizadas

### Antes:
- **Elementos de Despesa**: 70+ códigos genéricos
- **Fontes de Recursos**: 20+ códigos genéricos

### Depois:
- **Elementos de Despesa**: 25 códigos mais utilizados
- **Fontes de Recursos**: 17 códigos específicos do município

---

## 📋 Elementos de Despesa Simplificados

Agora incluem apenas os mais utilizados:

| Código | Descrição |
|--------|-----------|
| 04 | Contratação por Tempo Determinado |
| 08 | Outros Benefícios Assistenciais do Servidor |
| 11 | Vencimentos e Vantagens Fixas - Pessoal Civil |
| 13 | Obrigações Patronais |
| 14 | Diárias - Civil |
| 16 | Outras Despesas Variáveis - Pessoal Civil |
| 18 | Auxílio Financeiro a Estudante |
| 21 | Juros sobre a Dívida por Contrato |
| 30 | Material de Consumo |
| 32 | Material para Distribuição Gratuita |
| 35 | Serviços de Consultoria |
| 36 | Outros Serviços de Terceiros - PF |
| 39 | Outros Serviços de Terceiros - PJ |
| 40 | Serviços de TI e Comunicação - PJ |
| 46 | Auxílio-Alimentação |
| 47 | Obrigações Tributárias e Contributivas |
| 51 | Obras e Instalações |
| 52 | Equipamentos e Material Permanente |
| 61 | Aquisição de Imóveis |
| 70 | Rateio Consórcio Público |
| 71 | Principal da Dívida Resgatado |
| 91 | Sentenças Judiciais |
| 92 | Despesas de Exercícios Anteriores |
| 93 | Indenizações e Restituições |
| 99 | Reserva de Contingência |

---

## 💰 Fontes de Recursos Simplificadas

| Código | Descrição |
|--------|-----------|
| 01 | Tesouro |
| 02 | Transferências Estaduais - Vinculados |
| 03 | Recursos Próprios Fundos Especiais - Vinculados |
| 04 | Recursos Próprios Administração Indireta |
| 05 | Transferências Federais - Vinculados |
| 06 | Outras Fontes de Recursos |
| 07 | Operações de Crédito |
| 08 | Emendas Parlamentares Individuais |
| 19 | Recursos Extraorçamentários |
| 91 | Tesouro - Exercícios Anteriores |
| 92 | Transferências Estaduais - Ex. Anteriores |
| 93 | Recursos Fundos Especiais - Ex. Anteriores |
| 94 | Recursos Adm. Indireta - Ex. Anteriores |
| 95 | Transferências Federais - Ex. Anteriores |
| 96 | Outras Fontes - Ex. Anteriores |
| 97 | Operações Crédito - Ex. Anteriores |
| 98 | Emendas Parlamentares - Ex. Anteriores |

---

## ✨ Benefícios

1. **Interface Mais Limpa**: Menos opções para escolher
2. **Mais Rápido**: Encontra os códigos mais facilmente
3. **Focado**: Apenas o que realmente usa
4. **Prático**: Baseado no uso real do município

---

## 🔄 Se Precisar Adicionar Mais

É só editar o arquivo `audesp_codes.py`:

```python
# Adicione novos elementos em ELEMENTOS_DESPESA
ELEMENTOS_DESPESA = {
    "XX": "Nova Descrição",
    # ... resto dos códigos
}

# Adicione novas fontes em FONTES_RECURSOS
FONTES_RECURSOS = {
    "XX": "Nova Fonte",
    # ... resto dos códigos
}
```

---

## 📝 Arquivo Atualizado

`Projeto_lei/audesp_codes.py` - Linhas 293-320

Agora o sistema está mais simples e focado no que você realmente usa! 🎉
