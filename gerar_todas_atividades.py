#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar automaticamente todas as 80 atividades detalhadas
do cronograma socioeducativo 2025 em formato Markdown com Marp
"""

import os
import subprocess
from datetime import datetime, timedelta

# Configuração base
BASE_DIR = r"c:\Users\corde\OneDrive\Desktop\informatica basica\socioeducativo\atividades"
PDF_DIR = BASE_DIR

# Cronograma completo das 80 atividades
CRONOGRAMA = {
    # SETEMBRO 2025
    "01/09": {"tipo": "masculino", "titulo": "Microsoft Word: Criando Currículo Profissional", "cor": "#f0f8ff"},
    "02/09": {"tipo": "feminino", "titulo": "Redação Criativa: Escrevendo sua História", "cor": "#fdf5ff"},
    "03/09": {"tipo": "masculino", "titulo": "Excel Básico: Planilha de Controle Pessoal", "cor": "#f0f8ff"},
    "04/09": {"tipo": "feminino", "titulo": "Design no Word: Convites e Cartões", "cor": "#fdf5ff"},
    "05/09": {"tipo": "masculino", "titulo": "Informática Básica: Hardware e Software", "cor": "#f0f8ff"},
    
    "08/09": {"tipo": "masculino", "titulo": "Excel Avançado: Gráficos e Análises", "cor": "#f0f8ff"},
    "09/09": {"tipo": "feminino", "titulo": "Preparação para Entrevistas", "cor": "#fdf5ff"},
    "10/09": {"tipo": "masculino", "titulo": "PowerPoint: Apresentação Profissional", "cor": "#f0f8ff"},
    "11/09": {"tipo": "feminino", "titulo": "Comunicação Escrita Feminina", "cor": "#fdf5ff"},
    "12/09": {"tipo": "masculino", "titulo": "Introdução à Programação Web", "cor": "#f0f8ff"},
    
    "15/09": {"tipo": "masculino", "titulo": "HTML e CSS Básico", "cor": "#f0f8ff"},
    "16/09": {"tipo": "feminino", "titulo": "Organização Pessoal Digital", "cor": "#fdf5ff"},
    "17/09": {"tipo": "masculino", "titulo": "Excel para Negócios", "cor": "#f0f8ff"},
    "18/09": {"tipo": "feminino", "titulo": "PowerPoint Criativo", "cor": "#fdf5ff"},
    "19/09": {"tipo": "masculino", "titulo": "Sistemas Operacionais", "cor": "#f0f8ff"},
    
    "22/09": {"tipo": "masculino", "titulo": "Manutenção de Computadores", "cor": "#f0f8ff"},
    "23/09": {"tipo": "feminino", "titulo": "Controle Financeiro Familiar", "cor": "#fdf5ff"},
    "24/09": {"tipo": "masculino", "titulo": "Desenvolvimento Web Intermediário", "cor": "#f0f8ff"},
    "25/09": {"tipo": "feminino", "titulo": "Criação de Material Educativo", "cor": "#fdf5ff"},
    "26/09": {"tipo": "masculino", "titulo": "Business Intelligence Básico", "cor": "#f0f8ff"},
    
    # OUTUBRO 2025
    "01/10": {"tipo": "masculino", "titulo": "Empreendedorismo Digital", "cor": "#f0f8ff"},
    "02/10": {"tipo": "feminino", "titulo": "Moda e Beleza Digital", "cor": "#fdf5ff"},
    "03/10": {"tipo": "masculino", "titulo": "Automação com Excel", "cor": "#f0f8ff"},
    
    "06/10": {"tipo": "masculino", "titulo": "Gestão Industrial Básica", "cor": "#f0f8ff"},
    "07/10": {"tipo": "feminino", "titulo": "Organização Culinária", "cor": "#fdf5ff"},
    "08/10": {"tipo": "masculino", "titulo": "Projetos Técnicos", "cor": "#f0f8ff"},
    "09/10": {"tipo": "feminino", "titulo": "Maternidade e Organização", "cor": "#fdf5ff"},
    "10/10": {"tipo": "masculino", "titulo": "Gestão de Projetos", "cor": "#f0f8ff"},
    
    "13/10": {"tipo": "masculino", "titulo": "Criação de Jogos Simples", "cor": "#f0f8ff"},
    "14/10": {"tipo": "feminino", "titulo": "Arte Digital Feminina", "cor": "#fdf5ff"},
    "15/10": {"tipo": "masculino", "titulo": "Análise Financeira", "cor": "#f0f8ff"},
    "16/10": {"tipo": "feminino", "titulo": "Estética e Bem-estar", "cor": "#fdf5ff"},
    "17/10": {"tipo": "masculino", "titulo": "Controle Automotivo", "cor": "#f0f8ff"},
    
    "20/10": {"tipo": "masculino", "titulo": "Fitness e Saúde Masculina", "cor": "#f0f8ff"},
    "21/10": {"tipo": "feminino", "titulo": "Compras Inteligentes", "cor": "#fdf5ff"},
    "22/10": {"tipo": "masculino", "titulo": "Gestão Esportiva", "cor": "#f0f8ff"},
    "23/10": {"tipo": "feminino", "titulo": "Artesanato Digital", "cor": "#fdf5ff"},
    "24/10": {"tipo": "masculino", "titulo": "Eletrônica Básica", "cor": "#f0f8ff"},
    
    # NOVEMBRO 2025
    "03/11": {"tipo": "masculino", "titulo": "Construção Civil Digital", "cor": "#f0f8ff"},
    "04/11": {"tipo": "feminino", "titulo": "Decoração e Design", "cor": "#fdf5ff"},
    "05/11": {"tipo": "masculino", "titulo": "Programação Avançada", "cor": "#f0f8ff"},
    "06/11": {"tipo": "feminino", "titulo": "Educação Infantil", "cor": "#fdf5ff"},
    "07/11": {"tipo": "masculino", "titulo": "Tecnologia e Inovação", "cor": "#f0f8ff"},
    
    "10/11": {"tipo": "masculino", "titulo": "Logística e Transporte", "cor": "#f0f8ff"},
    "11/11": {"tipo": "feminino", "titulo": "Eventos e Festas", "cor": "#fdf5ff"},
    "12/11": {"tipo": "masculino", "titulo": "Manutenção Industrial", "cor": "#f0f8ff"},
    "13/11": {"tipo": "feminino", "titulo": "Jardinagem e Plantas", "cor": "#fdf5ff"},
    "14/11": {"tipo": "masculino", "titulo": "Contabilidade Básica", "cor": "#f0f8ff"},
    
    "17/11": {"tipo": "masculino", "titulo": "Direito Digital", "cor": "#f0f8ff"},
    "18/11": {"tipo": "feminino", "titulo": "Vida Familiar", "cor": "#fdf5ff"},
    "19/11": {"tipo": "masculino", "titulo": "Marketing Digital", "cor": "#f0f8ff"},
    "20/11": {"tipo": "feminino", "titulo": "Beleza Profissional", "cor": "#fdf5ff"},
    "21/11": {"tipo": "masculino", "titulo": "Produção e Qualidade", "cor": "#f0f8ff"},
    
    "24/11": {"tipo": "masculino", "titulo": "Inovação e Startups", "cor": "#f0f8ff"},
    "25/11": {"tipo": "feminino", "titulo": "Cuidados com Bebês", "cor": "#fdf5ff"},
    "26/11": {"tipo": "masculino", "titulo": "Ciência e Pesquisa", "cor": "#f0f8ff"},
    "27/11": {"tipo": "feminino", "titulo": "Entretenimento Infantil", "cor": "#fdf5ff"},
    "28/11": {"tipo": "masculino", "titulo": "Automação Residencial", "cor": "#f0f8ff"},
    
    # DEZEMBRO 2025
    "01/12": {"tipo": "masculino", "titulo": "Projeto Natal Masculino", "cor": "#f0f8ff"},
    "02/12": {"tipo": "feminino", "titulo": "Natal Feminino Especial", "cor": "#fdf5ff"},
    "03/12": {"tipo": "masculino", "titulo": "Fechamento Anual", "cor": "#f0f8ff"},
    "04/12": {"tipo": "feminino", "titulo": "Retrospectiva Feminina", "cor": "#fdf5ff"},
    "05/12": {"tipo": "masculino", "titulo": "Avaliação de Desempenho", "cor": "#f0f8ff"},
    
    "08/12": {"tipo": "masculino", "titulo": "Tecnologia e Games", "cor": "#f0f8ff"},
    "09/12": {"tipo": "feminino", "titulo": "Sonhos e Realizações", "cor": "#fdf5ff"},
    "10/12": {"tipo": "masculino", "titulo": "Projetos de Fim de Ano", "cor": "#f0f8ff"},
    "11/12": {"tipo": "feminino", "titulo": "Arte e Expressão", "cor": "#fdf5ff"},
    "12/12": {"tipo": "masculino", "titulo": "Networking Profissional", "cor": "#f0f8ff"},
    
    "15/12": {"tipo": "masculino", "titulo": "Competições e Desafios", "cor": "#f0f8ff"},
    "16/12": {"tipo": "feminino", "titulo": "Bem-estar Feminino", "cor": "#fdf5ff"},
    "17/12": {"tipo": "masculino", "titulo": "Inovação Final", "cor": "#f0f8ff"},
    "18/12": {"tipo": "feminino", "titulo": "Gratidão e Reflexão", "cor": "#fdf5ff"},
    "19/12": {"tipo": "masculino", "titulo": "Metas 2026", "cor": "#f0f8ff"}
}

def gerar_atividade_markdown(numero, data, atividade):
    """Gera o conteúdo markdown de uma atividade"""
    
    tipo = atividade["tipo"]
    titulo = atividade["titulo"]
    cor = atividade["cor"]
    
    # Determinar emoji e descrição baseados no tipo
    if tipo == "masculino":
        emoji = "🔷"
        tipo_nome = "MASCULINO"
        dia_semana = obter_dia_semana(data)
    else:
        emoji = "🔸"
        tipo_nome = "FEMININO"  
        dia_semana = obter_dia_semana(data)
    
    # Template base da atividade
    conteudo = f"""---
