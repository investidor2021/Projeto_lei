import streamlit as st
import pandas as pd
import uuid
import io
from datetime import date

from doc_projeto_lei import gerar_projeto_lei
from doc_decreto import gerar_decreto
from doc_lei_final import gerar_lei_final
import data_processor


st.markdown("""
<style>

/* Altura padrão para botões */
div.stButton > button {
    height: 38px;
    border-radius: 8px;
    font-weight: 600;
}

/* Altura padrão para inputs */
div[data-baseweb="input"] > div {
    height: 38px;
    border-radius: 8px;
}

/* Centralizar conteúdo do st.info */
div.stAlert {
    min-height: 38px;
    display: flex;
    align-items: center;
    border-radius: 8px;
    padding-top: 6px;
    padding-bottom: 6px;
}

/* Remove espaço extra do number_input */
div[data-baseweb="input"] input {
    padding-top: 6px;
    padding-bottom: 6px;
}

/* Deixa tudo mais alinhado verticalmente */
div.row-widget.stHorizontal {
    align-items: center;
}

/* Botão mais moderno */
div.stButton > button:hover {
    transform: scale(1.02);
    transition: 0.1s ease-in-out;
}

</style>
""", unsafe_allow_html=True)


# ===============================
# CONFIGURAÇÃO INICIAL
# ===============================
st.set_page_config(page_title="Gerador Legislativo", layout="wide")


st.title("🏛️ Gerador de Projetos, Leis e Decretos")

import sheets_client  # [NEW] Importação do client do Sheets
import audesp_codes

if "itens_credito" not in st.session_state:
    st.session_state.itens_credito = []
if "itens_anulacao" not in st.session_state:
    st.session_state.itens_anulacao = []

def abreviar_texto(texto):
    """Abrevia termos comuns para caber melhor no documento."""
    substituicoes = {
        "MANUTENÇÃO": "Manut.",
        "DESENVOLVIMENTO": "Desenv.",        
        "EDUCAÇÃO": "Educ.",
        "DEPARTAMENTO": "Depto.",
        "ENCARGOS": "Enc.",
        "SERVIÇOS": "Serv.",
        "INFRAESTRUTURA": "Infra.",
        "ADMINISTRAÇÃO": "Adm.",
        "SERVIÇOS":"Serv.",
        "TERCEIROS":"Terc.",
        "PESSOA FÍSICA":"PF",
        "PESSOA JURÍDICA":"PJ",
        "MATERIAL DE CONSUMO":"Mat. Cons.",
        "OUTROS BENEFÍCIOS ASSISTENCIAIS DO SERVIDOR E DO MILITAR":"Outros Ben. Assist. Serv. e Mil.",
        "VENCIMENTOS E VANTAGENS FIXAS - PESSOAL CIVIL":"Venc. e Vant. - P Civil",
        "DE":"de"


    }
    for original, abreviado in substituicoes.items():
        texto = texto.replace(original, abreviado)
    return texto

def formatar_moeda(valor):
    try:
        return f"{float(valor):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except:
        return "0,00"

def parse_moeda(valor_str):
    try:
        if isinstance(valor_str, str):
            limpo = valor_str.replace("R$", "").replace(" ", "").replace(".", "").replace(",", ".")
            if not limpo: return 0.0
            return float(limpo)
        return float(valor_str)
    except:
        return 0.0

def formatar_input(key):
    val_str = st.session_state.get(key, "")
    if val_str:
        val_float = parse_moeda(val_str)
        st.session_state[key] = formatar_moeda(val_float)

# ===============================
# FUNÇÕES AUXILIARES
# ===============================
def processar_planilha(file):
    df = pd.read_csv(file) if file.name.endswith(".csv") else pd.read_excel(file)
    df = df.iloc[1:].reset_index(drop=True)  # pula a primeira linha

    options = []
    for idx, row in df.iterrows():
        ficha = str(row.iloc[2]).strip()
        descricao = str(row.iloc[0]).strip()
        depto = str(row.iloc[1]).strip()
        nomedespesa = str(row.iloc[4]).strip()
        numdespesa = str(row.iloc[3]).strip()
        fonte = str(row.iloc[6]).strip()
        aplicacao = str(row.iloc[10]).strip()
        
        label = f"Ficha: {ficha} - {descricao} {numdespesa}.0{fonte}.{aplicacao} - {abreviar_texto(nomedespesa)} - {abreviar_texto(depto)}"
    
        
        options.append({
            "label": label,
            "label_docx": label,
            "id": f"{ficha}-{idx}",
            "ficha": ficha,
            "valor": 0.0
        })
    return options
    
    

