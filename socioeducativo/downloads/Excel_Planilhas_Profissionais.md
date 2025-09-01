---
marp: true
theme: default
paginate: true
header: 'Programa Socioeducativo - Informática Básica'
footer: 'Microsoft Excel - Planilhas Profissionais'
---

# MICROSOFT EXCEL: PLANILHAS QUE VOCÊ USARÁ NA VIDA REAL
## Atividade Prática Completa - 90 minutos

**Objetivo:** Dominar Excel criando 4 planilhas essenciais para vida pessoal e profissional

**Você vai criar:**
- Controle financeiro pessoal completo
- Planilha de controle de estoque simples
- Lista de contatos profissionais organizada  
- Dashboard de vendas com gráficos

**Material necessário:** Microsoft Excel instalado

---

## PARTE 1: CONFIGURAÇÃO E PRIMEIRO PROJETO (25 minutos)

### PLANILHA 1: Controle Financeiro Pessoal

**PASSO 1:** Abra o Excel
- Windows + R → digite `excel` → Enter
- Escolha "Pasta de trabalho em branco"

**PASSO 2:** Configure a planilha
- Renomeie a aba: clique direito em "Plan1" → "Renomear" → "Financeiro"
- Salve: Ctrl + S → "Controle_Financeiro_[SeuNome]"

**PASSO 3:** Crie o cabeçalho (digite exatamente)
```
A1: CONTROLE FINANCEIRO PESSOAL - 2024
A2: Nome: [SEU NOME COMPLETO]
A3: Período: Janeiro a Dezembro 2024
```

**PASSO 4:** Formate o cabeçalho
- A1: Fonte 16, negrito, centralizar em A1:F1
- A2 e A3: Fonte 12, negrito

**PASSO 5:** Crie a estrutura de receitas (linha 5)
```
A5: RECEITAS MENSAIS          B5: JAN    C5: FEV    D5: MAR    E5: ABR    F5: MAI
A6: Salário principal         B6: 2500   C6: 2500   D6: 2500   E6: 2500   F6: 2500
A7: Trabalho extra           B7: 400    C7: 500    D7: 300    E7: 600    F7: 450
A8: Vendas/comissões         B8: 200    C8: 150    D8: 300    E8: 250    F8: 350
A9: Outras receitas          B9: 100    C9: 80     D9: 120    E9: 90     F9: 150
A10: TOTAL RECEITAS          B10: =SOMA(B6:B9)     C10: =SOMA(C6:C9)
```

**Continue a fórmula:** Arraste B10 até F10 para copiar as fórmulas

**PASSO 6:** Crie estrutura de despesas (linha 12)
```
A12: DESPESAS MENSAIS
A13: Moradia (aluguel/financ.)  B13: 800   C13: 800   D13: 800   E13: 800   F13: 800
A14: Alimentação               B14: 600   C14: 550   D14: 700   E14: 580   F14: 620
A15: Transporte               B15: 300   C15: 280   D15: 350   E15: 320   F15: 290
A16: Saúde                    B16: 150   C16: 200   D16: 120   E16: 180   F16: 160
A17: Educação                 B17: 200   C17: 200   D17: 250   E17: 200   F17: 200
A18: Lazer                    B18: 300   C18: 250   D18: 400   E18: 350   F18: 280
A19: Outros gastos            B19: 150   C19: 180   D19: 200   E19: 120   F19: 170
A20: TOTAL DESPESAS           B20: =SOMA(B13:B19)   C20: =SOMA(C13:C19)
```

**Continue:** Arraste B20 até F20

**PASSO 7:** Calcule o saldo mensal
```
A22: SALDO MENSAL             B22: =B10-B20         C22: =C10-C20
```

**Continue:** Arraste B22 até F22

**PASSO 8:** Formate como moeda
- Selecione B6:F22
- Botão direito → Formatar células → Moeda → R$ (Real)

---

## PARTE 2: CONTROLE DE ESTOQUE (20 minutos)

### PLANILHA 2: Estoque de Loja/Casa

**PASSO 1:** Nova aba
- Clique direito nas abas → Inserir → Planilha
- Renomeie para "Estoque"