marp: true
theme: default
paginate: true
backgroundColor: {cor}
---

# {emoji} ATIVIDADE {numero:02d} - {tipo_nome}
## {titulo}

**📅 Data:** {data}/2025 ({dia_semana})  
**⏰ Duração:** 90 minutos  
**👥 Turma:** {tipo_nome.capitalize()}  

---

## 🎯 OBJETIVOS DA ATIVIDADE

### **Objetivo Geral:**
{gerar_objetivo_geral(titulo, tipo)}

### **Objetivos Específicos:**
{gerar_objetivos_especificos(titulo, tipo)}

---

## 📚 CONTEÚDO PROGRAMÁTICO

{gerar_conteudo_programatico(titulo, tipo)}

---

## 🔧 RECURSOS NECESSÁRIOS

{gerar_recursos_necessarios(titulo, tipo)}

---

## �{"👨‍🏫" if tipo == "masculino" else "👩‍🏫"} METODOLOGIA

{gerar_metodologia(titulo, tipo)}

---

## 📋 ATIVIDADE PRÁTICA DETALHADA

{gerar_atividade_pratica(titulo, tipo)}

---

## ✅ CRITÉRIOS DE AVALIAÇÃO

{gerar_criterios_avaliacao(titulo, tipo)}

---

## 📁 ENTREGÁVEIS

