import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import streamlit as st
import os

def get_connection():
    """
    Estabelece conexão com o Google Sheets.
    Suporta dois métodos:
    1. Streamlit Secrets (para deploy no Streamlit Cloud)
    2. Arquivo credenciais.json (para desenvolvimento local)
    
    Retorna o cliente gspread autenticado ou None se falhar.
    """
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    
    # Método 1: Tenta usar Streamlit Secrets (para deploy)
    try:
        if "gcp_service_account" in st.secrets:
            creds = ServiceAccountCredentials.from_json_keyfile_dict(
                st.secrets["gcp_service_account"],
                scope
            )
            client = gspread.authorize(creds)
            return client
    except Exception:
        pass  # Se falhar, tenta o método 2
    
    # Método 2: Usa arquivo local credenciais.json (para desenvolvimento)
    creds_file = "credenciais.json"
    
    if not os.path.exists(creds_file):
        st.error("❌ Arquivo credenciais.json não encontrado e Streamlit Secrets não configurado!")
        st.info("💡 Para desenvolvimento local: adicione o arquivo credenciais.json")
        st.info("💡 Para deploy: configure os Secrets no Streamlit Cloud")
        return None

    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
        client = gspread.authorize(creds)
        return client
    except Exception as e:
        st.error(f"❌ Erro ao autenticar no Google Sheets: {e}")
        return None

def get_data_from_sheets(sheet_key, worksheet_name="dotacao"):
    """
    Busca dados de uma planilha/aba específica e retorna um DataFrame.
    """
    client = get_connection()
    if not client:
        return None

    try:
        spreadsheet = client.open_by_key(sheet_key)
        sheet = spreadsheet.worksheet(worksheet_name)
        data = sheet.get_all_values()
        
        if not data:
            st.warning("A planilha está vazia.")
            return None

        # Assume que a primeira linha é o cabeçalho
        headers = data[0]
        rows = data[1:]
        df = pd.DataFrame(rows, columns=headers)
        return df

    except Exception as e:
        st.error(f"Erro ao ler a planilha: {e}")
        return None

def get_projetos_atividades(sheet_key, worksheet_name="projetos"):
    """
    Busca dados de projetos/atividades de uma aba específica.
    Retorna um dicionário no formato: {"XXXX": "Nome do Projeto/Atividade"}
    
    Espera-se que a planilha tenha 2 colunas:
    - Coluna A: Código (ex: "2051")
    - Coluna B: Descrição (ex: "MANUTENÇÃO DAS ATIVIDADES DA SAÚDE")
    """
    client = get_connection()
    if not client:
        return {}

    try:
        spreadsheet = client.open_by_key(sheet_key)
        sheet = spreadsheet.worksheet(worksheet_name)
        data = sheet.get_all_values()
        
        if not data or len(data) < 2:
            return {}

        # Pula o cabeçalho e cria o dicionário
        projetos = {}
        for row in data[1:]:  # Pula primeira linha (cabeçalho)
            if len(row) >= 2 and row[0].strip():
                codigo = row[0].strip()
                descricao = row[1].strip()
                projetos[codigo] = descricao
        
        return projetos

    except Exception as e:
        # Retorna dicionário vazio se a aba não existir ou houver erro
        # Isso permite que o sistema funcione mesmo sem a aba de projetos
        return {}

def get_aplicacoes(sheet_key, worksheet_name="aplicacoes"):
    """
    Busca dados de aplicações de uma aba específica.
    Retorna um dicionário no formato: {"XXXX": "Descrição da Aplicação"}
    
    Espera-se que a planilha tenha 2 colunas:
    - Coluna A: Código (ex: "0265")
    - Coluna B: Descrição (ex: "APLICAÇÃO ESPECÍFICA")
    """
    client = get_connection()
    if not client:
        return {}

    try:
        spreadsheet = client.open_by_key(sheet_key)
        sheet = spreadsheet.worksheet(worksheet_name)
        data = sheet.get_all_values()
        
        if not data or len(data) < 2:
            return {}

        # Pula o cabeçalho e cria o dicionário
        aplicacoes = {}
        for row in data[1:]:  # Pula primeira linha (cabeçalho)
            if len(row) >= 2 and row[0].strip():
                codigo = row[0].strip()
                descricao = row[1].strip()
                aplicacoes[codigo] = descricao
        
        return aplicacoes

    except Exception as e:
        # Retorna dicionário vazio se a aba não existir ou houver erro
        return {}


def add_projeto_atividade(sheet_key, worksheet_name, codigo, nome):
    """
    Adiciona um novo projeto/atividade na planilha do Google Sheets.
    
    Args:
        sheet_key: ID da planilha
        worksheet_name: Nome da aba (ex: "projetos")
        codigo: Código do projeto (ex: "2.126")
        nome: Nome do projeto (ex: "Manutenção da Saúde")
    """
    try:
        client = get_connection()
        if not client:
            raise Exception("Não foi possível conectar ao Google Sheets")
        
        sheet = client.open_by_key(sheet_key)
        worksheet = sheet.worksheet(worksheet_name)
        
        # Adiciona nova linha com código e nome
        worksheet.append_row([codigo, nome])
        
        return True
    
    except Exception as e:
        raise Exception(f"Erro ao salvar projeto: {str(e)}")
