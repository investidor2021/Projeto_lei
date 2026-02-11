import pandas as pd
from datetime import datetime, timedelta

def get_department_name(code):
    """
    Returns the department name based on the code.
    TODO: Update this dictionary with the actual 'De/Para' rules from the user.
    """
    # Placeholder mapping
    mapping = {
        # Example: "01": "Education",
    }
    # Return the code itself if no mapping is found, marked as 'Unknown'
    return mapping.get(str(code), f"DEP-{code}") 

def organize_sheet(file):
    """
    Reads an Excel or CSV file, extracts specific columns, 
    adds Department mapping, and calculates deadlines.
    """
    try:
        # Load data
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)
        
        # Define target columns by Excel letter (0-indexed)
        # D=3, F=5, H=7, J=9, K=10, W=22, AJ=35
        # We assume the user means the columns in the source file are at these positions.
        
        # Check if file has enough columns
        max_col_idx = 35
        if df.shape[1] <= max_col_idx:
            return None, f"Erro: A planilha tem apenas {df.shape[1]} colunas, mas precisamos da coluna AJ (índice 35)."

        # Extract specific columns using iloc
        # We start with D (3)
        # The user wants: D, F, H, J, K, W, AJ
        # Let's verify if the user meant specific headers or just positions. 
        # Usually exact positions are risky, but requested "Columns D, F..." implies position.
        
        col_indices = [3, 5, 7, 9, 10, 22, 35]
        
        # Select data
        result_df = df.iloc[:, col_indices].copy()
        
        # Get original column names to preserve or rename?
        # Let's stick to the extracted data. 
        # We might want to rename them for clarity if we knew what they were.
        # For now, keep original headers.
        
        # Insert "De/Para" (Department) after Column D (which is now at index 0 in result_df)
        # Column D is at result_df.columns[0]
        col_d_name = result_df.columns[0]
        
        # Apply mapping
        department_names = result_df[col_d_name].apply(get_department_name)
        
        # Insert at position 1 (after D)
        result_df.insert(1, "Departamento (De/Para)", department_names)
        
        # Date Logic (Column F)
        # In original file, F is index 5. In result_df, it was the second selected column, 
        # but we inserted one, so it is now at index 2?
        # Indices in result_df before insert: D(0), F(1), H(2)...
        # After insert: D(0), Dept(1), F(2), H(3)...
        
        col_f_name = result_df.columns[2] # This should be the Date column
        
        # Convert to datetime
        result_df[col_f_name] = pd.to_datetime(result_df[col_f_name], errors='coerce')
        
        # Calculate +90 days
        result_df["Prazo (90 dias)"] = result_df[col_f_name] + timedelta(days=90)
        
        # Status Check
        today = datetime.now()
        
        def check_status(deadline):
            if pd.isna(deadline):
                return "Data Inválida"
            
            days_remaining = (deadline - today).days
            
            if days_remaining < 0:
                return "Vencido"
            elif days_remaining <= 5: # Warning threshold
                return f"Vence em {days_remaining} dias"
            else:
                return "No Prazo"

        result_df["Status"] = result_df["Prazo (90 dias)"].apply(check_status)
        
        # Formatting Date Columns for display
        result_df[col_f_name] = result_df[col_f_name].dt.strftime('%d/%m/%Y')
        result_df["Prazo (90 dias)"] = result_df["Prazo (90 dias)"].dt.strftime('%d/%m/%Y')

        return result_df, None

    except Exception as e:
        return None, f"Erro ao processar planilha: {str(e)}"