def descricao_automatica(dotacao):
    # Versão inicial simples (depois você pode sofisticar)
    return f"Nova dotação criada automaticamente para {dotacao}"

# ===============================
# IDENTIFICAÇÃO
# ===============================
with st.expander("📄 1. Identificação", expanded=True):
    c1, c2, c3, c4, c5 = st.columns([1,1,1,1,1])

    tipo_doc = c1.radio("Tipo do Documento", ["Projeto de Lei", "Lei Finalizada", "Decreto"], horizontal=True)
    tipo_lei = c1.radio("Tipo de Crédito", ["Suplementar", "Especial"], horizontal=True)

    numero = c2.text_input("Número da Lei", placeholder="Ex: 5.182/2026")
    numero_projeto = c2.text_input("Número do Projeto", placeholder="Ex: 26/2026")
    municipio = c3.text_input("Município", "Vargem Grande do Sul")
    prefeito = c5.text_input("Prefeito", "CELSO LUIS RIBEIRO")
    
    secretaria = c5.text_input("Secretária", "RITA DE CÁSSIA CÔRTES FERRAZ")

    ppa = c4.text_input("PPA", "Lei n.º 5.144, de 21 de outubro de 2025")
    ldo = c4.text_input("LDO", "Lei n.º 5.112 de 18 de junho de 2025")
    
    # Campo de data
    data_doc = c3.date_input("Data do Documento", value=date.today())

# ===============================
# FONTES DE RECURSO
# ===============================
st.header("💰 2. Fontes de Recurso")

col_sup, col_exc, colrec = st.columns([1,1,2])

with col_sup:
    usa_sup = st.checkbox("Superávit Financeiro")
    val_sup_str = st.text_input("Valor Superávit", value=st.session_state.get("val_sup_str", "0,00"), key="val_sup_str", disabled=not usa_sup, on_change=lambda: formatar_input("val_sup_str"))
    val_sup = parse_moeda(val_sup_str)

with col_exc:
    usa_exc = st.checkbox("Excesso de Arrecadação")
    val_exc_str = st.text_input("Valor Excesso", value=st.session_state.get("val_exc_str", "0,00"), key="val_exc_str", disabled=not usa_exc, on_change=lambda: formatar_input("val_exc_str"))
    val_exc = parse_moeda(val_exc_str)

with colrec:
    # Label invisível para alinhar com os checkboxes
    #st.markdown("&nbsp;", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    
    # Se excesso estiver marcado, mostrar campo de origem
    origem_recursos = ""
    if usa_exc:
        origem_recursos = st.text_input(
            "Origem dos Recursos",
            placeholder="Ex: Proposta nº 63000724740202600, destinada ao custeio...",
            help="Informe a origem específica (proposta, convênio, etc.)",
            label_visibility="visible"
        )


# ===============================
# PLANILHA
# ===============================
# ===============================
# PLANILHA (Carregamento Automático)
# ===============================

# Se não estiver no session state, tenta carregar automaticamente
if "df_planilha" not in st.session_state:
    DEFAULT_SHEET_ID = "1EJN2eziO3rpv2KFavAMIJbD7UQyZZOChGLXt81VTHww"
    with st.spinner("Conectando automaticamente ao Google Sheets..."):
        df = sheets_client.get_data_from_sheets(DEFAULT_SHEET_ID, "dotacao")
        if df is not None:
             st.session_state["df_planilha"] = df
             st.success("Planilha carregada automaticamente!")
        else:
             st.error("Falha ao carregar planilha automaticamente. Verifique as credenciais.")

# Recupera do session state
df_planilha = st.session_state.get("df_planilha", None)

