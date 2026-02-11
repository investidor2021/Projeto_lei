# 🚀 Guia de Configuração para GitHub

## ✅ Arquivos Criados

Os seguintes arquivos foram criados para o repositório GitHub:

- ✅ `.gitignore` - Ignora arquivos sensíveis e temporários
- ✅ `README.md` - Documentação completa do projeto
- ✅ `requirements.txt` - Dependências Python
- ✅ `LICENSE` - Licença MIT
- ✅ `GUIA_PLANILHA_PROJETOS.md` - Guia de configuração das planilhas

## 📝 Passos para Enviar ao GitHub

### 1. Inicialize o repositório Git (se ainda não fez)

```bash
cd "c:\projetos GitHub\Proj_lei"
git init
```

### 2. Adicione o remote do seu repositório

```bash
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
```

### 3. Verifique os arquivos que serão commitados

```bash
git status
```

**IMPORTANTE**: Verifique se `credenciais.json` NÃO aparece na lista!

### 4. Adicione os arquivos

```bash
git add .
```

### 5. Faça o primeiro commit

```bash
git commit -m "Initial commit: Sistema completo de geração de projetos de lei com AUDESP"
```

### 6. Envie para o GitHub

```bash
git push -u origin main
```

Ou se seu branch principal for `master`:

```bash
git push -u origin master
```

## ⚠️ IMPORTANTE: Segurança

### Antes de fazer o push, VERIFIQUE:

1. ✅ O arquivo `credenciais.json` está no `.gitignore`
2. ✅ Execute: `git status` e confirme que `credenciais.json` NÃO aparece
3. ✅ Se aparecer, remova do staging: `git rm --cached credenciais.json`

### Se você já commitou credenciais por engano:

```bash
# Remova do histórico
git rm --cached credenciais.json
git commit -m "Remove credenciais.json"

# Force push (CUIDADO: só faça se for repositório novo)
git push -f origin main
```

## 📋 Estrutura de Commits Recomendada

### Primeiro Commit (Inicial)
```bash
git commit -m "Initial commit: Sistema completo de geração de projetos de lei com AUDESP"
```

### Commits Futuros - Use Mensagens Descritivas

**Exemplos:**
```bash
git commit -m "feat: Adiciona suporte para novos elementos de despesa"
git commit -m "fix: Corrige validação de códigos AUDESP"
git commit -m "docs: Atualiza README com novos exemplos"
git commit -m "refactor: Melhora performance do construtor de dotações"
```

**Prefixos recomendados:**
- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Documentação
- `refactor:` - Refatoração de código
- `style:` - Formatação
- `test:` - Testes
- `chore:` - Tarefas gerais

## 🔄 Workflow Recomendado

### Para trabalhar em novas features:

```bash
# Crie uma branch
git checkout -b feature/nova-funcionalidade

# Faça suas alterações e commits
git add .
git commit -m "feat: Descrição da funcionalidade"

# Volte para main e faça merge
git checkout main
git merge feature/nova-funcionalidade

# Envie para o GitHub
git push origin main
```

## 📦 Estrutura Final do Repositório

```
Proj_lei/
├── .gitignore                   ✅ Criado
├── LICENSE                      ✅ Criado
├── README.md                    ✅ Criado
├── requirements.txt             ✅ Criado
├── GUIA_PLANILHA_PROJETOS.md   ✅ Existente
├── main.py                      ✅ Existente
├── audesp_codes.py              ✅ Existente
├── sheets_client.py             ✅ Existente
├── data_processor.py            ✅ Existente
├── doc_projeto_lei.py           ✅ Existente
├── doc_decreto.py               ✅ Existente
├── doc_lei_final.py             ✅ Existente
├── doc_base.py                  ✅ Existente
└── credenciais.json             ❌ NÃO COMMITAR (ignorado)
```

## 🎨 Personalize o README

Antes de fazer o push, edite o `README.md` e substitua:

1. `SEU_USUARIO` pelo seu usuário do GitHub
2. `SEU_REPOSITORIO` pelo nome do seu repositório
3. Adicione screenshots se desejar (crie uma pasta `docs/images/`)

## 📸 Adicionar Screenshots (Opcional)

```bash
# Crie a pasta
mkdir -p docs/images

# Adicione suas imagens
# Depois referencie no README.md:
# ![Screenshot](docs/images/screenshot.png)
```

## ✨ Dicas Finais

1. **Mantenha commits pequenos e focados**
2. **Escreva mensagens de commit descritivas**
3. **Nunca commite credenciais ou dados sensíveis**
4. **Faça push regularmente para não perder trabalho**
5. **Use branches para features grandes**

## 🆘 Comandos Úteis

```bash
# Ver status
git status

# Ver histórico
git log --oneline

# Desfazer último commit (mantém alterações)
git reset --soft HEAD~1

# Desfazer alterações não commitadas
git checkout -- arquivo.py

# Ver diferenças
git diff

# Ver branches
git branch -a
```

---

**Pronto para enviar! 🚀**

Execute os comandos na ordem e seu projeto estará no GitHub!