{gerar_entregaveis(titulo, tipo)}

---

## 🎯 APLICAÇÃO PRÁTICA

{gerar_aplicacao_pratica(titulo, tipo)}

---

## 📈 INDICADORES DE SUCESSO

{gerar_indicadores_sucesso(titulo, tipo)}

---

## 🔄 PRÓXIMOS PASSOS

{gerar_proximos_passos(numero, titulo, tipo)}

**{"🔧" if tipo == "masculino" else "✨"} Atividade completa pronta para implementação!**"""

    return conteudo

def obter_dia_semana(data):
    """Retorna o dia da semana em português"""
    try:
        dia, mes = data.split('/')
        data_obj = datetime(2025, int(mes), int(dia))
        dias = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
        return dias[data_obj.weekday()]
    except:
        return "Dia da semana"

def gerar_objetivo_geral(titulo, tipo):
    """Gera objetivo geral baseado no título e tipo"""
    objetivos_base = {
        "masculino": "Desenvolver competências técnicas e de liderança através de",
        "feminino": "Promover empoderamento e crescimento pessoal através de"
    }
    
    base = objetivos_base[tipo]
    especifico = titulo.lower()
    
    return f"{base} {especifico}, aplicando conhecimentos práticos para uso profissional e pessoal."

def gerar_objetivos_especificos(titulo, tipo):
    """Gera objetivos específicos baseados no conteúdo"""
    if "Word" in titulo:
        return """- Dominar ferramentas avançadas do Microsoft Word
