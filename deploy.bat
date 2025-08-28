@echo off
echo ==========================================
echo    SCRIPT DE DEPLOY - INFORMATICA BASICA
echo ==========================================
echo.
echo Este script ira enviar seus arquivos para o GitHub
echo.
echo Pressione qualquer tecla para continuar...
pause > nul

echo.
echo Navegando para a pasta do projeto...
cd /d "c:\Users\corde\OneDrive\Desktop\informatica basica"

echo.
echo Enviando arquivos para o GitHub...
git push -u origin main

echo.
if %errorlevel% == 0 (
    echo ==========================================
    echo     SUCESSO! Arquivos enviados!
    echo ==========================================
    echo.
    echo Proximo passo:
    echo 1. Acesse: https://app.netlify.com
    echo 2. Clique em "New site from Git"
    echo 3. Escolha GitHub e selecione: cordeirotelecom/informatica-basica
    echo 4. Configure Publish directory: public
    echo 5. Clique em "Deploy site"
    echo.
) else (
    echo ==========================================
    echo     ERRO! Repositorio nao encontrado
    echo ==========================================
    echo.
    echo Primeiro crie o repositorio no GitHub:
    echo 1. Acesse: https://github.com/cordeirotelecom
    echo 2. Clique em "New repository"
    echo 3. Nome: informatica-basica
    echo 4. Marque "Public"
    echo 5. NAO marque nenhuma opcao extra
    echo 6. Clique em "Create repository"
    echo 7. Execute este script novamente
    echo.
)

echo.
echo Pressione qualquer tecla para fechar...
pause > nul
