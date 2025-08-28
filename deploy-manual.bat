@echo off
echo ========================================
echo     DEPLOY MANUAL - INFORMATICA BASICA
echo ========================================
echo.
echo IMPORTANTE: Execute DEPOIS de criar o repositorio no GitHub
echo.
echo 1. Acesse: https://github.com/new
echo 2. Nome: informatica-basica  
echo 3. Marque: Public
echo 4. Clique: Create repository
echo.
echo Depois pressione qualquer tecla para continuar...
pause > nul

echo.
echo Configurando repositorio remoto...
cd /d "c:\Users\corde\OneDrive\Desktop\informatica basica"

git remote add origin https://github.com/cordeirotelecom/informatica-basica.git

echo.
echo Enviando arquivos para GitHub...
git push -u origin main

if %errorlevel% == 0 (
    echo.
    echo ========================================
    echo         SUCESSO! ARQUIVO ENVIADO!
    echo ========================================
    echo.
    echo Repositorio: https://github.com/cordeirotelecom/informatica-basica
    echo.
    echo PROXIMO PASSO - NETLIFY:
    echo 1. Acesse: https://app.netlify.com
    echo 2. New site from Git
    echo 3. Selecione: cordeirotelecom/informatica-basica
    echo 4. Publish directory: public
    echo 5. Deploy site
    echo.
    start https://app.netlify.com
    echo.
) else (
    echo.
    echo ========================================
    echo              ERRO!
    echo ========================================
    echo.
    echo O repositorio ainda nao foi criado no GitHub.
    echo.
    echo 1. Acesse: https://github.com/new
    echo 2. Nome: informatica-basica
    echo 3. Marque: Public  
    echo 4. Create repository
    echo 5. Execute este script novamente
    echo.
    start https://github.com/new
)

echo.
pause