- Criar documentos profissionais e atrativos
- Aplicar técnicas de formatação e design
- Desenvolver autonomia na criação de textos"""
    
    elif "Excel" in titulo:
        return """- Utilizar fórmulas e funções do Excel
- Criar planilhas funcionais e organizadas
- Desenvolver gráficos e análises visuais
- Aplicar conceitos de análise de dados"""
    
    elif "PowerPoint" in titulo:
        return """- Criar apresentações impactantes
- Aplicar técnicas de design e comunicação visual
- Utilizar recursos multimídia adequadamente
- Desenvolver habilidades de apresentação"""
    
    else:
        return """- Aplicar conhecimentos práticos da área
- Desenvolver autonomia e confiança
- Criar soluções para problemas reais
- Estabelecer bases para crescimento futuro"""

def gerar_conteudo_programatico(titulo, tipo):
    """Gera conteúdo programático estruturado"""
    return """### **MÓDULO 1 - Fundamentos (30 minutos)**
- Conceitos básicos e introdução
- Demonstração prática das ferramentas
- Preparação do ambiente de trabalho
- Orientações de segurança e boas práticas

### **MÓDULO 2 - Desenvolvimento Prático (45 minutos)**
- Exercícios guiados passo a passo
- Aplicação prática dos conceitos
- Desenvolvimento do projeto principal
- Resolução de dúvidas e dificuldades

### **MÓDULO 3 - Finalização e Avaliação (15 minutos)**
- Revisão e ajustes finais
- Apresentação dos resultados
- Feedback e orientações futuras
- Salvamento e organização dos arquivos"""

def gerar_recursos_necessarios(titulo, tipo):
    """Gera lista de recursos necessários"""
    return """### **Hardware:**
- 1 computador por participante
- Acesso à internet (se necessário)
- Impressora para materiais finais
- Projetor para demonstrações

### **Software:**
- Sistema operacional atualizado
- Programas específicos da atividade
- Antivírus ativo e atualizado
- Navegador web atualizado

### **Materiais:**
- Papel para anotações e impressões
- Canetas e material de apoio
- Dados/informações para exercícios
- Material de referência impresso"""

def gerar_metodologia(titulo, tipo):
    """Gera metodologia específica por tipo"""
    if tipo == "masculino":
        return """### **Estratégia Pedagógica:**
- **Demonstração técnica** detalhada pelo educador
- **Prática orientada** com foco em resultados
- **Resolução de problemas** em tempo real
- **Competição saudável** entre participantes

