from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from datetime import datetime
import io

def format_currency(valor):
    """Formata valor monetário"""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def extenso_brl(valor):
    """Retorna valor por extenso (simplificado)"""
    # Implementação simplificada - você pode melhorar depois
    return f"{int(valor)} reais"

def gerar_lei_final(dados):
    """
    Gera a Lei Finalizada em formato DOCX seguindo o modelo oficial.
    """
    
    doc = Document()
    
    # Configurar margens
    sections = doc.sections
    for section in sections:
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin = Cm(3.0)
        section.right_margin = Cm(2.0)
    
    # =============================
    # TÍTULO
    # =============================
    p_titulo = doc.add_paragraph()
    p_titulo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p_titulo.add_run(f"LEI N.º {dados['numero']}")
    run.bold = True
    run.font.size = Pt(12)
    
    # Número do Projeto
    p_projeto = doc.add_paragraph()
    p_projeto.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p_projeto.add_run(f"Projeto de Lei n.º {dados.get('numero_projeto', '')}")
    run.font.size = Pt(11)
    
    # Espaço
    doc.add_paragraph()
    
    # =============================
    # EMENTA
    # =============================
    p_ementa = doc.add_paragraph()
    p_ementa.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p_ementa.add_run(f"Dispõe sobre a abertura de Crédito Adicional {dados['tipo_lei']}")
    run.font.size = Pt(12)
    
    # Espaço
    doc.add_paragraph()
    
    # =============================
    # INTRODUÇÃO
    # =============================
    p_intro = doc.add_paragraph()
    p_intro.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_intro.add_run(f"         O Prefeito Municipal de {dados['municipio']}, Estado de São Paulo:")
    
    # Espaço
    doc.add_paragraph()
    
    # Faço saber
    p_faco_saber = doc.add_paragraph()
    p_faco_saber.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_faco_saber.add_run("         Faço saber que a Câmara Municipal decreta e eu sanciono a seguinte Lei:")
    
    # Espaço
    doc.add_paragraph()
    
    # =============================
    # ARTIGO 1º - CRÉDITOS
    # =============================
    p_art1 = doc.add_paragraph()
    p_art1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    # Determinar finalidade baseado no tipo
    if dados['tipo_lei'] == 'Especial':
        finalidade = "para atender contabilização de despesas de custeio, na seguinte dotação:"
    else:
        finalidade = "para atender as seguintes dotações:"
    
    p_art1.add_run(
        f"         Art. 1º Fica o Executivo Municipal autorizado a abrir no Departamento de Finanças, "
        f"desta Prefeitura, um Crédito Adicional {dados['tipo_lei']}, na importância de "
        f"{format_currency(dados['total_credito'])} ({extenso_brl(dados['total_credito'])}), "
        f"{finalidade}"
    )
    
    # Espaço
    doc.add_paragraph()
    
    # Lista de créditos
    for item in dados['itens_credito']:
        p_item = doc.add_paragraph()
        p_item.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        
        ficha = item.get('ficha', '')
        label = item.get('label', '')
        valor = item.get('valor', 0)
        
        p_item.add_run(f"{ficha} – {label}\t{format_currency(valor)}")
        p_item.paragraph_format.tab_stops.add_tab_stop(Cm(15))
    
    # Total
    p_total = doc.add_paragraph()
    p_total.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = p_total.add_run(f"TOTAL\t{format_currency(dados['total_credito'])}")
    run.bold = True
    p_total.paragraph_format.tab_stops.add_tab_stop(Cm(15))
    
    # Espaço
    doc.add_paragraph()
    
    # =============================
    # ARTIGO 2º - FONTES
    # =============================
    p_art2 = doc.add_paragraph()
    p_art2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    # Verificar se há superávit ou anulações
    total_fontes = dados.get('val_sup', 0) + sum(i['valor'] for i in dados.get('itens_anulacao', []))
    
    if dados.get('val_sup', 0) > 0:
        # Artigo 2 com superávit financeiro
        p_art2.add_run(
            f"Art. 2º As despesas decorrentes desta lei serão suportadas, ainda, com recursos provenientes do "
            f"superávit financeiro, apurado na Prefeitura Municipal, nos termos do inc. I, § 1º, do art. 43, "
            f"da Lei n.º 4.320, de 17 de março de 1964, constituído pela diferença positiva entre o ativo e o "
            f"passivo financeiro, apurado no Balanço Patrimonial do exercício de 2025, na importância de "
            f"{format_currency(dados['val_sup'])} ({extenso_brl(dados['val_sup'])})."
        )
    elif dados.get('itens_anulacao'):
        # Artigo 2 com anulações
        p_art2.add_run(
            "Art. 2º Para cobertura do crédito autorizado no artigo anterior serão anuladas as seguintes dotações:"
        )
        
        # Espaço
        doc.add_paragraph()
        
        # Lista de anulações
        for item in dados['itens_anulacao']:
            p_item = doc.add_paragraph()
            p_item.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            
            ficha = item.get('ficha', '')
            label = item.get('label', '')
            valor = item.get('valor', 0)
            
            p_item.add_run(f"{ficha} – {label}\t{format_currency(valor)}")
            p_item.paragraph_format.tab_stops.add_tab_stop(Cm(15))
        
        # Total anulações
        total_anulacao = sum(i['valor'] for i in dados['itens_anulacao'])
        p_total_anul = doc.add_paragraph()
        p_total_anul.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p_total_anul.add_run(f"TOTAL\t{format_currency(total_anulacao)}")
        run.bold = True
        p_total_anul.paragraph_format.tab_stops.add_tab_stop(Cm(15))
    
    # Espaço
    doc.add_paragraph()
    
    # =============================
    # ARTIGO 3º - PPA/LDO
    # =============================
    p_art3 = doc.add_paragraph()
    p_art3.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    # Extrair informações das leis
    ldo_info = dados.get('ldo', '')
    ppa_info = dados.get('ppa', '')
    
    p_art3.add_run(
        f"Art. 3º Fica o Poder Executivo Municipal autorizado, ainda, a proceder à inclusão do projeto "
        f"previsto nesta Lei, no valor de {format_currency(dados['total_credito'])} "
        f"({extenso_brl(dados['total_credito'])}), no Plano Plurianual - {ppa_info} e na Lei de "
        f"Diretrizes Orçamentárias - {ldo_info}, em vigência neste exercício, para atender às alterações "
        f"introduzidas pelo Sistema Audesp do Tribunal de Contas do Estado de São Paulo."
    )
    
    # Espaço
    doc.add_paragraph()
    
    # =============================
    # ARTIGO 4º - VIGÊNCIA
    # =============================
    p_art4 = doc.add_paragraph()
    p_art4.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_art4.add_run("           Art. 4º Esta lei entra em vigor na data de sua publicação.")
    
    # Espaço
    doc.add_paragraph()
    
    # =============================
    # DATA E LOCAL
    # =============================
    hoje = datetime.now()
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 
             'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    data_extenso = f"{hoje.day} de {meses[hoje.month-1]} de {hoje.year}"
    
    p_data = doc.add_paragraph()
    p_data.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_data.add_run(f"Prefeitura Municipal de {dados['municipio']}, {data_extenso}.")
    
    # Espaço
    doc.add_paragraph()
    doc.add_paragraph()
    doc.add_paragraph()
    
    # =============================
    # ASSINATURA PREFEITO
    # =============================
    p_prefeito = doc.add_paragraph()
    p_prefeito.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p_prefeito.add_run(dados['prefeito'])
    run.bold = True
    
    # Espaço
    doc.add_paragraph()
    
    # =============================
    # REGISTRO E PUBLICAÇÃO
    # =============================
    p_registro = doc.add_paragraph()
    p_registro.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_registro.add_run(
        f"\tRegistrada e publicada na Secretaria Geral da Prefeitura Municipal de {dados['municipio']}, "
        f"Estado de São Paulo, em {data_extenso}."
    )
    
    # Espaço
    doc.add_paragraph()
    doc.add_paragraph()
    doc.add_paragraph()
    
    # =============================
    # ASSINATURA SECRETÁRIA
    # =============================
    p_secretaria = doc.add_paragraph()
    p_secretaria.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p_secretaria.add_run(dados.get('secretaria', 'RITA DE CÁSSIA CÔRTES FERRAZ'))
    run.bold = True
    
    # =============================
    # SALVAR
    # =============================
    buffer = io.BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer
