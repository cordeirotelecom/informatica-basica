---
marp: true
theme: default
paginate: true
backgroundColor: #f0f8ff
---

# 📊 ATIVIDADE 03 - MASCULINO
## Excel Básico: Planilha de Controle Pessoal

**📅 Data:** 03/09/2025 (Quarta-feira)  
**⏰ Duração:** 90 minutos  
**👥 Turma:** Masculina  

---

## 🎯 OBJETIVOS DA ATIVIDADE

### **Objetivo Geral:**
Introduzir conceitos fundamentais de planilhas eletrônicas através da criação de um sistema de controle pessoal masculino.

### **Objetivos Específicos:**
- Dominar interface e navegação do Excel
- Aplicar fórmulas básicas para cálculos automáticos
- Criar sistema de controle financeiro pessoal
- Desenvolver primeiro dashboard com gráficos

---

## 📚 CONTEÚDO PROGRAMÁTICO

### **MÓDULO 1 - Interface do Excel (20 minutos)**
- Células, linhas e colunas
- Barra de fórmulas e ferramentas
- Navegação e seleção eficiente
- Formatação básica de células

### **MÓDULO 2 - Criação de Planilha (50 minutos)**
- Estrutura de controle financeiro
- Inserção e validação de dados
- Fórmulas básicas: SOMA, MÉDIA, SE
- Formatação condicional automática

### **MÓDULO 3 - Gráfico e Análise (20 minutos)**
- Criação de gráfico de colunas
- Personalização visual
- Interpretação de dados
- Relatório executivo simples

---

## 🔧 RECURSOS NECESSÁRIOS

### **Hardware:**
- 1 computador por participante
- Calculadora (para conferência)
- Impressora para relatórios

### **Software:**
- Microsoft Excel 2016 ou superior
- Acesso a funções básicas
- Templates pré-configurados

### **Materiais:**
- Dados financeiros pessoais (simulados)
- Papel para anotações
- Caneta para cálculos manuais

---

## 👨‍🏫 METODOLOGIA

### **Estratégia Pedagógica:**
- **Demonstração passo-a-passo** pelo educador
- **Prática imediata** após cada conceito
- **Resolução de problemas** em tempo real
- **Competição saudável** entre participantes

### **Abordagem Masculina:**
- Foco em resultados quantificáveis
- Aplicação prática imediata
- Lógica matemática e objetiva
- Preparação para gestão e liderança

---

## 📋 ATIVIDADE PRÁTICA DETALHADA

### **ETAPA 1: Configuração Inicial (10 min)**

#### **Preparação do Excel:**
1. Abrir Excel e criar nova pasta de trabalho
2. Renomear planilha para "Controle_Pessoal"
3. Configurar zoom para 100%
4. Ativar grade e cabeçalhos
5. Definir região como Brasil (R$ e datas)

#### **Layout Inicial:**
```
A1: CONTROLE FINANCEIRO PESSOAL - [SEU NOME]
A2: Mês de Referência: Setembro/2025
A3: [vazio]
A4: RECEITAS
A5: [cabeçalhos da tabela]
```

---

### **ETAPA 2: Estrutura de Receitas (15 min)**

#### **Tabela de Receitas:**
```
   A           B           C           D
4  RECEITAS
5  Fonte       Valor       Data        Status
6  Salário     R$ 3.500    01/09/2025  Recebido
7  Freelance   R$ 800      05/09/2025  Pendente
8  Investim.   R$ 150      30/09/2025  Projetado
9  Outros      R$ 200      15/09/2025  Recebido
10 
11 TOTAL:      =SOMA(B6:B9)
```

#### **Formatação Aplicada:**
- **A4**: Calibri Bold 14pt, fundo azul claro
- **A5:D5**: Calibri Bold 11pt, bordas
- **B6:B9**: Formato moeda (R$)
- **C6:C9**: Formato data brasileira
- **B11**: Fórmula SOMA com formatação destacada

---

### **ETAPA 3: Estrutura de Despesas (15 min)**

#### **Tabela de Despesas Categorizada:**
```
   A              B           C           D
13 DESPESAS FIXAS
14 Categoria       Valor       Vencim.     Status
15 Moradia         R$ 1.200    05/09/2025  Pago
16 Transporte      R$ 380      10/09/2025  Pendente
17 Alimentação     R$ 600      01/09/2025  Pago
18 Telefone        R$ 89       15/09/2025  Pendente
19 Internet        R$ 79       20/09/2025  Agendado
20
21 SUBTOTAL:       =SOMA(B15:B19)
22
23 DESPESAS VARIÁVEIS
24 Categoria       Valor       Data        Necessid.
25 Lazer           R$ 300      Variável    Opcional
26 Vestuário       R$ 200      Variável    Baixa
27 Saúde           R$ 150      Conforme    Alta
28 Educação        R$ 250      Mensais     Alta
29
30 SUBTOTAL:       =SOMA(B25:B28)
31
32 TOTAL GERAL:    =B21+B30
```

---

### **ETAPA 4: Análise Financeira (10 min)**

#### **Dashboard de Indicadores:**
```
   A                    B               C
34 ANÁLISE FINANCEIRA
35
36 Total Receitas:      =B11           [fórmula]
37 Total Despesas:      =B32           [fórmula]
38 Saldo do Mês:        =B36-B37       [fórmula]
39 % Gastos/Receita:    =B37/B36       [formato %]
40
41 Status:              =SE(B38>0;"POSITIVO";"ATENÇÃO")
42
43 META DE ECONOMIA:    R$ 500
44 Economia Real:       =B38
45 Meta Atingida:       =SE(B44>=B43;"SIM";"NÃO")
```

#### **Formatação Condicional:**
- **B38**: Verde se positivo, vermelho se negativo
- **B39**: Verde se <70%, amarelo 70-85%, vermelho >85%
- **B41**: Verde para "POSITIVO", vermelho para "ATENÇÃO"

---

### **ETAPA 5: Fórmulas Avançadas (10 min)**

#### **Controle por Categoria:**
```
   A                 B                C
47 ANÁLISE POR CATEGORIA
48
49 Maior Despesa:    =MÁXIMO(B15:B19)
50 Menor Despesa:    =MÍNIMO(B15:B19)
51 Média Despesas:   =MÉDIA(B15:B19)
52
53 Dias até Salário: =DIAS(C6;HOJE())
54 Gasto Diário Médio: =B37/30
55
56 PROJEÇÃO ANUAL:
57 Receita Anual:    =B36*12
58 Despesa Anual:    =B37*12
59 Economia Anual:   =B57-B58
```

#### **Validação de Dados:**
- Dropdown para Status: "Pago", "Pendente", "Agendado"
- Dropdown para Necessidade: "Alta", "Média", "Baixa", "Opcional"

---

### **ETAPA 6: Criação de Gráfico (15 min)**

#### **Gráfico de Despesas por Categoria:**
1. **Selecionar dados:** A14:B19 (Despesas Fixas)
2. **Inserir gráfico:** Tipo Coluna Agrupada
3. **Personalizar:**
   - Título: "Distribuição de Despesas Fixas"
   - Cores: Tema azul empresarial
   - Rótulos de dados: Valores em R$
   - Eixo Y: Formatação moeda

#### **Gráfico de Pizza - Receitas:**
1. **Dados:** A5:B9 (fontes de receita)
2. **Tipo:** Pizza 2D
3. **Personalização:**
   - Título: "Composição das Receitas"
   - Porcentagens visíveis
   - Cores diferenciadas por fonte

---

### **ETAPA 7: Relatório Executivo (10 min)**

