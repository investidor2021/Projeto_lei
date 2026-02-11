# 🔐 SEGURANÇA - Arquivos com Credenciais

## ⚠️ NUNCA COMMITE ESTES ARQUIVOS:

- ❌ `credenciais.json`
- ❌ `secrets.toml.example`
- ❌ `secrets_alternative.toml`
- ❌ `secrets.toml`
- ❌ `.streamlit/secrets.toml`

## ✅ Proteção Aplicada

O `.gitignore` foi atualizado para ignorar todos esses arquivos automaticamente.

## 🔍 Como Verificar Antes de Commitar

**SEMPRE execute antes de fazer commit:**

```bash
git status
```

**Verifique que NÃO aparecem:**
- credenciais.json
- secrets.toml.example
- secrets_alternative.toml

Se aparecerem, **NÃO FAÇA COMMIT!**

## 🆘 Se Já Commitou Por Engano

### Se ainda NÃO fez push:

```bash
# Remova do staging
git rm --cached secrets.toml.example
git rm --cached secrets_alternative.toml

# Commit a remoção
git commit -m "Remove arquivos de credenciais"
```

### Se JÁ fez push:

```bash
# Remova do histórico (CUIDADO!)
git rm --cached secrets.toml.example
git rm --cached secrets_alternative.toml
git commit -m "Remove credenciais do repositório"

# Force push (só faça se for repositório novo/privado)
git push -f origin main
```

**IMPORTANTE**: Depois disso, você DEVE:
1. Revogar as credenciais antigas no Google Cloud Console
2. Criar novas credenciais
3. Atualizar o arquivo local

## 📋 Checklist de Segurança

Antes de cada push, verifique:

- [ ] Executei `git status`
- [ ] Nenhum arquivo `*.json` aparece (exceto package.json se tiver)
- [ ] Nenhum arquivo `*.toml` aparece
- [ ] Nenhum arquivo em `.streamlit/` aparece
- [ ] O `.gitignore` está commitado

## ✅ Como Usar no Streamlit Cloud

**Método Correto:**

1. **NÃO** commite os arquivos de secrets
2. Copie o conteúdo de `secrets_alternative.toml`
3. Cole em **Streamlit Cloud > Settings > Secrets**
4. Pronto! As credenciais ficam seguras no Streamlit Cloud

## 🎯 Resumo

**Desenvolvimento Local**: Use `credenciais.json` (não commitado)

**Streamlit Cloud**: Use Secrets via interface web (não commitado)

**GitHub**: Apenas código, SEM credenciais!

---

**Lembre-se**: Credenciais no GitHub = RISCO DE SEGURANÇA! 🚨