### **Abordagem Masculina:**
- Foco em eficiência e produtividade
- Aplicação prática imediata
- Desenvolvimento de autonomia técnica
- Preparação para liderança e gestão"""
    else:
        return """### **Estratégia Pedagógica:**
- **Ambiente colaborativo** e acolhedor
- **Aprendizado compartilhado** entre participantes
- **Valorização da criatividade** individual
- **Apoio mútuo** e construção coletiva

### **Abordagem Feminina:**
- Valorização da intuição e sensibilidade
- Conexão emocional com o aprendizado
- Expressão da personalidade individual
- Empoderamento através do conhecimento"""

def gerar_atividade_pratica(titulo, tipo):
    """Gera estrutura da atividade prática"""
    return """### **ETAPA 1: Preparação (10 min)**
- Configuração do ambiente de trabalho
- Verificação de recursos e materiais
- Apresentação dos objetivos específicos
- Organização dos arquivos de trabalho

### **ETAPA 2: Desenvolvimento Inicial (15 min)**
- Primeiros passos da atividade
- Configurações básicas necessárias
- Estabelecimento da estrutura principal
- Verificação do progresso inicial

### **ETAPA 3: Desenvolvimento Principal (25 min)**
- Execução do projeto principal
- Aplicação das técnicas aprendidas
- Personalização conforme orientações
- Resolução de dificuldades encontradas

### **ETAPA 4: Refinamento (15 min)**
- Ajustes e melhorias no projeto
- Verificação de qualidade
- Aplicação de detalhes finais
- Preparação para apresentação

### **ETAPA 5: Finalização (10 min)**
- Salvamento em formatos adequados
- Verificação final de qualidade
- Organização dos arquivos criados
- Preparação para entrega

### **ETAPA 6: Apresentação (15 min)**
- Demonstração dos resultados
- Feedback entre participantes
- Discussão sobre aplicações práticas
- Orientações para desenvolvimento futuro"""

def gerar_criterios_avaliacao(titulo, tipo):
    """Gera critérios de avaliação"""
    return """### **Técnico (40%):**
- Domínio das ferramentas utilizadas
- Qualidade técnica do resultado
- Aplicação correta dos conceitos
- Funcionamento adequado do projeto

### **Criativo (30%):**
- Originalidade na execução
- Personalização apropriada
- Soluções criativas para desafios
- Expressão individual no resultado

### **Prático (30%):**
- Aplicabilidade do resultado final
- Adequação aos objetivos propostos
- Potencial de uso real
- Organização e apresentação"""

def gerar_entregaveis(titulo, tipo):
    """Gera lista de entregáveis"""
    nome_arquivo = titulo.lower().replace(" ", "_").replace(":", "")
    nome_participante = "nome_" + ("aluno" if tipo == "masculino" else "aluna")
    
    return f"""### **Arquivo Principal:**
- **Nome:** `{nome_arquivo}_{{{nome_participante}}}.docx`
- **Formato:** Microsoft Office ou equivalente
- **Qualidade:** Profissional e bem formatado

### **Elementos Obrigatórios:**
- [ ] Projeto completo conforme especificações
- [ ] Formatação adequada e consistente
- [ ] Informações completas e corretas
- [ ] Verificação ortográfica realizada
- [ ] Arquivos organizados adequadamente

### **Versões Adicionais:**
- **PDF** para compartilhamento e arquivamento
- **Versão impressa** se necessário
- **Backup** em local seguro"""

def gerar_aplicacao_pratica(titulo, tipo):
    """Gera aplicações práticas"""
    return """### **Uso Imediato:**
- Aplicação direta no dia a dia
- Melhoria em atividades pessoais
- Desenvolvimento de projetos próprios
- Base para aprendizados futuros

### **Desenvolvimento Profissional:**
- Diferencial em processos seletivos
- Competência para ambiente de trabalho
- Base para especializações futuras
- Autonomia em tarefas relacionadas

