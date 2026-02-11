# 🚀 Comandos Prontos para GitHub

## ⚡ Copie e Cole Estes Comandos

### 1️⃣ Inicializar Git e Fazer Primeiro Commit

```bash
cd "c:\projetos GitHub\Proj_lei"
git init
git add .
git commit -m "Initial commit: Sistema completo de geração de projetos de lei com AUDESP"
```

### 2️⃣ Conectar ao Repositório GitHub

**Substitua `SEU_USUARIO` e `SEU_REPOSITORIO` pelos valores corretos!**

```bash
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
```

### 3️⃣ Enviar para o GitHub

```bash
git branch -M main
git push -u origin main
```

---

## ✅ Verificação de Segurança

**ANTES de fazer o push, execute:**

```bash
git status
```

**Verifique que `credenciais.json` NÃO aparece na lista!**

Se aparecer, execute:

```bash
git rm --cached credenciais.json
git commit -m "Remove credenciais.json do repositório"
```

---

## 📋 Resumo dos Arquivos Criados

✅ `.gitignore` - Protege arquivos sensíveis
✅ `README.md` - Documentação completa
✅ `requirements.txt` - Dependências
✅ `LICENSE` - Licença MIT
✅ `GITHUB_SETUP.md` - Guia detalhado
✅ `COMANDOS_GIT.md` - Este arquivo

---

## 🔄 Comandos para Atualizações Futuras

```bash
# Verificar status
git status

# Adicionar alterações
git add .

# Commit
git commit -m "Descrição das alterações"

# Enviar para GitHub
git push
```

---

## 🆘 Comandos Úteis

```bash
# Ver histórico de commits
git log --oneline

# Ver diferenças não commitadas
git diff

# Desfazer alterações não commitadas
git checkout -- nome_arquivo.py

# Ver branches
git branch -a
```

---

## 🎯 Próximos Passos

1. ✅ Execute os comandos da seção 1️⃣
2. ✅ Execute os comandos da seção 2️⃣ (substitua os valores!)
3. ✅ Verifique a segurança
4. ✅ Execute os comandos da seção 3️⃣
5. 🎉 Pronto! Seu projeto está no GitHub!

---

**Dica**: Mantenha este arquivo para referência futura!
