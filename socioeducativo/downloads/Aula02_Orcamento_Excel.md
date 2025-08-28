# Atividade 02: Orçamento Familiar Completo no Excel

## Objetivo
Aprender a criar e gerenciar um orçamento familiar completo usando Microsoft Excel, desenvolvendo habilidades financeiras essenciais para controle de gastos, planejamento e economia doméstica. Esta atividade aborda desde conceitos básicos até planilhas avançadas.

---

## Módulo 1: Educação Financeira Básica

### O que é Orçamento Familiar?
O orçamento familiar é uma ferramenta que ajuda a controlar o dinheiro que entra e sai da sua casa. Ele serve para:
- Saber para onde vai seu dinheiro
- Evitar dívidas
- Conseguir guardar dinheiro
- Realizar sonhos e metas

### Leitura Reflexiva
> "Quem não controla seu dinheiro, é controlado por ele. O orçamento não é uma prisão, é uma ferramenta de liberdade financeira."

**Perguntas para reflexão:**
1. Você sabe exatamente quanto ganha por mês?
2. Você sabe quanto gasta por mês?
3. Onde você mais gasta dinheiro?
4. Já ficou sem dinheiro antes do final do mês?
5. Tem algum sonho que precisa de dinheiro para realizar?

**Escreva suas respostas:**
```
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________
4. _________________________________________________
5. _________________________________________________
```

---

## Módulo 2: Levantamento de Receitas e Gastos

### Exercício 1: Mapeando suas Receitas
Liste todas as formas que você/sua família recebe dinheiro:

| Fonte de Renda | Valor Mensal | Quando Recebe |
|----------------|--------------|---------------|
| Salário        | R$ 1.500,00  | Todo dia 5    |
| Freelances     | R$ 300,00    | Variável      |
| Outros         |              |               |
| **TOTAL**      | **R$ 1.800,00** |           |

**Sua Planilha de Receitas:**
| Fonte de Renda | Valor Mensal | Quando Recebe |
|----------------|--------------|---------------|
|                |              |               |
|                |              |               |
|                |              |               |
|                |              |               |
| **TOTAL**      |              |               |

### Exercício 2: Mapeando seus Gastos
Anote TODOS os gastos do mês passado (use extratos, notas fiscais, memória):

#### Gastos Fixos (todo mês é igual)
| Item           | Valor        | Obrigatório? |
|----------------|--------------|--------------|
| Aluguel        | R$ 800,00    | Sim          |
| Luz            | R$ 150,00    | Sim          |
| Água           | R$ 80,00     | Sim          |
| Internet       | R$ 90,00     | Sim          |
| Celular        | R$ 50,00     | Sim          |
| **SUBTOTAL**   | **R$ 1.170,00** |           |

**Seus Gastos Fixos:**
| Item           | Valor        | Obrigatório? |
|----------------|--------------|--------------|
|                |              |              |
|                |              |              |
|                |              |              |
|                |              |              |
|                |              |              |
| **SUBTOTAL**   |              |              |

#### Gastos Variáveis (mudam todo mês)
| Item           | Valor        | Necessário?  |
|----------------|--------------|--------------|
| Mercado        | R$ 400,00    | Sim          |
| Transporte     | R$ 120,00    | Sim          |
| Roupas         | R$ 100,00    | Não          |
| Lazer          | R$ 80,00     | Não          |
| **SUBTOTAL**   | **R$ 700,00**|              |

**Seus Gastos Variáveis:**
| Item           | Valor        | Necessário?  |
|----------------|--------------|--------------|
|                |              |              |
|                |              |              |
|                |              |              |
|                |              |              |
|                |              |              |
| **SUBTOTAL**   |              |              |

---

## Módulo 3: Criando a Planilha no Excel

### Passo a Passo Detalhado

#### Etapa 1: Configuração Inicial
1. Abra o Microsoft Excel
2. Clique em "Pasta de trabalho em branco"
3. Na célula A1 digite: "ORÇAMENTO FAMILIAR"
4. Deixe em negrito e aumente a fonte
5. Na célula A2 digite o mês/ano: "AGOSTO/2025"

#### Etapa 2: Criando a Estrutura
```
A3: RECEITAS
A4: Salário
A5: Outros
A6: TOTAL RECEITAS

B4: 1500
B5: 300
B6: =B4+B5

A8: GASTOS FIXOS
A9: Aluguel
A10: Luz
A11: Água
A12: Internet
A13: TOTAL FIXOS

B9: 800
B10: 150
B11: 80
B12: 90
B13: =B9+B10+B11+B12
```