if st.button("🔄 Recarregar Dados da Planilha"):
    DEFAULT_SHEET_ID = "1EJN2eziO3rpv2KFavAMIJbD7UQyZZOChGLXt81VTHww"
    with st.spinner("Recarregando..."):
        df = sheets_client.get_data_from_sheets(DEFAULT_SHEET_ID, "dotacao")
        if df is not None:
             st.session_state["df_planilha"] = df
             st.rerun()

# Lógica de processamento comum (adaptada para usar o DF já carregado)
def processar_dataframe(df):
    options = []
    for idx, row in df.iterrows():
        # Adaptação para garantir que acessamos as colunas corretas pelo índice
        # O código original usava iloc com índices fixos. Vamos manter, assumindo que a estrutura da planilha online é igual.
        try:
            ficha = str(row.iloc[2]).strip()
            descricao = str(row.iloc[0]).strip()
            depto = str(row.iloc[1]).strip()
            nomedespesa = str(row.iloc[4]).strip()
            numdespesa = str(row.iloc[3]).strip()
            fonte = str(row.iloc[6]).strip()
            aplicacao = str(row.iloc[14]).strip()
            
            label = f"Ficha: {ficha} - {descricao} {numdespesa}.0{fonte}.{aplicacao} - {abreviar_texto(nomedespesa)} - {abreviar_texto(depto)}"
        
            options.append({
                "label": label,
                "label_docx": label,
                "id": f"{ficha}-{idx}",
                "ficha": ficha,
                "valor": 0.0,
                # Campos brutos para o DOCX
                "descricao": descricao,
                "depto": depto,
                "nomedespesa": nomedespesa,
                "numdespesa": numdespesa,
                "fonte": fonte,
                "aplicacao": aplicacao
            })
        except Exception as e:
            # Caso a linha esteja vazia ou incompleta
            continue
            
    return options

opcoes_planilha = []
if df_planilha is not None:
    todas = processar_dataframe(df_planilha)
    usados = st.session_state.itens_credito + st.session_state.itens_anulacao
    
    # Função auxiliar local, duplicada pois a original estava dentro de um if
    def filtrar_opcoes_livres(opcoes, usados):
        usados_ids = {i["id"] for i in usados}
        return [o for o in opcoes if o["id"] not in usados_ids]
        
    opcoes_planilha = filtrar_opcoes_livres(todas, usados)

# ===============================
# CRÉDITO
# ===============================
colcred, colanul = st.columns(2)

with colcred:
    st.header("➕ 3. Crédito")
    if tipo_lei == "Suplementar":
       
        col1, col2, col3 = st.columns([5, 1, 1])

        with col1:
            item = st.selectbox("Escolha a ficha", options=opcoes_planilha, format_func=lambda x: x["label"])

        with col2:
            valor_str = st.text_input("Valor R$", value=st.session_state.get("valor_credito_simples_str", "0,00"), key="valor_credito_simples_str", on_change=lambda: formatar_input("valor_credito_simples_str"))
            valor = parse_moeda(valor_str)

        with col3:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("➕", use_container_width=True, key="btn_add_credito_simples"):
                if item:
                    novo = {**item, "valor": valor}
                    st.session_state.itens_credito.append(novo)
                    st.success("Crédito adicionado!")
                else:
                    st.warning("Selecione uma ficha válida para crédito.")

    else:
        st.info("Preencha os dados abaixo.")
        # import audesp_codes


# ===============================
# ANULAÇÃO (sempre pela planilha)
# ===============================
with colanul:
    st.header("➖ 4. Anulação")

    if opcoes_planilha:
        col1, col2, col3 = st.columns([5,1,1])

        with col1:
            item_a = st.selectbox("Escolha a ficha para anulação", options=opcoes_planilha, format_func=lambda x: x["label"])
        
        with col2:
            valor_a_str = st.text_input("Valor R$", value=st.session_state.get("valor_anulacao_str", "0,00"), key="valor_anulacao_str", on_change=lambda: formatar_input("valor_anulacao_str"))
            valor_a = parse_moeda(valor_a_str)

        with col3:
            st.markdown("<br>", unsafe_allow_html=True)
            
            if st.button("➕", use_container_width=True, key="btn_add_anulacao"):
                if item_a:
                    novo = {**item_a, "valor": valor_a}
                    st.session_state.itens_anulacao.append(novo)
                    st.success("Anulação adicionada!")
                else:
                    st.warning("Selecione uma ficha válida para anulação.")