#### **Resumo Gerencial:**
```
   A                    B
61 RELATÓRIO EXECUTIVO - SETEMBRO 2025
62
63 Situação Geral:      [Status calculado]
64 Principal Fonte:     Salário (77% da receita)
65 Maior Gasto:         Moradia (34% das despesas)
66 Oportunidade:        Reduzir gastos variáveis
67
68 AÇÕES RECOMENDADAS:
69 1. Monitorar gastos com lazer
70 2. Buscar receitas extras
71 3. Revisar contratos fixos
72 4. Manter reserva de emergência
```

---

### **ETAPA 8: Proteção e Backup (5 min)**

#### **Medidas de Segurança:**
1. **Proteger fórmulas:** Bloquear células com fórmulas
2. **Senha na planilha:** Opcional para dados pessoais
3. **Backup automático:** Configurar salvamento
4. **Versão PDF:** Para arquivamento

---

## ✅ CRITÉRIOS DE AVALIAÇÃO

### **Técnico (50%):**
- Fórmulas funcionando corretamente
- Formatação consistente e profissional
- Gráficos bem configurados
- Estrutura lógica da planilha

### **Funcional (30%):**
- Dados completos e realistas
- Análise financeira coerente
- Relatório executivo claro
- Usabilidade da planilha

### **Criativo (20%):**
- Personalização visual apropriada
- Insights adicionais identificados
- Melhorias propostas
- Apresentação final

---

## 📁 ENTREGÁVEIS

### **Arquivo Principal:**
- **Nome:** `controle_pessoal_[nome_aluno].xlsx`
- **Formato:** Microsoft Excel (.xlsx)
- **Planilhas:** Controle_Pessoal (principal)

### **Elementos Obrigatórios:**
- [ ] Tabela de receitas completa
- [ ] Tabela de despesas categorizada
- [ ] Fórmulas de análise funcionando
- [ ] 2 gráficos personalizados
- [ ] Relatório executivo
- [ ] Formatação condicional aplicada

### **Versão Adicional:**
- **PDF do dashboard** para apresentação
- **Template em branco** para replicação

---

## 🎯 APLICAÇÃO PRÁTICA

### **Cenários de Uso:**
- Controle financeiro pessoal mensal
- Planejamento de investimentos
- Análise de gastos familiares
- Preparação para empréstimos

### **Expansões Futuras:**
- Controle de múltiplas contas
- Planejamento de metas financeiras
- Comparativo mensal/anual
- Integração com apps bancários

---

## 📊 COMPETÊNCIAS DESENVOLVIDAS

### **Excel Básico:**
- Navegação eficiente
- Formatação de células
- Fórmulas matemáticas básicas
- Criação de gráficos

### **Análise Financeira:**
- Categorização de gastos
- Cálculo de indicadores
- Interpretação de dados
- Relatórios executivos

### **Gestão Pessoal:**
- Organização financeira
- Planejamento de metas
- Controle de orçamento
- Tomada de decisões baseada em dados

---

## 📈 INDICADORES DE SUCESSO

### **Imediatos:**
- 100% dos participantes criam planilha funcional
- Fórmulas básicas dominadas
- Gráficos criados corretamente

### **Médio Prazo:**
- Uso contínuo da planilha criada
- Adaptação para necessidades pessoais
- Melhoria no controle financeiro

### **Longo Prazo:**
- Desenvolvimento de outras planilhas
- Base sólida para Excel avançado
- Aplicação profissional dos conhecimentos

---

## 🔄 PRÓXIMOS PASSOS

### **Atividade Seguinte:**
Design no Word: Convites e Cartões (04/09 - Feminino)

### **Conexões:**
- Excel Avançado: Gráficos e Análises (08/09)
- Excel para Negócios (17/09)
- Business Intelligence Básico (26/09)

### **Preparação:**
Salvar a planilha criada para usar como base nas próximas atividades de Excel.

**📊 Atividade completa para estabelecer bases sólidas em Excel com aplicação prática masculina!**
