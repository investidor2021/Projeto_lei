# ✅ Estrutura Correta do Projeto para Deploy

## 📁 Estrutura Atual (CORRIGIDA)

```
Projeto_lei/                    ← Pasta principal do repositório
├── .git/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt            ← Dependências
├── main.py                     ← Arquivo principal
├── audesp_codes.py            ← ✅ COPIADO
├── sheets_client.py
├── data_processor.py
├── doc_base.py
├── doc_projeto_lei.py
├── doc_decreto.py
├── doc_lei_final.py
├── DEPLOY_CHECKLIST.md
├── TROUBLESHOOTING_SECRETS.md
├── secrets_alternative.toml
└── GUIA_PLANILHA_PROJETOS.md
```

## ⚠️ Problema Anterior

O `audesp_codes.py` estava na pasta raiz, mas o `main.py` estava em `Projeto_lei/`, causando:
```
ModuleNotFoundError: No module named 'audesp_codes'
```

## ✅ Solução Aplicada

Copiamos `audesp_codes.py` para dentro da pasta `Projeto_lei/`.

## 🚀 Próximos Passos

### 1. Fazer Commit da Correção

```bash
cd "c:\projetos GitHub\Proj_lei\Projeto_lei"
git add audesp_codes.py
git commit -m "fix: Adiciona audesp_codes.py ao diretório correto"
git push
```

### 2. Verificar no Streamlit Cloud

Após o push, o Streamlit Cloud vai:
- ✅ Detectar a mudança
- ✅ Fazer redeploy automático
- ✅ Encontrar o módulo `audesp_codes`

## 📋 Checklist de Arquivos Necessários

Verifique que TODOS estes arquivos estão em `Projeto_lei/`:

- [x] `main.py`
- [x] `audesp_codes.py` ← **CORRIGIDO**
- [x] `sheets_client.py`
- [x] `data_processor.py`
- [x] `doc_base.py`
- [x] `doc_projeto_lei.py`
- [x] `doc_decreto.py`
- [x] `doc_lei_final.py`
- [x] `requirements.txt`

## 🔍 Como Verificar

Execute este comando para listar todos os arquivos Python:

```bash
cd "c:\projetos GitHub\Proj_lei\Projeto_lei"
dir *.py
```

Você deve ver:
- audesp_codes.py
- data_processor.py
- doc_base.py
- doc_decreto.py
- doc_lei_final.py
- doc_projeto_lei.py
- main.py
- mainorigianl.py
- sheets_client.py

## ✨ Tudo Pronto!

Agora todos os módulos estão no lugar correto e o import vai funcionar!
