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

def gerar_decreto(dados):
    """
    Gera um Decreto em formato DOCX seguindo o modelo oficial.
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
    run = p_titulo.add_run(f"DECRETO N.º {dados['numero']}")
    run.bold = True
    run.font.size = Pt(12)
    
    # =============================
    # EMENTA
    # =============================
    p_ementa = doc.add_paragraph()
    p_ementa.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p_ementa.add_run(f"Dispõe sobre a autorização para abertura de Crédito Adicional {dados['tipo_lei']}")
    run.font.size = Pt(12)
    
    # Espaço
    doc.add_paragraph()
    
    # =============================
    # INTRODUÇÃO
    # =============================
    p_intro = doc.add_paragraph()
    p_intro.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_intro.add_run(f"        O Prefeito Municipal de {dados['municipio']}, Estado de São Paulo, usando de suas atribuições legais,")
    
    # Espaço
    doc.add_paragraph()
    
    # DECRETA
    p_decreta = doc.add_paragraph()
    p_decreta.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run = p_decreta.add_run("         DECRETA:")
    run.bold = True
    
    # Espaço
    doc.add_paragraph()
    
    # =============================
    # ARTIGO 1º - CRÉDITOS
    # =============================
    p_art1 = doc.add_paragraph()
    p_art1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_art1.add_run(
        f"         Art.1º Fica o Executivo Municipal autorizado a abrir no Departamento de Finanças/ "
        f"Divisão de Controle Financeiro da Prefeitura, um Crédito Adicional {dados['tipo_lei']} "
        f"na importância de {format_currency(dados['total_credito'])} ({extenso_brl(dados['total_credito'])}), "
        f"para atender as seguintes dotações:"
    )
    
    # Espaço
    doc.add_paragraph()
    
    # Tabela de créditos
    for item in dados['itens_credito']:
        p_item = doc.add_paragraph()
        p_item.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        
        # Ficha/código e descrição
        ficha = item.get('ficha', '')
        label = item.get('label', '')
        valor = item.get('valor', 0)
        
        # Formatar linha
        p_item.add_run(f"{ficha}\t{label}\t{format_currency(valor)}")
        p_item.paragraph_format.tab_stops.add_tab_stop(Cm(1))
        p_item.paragraph_format.tab_stops.add_tab_stop(Cm(15))
    
    # Total
    p_total = doc.add_paragraph()
    p_total.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p_total.add_run(f"TOTAL\t{format_currency(dados['total_credito'])}")
    run.bold = True
    
    # Espaço
    doc.add_paragraph()
    doc.add_paragraph()
    
    # =============================
    # ARTIGO 2º - ANULAÇÕES
    # =============================
    p_art2 = doc.add_paragraph()
    p_art2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_art2.add_run(
        "         Art.2º Para cobertura do crédito autorizado no artigo anterior serão anuladas as seguintes dotações:"
    )
    
    # Espaço
    doc.add_paragraph()
    
    # Tabela de anulações
    for item in dados['itens_anulacao']:
        p_item = doc.add_paragraph()
        p_item.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        
        ficha = item.get('ficha', '')
        label = item.get('label', '')
        valor = item.get('valor', 0)
        
        p_item.add_run(f"{ficha}\t{label}\t{format_currency(valor)}")
        p_item.paragraph_format.tab_stops.add_tab_stop(Cm(1))
        p_item.paragraph_format.tab_stops.add_tab_stop(Cm(15))
    
    # Total
    total_anulacao = sum(i['valor'] for i in dados['itens_anulacao'])
    p_total_anul = doc.add_paragraph()
    p_total_anul.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p_total_anul.add_run(f"TOTAL\t{format_currency(total_anulacao)}")
    run.bold = True
    
    # Espaço
    doc.add_paragraph()
    
    # =============================
    # ARTIGO 3º - PPA/LDO
    # =============================
    p_art3 = doc.add_paragraph()
    p_art3.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    # Extrair números das leis
    ldo_num = dados.get('ldo', '').split('nº')[1].strip() if 'nº' in dados.get('ldo', '') else dados.get('ldo', '')
    ppa_num = dados.get('ppa', '').split('nº')[1].strip() if 'nº' in dados.get('ppa', '') else dados.get('ppa', '')
    
    p_art3.add_run(
        f"         Art.3º As alterações promovidas nos artigos 1º e 2º do presente decreto, passam a fazer parte "
        f"da LDO nº {ldo_num} e PPA nº {ppa_num} visando atender ao disposto nos artigos 165 e 168 da CF, "
        f"artigo 2º da Instrução nº 2, do Tribunal de Contas do Estado de São Paulo, da LC 101, de 04 de maio de 2.000 e, "
        f"finalmente, para atender ao Projeto Audesp do Tribunal de Contas do Estado de São Paulo."
    )
    
    # Espaço
    p_art4_space = doc.add_paragraph()
    p_art4_space.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    # =============================
    # ARTIGO 4º - VIGÊNCIA
    # =============================
    p_art4 = doc.add_paragraph()
    p_art4.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_art4.add_run("       Art.4º Este decreto entra em vigor na data de sua publicação.")
    
    # Espaço
    p_local = doc.add_paragraph()
    p_local.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    # =============================
    # DATA E LOCAL
    # =============================
    hoje = datetime.now()
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 
             'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    data_extenso = f"{hoje.day} de {meses[hoje.month-1]} de {hoje.year}"
    
    p_data = doc.add_paragraph()
    p_data.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_data.add_run(f"        {dados['municipio']}, {data_extenso}.")
    
    # Espaço
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
    doc.add_paragraph()
    
    # =============================
    # REGISTRO E PUBLICAÇÃO
    # =============================
    p_registro = doc.add_paragraph()
    p_registro.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_registro.add_run(
        f"         Registrado e publicado na Secretaria Geral da Prefeitura Municipal de {dados['municipio']}, "
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