**PASSO 2:** Cabeçalho do controle
```
A1: CONTROLE DE ESTOQUE
A2: Responsável: [SEU NOME]
A3: Última atualização: [DATA DE HOJE]

A5: CÓDIGO   B5: PRODUTO              C5: CATEGORIA    D5: QTDE    E5: PREÇO UNIT   F5: VALOR TOTAL   G5: ESTOQUE MÍN   H5: STATUS
A6: 001      B6: Caneta azul          C6: Material     D6: 50      E6: 1,50         F6: =D6*E6        G6: 10            H6: =SE(D6<G6;"REPOR";"OK")
A7: 002      B7: Papel A4 (resma)     C7: Material     D7: 8       E7: 25,00        F7: =D7*E7        G7: 5             H7: =SE(D7<G7;"REPOR";"OK")
A8: 003      B8: Grampeador           C8: Equipamento  D8: 3       E8: 15,00        F8: =D8*E8        G8: 2             H8: =SE(D8<G8;"REPOR";"OK")
A9: 004      B9: Tinta impressora     C9: Suprimento   D9: 2       E9: 80,00        F9: =D9*E9        G9: 3             H9: =SE(D9<G9;"REPOR";"OK")
A10: 005     B10: Clips               C10: Material    D10: 25     E10: 3,00        F10: =D10*E10     G10: 10           H10: =SE(D10<G10;"REPOR";"OK")
A11: 006     B11: Post-it             C11: Material    D11: 15     E11: 4,50        F11: =D11*E11     G11: 8            H11: =SE(D11<G11;"REPOR";"OK")
A12: 007     B12: Calculadora         C12: Equipamento D12: 1      E12: 35,00       F12: =D12*E12     G12: 2            H12: =SE(D12<G12;"REPOR";"OK")
A13: 008     B13: Fita adesiva        C13: Material    D13: 20     E13: 2,00        F13: =D13*E13     G13: 5            H13: =SE(D13<G13;"REPOR";"OK")

A15: TOTAL GERAL:                                                                    F15: =SOMA(F6:F13)
```

**PASSO 3:** Formatação especial
- E6:F15 → Formato moeda (R$)
- H6:H13 → Formatação condicional:
  - Selecione H6:H13 → Página Inicial → Formatação Condicional
  - "Realçar Regras das Células" → "Texto que Contém"
  - Digite "REPOR" → Escolha formato vermelho

**PASSO 4:** Adicione filtros
- Selecione A5:H13
- Dados → Filtro
- Agora você pode filtrar por categoria, status, etc.

---

## PARTE 3: LISTA DE CONTATOS PROFISSIONAIS (15 minutos)

### PLANILHA 3: Rede de Contatos

**PASSO 1:** Nova aba "Contatos"

**PASSO 2:** Estrutura completa
```
A1: LISTA DE CONTATOS PROFISSIONAIS
A3: NOME COMPLETO    B3: EMPRESA         C3: CARGO           D3: TELEFONE      E3: EMAIL                 F3: LINKEDIN           G3: ÁREA          H3: OBSERVAÇÕES
A4: João Silva       B4: Tech Solutions  C4: Gerente RH      D4: (11)99999-1234 E4: joao@techsol.com     F4: /in/joaosilva      G4: Recursos Humanos  H4: Contato para vagas TI
A5: Maria Santos     B5: Consultoria ABC C5: Consultora      D5: (11)98888-5678 E5: maria@abcconsult.com F5: /in/mariasantos    G5: Consultoria       H5: Especialista em carreira
A6: Pedro Oliveira   B6: Banco Central   C6: Analista        D6: (11)97777-9012 E6: pedro@bancoc.gov.br  F6: /in/pedrooliveira  G6: Financeiro        H6: Concurso público 2024
A7: Ana Costa        B7: Magazine Luiza  C7: Supervisora     D7: (11)96666-3456 E7: ana@magalu.com       F7: /in/anacosta       G7: Varejo            H7: Oportunidades vendas
A8: Carlos Ferreira  B8: SENAC          C8: Instrutor       D8: (11)95555-7890 E8: carlos@senac.br      F8: /in/carlosferreira G8: Educação          H8: Cursos profissionalizantes
A9: Lucia Almeida    B9: Freelancer     C9: Designer        D9: (11)94444-2468 E9: lucia@designer.com   F9: /in/luciaalmeida   G9: Design            H9: Projetos gráficos
A10: Roberto Lima    B10: Atacadão      C10: Gerente        D10: (11)93333-1357 E10: roberto@atacadao.com F10: /in/robertolima   G10: Supermercado     H10: Vagas operacionais
A11: Fernanda Rocha  B11: Prefeitura SP C11: Assistente     D11: (11)92222-8024 E11: fer@prefeitura.sp   F11: /in/fernandarocha G11: Público          H11: Concursos municipais

A13: TOTAL DE CONTATOS: B13: =CONT.VALORES(A4:A11)
A14: ÁREAS REPRESENTADAS: B14: =CONT.SE(G4:G11;"<>")
```

**PASSO 3:** Formatação e organização
- Congele a primeira linha: Exibir → Congelar Painéis → Congelar Linha Superior
- Adicione filtros em A3:H11
- Formate cabeçalhos com fundo azul claro

---

## PARTE 4: DASHBOARD DE VENDAS (30 minutos)

### PLANILHA 4: Relatório de Vendas com Gráficos

**PASSO 1:** Nova aba "Vendas"

