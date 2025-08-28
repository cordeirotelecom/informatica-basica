# Sistema de Conversão PDF

## Instruções para Configurar Downloads PDF

### Opção 1: Via NPM (Recomendado)
```bash
npm install -g markdown-pdf
```

### Opção 2: Via Python 
```bash
pip install markdown
pip install pdfkit
```

### Opção 3: Online (Temporário)
Use conversores online como:
- https://www.markdowntopdf.com/
- https://dillinger.io/

### Gerando PDFs das Atividades

Para cada arquivo .md, execute:
```bash
markdown-pdf arquivo.md -o arquivo.pdf
```

### Script Automático
Execute o script `gerar-pdfs.bat` para converter todos os arquivos:

```batch
@echo off
echo Convertendo arquivos Markdown para PDF...

cd socioeducativo\downloads
for %%f in (*.md) do (
    echo Convertendo %%f...
    markdown-pdf "%%f" -o "%%~nf.pdf"
)

cd ..\atividades
for %%f in (*.md) do (
    echo Convertendo %%f...
    markdown-pdf "%%f" -o "%%~nf.pdf"
)

echo Conversão concluída!
pause
```

### Verificação
Após a conversão, os arquivos PDF estarão disponíveis para download nos links das atividades.