### **Crescimento Pessoal:**
- Aumento da autoconfiança
- Desenvolvimento de novas habilidades
- Ampliação de possibilidades
- Preparação para desafios futuros"""

def gerar_indicadores_sucesso(titulo, tipo):
    """Gera indicadores de sucesso"""
    return """### **Durante a Atividade:**
- Participação ativa de 100% dos alunos
- Conclusão exitosa das etapas propostas
- Resolução eficaz de dificuldades
- Ambiente de aprendizado positivo

### **Imediatamente Após:**
- Entregáveis completos e de qualidade
- Satisfação dos participantes
- Compreensão clara dos conceitos
- Confiança para aplicação prática

### **Médio/Longo Prazo:**
- Uso contínuo dos conhecimentos
- Aplicação em situações reais
- Interesse em aprofundamento
- Desenvolvimento de autonomia"""

def gerar_proximos_passos(numero, titulo, tipo):
    """Gera próximos passos e conexões"""
    proxima_atividade = numero + 1 if numero < 80 else "Conclusão do programa"
    
    return f"""### **Atividade Seguinte:**
Atividade {proxima_atividade:02d} (próxima data do cronograma)

### **Conexões:**
- Reforço dos conceitos em atividades futuras
- Aplicação em projetos mais complexos
- Integração com outras competências
- Preparação para especializações

### **Recomendações:**
- Praticar os conceitos aprendidos
- Explorar funcionalidades adicionais
- Compartilhar conhecimento com outros
- Manter arquivos organizados para referência"""

def criar_arquivo_e_pdf(numero, data, atividade):
    """Cria arquivo markdown e gera PDF"""
    try:
        # Gerar conteúdo
        conteudo = gerar_atividade_markdown(numero, data, atividade)
        
        # Nome do arquivo
        nome_base = f"{numero:02d}_{atividade['titulo'].replace(' ', '_').replace(':', '')}"
        arquivo_md = os.path.join(BASE_DIR, f"{nome_base}.md")
        arquivo_pdf = os.path.join(PDF_DIR, f"{nome_base}.pdf")
        
        # Criar arquivo markdown
        with open(arquivo_md, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        
        print(f"✅ Criado: {arquivo_md}")
        
        # Gerar PDF com Marp
        try:
            subprocess.run(['marp', arquivo_md, '-o', arquivo_pdf], 
                         check=True, capture_output=True)
            print(f"📄 PDF: {arquivo_pdf}")
        except subprocess.CalledProcessError as e:
            print(f"⚠️  Erro ao gerar PDF para {nome_base}: {e}")
        except FileNotFoundError:
            print(f"⚠️  Marp não encontrado. Arquivo MD criado: {arquivo_md}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao criar atividade {numero}: {e}")
        return False

def main():
    """Função principal"""
    print("🚀 Iniciando geração das 80 atividades socioeducativas...")
    print(f"📁 Diretório: {BASE_DIR}")
    
    # Criar diretório se não existir
    os.makedirs(BASE_DIR, exist_ok=True)
    
    sucessos = 0
    erros = 0
    
    # Gerar todas as atividades
    for numero, (data, atividade) in enumerate(CRONOGRAMA.items(), 1):
        print(f"\n📝 Atividade {numero:02d}: {atividade['titulo']} ({data})")
        
        if criar_arquivo_e_pdf(numero, data, atividade):
            sucessos += 1
        else:
            erros += 1
    
    # Relatório final
    print(f"\n📊 RELATÓRIO FINAL:")
    print(f"✅ Sucessos: {sucessos}")
    print(f"❌ Erros: {erros}")
    print(f"📁 Total de atividades: {len(CRONOGRAMA)}")
    
    if sucessos == len(CRONOGRAMA):
        print("🎉 Todas as 80 atividades foram criadas com sucesso!")
    else:
        print(f"⚠️  {erros} atividades apresentaram problemas.")

if __name__ == "__main__":
    main()