# ===============================
# CRÉDITO ESPECIAL (FULL WIDTH)
# ===============================
if tipo_lei == "Especial":
    #st.subheader("Crédito Especial - Construtor Completo de Dotação AUDESP")
    
    # Importar o módulo de códigos AUDESP
    # import audesp_codes

     # Carregar dados dinâmicos da planilha
    DEFAULT_SHEET_ID = "1EJN2eziO3rpv2KFavAMIJbD7UQyZZOChGLXt81VTHww"

    if "projetos_atividades" not in st.session_state:
        projetos_sheets = sheets_client.get_projetos_atividades(DEFAULT_SHEET_ID, "projetos")
        st.session_state["projetos_atividades"] = projetos_sheets

    if "aplicacoes_disponiveis" not in st.session_state:
        aplicacoes_sheets = sheets_client.get_aplicacoes(DEFAULT_SHEET_ID, "aplicacoes")
        st.session_state["aplicacoes_disponiveis"] = aplicacoes_sheets

    projetos_disponiveis = st.session_state.get("projetos_atividades", {})
    aplicacoes_disponiveis = st.session_state.get("aplicacoes_disponiveis", {})

    # Valores padrão se não houver na planilha
    if not projetos_disponiveis:
        projetos_disponiveis = {
            "0126": "ATIVIDADE - MANUTENÇÃO ADMINISTRATIVA",
            "0001": "PROJETO - INFRAESTRUTURA",
            "0051": "ATIVIDADE - MANUTENÇÃO OPERACIONAL"
        }

    if not aplicacoes_disponiveis:
        aplicacoes_disponiveis = {
            "0001": "APLICAÇÃO GERAL",
            "0265": "APLICAÇÃO FUNDEB",
            "0100": "APLICAÇÃO SAÚDE"
        }

    # Toggle para modo avançado
    #modo_avancado = st.checkbox("🔧 Modo Avançado (mostrar todos os componentes)", value=False)
    
    #if not modo_avancado:
    #    st.info("💡 **Modo Simplificado**: Preencha apenas os componentes principais. Os demais usarão valores padrão.")

    st.markdown("---")

    # ===== COMPONENTES PRINCIPAIS (sempre visíveis) =====
    st.markdown("### 📋 Itens da nova dotação")

    col1, col2, col3, col4   = st.columns([1,0.75,0.5,0.75])

    with col1:
    # Departamento
        opcoes_depto = audesp_codes.obter_opcoes_departamento()
        depto_selecionado = st.selectbox(
            "Departamento",
            options=[cod for cod, _ in opcoes_depto],
            format_func=lambda x: next(label for cod, label in opcoes_depto if cod == x),
            key="depto_completo"
        )
       

    with col2:
    # Subfunção
        opcoes_subfuncao = audesp_codes.obter_opcoes_subfuncao()
        subfuncao_selecionada = st.selectbox(
            "Subfunção",
            options=[cod for cod, _ in opcoes_subfuncao],
            format_func=lambda x: next(label for cod, label in opcoes_subfuncao if cod == x),
            key="subfuncao_completo"
        )

        
    with col3:
    # Função
        opcoes_funcao = audesp_codes.obter_opcoes_funcao()
        funcao_selecionada = st.selectbox(
            "Função",
            options=[cod for cod, _ in opcoes_funcao],
            format_func=lambda x: next(label for cod, label in opcoes_funcao if cod == x),
            key="funcao_completo"
        )

    with col4:
         # Programa
        opcoes_programa = audesp_codes.obter_opcoes_programa()
        programa_selecionado = st.selectbox(
            "Programa",
            options=[cod for cod, _ in opcoes_programa],
            format_func=lambda x: next(label for cod, label in opcoes_programa if cod == x),
            key="programa_completo"
        )    
    
    col1, col2, col3 = st.columns([2,4,1])
    
    with col1:
         # Número do Projeto/Atividade com opção manual
        modo_projeto = st.radio(
            "Projeto/Atividade",
            options=["Selecionar da lista", "Digitar manualmente"],
            key="modo_projeto",
            horizontal=True
        )    
    
    with col2:
        if modo_projeto == "Selecionar da lista":
            opcoes_num_projeto = [(cod, f"{cod} - {nome}") for cod, nome in sorted(projetos_disponiveis.items())]
            num_projeto_selecionado = st.selectbox(
                "Número Proj/Ativ",
                options=[cod for cod, _ in opcoes_num_projeto],
                format_func=lambda x: next(label for cod, label in opcoes_num_projeto if cod == x),
                key="num_projeto_completo"
            )
        else:
        # Entrada manual
            col_cod, col_nome = st.columns([1, 5])
            with col_cod:
                num_projeto_selecionado = st.text_input(
                    "Código",
                    placeholder="Ex: 2.126",
                    key="num_projeto_manual_cod"
            )
            with col_nome:
                nome_projeto_manual = st.text_input(
                    "Nome do Projeto/Atividade",
                    placeholder="Ex: Manutenção da Saúde",
                    key="num_projeto_manual_nome"
            )
        
        # Validação: verificar se o código já existe
            if num_projeto_selecionado and num_projeto_selecionado in projetos_disponiveis:
                st.info(f"ℹ️ Este código já existe na planilha: **{projetos_disponiveis[num_projeto_selecionado]}**")
       
        with col3:
            st.write("")
            st.write("")
        # Botão para salvar na planilha
            if st.button("💾 Salvar na Planilha", key="salvar_projeto"):
                if num_projeto_selecionado and nome_projeto_manual:
                # Verificar novamente se já existe antes de salvar
                    if num_projeto_selecionado in projetos_disponiveis:
                        st.warning(f"⚠️ Código {num_projeto_selecionado} já existe: {projetos_disponiveis[num_projeto_selecionado]}")
                    else:
                        try:
                        # Salvar na planilha do Google Sheets
                            sheets_client.add_projeto_atividade(
                                DEFAULT_SHEET_ID,
                                "projetos",
                                num_projeto_selecionado,
                                nome_projeto_manual
                            )
                        # Atualizar session state
                            st.session_state["projetos_atividades"][num_projeto_selecionado] = nome_projeto_manual
                            projetos_disponiveis[num_projeto_selecionado] = nome_projeto_manual
                            st.success(f"✅ Projeto {num_projeto_selecionado} - {nome_projeto_manual} salvo!")
                            st.rerun()
                        except Exception as e:
                            st.error(f"Erro ao salvar: {str(e)}")
                else:
                    st.warning("Preencha código e nome do projeto")
    
    

    # ===== MODO DE ELEMENTO DE DESPESA =====
    #st.markdown("---")
    
    col_modo, col_elem, col_fonte, col_aplic  = st.columns([1,2,0.5,1.5])

    with col_modo:
        modo_elemento = st.radio(
            "Modo de seleção",
            options=["Simplificado", "Completo"],
            horizontal=True,
            help="Simplificado: código completo pronto. Completo: preencher cada campo separadamente."
        )
    
    if modo_elemento == "Simplificado":
        # Modo simplificado: elemento, fonte e aplicação em 3 colunas
        
        
        with col_elem:
            opcoes_elemento_simp = audesp_codes.obter_opcoes_elemento_simplificado()
            elemento_completo_selecionado = st.selectbox(
                "Elemento de Despesa (Código Completo)",
                options=[cod for cod, _ in opcoes_elemento_simp],
                format_func=lambda x: next(label for cod, label in opcoes_elemento_simp if cod == x),
                key="elemento_simplificado",
                help="Código completo no formato Cat.Grupo.Mod.Elem.Desdobr"
            )
        
        with col_fonte:
            opcoes_fonte = audesp_codes.obter_opcoes_fonte()
            fonte_selecionada = st.selectbox(
                "Fonte de Recursos",
                options=[cod for cod, _ in opcoes_fonte],
                format_func=lambda x: next(label for cod, label in opcoes_fonte if cod == x),
                key="fonte_simplificado"
            )
        
        with col_aplic:
            opcoes_aplicacao = audesp_codes.obter_opcoes_aplicacao()
            aplicacao_selecionada = st.selectbox(
                "Código Aplicação",
                options=[cod for cod, _ in opcoes_aplicacao],
                format_func=lambda x: next(label for cod, label in opcoes_aplicacao if cod == x),
                key="aplicacao_simplificado"
            )
        
        # Extrair componentes do código completo
        # Formato: 3.1.90.11.00 = Cat.Grupo.Mod.Elem.Desdobr
        partes = elemento_completo_selecionado.split(".")
        cat_econ_selecionada = partes[0]
        grupo_desp_selecionado = partes[1]
        modalidade_selecionada = partes[2]
        elemento_selecionado = partes[3]
        desdobramento = ".".join(partes[4:]) if len(partes) > 4 else "00"
        
        # Grupo de natureza fixo (Atividade)
        grupo_nat_selecionado = "3"
        
    else:
        # Modo completo: todos os campos individuais
        st.markdown("---")
        st.markdown("### 🔬 Natureza da Despesa")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # Categoria Econômica
            opcoes_cat_econ = audesp_codes.obter_opcoes_categoria_economica()
            cat_econ_selecionada = st.selectbox(
                "Categoria Econômica",
                options=[cod for cod, _ in opcoes_cat_econ],
                format_func=lambda x: next(label for cod, label in opcoes_cat_econ if cod == x),
                key="cat_econ_completo"
            )
            
            # Grupo de Despesa
            opcoes_grupo_desp = audesp_codes.obter_opcoes_grupo_despesa()
            grupo_desp_selecionado = st.selectbox(
                "Grupo de Despesa",
                options=[cod for cod, _ in opcoes_grupo_desp],
                format_func=lambda x: next(label for cod, label in opcoes_grupo_desp if cod == x),
                key="grupo_desp_completo"
            )
        
        with col2:
            # Modalidade de Aplicação
            opcoes_modalidade = audesp_codes.obter_opcoes_modalidade()
            modalidade_selecionada = st.selectbox(
                "Modalidade de Aplicação",
                options=[cod for cod, _ in opcoes_modalidade],
                format_func=lambda x: next(label for cod, label in opcoes_modalidade if cod == x),
                key="modalidade_completo",
                index=list(dict(opcoes_modalidade).keys()).index("90") if "90" in dict(opcoes_modalidade) else 0
            )
            
            # Elemento de Despesa
            opcoes_elemento = audesp_codes.obter_opcoes_elemento()
            elemento_selecionado = st.selectbox(
                "Elemento de Despesa",
                options=[cod for cod, _ in opcoes_elemento],
                format_func=lambda x: next(label for cod, label in opcoes_elemento if cod == x),
                key="elemento_completo"
            )
        
        with col3:
            # Desdobramento
            desdobramento = st.text_input(
                "Desdobramento",
                value="00.00.00.00.00",
                key="desdobramento_completo",
                help="Formato: XX.XX.XX.XX.XX"
            )
            
            # Fonte de Recursos
            opcoes_fonte = audesp_codes.obter_opcoes_fonte()
            fonte_selecionada = st.selectbox(
                "Fonte de Recursos",
                options=[cod for cod, _ in opcoes_fonte],
                format_func=lambda x: next(label for cod, label in opcoes_fonte if cod == x),
                key="fonte_completo"
            )
        
        # Aplicação
        opcoes_aplicacao = [(cod, f"{cod} - {nome}") for cod, nome in sorted(aplicacoes_disponiveis.items())]
        aplicacao_selecionada = st.selectbox(
            "Aplicação",
            options=[cod for cod, _ in opcoes_aplicacao],
            format_func=lambda x: next(label for cod, label in opcoes_aplicacao if cod == x),
            key="aplicacao_completo"
        )
        
        # Grupo de natureza fixo (Atividade)
        grupo_nat_selecionado = "3"

    # Compor o código completo
    dotacao_completa = audesp_codes.compor_dotacao_completa(
        depto_selecionado,
        funcao_selecionada,
        subfuncao_selecionada,
        programa_selecionado,
        num_projeto_selecionado,
        cat_econ_selecionada,
        grupo_desp_selecionado,
        modalidade_selecionada,
        elemento_selecionado,
        desdobramento,
        fonte_selecionada,
        aplicacao_selecionada
    )

    # Obter nome do elemento e departamento para descrição
    if modo_elemento == "Simplificado":
        # Extrair nome do elemento do código completo
        elemento_nome = next((nome for cod, nome in audesp_codes.obter_opcoes_elemento_simplificado() if cod == elemento_completo_selecionado), "")
        # Remover o código do início
        elemento_nome = elemento_nome.split(" - ", 1)[1] if " - " in elemento_nome else elemento_nome
    else:
        # Buscar nome do elemento
        elemento_nome = audesp_codes.ELEMENTOS_DESPESA_DETALHADOS.get(elemento_selecionado, "")

    # Buscar nome do departamento
    depto_nome = audesp_codes.DEPARTAMENTOS.get(depto_selecionado, "")

    # Montar descrição no formato DOCX
    descricao_docx = f"{dotacao_completa} - {elemento_nome} - {depto_nome}"

    # Exibir o código completo e descrição
    st.markdown("---")

    st.markdown("### 📋 Código da Dotação Orçamentária Completo")

    col1, col2, col3, col4  = st.columns([10,2,0.5,0.5])

    with col1:
      st.write("")
      
      st.info(descricao_docx)

    
    with col2:
        st.write("")
        #st.markdown("<br>", unsafe_allow_html=True)        
        
        # Função de callback para formatar o valor
        def formatar_valor():
            val_str = st.session_state.get("valor_credito_completo_str", "")
            if val_str:
                val_float = parse_moeda(val_str)
                st.session_state["valor_credito_completo_str"] = formatar_moeda(val_float)

        # Input de texto que formata ao perder o foco (Enter/Tab)
        valor_str = st.text_input(
            "Valor", 
            value="0,00" if "valor_credito_completo_str" not in st.session_state else st.session_state["valor_credito_completo_str"],
            key="valor_credito_completo_str",
            on_change=formatar_valor,
            label_visibility="collapsed"
        )
        
        # Converter para float para uso no backend
        valor = parse_moeda(valor_str)

    with col3:
        st.write("")
        adicionar = st.button("➕", use_container_width=False, key="btn_add_credito_completo")

    if adicionar:
        item_manual = {
            "label": descricao_docx,
            "label_docx": descricao_docx,
            "id": f"manual-{uuid.uuid4()}",
            "ficha": dotacao_completa,
            "valor": valor
        }
        st.session_state.itens_credito.append(item_manual)
        st.success(f"✅ Crédito especial adicionado!\n\n**Código:** {dotacao_completa}")
    
    with col4:
        st.write("")
        recarregar = st.button("🔄", use_container_width= False)
        # Botão para recarregar dados da planilha
        if recarregar:
            projetos_sheets = sheets_client.get_projetos_atividades(DEFAULT_SHEET_ID, "projetos")
            aplicacoes_sheets = sheets_client.get_aplicacoes(DEFAULT_SHEET_ID, "aplicacoes")
            st.session_state["projetos_atividades"] = projetos_sheets
            st.session_state["aplicacoes_disponiveis"] = aplicacoes_sheets
            st.rerun()



