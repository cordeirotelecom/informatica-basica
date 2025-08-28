@echo off
echo ========================================
echo     CRIADOR DE REPOSITORIO GITHUB
echo ========================================
echo.
echo Este script vai criar o repositorio no GitHub
echo e enviar todos os arquivos automaticamente.
echo.
echo IMPORTANTE: Tenha suas credenciais do GitHub prontas!
echo.
pause

echo.
echo Criando repositorio no GitHub...
echo.

REM Usar GitHub CLI se estiver instalado
where gh >nul 2>nul
if %errorlevel% == 0 (
    echo Usando GitHub CLI...
    cd /d "c:\Users\corde\OneDrive\Desktop\informatica basica"
    gh repo create informatica-basica --public --description "Site educacional de informatica basica com area de ressocializacao"
    git remote add origin https://github.com/cordeirotelecom/informatica-basica.git
    git push -u origin main
    echo.
    echo ========================================
    echo     REPOSITORIO CRIADO COM SUCESSO!
    echo ========================================
    echo.
    echo Acesse: https://github.com/cordeirotelecom/informatica-basica
    echo.
) else (
    echo GitHub CLI nao encontrado.
    echo.
    echo OPCAO 1 - Instalar GitHub CLI:
    echo 1. Acesse: https://cli.github.com/
    echo 2. Baixe e instale
    echo 3. Execute: gh auth login
    echo 4. Execute este script novamente
    echo.
    echo OPCAO 2 - Criar manualmente:
    echo 1. Acesse: https://github.com/new
    echo 2. Nome: informatica-basica
    echo 3. Marque Public
    echo 4. Create repository
    echo 5. Execute: deploy-manual.bat
    echo.
)

pause
