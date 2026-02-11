# 🏛️ Gerador de Projetos de Lei Orçamentária - AUDESP

Sistema completo para geração de documentos legislativos municipais (Projetos de Lei, Decretos e Leis) com suporte à estrutura orçamentária AUDESP do Tribunal de Contas do Estado de São Paulo.

## 📋 Funcionalidades

### 🎯 Principais Recursos

- **Geração Automática de Documentos**
  - Projeto de Lei (formato oficial)
  - Decreto de abertura de crédito
  - Lei final aprovada
  - Exportação em DOCX com formatação profissional

- **Sistema Completo AUDESP**
  - Estrutura de dotação orçamentária com 13 componentes
  - Modo simplificado (6 componentes principais)
  - Modo avançado (controle total de todos os componentes)
  - Validação automática de códigos

- **Integração Google Sheets**
  - Importação de fichas orçamentárias
  - Gerenciamento dinâmico de projetos/atividades
  - Controle de aplicações orçamentárias
  - Sincronização em tempo real

- **Interface Intuitiva**
  - Construtor visual de dotações
  - Descrições automáticas
  - Validação de valores
  - Preview em tempo real

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- Conta Google (para integração com Google Sheets)

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/SEU_USUARIO/Proj_lei.git
cd Proj_lei
```

2. **Crie um ambiente virtual**
```bash
python -m venv .venv
```

3. **Ative o ambiente virtual**

Windows:
```bash
.venv\Scripts\activate
```

Linux/Mac:
```bash
source .venv/bin/activate
```

4. **Instale as dependências**
```bash
pip install -r requirements.txt
```

5. **Configure as credenciais do Google Sheets**

   a. Acesse o [Google Cloud Console](https://console.cloud.google.com/)
   
   b. Crie um novo projeto ou selecione um existente
   
   c. Ative a API do Google Sheets e Google Drive
   
   d. Crie uma conta de serviço e baixe o arquivo JSON
   
   e. Renomeie o arquivo para `credenciais.json` e coloque na raiz do projeto
   
   f. Compartilhe sua planilha com o email da conta de serviço

## 📖 Como Usar

### Iniciando o Sistema

```bash
streamlit run main.py
```

O sistema abrirá automaticamente no navegador em `http://localhost:8501`

### Estrutura da Planilha Google Sheets

O sistema espera uma planilha com as seguintes abas:

#### Aba Principal (Fichas Orçamentárias)
| Coluna | Conteúdo | Exemplo |
|--------|----------|---------|
| D | Código da Ficha | 01.02.20.10.122.0017.2051 |
| F | Descrição | MANUTENÇÃO DAS ATIVIDADES |
| H | Valor Disponível | 150000.00 |

#### Aba "projetos" (Opcional)
| Código | Descrição |
|--------|-----------|
| 0126 | ATIVIDADE - MANUTENÇÃO ADMINISTRATIVA |
| 0001 | PROJETO - INFRAESTRUTURA |

#### Aba "aplicacoes" (Opcional)
| Código | Descrição |
|--------|-----------|
| 0001 | APLICAÇÃO GERAL |
| 0265 | APLICAÇÃO FUNDEB |

### Criando um Projeto de Lei

1. **Configure os dados básicos**
   - Número do projeto
   - Autor
   - Tipo de crédito (Suplementar/Especial)
   - Justificativa

2. **Adicione os créditos**
   - **Modo Planilha**: Selecione fichas existentes
   - **Modo Manual**: Use o construtor de dotações AUDESP

3. **Adicione as anulações**
   - Selecione as fichas a serem anuladas
   - Informe os valores

4. **Gere os documentos**
   - Clique em "Gerar Documentos"
   - Baixe os arquivos DOCX gerados

## 🔧 Estrutura AUDESP

### Código Completo (13 componentes)

