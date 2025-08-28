# Guia Completo de Deploy - Informática Básica

## 1. Subir para o GitHub

### Primeiro, certifique-se de que você já criou o repositório no GitHub:
1. Acesse https://github.com/cordeirotelecom
2. Clique em "New repository"
3. Nome: `informatica-basica`
4. Deixe público
5. Clique em "Create repository"

### Para enviar os arquivos:
```powershell
cd "c:\Users\corde\OneDrive\Desktop\informatica basica"
git push -u origin main
```

## 2. Deploy no Netlify

### Passo a passo:
1. Acesse https://app.netlify.com
2. Clique em "New site from Git"
3. Escolha "GitHub" e autorize
4. Selecione o repositório `cordeirotelecom/informatica-basica`
5. Configurações de build:
   - Build command: (deixe vazio)
   - Publish directory: `public`
6. Clique em "Deploy site"

### Proteção da pasta socioeducativo:
1. No painel do Netlify, vá em "Site settings"
2. Na sidebar, clique em "Access control"
3. Em "Visitor access", escolha "Password protection"
4. Defina uma senha forte
5. Clique em "Save"

## 3. Configuração de Domínio (Opcional)
1. No Netlify, vá em "Domain settings"
2. Clique em "Add custom domain"
3. Digite seu domínio personalizado
4. Configure DNS conforme instruções

## 4. Atualizações Futuras
Para atualizar o site:
```powershell
cd "c:\Users\corde\OneDrive\Desktop\informatica basica"
git add .
git commit -m "Descrição da atualização"
git push
```

## 5. Adicionando Conteúdo

### Para adicionar novas aulas:
1. Crie `aulas/aula03.html`, `aulas/aula04.html`, etc.
2. Atualize os menus de navegação em todos os arquivos
3. Adicione links na página inicial

### Para adicionar atividades socioeducativo:
1. Crie novos arquivos em `socioeducativo/`
2. Adicione PDFs, documentos Word/Excel de exemplo
3. Atualize a página `socioeducativo/index.html`

## 6. Senha Atual do Socioeducativo
- Usuário: `cordeirotelecom`
- Senha: `senha123`
- Para alterar, edite o arquivo `netlify/functions/auth-socioeducativo.js`

## 7. Estrutura de Pastas
```
informatica-basica/
├── public/           # Arquivos públicos do site
├── aulas/           # Aulas abertas
├── socioeducativo/  # Área restrita
├── netlify/         # Configurações Netlify
├── .github/         # Configurações GitHub
└── README.md        # Documentação
```