#### Etapa 3: Formatação
1. Selecione as células com valores
2. Clique com botão direito > "Formatar células"
3. Escolha "Moeda" > "R$"
4. Use cores diferentes para receitas (verde) e gastos (vermelho)

### Exercício Prático
Crie sua planilha seguindo o passo a passo acima. Salve como "Orcamento_MeuNome.xlsx"

---

## Módulo 4: Fórmulas Essenciais do Excel

### Fórmulas Básicas que Você Vai Usar

#### Soma
```
=SOMA(B4:B6)  // Soma da célula B4 até B6
```

#### Subtração
```
=B6-B13  // Receitas menos gastos
```

#### Porcentagem
```
=B9/B13*100  // Quanto % o aluguel representa dos gastos
```

#### Média
```
=MÉDIA(B4:B6)  // Média das receitas
```

### Exercício de Fórmulas
1. Calcule o total de receitas
2. Calcule o total de gastos
3. Calcule o saldo (receitas - gastos)
4. Calcule quanto % representa cada gasto
5. Crie uma fórmula que diga se sobrou ou faltou dinheiro

---

## Módulo 5: Análise Financeira

### Interpretando os Resultados

**Se SOBROU dinheiro:**
- Parabéns! Você está no azul
- Defina onde investir essa sobra
- Crie uma reserva de emergência

**Se FALTOU dinheiro:**
- Analise onde pode cortar gastos
- Veja se pode aumentar a renda
- Priorize gastos essenciais

### Exercício de Análise
Com base na sua planilha, responda:

1. **Sobrou ou faltou dinheiro?**
```
_________________________________________________
```

2. **Qual seu maior gasto?**
```
_________________________________________________
```

3. **Que gastos pode cortar?**
```
_________________________________________________
```

4. **Como pode aumentar a renda?**
```
_________________________________________________
```

---

## Módulo 6: Planejamento de Metas

### Definindo Objetivos Financeiros

#### Meta de Curto Prazo (até 6 meses)
Exemplo: Comprar um celular novo - R$ 800,00
- Quanto guardar por mês: R$ 800 ÷ 6 = R$ 133,33

#### Meta de Médio Prazo (6 meses a 2 anos)
Exemplo: Fazer um curso técnico - R$ 2.400,00
- Quanto guardar por mês: R$ 2.400 ÷ 24 = R$ 100,00

#### Meta de Longo Prazo (mais de 2 anos)
Exemplo: Comprar uma casa - R$ 20.000,00 (entrada)
- Quanto guardar por mês: R$ 20.000 ÷ 60 = R$ 333,33

### Suas Metas
**Curto Prazo:**
Meta: ________________________________
Valor: ________________________________
Meses: ________________________________
Por mês: ______________________________

**Médio Prazo:**
Meta: ________________________________
Valor: ________________________________
Meses: ________________________________
Por mês: ______________________________

**Longo Prazo:**
Meta: ________________________________
Valor: ________________________________
Meses: ________________________________
Por mês: ______________________________

---

## Módulo 7: Criando Gráficos no Excel

### Passo a Passo para Gráfico de Pizza (Gastos)

1. Selecione os dados dos gastos (nomes e valores)
2. Clique na aba "Inserir"
3. Escolha "Gráfico de Pizza"
4. Personalize cores e título
5. Adicione porcentagens

### Passo a Passo para Gráfico de Colunas (Receitas vs Gastos)

1. Crie uma tabela: Receitas | Gastos
2. Insira os valores totais
3. Selecione a tabela
4. Inserir > Gráfico de Colunas
5. Formate conforme sua preferência

### Exercício
Crie os dois gráficos na sua planilha e analise os resultados.

---

## Módulo 8: Controle Diário de Gastos

### Planilha de Controle Diário

Crie uma nova aba chamada "Controle Diário":

| Data  | Item Comprado | Valor    | Categoria | Necessário? |
|-------|---------------|----------|-----------|-------------|
| 01/08 | Pão           | R$ 5,00  | Alimentação| Sim        |
| 01/08 | Refrigerante  | R$ 4,00  | Alimentação| Não        |
| 02/08 | Ônibus        | R$ 4,50  | Transporte | Sim        |

### Exercício Semanal
Durante uma semana, anote TODOS os gastos nesta planilha. No final, some e analise.

---

## Módulo 9: Dicas de Economia Doméstica

