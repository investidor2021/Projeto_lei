from docx import Document
from datetime import date
from doc_base import (
    configurar_estilo, adicionar_titulo, adicionar_ementa,
    adicionar_lista_creditos, adicionar_lista_anulacoes,
    adicionar_data_assinatura, salvar_docx,
    format_currency, extenso_brl
)

def gerar_decreto(dados):
    """
    Gera um Decreto em formato DOCX.
    Linguagem direta: o Prefeito decreta e acabou a discussão.
    """

    doc = Document()
    configurar_estilo(doc)

    # =============================
    # TÍTULO
    # =============================
    titulo = f"DECRETO Nº {dados['numero']} / {date.today().year}"
    adicionar_titulo(doc, titulo)

    # =============================
    # EMENTA
    # =============================
    ementa = (
        f"Dispõe sobre a abertura de Crédito Adicional {dados['tipo_lei']} na importância de "
        f"{format_currency(dados['total_credito'])} ({extenso_brl(dados['total_credito'])}), "
        f"e dá outras providências."
    )
    adicionar_ementa(doc, ementa)

    # =============================
    # INTRODUÇÃO
    # =============================
    doc.add_paragraph(
        f"O Prefeito Municipal de {dados['municipio']}, no uso de suas atribuições legais,\n\n"
        "DECRETA:"
    )

    # =============================
    # ARTIGO 1º - CRÉDITOS
    # =============================
    doc.add_paragraph(
        f"Art. 1º Fica o Poder Executivo autorizado a abrir um Crédito Adicional "
        f"{dados['tipo_lei']} no valor de {format_currency(dados['total_credito'])} "
        f"({extenso_brl(dados['total_credito'])}), para as seguintes dotações:"
    )

    adicionar_lista_creditos(doc, dados['itens_credito'])

    doc.add_paragraph(f"\nTotal: {format_currency(dados['total_credito'])}")

    # =============================
    # ARTIGO 2º - FONTES
    # =============================
    doc.add_paragraph(
        "Art. 2º Para cobertura do crédito aberto no artigo anterior, "
        "serão utilizados recursos provenientes de:"
    )

    if dados['val_sup'] > 0:
        doc.add_paragraph(
            f"- Superávit Financeiro apurado no exercício anterior: {format_currency(dados['val_sup'])}"
        )

    if dados['val_exc'] > 0:
        doc.add_paragraph(
            f"- Excesso de Arrecadação: {format_currency(dados['val_exc'])}"
        )

    if dados['itens_anulacao']:
        adicionar_lista_anulacoes(doc, dados['itens_anulacao'])

    # =============================
    # ARTIGO 3º - PPA / LDO
    # =============================
    doc.add_paragraph(
        f"Art. 3º Ficam alterados os anexos correspondentes do Plano Plurianual – {dados['ppa']} "
        f"e da Lei de Diretrizes Orçamentárias – {dados['ldo']}."
    )

    # =============================
    # ARTIGO 4º - VIGÊNCIA
    # =============================
    doc.add_paragraph(
        "Art. 4º Este Decreto entra em vigor na data de sua publicação, "
        "revogadas as disposições em contrário."
    )

    # =============================
    # DATA E ASSINATURA
    # =============================
    adicionar_data_assinatura(doc, dados['municipio'], dados['prefeito'])

    # =============================
    # JUSTIFICATIVA (opcional)
    # =============================
    if dados.get("justificativa"):
        doc.add_page_break()
        p = doc.add_paragraph("JUSTIFICATIVA")
        p.runs[0].bold = True
        p.alignment = 1
        doc.add_paragraph(dados["justificativa"])

    # =============================
    # SALVAR
    # =============================
    return salvar_docx(doc)
