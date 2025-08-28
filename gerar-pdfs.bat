@echo off
echo Gerando PDFs das atividades...
echo.

:: Instalar markdown-pdf se não estiver instalado
npm list -g markdown-pdf >nul 2>&1
if %errorlevel% neq 0 (
    echo Instalando markdown-pdf...
    npm install -g markdown-pdf
)

:: Converter arquivos downloads
cd socioeducativo\downloads
echo Convertendo arquivos de downloads...
for %%f in (*.md) do (
    echo   %%f -^> %%~nf.pdf
    markdown-pdf "%%f" -o "%%~nf.pdf"
)

:: Converter arquivos atividades
cd ..\atividades
echo Convertendo arquivos de atividades...
for %%f in (*.md) do (
    echo   %%f -^> %%~nf.pdf
    markdown-pdf "%%f" -o "%%~nf.pdf"
)

cd ..\..
echo.
echo Conversão concluída!
echo Os arquivos PDF foram gerados nas pastas correspondentes.
pause
