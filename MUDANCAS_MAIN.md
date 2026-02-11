# Mudanças necessárias no main.py

## Localização: Após linha 115 (val_exc)

Adicionar o seguinte código:

```python
# Campo de origem para excesso de arrecadação
origem_recursos = ""
if usa_exc and val_exc > 0:
    origem_recursos = st.text_input(
        "Origem dos Recursos",
        placeholder="Ex: Proposta nº 63000724740202600, destinada ao custeio...",
        help="Informe a origem específica (proposta, convênio, etc.)"
    )
```

## Localização: Seção "GERAR DOCUMENTO" (por volta da linha 590)

Modificar o dicionário `dados` para incluir `origem_recursos`:

```python
dados = {
    "tipo_lei": tipo_lei,
    "numero": numero,
    "municipio": municipio,
    "prefeito": prefeito,
    "ppa": ppa,
    "ldo": ldo,
    "val_sup": val_sup,
    "val_exc": val_exc,
    "origem_recursos": origem_recursos,  # <- ADICIONAR ESTA LINHA
    "itens_credito": st.session_state.itens_credito,
    "itens_anulacao": st.session_state.itens_anulacao,
    "total_credito": total_credito,
    "justificativa": justificativa
}
```
