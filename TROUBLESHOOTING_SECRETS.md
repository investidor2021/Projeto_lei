# 🔧 Troubleshooting - Erro de URL no Streamlit Secrets

## ❌ Erro Atual

```
Invalid URL 'https=//oauth2.googleapis.com/token': No scheme supplied
```

## 🔍 Causa

Este erro acontece quando o Streamlit Cloud interpreta mal o formato TOML ao copiar/colar.

## ✅ Soluções

### Solução 1: Usar Arquivo Alternativo (RECOMENDADO)

1. Abra o arquivo `secrets_alternative.toml`
2. Copie TODO o conteúdo
3. No Streamlit Cloud:
   - Vá em **Settings > Secrets**
   - **DELETE** todo o conteúdo anterior
   - Cole o novo conteúdo
   - Clique em **Save**
4. Reinicie a aplicação

### Solução 2: Verificar Formatação Manual

Se ainda der erro, verifique no Streamlit Cloud Secrets que:

**CORRETO:**
```toml
token_uri = "https://oauth2.googleapis.com/token"
```

**ERRADO:**
```toml
token_uri = "https=//oauth2.googleapis.com/token"
```

Note o `:` após `https` - deve ser dois-pontos, não igual!

### Solução 3: Usar JSON Direto (Alternativa)

Se o TOML continuar dando problema, você pode usar JSON:

1. No Streamlit Cloud, vá em **Settings > Secrets**
2. Cole este formato:

```toml
[gcp_service_account]
```

Depois cole o conteúdo do seu `credenciais.json` embaixo, mas INDENTADO:

```toml
[gcp_service_account]
  type = "service_account"
  project_id = "oganizadorsubelemento"
  ...
```

## 🔄 Passos Detalhados

### Passo 1: Limpar Secrets Atuais

1. Streamlit Cloud > **Settings > Secrets**
2. **Selecione tudo** (Ctrl+A)
3. **Delete**

### Passo 2: Copiar Novo Formato

1. Abra `secrets_alternative.toml`
2. Copie TODO (Ctrl+A, Ctrl+C)

### Passo 3: Colar no Streamlit

1. Cole no campo Secrets (Ctrl+V)
2. **NÃO edite nada manualmente**
3. Clique em **Save**

### Passo 4: Verificar

Após salvar, verifique visualmente que as URLs estão corretas:
- ✅ `https://` (com dois-pontos)
- ❌ `https=//` (com igual)

### Passo 5: Reiniciar

1. Clique em **Reboot app**
2. Aguarde reiniciar
3. Teste a conexão

## 🆘 Se Ainda Não Funcionar

### Opção A: Testar Localmente Primeiro

1. Crie pasta `.streamlit` no projeto:
```bash
mkdir .streamlit
```

2. Copie `secrets_alternative.toml` para `.streamlit/secrets.toml`

3. Teste localmente:
```bash
streamlit run main.py
```

4. Se funcionar localmente, o problema é no Streamlit Cloud

### Opção B: Usar Variáveis de Ambiente

Edite `sheets_client.py` para aceitar variáveis de ambiente também.

## 📋 Checklist de Verificação

- [ ] Deletou todo o conteúdo antigo dos Secrets
- [ ] Copiou de `secrets_alternative.toml` (não do example)
- [ ] Não editou nada manualmente após colar
- [ ] Verificou que URLs têm `https://` (com dois-pontos)
- [ ] Salvou as mudanças
- [ ] Reiniciou a aplicação
- [ ] Compartilhou planilha com o email da service account

## 🎯 Email da Service Account

Não esqueça de compartilhar sua planilha Google Sheets com:

```
organizsubelemento@oganizadorsubelemento.iam.gserviceaccount.com
```

Permissão: **Editor**

## 📞 Última Opção

Se nada funcionar, você pode:

1. Manter `credenciais.json` no repositório (NÃO RECOMENDADO para produção)
2. Adicionar ao `.gitignore` depois do deploy
3. Ou usar outro serviço de deploy que aceite arquivos de credenciais

**Mas tente as soluções acima primeiro!**