st.header("📋 5. Resumo")
colcred, colanul = st.columns(2)

with colcred:
    # --- CRÉDITOS ---
    st.subheader("Créditos Adicionais")
    if st.session_state.itens_credito:
        # Cabeçalho da tabela
        c1, c2, c3 = st.columns([7, 2, 1])
        c1.markdown("**Descrição**")
        c2.markdown("**Valor**")
        c3.markdown("**Ação**")
        st.markdown("---")
        
        # Itens
        for idx, it in enumerate(st.session_state.itens_credito):
            c1, c2, c3 = st.columns([7, 2, 1])
            c1.text(it['label'])
            c2.text(f"R$ {it['valor']:,.2f}")
            if c3.button("❌", key=f"del_credito_{it['id']}"):
                st.session_state.itens_credito.pop(idx)
                st.rerun()
    else:
        st.info("Nenhum crédito adicionado.")

with colanul:
    # --- ANULAÇÕES ---
    st.subheader("Anulações de Dotações")
    if st.session_state.itens_anulacao:
        # Cabeçalho da tabela
        c1, c2, c3 = st.columns([7, 2, 1])
        c1.markdown("**Descrição**")
        c2.markdown("**Valor**")
        c3.markdown("**Ação**")
        st.markdown("---")
        
        # Itens
        for idx, it in enumerate(st.session_state.itens_anulacao):
            c1, c2, c3 = st.columns([7, 2, 1])
            c1.text(it['label'])
            c2.text(f"R$ {it['valor']:,.2f}")
            if c3.button("❌", key=f"del_anulacao_{it['id']}"):
                st.session_state.itens_anulacao.pop(idx)
                st.rerun()
    else:
        st.info("Nenhuma anulação adicionada.")