### 20 Dicas para Economizar

1. **Energia elétrica:**
   - Desligue aparelhos da tomada
   - Use lâmpadas LED
   - Evite abrir a geladeira sem necessidade

2. **Água:**
   - Banhos mais rápidos
   - Feche a torneira ao escovar dentes
   - Reutilize água da máquina de lavar

3. **Alimentação:**
   - Faça lista de compras
   - Compare preços
   - Cozinhe em casa

4. **Transporte:**
   - Use transporte público
   - Caminhe quando possível
   - Compartilhe caronas

5. **Entretenimento:**
   - Use promoções de cinema
   - Faça programas gratuitos
   - Compartilhe assinaturas

### Desafio
Escolha 5 dicas e aplique por um mês. Calcule quanto economizou.

---

## Módulo 10: Reserva de Emergência

### O que é Reserva de Emergência?
É um dinheiro guardado para situações imprevistas:
- Perda de emprego
- Problemas de saúde
- Consertos urgentes
- Oportunidades

### Quanto Guardar?
- **Ideal:** 6 meses de gastos
- **Mínimo:** 3 meses de gastos
- **Para começar:** R$ 500,00

### Como Criar?
1. Calcule seus gastos mensais
2. Multiplique por 6
3. Divida por 12 meses
4. Guarde esse valor todo mês

### Exercício
**Seus gastos mensais:** R$ _________
**Meta de reserva (x6):** R$ _________
**Valor mensal para guardar:** R$ _________

---

## Módulo 11: Planilha Avançada - Projeção Anual

### Criando Projeção para 12 Meses

Crie uma planilha com:
- Receitas projetadas mês a mês
- Gastos fixos
- Gastos variáveis estimados
- Saldo acumulado
- Gráfico de evolução

### Estrutura:
```
    JAN  FEV  MAR  ABR  MAI  JUN  JUL  AGO  SET  OUT  NOV  DEZ
REC 1800 1800 1800 1800 1800 1800 1800 1800 1800 1800 1800 1800
GAS 1700 1700 1700 1700 1700 1700 1700 1700 1700 1700 1700 1700
SAL  100  100  100  100  100  100  100  100  100  100  100  100
ACU  100  200  300  400  500  600  700  800  900 1000 1100 1200
```

### Exercício
Crie sua projeção anual e analise em que mês conseguirá suas metas.

---

## Módulo 12: Avaliação e Reflexão Final

### Autoavaliação

**Conhecimento adquirido:**
- [ ] Sei fazer um orçamento básico
- [ ] Conheço minhas receitas e gastos
- [ ] Sei usar fórmulas básicas do Excel
- [ ] Criei metas financeiras
- [ ] Entendo a importância da reserva de emergência

**Mudanças planejadas:**
1. Que gastos vou cortar? ____________________
2. Como vou aumentar minha renda? ____________
3. Qual minha primeira meta? _________________
4. Quando vou revisar meu orçamento? __________

### Plano de Ação dos Próximos 30 Dias

**Semana 1:**
- [ ] Anotar todos os gastos diariamente
- [ ] Atualizar a planilha semanalmente

**Semana 2:**
- [ ] Identificar 3 gastos para cortar
- [ ] Pesquisar formas de renda extra

**Semana 3:**
- [ ] Implementar cortes planejados
- [ ] Começar a guardar para reserva

**Semana 4:**
- [ ] Revisar o orçamento do mês
- [ ] Planejar o próximo mês

### Reflexão Final
Escreva um texto sobre o que aprendeu e como pretende aplicar:

```
_________________________________________________
_________________________________________________
_________________________________________________
_________________________________________________
_________________________________________________
_________________________________________________
_________________________________________________
_________________________________________________
```

---

## Recursos Complementares

### Links Úteis
- Calculadora de juros compostos online
- Apps de controle financeiro
- Cursos gratuitos de educação financeira
- Simuladores de investimento

### Modelos de Planilhas
- Orçamento básico
- Controle de gastos diário
- Planejamento de metas
- Controle de dívidas

### Próximos Passos
Após dominar o orçamento básico:
1. Aprenda sobre investimentos
2. Estude sobre financiamento imobiliário
3. Conheça produtos bancários
4. Desenvolva múltiplas fontes de renda

---

## Download PDF
[⬇️ Baixar esta atividade em PDF](./Aula02_Orcamento_Excel.pdf)

## Voltar ao Menu
[← Voltar para atividades](../README.md)
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