**PASSO 2:** Dados de vendas mensais
```
A1: DASHBOARD DE VENDAS - 2024
A3: MÊS        B3: META      C3: REALIZADO   D3: %ATINGIDO    E3: VENDEDOR 1   F3: VENDEDOR 2   G3: VENDEDOR 3
A4: Janeiro    B4: 50000     C4: 52000       D4: =C4/B4       E4: 18000        F4: 17000        G4: 17000
A5: Fevereiro  B5: 55000     C5: 48000       D5: =C5/B5       E5: 16000        F5: 15000        G5: 17000
A6: Março      B6: 60000     C6: 65000       D6: =C6/B6       E6: 22000        F6: 21000        G6: 22000
A7: Abril      B7: 58000     C7: 61000       D7: =C7/B7       E7: 20000        F7: 20000        G7: 21000
A8: Maio       B8: 62000     C8: 59000       D8: =C8/B8       E8: 19000        F8: 19000        G8: 21000
A9: Junho      B9: 65000     C9: 70000       D9: =C9/B9       E9: 23000        F9: 22000        G9: 25000

A11: TOTAIS:   B11: =SOMA(B4:B9)  C11: =SOMA(C4:C9)  D11: =C11/B11    E11: =SOMA(E4:E9)  F11: =SOMA(F4:F9)  G11: =SOMA(G4:G9)
```

**PASSO 3:** Formatação dos números
- B4:C11 → Formato moeda
- D4:D11 → Formato percentual (%)
- E4:G11 → Formato moeda

**PASSO 4:** Análise de desempenho
```
A13: ANÁLISE DE DESEMPENHO
A14: Melhor mês (vendas):    B14: =ÍNDICE(A4:A9,CORRESP(MÁXIMO(C4:C9),C4:C9,0))
A15: Pior mês (vendas):      B15: =ÍNDICE(A4:A9,CORRESP(MÍNIMO(C4:C9),C4:C9,0))
A16: Média mensal:           B16: =MÉDIA(C4:C9)
A17: Crescimento total:      B17: =(C9-C4)/C4

A19: RANKING DE VENDEDORES
A20: 1º Lugar:               B20: =SE(E11>F11,SE(E11>G11,"Vendedor 1",SE(G11>F11,"Vendedor 3","Vendedor 2")),SE(F11>G11,"Vendedor 2","Vendedor 3"))
A21: Melhor vendas:          B21: =MÁXIMO(E11,F11,G11)
```

**PASSO 5:** Criar gráfico de vendas mensais
1. Selecione A3:C9
2. Inserir → Gráficos → Colunas Agrupadas
3. Mova o gráfico para posição E13:J25
4. Título do gráfico: "Vendas x Meta Mensal"

**PASSO 6:** Criar gráfico de pizza (vendedores)
1. Selecione E3:G3 e E11:G11 (use Ctrl para selecionar múltiplas áreas)
2. Inserir → Gráficos → Pizza
3. Posicione em E27:J35
4. Título: "Participação por Vendedor"

**PASSO 7:** Formatação condicional para metas
- Selecione D4:D9
- Formatação Condicional → Barras de Dados → Escolha azul
- Adicione segunda regra: Maior que 100% → Fundo verde

---

## FINALIZANDO SEU TRABALHO (5 minutos)

### Revisão e Organização Final

**PASSO 1:** Verifique todas as fórmulas
- Teste mudando alguns valores
- Veja se cálculos atualizam automaticamente
- Corrija erros se houver

**PASSO 2:** Formatação final
- Ajuste largura das colunas (duplo clique na divisa)
- Alinhe títulos centralizados
- Deixe números alinhados à direita

**PASSO 3:** Proteja suas fórmulas
- Selecione células com fórmulas
- Botão direito → Formatar células → Proteção → Bloqueada
- Revisão → Proteger Planilha → OK

**PASSO 4:** Salve em múltiplos formatos
- Ctrl + S (salva .xlsx)
- Arquivo → Exportar → PDF → Cada aba em página separada

---

## FUNCIONALIDADES AVANÇADAS APRENDIDAS

### Fórmulas Essenciais que Você Domina Agora:

✅ **SOMA()** - Somar intervalos de células
✅ **SE()** - Condições lógicas simples  
✅ **MÁXIMO()/MÍNIMO()** - Encontrar maior e menor valor
✅ **MÉDIA()** - Calcular médias
✅ **CONT.VALORES()** - Contar células com dados
✅ **ÍNDICE()/CORRESP()** - Buscar valores em listas

### Formatação Profissional:
✅ **Formatação condicional** - Cores automáticas por regras
✅ **Filtros** - Organizar e encontrar dados rapidamente
✅ **Gráficos** - Visualização profissional de dados
✅ **Congelar painéis** - Manter cabeçalhos sempre visíveis
✅ **Proteção** - Evitar alterações acidentais

### Aplicações Práticas:
✅ **Controle financeiro pessoal** - Organize sua vida financeira
✅ **Gestão de estoque** - Para pequenos negócios
✅ **Rede de contatos** - Networking profissional organizado
✅ **Relatórios de vendas** - Análise de performance

**Próximos passos:** Use estas planilhas como modelo para criar suas próprias versões personalizadas. Excel é uma ferramenta poderosa que você agora domina!
