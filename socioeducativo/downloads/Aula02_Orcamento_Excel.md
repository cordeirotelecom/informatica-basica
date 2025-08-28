# AULA 02 - ORÇAMENTO FINANCEIRO
**Socioeducativo - Informática Básica**

## 📋 OBJETIVO DA AULA
Ensinar como criar e controlar um orçamento familiar usando Microsoft Excel, desenvolvendo consciência financeira e habilidades de planejamento.

## 🎯 COMPETÊNCIAS DESENVOLVIDAS
- Educação financeira
- Organização de dados
- Planejamento pessoal
- Tomada de decisões conscientes

## 📊 ATIVIDADE PRÁTICA

### PASSO 1: Abrir o Microsoft Excel
1. Clique no botão Iniciar
2. Procure por "Excel"
3. Clique em "Microsoft Excel"
4. Escolha "Pasta de trabalho em branco"

### PASSO 2: Criar a Estrutura da Planilha

#### Cabeçalho (Linha 1):
```
A1: CONTROLE FINANCEIRO PESSOAL
```

#### Títulos das Colunas (Linha 3):
```
A3: DATA
B3: DESCRIÇÃO
C3: CATEGORIA
D3: ENTRADA (+)
E3: SAÍDA (-)
F3: SALDO
```

### PASSO 3: Formatação Inicial
1. Selecione A1 e digite o título
2. Selecione A1:F1 e clique em "Mesclar e Centralizar"
3. Aumente a fonte para 14 e deixe em negrito
4. Formate as colunas D e E como moeda (R$)

### PASSO 4: Inserir Dados de Exemplo

#### RECEITAS:
```
01/03/2025 | Salário | Trabalho | R$ 1.500,00 | | 
05/03/2025 | Freelance | Renda Extra | R$ 200,00 | |
```

#### DESPESAS:
```
02/03/2025 | Supermercado | Alimentação | | R$ 350,00 |
03/03/2025 | Conta de Luz | Casa | | R$ 120,00 |
04/03/2025 | Transporte | Mobilidade | | R$ 180,00 |
06/03/2025 | Remédio | Saúde | | R$ 45,00 |
07/03/2025 | Roupa | Vestuário | | R$ 80,00 |
```

### PASSO 5: Criar Fórmulas de Cálculo

#### Na coluna F (Saldo), usar fórmulas:
```
F4: =D4-E4 (para a primeira linha)
F5: =F4+D5-E5 (para as demais linhas)
```

#### Totais (na linha após os dados):
```
TOTAL ENTRADAS: =SOMA(D:D)
TOTAL SAÍDAS: =SOMA(E:E)
SALDO FINAL: =SOMA(D:D)-SOMA(E:E)
```

### PASSO 6: Criar Resumo por Categoria

#### Em uma nova área da planilha:
```
GASTOS POR CATEGORIA:
Alimentação: =SOMASE(C:C,"Alimentação",E:E)
Casa: =SOMASE(C:C,"Casa",E:E)
Mobilidade: =SOMASE(C:C,"Mobilidade",E:E)
Saúde: =SOMASE(C:C,"Saúde",E:E)
Vestuário: =SOMASE(C:C,"Vestuário",E:E)
```

### PASSO 7: Salvar o Arquivo
1. Pressione Ctrl + S
2. Nome: "Orcamento_[SeuNome]_[Mes][Ano]"
3. Salvar em: Documentos

## 💰 CONCEITOS FINANCEIROS IMPORTANTES

### 🟢 RECEITAS (DINHEIRO QUE ENTRA):
- Salário
- Freelances
- Vendas
- Benefícios
- Renda extra

### 🔴 DESPESAS (DINHEIRO QUE SAI):

#### ESSENCIAIS (Prioridade 1):
- Alimentação
- Moradia (aluguel/financiamento)
- Transporte
- Saúde
- Educação

#### IMPORTANTES (Prioridade 2):
- Vestuário
- Comunicação (telefone/internet)
- Lazer moderado

#### SUPÉRFLUOS (Prioridade 3):
- Compras desnecessárias
- Lazer excessivo
- Impulsos

## 🎯 EXERCÍCIOS PRÁTICOS

### EXERCÍCIO 1: Seu Orçamento Real
Crie uma planilha com seus dados reais (ou projeções):
1. Liste todas suas fontes de renda
2. Liste todos seus gastos do mês
3. Calcule se está no azul ou vermelho

### EXERCÍCIO 2: Planejamento de Economia
1. Defina uma meta de economia mensal: R$ ______
2. Identifique 3 gastos que pode reduzir:
   - Gasto 1: ________________
   - Gasto 2: ________________
   - Gasto 3: ________________

### EXERCÍCIO 3: Simulação de Emergência
E se acontecer um imprevisto de R$ 500,00?
1. Como você conseguiria esse dinheiro?
2. Onde poderia cortar gastos?

## 🤔 REFLEXÃO E DISCUSSÃO

### Perguntas para Pensar:
1. **Como o controle financeiro pode mudar sua vida?**
   - Reduz estresse
   - Permite planejar o futuro
   - Evita dívidas

2. **Qual a diferença entre necessidade e desejo?**
   - Necessidade: preciso para viver
   - Desejo: quero ter, mas posso viver sem

3. **Como ensinar educação financeira para crianças?**
   - Exemplo pessoal
   - Mesada controlada
   - Explicar valor do dinheiro

## 📈 METAS FINANCEIRAS

### CURTO PRAZO (1-6 meses):
- Criar reserva de emergência
- Quitar dívidas pequenas
- Controlar gastos

### MÉDIO PRAZO (6 meses - 2 anos):
- Comprar algo necessário
- Fazer um curso
- Melhorar condições de vida

### LONGO PRAZO (2+ anos):
- Casa própria
- Aposentadoria
- Educação dos filhos

## 💡 DICAS DE ECONOMIA

### 🏠 EM CASA:
- Apagar luzes desnecessárias
- Economizar água
- Cozinhar em casa
- Reutilizar quando possível

### 🛒 COMPRAS:
- Fazer lista antes de sair
- Comparar preços
- Evitar compras por impulso
- Aproveitar promoções reais

### 🚌 TRANSPORTE:
- Usar transporte público
- Caminhar quando possível
- Organizar trajetos
- Dividir caronas

## 📚 ATIVIDADE COMPLEMENTAR

### Plano de Ação Financeira:
1. **Minha situação atual:**
   - Renda: R$ ______
   - Gastos: R$ ______
   - Sobra/Falta: R$ ______

2. **Minha meta para os próximos 3 meses:**
   _________________________________

3. **3 ações que vou tomar:**
   - Ação 1: ________________
   - Ação 2: ________________
   - Ação 3: ________________

---

**"O dinheiro não traz felicidade, mas a organização financeira traz tranquilidade"**

*Desenvolvido com técnicas de planejamento de gestão sistêmica para desenvolvimento harmônico sustentável*