# --- FONTES ---
st.subheader("💰 Fontes de Recursos Detalhadas")

# Calcular totais
total_credito = sum(i["valor"] for i in st.session_state.itens_credito)
total_anulacao = sum(i["valor"] for i in st.session_state.itens_anulacao)
total_fontes = total_anulacao + val_sup + val_exc

col1, col2 = st.columns(2)

with col1:
    # Mostrar discriminação das fontes
    if val_sup > 0:
        c1, c2 = st.columns([6, 2])
        c1.text("Superávit Financeiro")
        c2.text(f"R$ {val_sup:,.2f}")

    if val_exc > 0:
        c1, c2 = st.columns([6, 2])
        c1.text(f"Excesso de Arrecadação ({origem_recursos if origem_recursos else 'Sem origem definida'})")
        c2.text(f"R$ {val_exc:,.2f}")

    if total_anulacao > 0:
        c1, c2 = st.columns([6, 2])
        c1.text("Anulação de Dotações")
        c2.text(f"R$ {total_anulacao:,.2f}")

with col2:
    st.markdown(f"### Total de Créditos: R$ {total_credito:,.2f}")
    st.markdown(f"### Total de Fontes: R$ {total_fontes:,.2f}")
    
    if round(total_credito, 2) == round(total_fontes, 2):
        st.success("✅ Valores batem!")
    else:
        st.error(f"❌ Diferença: R$ {total_credito - total_fontes:,.2f}")

