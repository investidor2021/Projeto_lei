import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import streamlit as st
import os

def get_connection():
    """
    Estabelece conexão com o Google Sheets usando 'credenciais.json'.
    Retorna o cliente gspread autenticado ou None se falhar.
    """
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    
    creds_file = "credenciais.json"
    
    if not os.path.exists(creds_file):
        st.error(f"⚠️ Arquivo '{creds_file}' não encontrado na pasta do projeto.")
        return None

    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
        client = gspread.authorize(creds)
        return client
    except Exception as e:
        st.error(f"Erro ao autenticar no Google Sheets: {e}")
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
