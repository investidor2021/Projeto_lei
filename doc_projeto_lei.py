from docx import Document
from datetime import date
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from doc_base import (
    configurar_estilo, adicionar_titulo, adicionar_ementa,
    adicionar_data_assinatura, salvar_docx,
    format_currency, extenso_brl
)


def classify_expense_type(itens_credito):
    """
    Classifica as despesas em 'de capital', 'de custeio' ou ambas.
    Critério: 
      - Custeio: começa com '3' (Ex: 3.3.90.36)
      - Capital: começa com '4' (Ex: 4.4.90.52)
    """
    tem_custeio = False
    tem_capital = False
    
    for item in itens_credito:
        # Tenta pegar do campo bruto 'numdespesa', senão tenta extrair do label ou ficha
        # O ideal é usar o campo 'numdespesa' que adicionamos no main.py
        nd = item.get('numdespesa', '')
        if not nd:
             # Fallback simples: tenta achar no label algo que pareça um elemento de despesa (ex: 3.3.90)
             # Mas assumindo que o main.py foi atualizado corretemante, 'numdespesa' deve existir.
             pass
        
        # Limpa possível formatação extra
        nd = str(nd).strip()
        
        if nd.startswith('3'):
            tem_custeio = True
        elif nd.startswith('4'):
            tem_capital = True
            
    if tem_custeio and tem_capital:
        return "de capital e de custeio"
    elif tem_capital:
        return "de capital"
    elif tem_custeio:
        return "de custeio"
    else:
        return "de custeio e capital" # Default caso não identifique

def add_table_row(table, item, is_header=False):
    """
    Adiciona uma linha formatada na tabela.
    Layout esperado com 2 colunas:
    | Ficha...Completa... | Valor |
    """
    cells = table.add_row().cells

    # Dados brutos
    ficha = item.get('ficha', '')
    depto = item.get('depto', '')
    descricao = item.get('descricao', '') 
    numdespesa = item.get('numdespesa', '')
    nomedespesa = item.get('nomedespesa', '')
    fonte = item.get('fonte', '')
    aplicacao = item.get('aplicacao', '')

    # Formatar string completa da coluna 1
    # Ex: 6 - 01.02... 3.3.90... - OUTROS... - Manut...
    texto_completo = f"{ficha} - {descricao} {numdespesa}.0{fonte}.{aplicacao} - {nomedespesa} - {depto}"

    c0 = cells[0].paragraphs[0]
    c0.text = texto_completo
    c0.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    c1 = cells[1].paragraphs[0]
    val = format_currency(item.get('valor', 0))
    # Hack para remover o R$ e alinhar melhor se quiser, mas o usuário pediu "R$ 45.00"
    # Vamos manter o format_currency padrão
    c1.text = val
    c1.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    # Ajuste de fonte pra caber

    # Ajuste de fonte pra caber
    for c in cells:
        for p in c.paragraphs:
            for r in p.runs:
                r.font.size = Pt(8)
                r.font.name = 'Times New Roman'