st.markdown("---")

# ===============================
# JUSTIFICATIVA
# ===============================
st.header("✍️ 6. Justificativa")
justificativa = st.text_area("Digite a justificativa")

# ===============================
# GERAR DOCUMENTO
# ===============================
st.header("📥 7. Gerar Documento")

if st.button("Gerar DOCX"):
    if round(total_credito, 2) != round(total_fontes, 2):
        st.error("Os valores de crédito e fontes não batem. O financeiro surtou.")
    else:
        dados = {
            "tipo_lei": tipo_lei,
            "numero": numero,
            "numero_projeto": numero_projeto,
            "municipio": municipio,
            "prefeito": prefeito,
            "secretaria": secretaria,
            "ppa": ppa,
            "ldo": ldo,
            "val_sup": val_sup,
            "val_exc": val_exc,
            "origem_recursos": origem_recursos,
            "itens_credito": st.session_state.itens_credito,
            "itens_anulacao": st.session_state.itens_anulacao,
            "total_credito": total_credito,
            "justificativa": justificativa,
            "data_doc": data_doc
        }

        if tipo_doc == "Projeto de Lei":
            buffer = gerar_projeto_lei(dados)
        elif tipo_doc == "Lei Finalizada":
            buffer = gerar_lei_final(dados)
        else:
            buffer = gerar_decreto(dados)

        st.download_button(
            label="⬇️ Baixar Documento",
            data=buffer,
            file_name=f"{tipo_doc}_{numero}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
