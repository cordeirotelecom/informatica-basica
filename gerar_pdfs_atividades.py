#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar PDFs de todas as atividades criadas
"""

import os
import subprocess
import glob

# Diretório das atividades
ATIVIDADES_DIR = r"c:\Users\corde\OneDrive\Desktop\informatica basica\socioeducativo\atividades"

def gerar_pdfs():
    """Gera PDFs para todos os arquivos .md na pasta atividades"""
    
    # Buscar todos os arquivos .md
    pattern = os.path.join(ATIVIDADES_DIR, "*.md")
    arquivos_md = glob.glob(pattern)
    
    print(f"🔍 Encontrados {len(arquivos_md)} arquivos Markdown")
    
    sucessos = 0
    erros = 0
    
    for arquivo_md in arquivos_md:
        try:
            # Nome do arquivo PDF
            arquivo_pdf = arquivo_md.replace('.md', '.pdf')
            
            # Comando marp
            cmd = ['marp', arquivo_md, '-o', arquivo_pdf]
            
            print(f"📄 Gerando: {os.path.basename(arquivo_pdf)}")
            
            # Executar comando
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ Sucesso: {os.path.basename(arquivo_pdf)}")
                sucessos += 1
            else:
                print(f"❌ Erro: {os.path.basename(arquivo_md)} - {result.stderr}")
                erros += 1
                
        except Exception as e:
            print(f"❌ Exceção: {os.path.basename(arquivo_md)} - {e}")
            erros += 1
    
    print(f"\n📊 RELATÓRIO:")
    print(f"✅ PDFs criados com sucesso: {sucessos}")
    print(f"❌ Erros: {erros}")
    print(f"📁 Total processado: {len(arquivos_md)}")

if __name__ == "__main__":
    print("🚀 Iniciando geração de PDFs das atividades...")
    gerar_pdfs()
    print("🎉 Processo concluído!")
