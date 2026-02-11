# ✅ Checklist Final - Deploy no Streamlit Cloud

## 📦 Arquivos Necessários (Todos Criados!)

- ✅ `requirements.txt` - Com todas as 7 dependências (incluindo num2words)
- ✅ `secrets.toml.example` - Template com suas credenciais convertidas
- ✅ `.gitignore` - Protege credenciais e arquivos temporários
- ✅ `README.md` - Documentação completa
- ✅ `LICENSE` - Licença MIT
- ✅ `sheets_client.py` - Atualizado para Streamlit Secrets

## 🚀 Passos para Deploy

### 1. Fazer Push para GitHub

```bash
cd "c:\projetos GitHub\Proj_lei\Projeto_lei"
git init
git add .
git status  # VERIFIQUE que credenciais.json NÃO aparece!
git commit -m "Initial commit: Sistema AUDESP completo"
git remote add origin https://github.com/SEU_USUARIO/SEU_REPO.git
git branch -M main
git push -u origin main
```

### 2. Configurar Streamlit Cloud

1. Acesse https://share.streamlit.io/
2. Clique em **New app**
3. Conecte seu repositório GitHub
4. Selecione:
   - **Repository**: seu-usuario/seu-repo
   - **Branch**: main
   - **Main file path**: main.py

### 3. Configurar Secrets

1. No Streamlit Cloud, clique em **⚙️ Settings**
2. Vá em **Secrets**
3. Abra o arquivo `secrets.toml.example`
4. **Copie TODO o conteúdo** (já está no formato correto!)
5. **Cole** na área de Secrets do Streamlit Cloud
6. Clique em **Save**

### 4. Deploy Automático

O Streamlit Cloud vai:
- ✅ Instalar as dependências do `requirements.txt`
- ✅ Carregar os secrets configurados
- ✅ Iniciar sua aplicação

## 🔐 Configuração do Google Sheets

1. Abra sua planilha do Google Sheets
2. Clique em **Compartilhar**
3. Adicione o email: `organizsubelemento@oganizadorsubelemento.iam.gserviceaccount.com`
4. Dê permissão de **Editor**

## ✅ Dependências Instaladas

```
streamlit>=1.30.0
pandas>=2.0.0
python-docx>=0.8.11
gspread>=5.11.0
oauth2client>=4.1.3
openpyxl>=3.1.0
num2words>=0.5.12  ← ADICIONADO (corrige o erro)
```

## 🎯 Pronto!

Após seguir esses passos, sua aplicação estará online e funcionando!

**URL da aplicação**: `https://seu-usuario-seu-repo.streamlit.app`

## 🔄 Atualizações Futuras

Para atualizar a aplicação:

```bash
git add .
git commit -m "Descrição da atualização"
git push
```

O Streamlit Cloud detecta automaticamente e faz o redeploy!

## 🆘 Troubleshooting

**Erro de módulo não encontrado?**
- Verifique se a dependência está no `requirements.txt`
- Reinicie a aplicação no Streamlit Cloud

**Erro de autenticação Google Sheets?**
- Verifique se os Secrets foram configurados corretamente
- Confirme que compartilhou a planilha com o email da service account

**Aplicação não inicia?**
- Verifique os logs no Streamlit Cloud
- Clique em **Manage app** → **Logs**
