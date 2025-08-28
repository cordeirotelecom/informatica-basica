@echo off
echo ==========================================
echo    DEPLOY AUTOMATICO - cordeirotelecom
echo ==========================================
echo.
echo Conta GitHub: cordeirotelecom
echo Repositorio: informatica-basica
echo.
echo PASSO 1: Criando repositorio no GitHub...
echo.
echo ABRA O NAVEGADOR E:
echo 1. Va em: https://github.com/new
echo 2. Repository name: informatica-basica
echo 3. Marque "Public"
echo 4. NAO marque nenhuma opcao extra
echo 5. Clique "Create repository"
echo.
echo Pressione ENTER depois de criar o repositorio...
pause

echo.
echo PASSO 2: Enviando arquivos...
echo.
cd /d "c:\Users\corde\OneDrive\Desktop\informatica basica"
git push -u origin main

if %errorlevel% == 0 (
    echo.
    echo ==========================================
    echo        SUCESSO! Arquivos enviados!
    echo ==========================================
    echo.
    echo PASSO 3: Deploy no Netlify
    echo.
    echo ABRA: https://app.netlify.com
    echo 1. Faca login no Netlify
    echo 2. Clique "New site from Git"
    echo 3. Escolha "GitHub"
    echo 4. Selecione: cordeirotelecom/informatica-basica
    echo 5. Publish directory: public
    echo 6. Clique "Deploy site"
    echo.
    echo CREDENCIAIS AREA RESTRITA:
    echo Usuario: cordeirotelecom
    echo Senha: Socio2025!@#
    echo.
    start https://app.netlify.com
    
) else (
    echo.
    echo ==========================================
    echo     ERRO! Crie o repositorio primeiro
    echo ==========================================
    echo.
    echo 1. Va em: https://github.com/new
    echo 2. Nome: informatica-basica  
    echo 3. Marque Public
    echo 4. Crie o repositorio
    echo 5. Execute este script novamente
    echo.
    start https://github.com/new
)

echo.
echo Pressione qualquer tecla para fechar...
pause > nul