def gerar_projeto_lei(dados):
    doc = Document()
    configurar_estilo(doc)
    
    # ---------------------------------------------------------
    # TÍTULO E EMENTA
    # ---------------------------------------------------------
    # Ex: Dispõe sobre a abertura de Crédito Adicional Especial
    
    # Espaço inicial
    doc.add_paragraph()
    
    p = doc.add_paragraph(f"Dispõe sobre a abertura de Crédito Adicional {dados['tipo_lei']}")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.runs[0].bold = True
    p.runs[0].font.size = Pt(12)
    
    doc.add_paragraph() # Espaço

    # ---------------------------------------------------------
    # PREÂMBULO
    # ---------------------------------------------------------
    # O Prefeito Municipal de Vargem Grande do Sul, Estado de São Paulo:
    # Faço saber que a Câmara Municipal decreta e eu sanciono a seguinte Lei:
    
    p = doc.add_paragraph(f"O Prefeito Municipal de {dados['municipio']}, Estado de São Paulo:")
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    doc.add_paragraph()
    
    p = doc.add_paragraph("Faço saber que a Câmara Municipal decreta e eu sanciono a seguinte Lei:")
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    doc.add_paragraph()

    # ---------------------------------------------------------
    # ARTIGO 1º
    # ---------------------------------------------------------
    # Art.1º Fica o Executivo Municipal autorizado a abrir no Departamento de Finanças desta Prefeitura, 
    # um Crédito Adicional Especial, na importância de R$ X (extenso), para atender contabilização 
    # de despesas de capital/custeio, na seguinte dotação:
    
    tipo_despesa_str = classify_expense_type(dados['itens_credito'])
    
    texto_art1 = (
        f"Art. 1º Fica o Executivo Municipal autorizado a abrir no Departamento de Finanças desta Prefeitura, "
        f"um Crédito Adicional {dados['tipo_lei']}, na importância de {format_currency(dados['total_credito'])} "
        f"({extenso_brl(dados['total_credito'])}), para atender contabilização de despesas {tipo_despesa_str}, "
        "na(s) seguinte(s) dotação(ões):"
    )
    
    p = doc.add_paragraph(texto_art1)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.first_line_indent = Cm(1.27)
    
    doc.add_paragraph() # Espaço antes da tabela

    # ---------------------------------------------------------
    # TABELA DE DOTAÇÕES
    # ---------------------------------------------------------
    # Criar tabela com 2 colunas
    table = doc.add_table(rows=1, cols=2)
    table.style = "Table Grid"
    table.allow_autofit = False 
    
    # Definindo larguras ~80% e ~20%
    # Total ~6.2in
    # Col 0: 5.0 in
    # Col 1: 1.25 in
    
    # Converted from 12.94cm and 2.67cm
    widths = [Cm(12.93), Cm(2.67)]
    
    for row in table.rows:
        for idx, width in enumerate(widths):
            row.cells[idx].width = width

    # Sem cabeçalho "Dotação" / "Valor" conforme pedido
    
    # Preencher itens
    for item in dados['itens_credito']:
        add_table_row(table, item)
        
    doc.add_paragraph()
    
    # Totais
    p = doc.add_paragraph(f"TOTAL   {format_currency(dados['total_credito'])}")
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p.runs[0].bold = True
    
    doc.add_paragraph()

    # ---------------------------------------------------------
    # ARTIGO 2º - FONTES (EXCESSO OU SUPERÁVIT)
    # ---------------------------------------------------------
    # Lógica combinada para gerar os artigos 2 e 3 baseado nas fontes, conforme modelo
    
    # Se houver EXCESSO:
    # Art.2° As despesas decorrentes desta lei serão suportadas com recursos provenientes de excesso de arrecadação, 
    # nos termos do inciso II, § 1º, do artigo 43, da Lei nº 4.320, de 17 de março de 1964...
    
    art_num = 2
    
    if dados['val_exc'] > 0:
        texto_exc = (
            f"Art. {art_num}º As despesas decorrentes desta lei serão suportadas com recursos provenientes de "
            f"excesso de arrecadação, nos termos do inciso II, § 1º, do artigo 43, da Lei nº 4.320, de 17 de março de 1964, "
            f"na importância de {format_currency(dados['val_exc'])} ({extenso_brl(dados['val_exc'])})."
        )
        p = doc.add_paragraph(texto_exc)
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.first_line_indent = Cm(1.27)
        doc.add_paragraph()
        art_num += 1
        
    # Se houver SUPERÁVIT:
    # Art. 3º As despesas decorrentes desta lei serão suportadas, ainda, com recursos provenientes do superávit financeiro...
    # inciso I, § 1º, do art. 43...
    
    if dados['val_sup'] > 0:
        conector = ", ainda," if dados['val_exc'] > 0 else ""
        texto_sup = (
            f"Art. {art_num}º As despesas decorrentes desta lei serão suportadas{conector} com recursos provenientes do "
            f"superávit financeiro, apurado na Prefeitura Municipal, nos termos do inc. I, § 1º, do art. 43, "
            f"da Lei n.º 4.320, de 17 de março de 1964, constituído pela diferença positiva entre o ativo e o passivo financeiro, "
            f"apurado no Balanço Patrimonial do exercício anterior, na importância de {format_currency(dados['val_sup'])} "
            f"({extenso_brl(dados['val_sup'])})."
        )
        p = doc.add_paragraph(texto_sup)
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.first_line_indent = Cm(1.27)
        doc.add_paragraph()
        art_num += 1

    # Se houver ANULAÇÃO (Redução de dotação):
    # Art. Xº ... suportadas por anulação parcial ou total das seguintes dotações... (inciso III)
    if dados['itens_anulacao']:
        conector = ", ainda," if (dados['val_exc'] > 0 or dados['val_sup'] > 0) else ""
        total_anul = sum(i['valor'] for i in dados['itens_anulacao'])
        texto_anul = (
             f" Art. {art_num}º As despesas decorrentes desta lei serão suportadas{conector} com recursos provenientes de "
             f"anulação parcial ou total de dotações orçamentárias, nos termos do inciso III, § 1º, do artigo 43, "
             f"da Lei nº 4.320, de 17 de março de 1964, na importância de {format_currency(total_anul)} "
             f"({extenso_brl(total_anul)}), conforme abaixo:"
        )
        p = doc.add_paragraph(texto_anul)
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.first_line_indent = Cm(1.27)
        
        # Tabela de anulação (2 colunas)
        table_a = doc.add_table(rows=1, cols=2)
        table_a.style = 'Table Grid'
        table_a.autofit = False
        widths = [Cm(12.93), Cm(2.67)]
        for row in table_a.rows:
            for idx, width in enumerate(widths):
                row.cells[idx].width = width
                
        # Sem cabeçalho
        for item in dados['itens_anulacao']:
            add_table_row(table_a, item)
            
        doc.add_paragraph()
        art_num += 1


    # ---------------------------------------------------------
    # ARTIGO PPA / LDO
    # ---------------------------------------------------------
    # Art. 4º Fica o Poder Executivo Municipal autorizado, ainda, a proceder à inclusão do projeto previsto nesta Lei...
    
    texto_ppa = (
        f"Art. {art_num}º Fica o Poder Executivo Municipal autorizado, ainda, a proceder à inclusão do projeto previsto nesta Lei, "
        f"no valor de {format_currency(dados['total_credito'])} ({extenso_brl(dados['total_credito'])}), "
        f"no Plano Plurianual - {dados['ppa']} e na Lei de Diretrizes Orçamentárias - {dados['ldo']}, "
        "em vigência neste exercício, para atender às alterações introduzidas pelo Sistema Audesp do Tribunal de Contas do Estado de São Paulo."
    )
    p = doc.add_paragraph(texto_ppa)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.first_line_indent = Cm(1.27)
    doc.add_paragraph()
    art_num += 1

    # ---------------------------------------------------------
    # ARTIGO VIGÊNCIA
    # ---------------------------------------------------------
    p = doc.add_paragraph(f"Art. {art_num}º Esta lei entra em vigor na data de sua publicação.")
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.first_line_indent = Cm(1.27)
    doc.add_paragraph()

    # ---------------------------------------------------------
    # DATA E ASSINATURA
    # ---------------------------------------------------------
    # Prefeitura Municipal de Vargem Grande do Sul,       de                 de 2025.
    
    meses = {1:'janeiro', 2:'fevereiro', 3:'março', 4:'abril', 5:'maio', 6:'junho',
             7:'julho', 8:'agosto', 9:'setembro', 10:'outubro', 11:'novembro', 12:'dezembro'}
    hoje = date.today()
    data_extenso = f"{dados['municipio']}, {hoje.day} de {meses[hoje.month]} de {hoje.year}."
    
    p = doc.add_paragraph(data_extenso)
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    
    doc.add_paragraph("\n\n")
    
    p = doc.add_paragraph(dados['prefeito'].upper())
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.runs[0].bold = True
    
    p = doc.add_paragraph("Prefeito Municipal")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # ---------------------------------------------------------
    # JUSTIFICATIVA (Opcional, em nova página)
    # ---------------------------------------------------------
    if dados.get("justificativa"):
        doc.add_page_break()
        p = doc.add_paragraph("JUSTIFICATIVA")
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].bold = True
        doc.add_paragraph("\n")
        
        p = doc.add_paragraph(dados["justificativa"])
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    return salvar_docx(doc)