```
01.02.16.12.361.0013.30126.3.1.90.11.00.00.00.00.00.02.0265
│  │  │  │  │   │    │ │   │ │ │  │  │  │  │  │  │  │  └─── Aplicação
│  │  │  │  │   │    │ │   │ │ │  │  │  │  │  │  │  └────── Fonte
│  │  │  │  │   │    │ │   └─┴─┴──┴──┴──┴──┴──┴──┴───────── Desdobramento
│  │  │  │  │   │    │ │   │ │ └──────────────────────────── Elemento
│  │  │  │  │   │    │ │   │ └────────────────────────────── Modalidade
│  │  │  │  │   │    │ │   └──────────────────────────────── Grupo Despesa
│  │  │  │  │   │    │ └──────────────────────────────────── Categoria Econ.
│  │  │  │  │   │    └────────────────────────────────────── Número Proj/Ativ
│  │  │  │  │   └─────────────────────────────────────────── Programa
│  │  │  │  └─────────────────────────────────────────────── Subfunção
│  │  │  └───────────────────────────────────────────────────── Função
│  │  └──────────────────────────────────────────────────────── Departamento
```

### Modo Simplificado

Preencha apenas os componentes principais:
- Departamento
- Função
- Subfunção
- Programa
- Tipo (Projeto/Atividade)
- Número do Projeto/Atividade

Os demais componentes usam valores padrão inteligentes.

### Modo Avançado

Controle total sobre todos os 13 componentes para casos especiais.

## 📁 Estrutura do Projeto

```
Proj_lei/
├── main.py                      # Aplicação principal Streamlit
├── audesp_codes.py              # Dicionários e funções AUDESP
├── sheets_client.py             # Integração Google Sheets
├── data_processor.py            # Processamento de dados
├── doc_projeto_lei.py           # Geração de Projeto de Lei
├── doc_decreto.py               # Geração de Decreto
├── doc_lei_final.py             # Geração de Lei Final
├── doc_base.py                  # Funções base para documentos
├── credenciais.json             # Credenciais Google (NÃO COMMITAR!)
├── requirements.txt             # Dependências Python
├── .gitignore                   # Arquivos ignorados pelo Git
├── README.md                    # Este arquivo
└── GUIA_PLANILHA_PROJETOS.md   # Guia de configuração
```

## 🔐 Segurança

⚠️ **IMPORTANTE**: O arquivo `credenciais.json` contém informações sensíveis e **NÃO DEVE** ser commitado no Git.

O arquivo `.gitignore` já está configurado para ignorar:
- `credenciais.json`
- Arquivos de ambiente virtual
- Cache do Python
- Arquivos temporários

## 🛠️ Tecnologias Utilizadas

- **Streamlit** - Interface web interativa
- **Python-docx** - Geração de documentos Word
- **Pandas** - Manipulação de dados
- **gspread** - Integração Google Sheets
- **oauth2client** - Autenticação Google

## 📝 Dicionários AUDESP Incluídos

- ✅ 52 Departamentos municipais
- ✅ 28 Funções de governo
- ✅ 100+ Subfunções de governo
- ✅ 36 Programas
- ✅ 3 Grupos de natureza
- ✅ 2 Categorias econômicas
- ✅ 6 Grupos de despesa
- ✅ 28 Modalidades de aplicação
- ✅ 70+ Elementos de despesa
- ✅ 20+ Fontes de recursos

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 👥 Autor

Desenvolvido para auxiliar na gestão orçamentária municipal seguindo as normas do TCE-SP.

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique a documentação em `GUIA_PLANILHA_PROJETOS.md`
2. Abra uma issue no GitHub
3. Consulte o código de exemplo nos arquivos

## 🎯 Roadmap

- [ ] Exportação para PDF
- [ ] Histórico de versões de documentos
- [ ] Validação automática de limites orçamentários
- [ ] Dashboard de análise orçamentária
- [ ] Integração com sistemas contábeis

## ⚡ Início Rápido

```bash
# Clone e configure
git clone https://github.com/SEU_USUARIO/Proj_lei.git
cd Proj_lei
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt

# Configure credenciais.json (veja seção Instalação)

# Execute
streamlit run main.py
```

---

**Desenvolvido com ❤️ para facilitar a gestão orçamentária municipal**
