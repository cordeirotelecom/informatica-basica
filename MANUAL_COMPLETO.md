# 🚀 Manual Completo de Deploy - Informática Básica

## 📋 Pré-requisitos
1. Conta no GitHub (github.com)
2. Conta no Netlify (netlify.com)

---

## 📂 PASSO 1: Criar Repositório no GitHub

### 1.1 Acessar GitHub
- Vá para https://github.com/cordeirotelecom
- Clique em "New repository" (botão verde)

### 1.2 Configurar Repositório
- **Repository name:** `informatica-basica`
- **Description:** "Site educacional de informática básica com área de ressocialização"
- ✅ **Public** (marcar esta opção)
- ❌ **NÃO marcar** "Add a README file"
- ❌ **NÃO marcar** "Add .gitignore"
- ❌ **NÃO marcar** "Choose a license"
- Clicar em **"Create repository"**

---

## 💻 PASSO 2: Enviar Arquivos para GitHub

### 2.1 Abrir PowerShell
```powershell
# Navegar para a pasta do projeto
cd "c:\Users\corde\OneDrive\Desktop\informatica basica"

# Enviar arquivos para GitHub
git push -u origin main
```

### 2.2 Se der erro "repository not found":
1. Verifique se criou o repositório com o nome exato: `informatica-basica`
2. Se ainda não criou, volte ao Passo 1
3. Se já criou, tente novamente o comando git push

---

## 🌐 PASSO 3: Deploy no Netlify

### 3.1 Acessar Netlify
- Vá para https://app.netlify.com
- Faça login (ou crie conta se não tiver)
- Clique em **"New site from Git"**

### 3.2 Conectar GitHub
- Escolha **"GitHub"**
- Autorize o Netlify a acessar sua conta GitHub
- Procure e selecione: **cordeirotelecom/informatica-basica**

### 3.3 Configurar Build
- **Branch to deploy:** main
- **Build command:** (deixar vazio)
- **Publish directory:** `public`
- Clicar em **"Deploy site"**

### 3.4 Aguardar Deploy
- O Netlify vai gerar uma URL temporária (ex: amazing-site-123456.netlify.app)
- Aguarde alguns minutos para o site ficar online

---

## 🔒 PASSO 4: Proteger Área Socioeducativo

### 4.1 Configurar Proteção
- No painel do Netlify, vá em **"Site settings"**
- Na barra lateral, clique em **"Access control"**
- Em **"Visitor access"**, escolha **"Password protection"**

### 4.2 Definir Senha
- **Username:** cordeirotelecom
- **Password:** (escolha uma senha forte)
- Clique em **"Save"**

**⚠️ IMPORTANTE:** Esta proteção vai proteger TODO o site. Para proteger apenas a pasta socioeducativo, use a configuração avançada no arquivo `netlify.toml` que já está configurado.

---

## 🎯 PASSO 5: Personalizar Domínio (Opcional)

### 5.1 Domínio Personalizado
- No Netlify, vá em **"Domain settings"**
- Clique em **"Add custom domain"**
- Digite seu domínio (ex: informatica-basica.com.br)
- Siga as instruções para configurar DNS

---

## 🔄 PASSO 6: Atualizar o Site

### 6.1 Para adicionar mais conteúdo:
```powershell
# Navegar para a pasta do projeto
cd "c:\Users\corde\OneDrive\Desktop\informatica basica"

# Adicionar alterações
git add .

# Criar commit com descrição
git commit -m "Descrição da alteração feita"

# Enviar para GitHub
git push
```

### 6.2 O Netlify atualiza automaticamente
- Toda vez que você fizer `git push`, o Netlify detecta e atualiza o site
- Aguarde 2-3 minutos para as mudanças aparecerem online

---

## 📁 Estrutura Atual do Projeto

```
informatica-basica/
├── public/                 # Arquivos públicos do site
│   ├── index.html         # Página principal
│   └── style.css          # Estilos
├── aulas/                 # Aulas abertas ao público
│   ├── aula01.html        # Introdução à Informática
│   ├── aula02.html        # Sistemas Operacionais
│   ├── aula03.html        # Internet e Navegadores
│   ├── aula04.html        # Microsoft Word
│   ├── aula05.html        # Microsoft Excel
│   └── aula06.html        # Microsoft PowerPoint
├── socioeducativo/        # Área restrita (protegida)
│   ├── index.html         # Página principal socioeducativo
│   ├── aula01.html        # Word - Criando Currículo
│   ├── aula02.html        # Excel - Orçamento Financeiro
│   ├── aula03.html        # PowerPoint - Profissões e Ética
│   ├── aula04.html        # Planejamento Financeiro Avançado
│   ├── aula05.html        # Projeto de Vida e Cursos IFSC
│   └── recursos.html      # Biblioteca de recursos
├── netlify/               # Configurações Netlify
│   └── functions/
│       └── auth-socioeducativo.js
├── .github/               # Configurações GitHub
│   └── copilot-instructions.md
├── netlify.toml           # Configurações de deploy
├── .gitignore             # Arquivos ignorados pelo Git
├── README.md              # Documentação do projeto
└── DEPLOY_GUIDE.md        # Este guia
```

---

## 🆘 Resolução de Problemas

### ❌ Erro "repository not found"
- Verifique se o repositório foi criado no GitHub
- Confirme o nome exato: `informatica-basica`
- Verifique se está logado na conta correta: cordeirotelecom

### ❌ Site não carrega no Netlify
- Verifique se a pasta "public" está configurada como publish directory
- Aguarde alguns minutos após o deploy
- Verifique se não há erros na aba "Deploys" do Netlify

### ❌ Área socioeducativo não protegida
- Verifique se o arquivo `netlify.toml` foi enviado
- Configure proteção manual em "Site settings" > "Access control"

---

## 📞 Próximos Passos

1. ✅ Criar repositório GitHub
2. ✅ Fazer primeiro push
3. ✅ Configurar Netlify
4. ✅ Testar o site online
5. ✅ Proteger área socioeducativo
6. 📝 Adicionar mais conteúdo conforme necessário
7. 📚 Criar material PDF para download
8. 🎨 Personalizar design se desejado

---

## 💡 Dicas de Uso

### Para Educadores:
- Use as atividades sem internet
- Foque no desenvolvimento socioemocional
- Adapte conforme o perfil do grupo
- Promova discussões sobre ética e valores

### Para Administradores:
- Backup regular dos arquivos
- Monitorar acesso à área restrita
- Atualizar conteúdo periodicamente
- Coletar feedback dos usuários

---

**🏆 Parabéns! Seu site educacional está pronto para impactar vidas!**
