---
name: study-plan
description: Use quando o estudante quer organizar o que estudar, em que ordem e em quanto tempo. Também serve quando ele diz que está perdido ou não sabe por onde começar.
---

# Skill: Plano de estudos

Ajuda o estudante a transformar um objetivo de carreira em um plano de estudos claro, realista e conectado às experiências da DIO.

## Quando usar

O estudante quer saber o que estudar, sente que está perdido, ou pediu ajuda para se organizar. Se ele ainda está escolhendo entre as Formações da Carreira AI Builder, use antes a skill `ai-builder-path`.

## Princípio: ancore o plano no conteúdo real da DIO

Sempre construa o plano em torno de algo concreto que existe na DIO:
- uma experiência educacional (Bootcamp, Formação ou Aceleração), ou
- uma Carreira da DIO (https://www.dio.me/#careers).

E baseie o plano no **conteúdo real** dessa experiência (os módulos da página pública dela, a LP), nunca apenas no nome dela ou no seu conhecimento geral do tema. Se a base for uma Carreira, escolha com o estudante a primeira Formação ou o primeiro Bootcamp dela e siga os módulos dessa experiência.

## Processo

### 1. Entenda o objetivo e o perfil

Se o estudante já trouxe um objetivo claro ou um plano de ação (por exemplo, o que montou em um Curso), parta dele e pergunte só o que faltar. Caso contrário, faça perguntas, uma de cada vez, para entender:
- O objetivo dele (por exemplo: primeiro emprego, mudar de área, concluir um Bootcamp específico).
- O nível atual no assunto (nunca estudou, sabe o básico, já tem experiência).
- Quanto tempo por dia ou por semana ele consegue dedicar, e em quais dias.
- Se existe um prazo.

O perfil é importante: quanto melhor você o conhece, mais simples e executável fica o plano. Comece pelo objetivo e vá aprofundando, sem perguntar tudo de uma vez.

### 2. Descubra os módulos da trilha (não pule, e não escreva código)

O plano precisa seguir os módulos reais da trilha, não o seu conhecimento geral do tema. Mas conseguir esses módulos tem que ser barato e rápido.

> IMPORTANTE: **Nunca escreva nem rode scripts para ler, baixar ou raspar a página** (veja a regra 8 do `AGENTS.md`). E não busque a ementa perfeita e completa: uma visão geral dos módulos principais já basta.

Siga esta ordem e pare assim que tiver os módulos:

1. **Encontre a LP pública.** O estudante costuma compartilhar o link de acesso interno, no padrão `https://web.dio.me/track/SLUG`. O slug é a parte final dele. Se o tipo não estiver claro (o link `track/SLUG` é igual para todos), use as pistas da conversa ou pergunte ao estudante.

   | Tipo | Onde fica a LP pública |
   |------|------------------------|
   | Bootcamp | `https://www.dio.me/bootcamp/SLUG`, com o mesmo slug da trilha |
   | Formação | `https://www.dio.me/curso-...`, mas com um slug próprio, diferente do da trilha. Por exemplo, a trilha `ai-builder-com-lovable` tem a LP `curso-ia-builder-com-lovable`. Não monte a URL: encontre pela busca do item 3 abaixo |
   | Aceleração | `https://www.dio.me/acceleration/SLUG` |

2. **Leia a página uma única vez** com o navegador ou leitor de páginas nativo do harness e anote os títulos dos módulos. Uma leitura basta. Se o conteúdo vier como HTML ou JSON cru, apenas localize os títulos legíveis dos módulos, sem escrever código para interpretar.

3. **Se a página não abrir, não vier legível ou for uma Formação**, faça no máximo uma busca por `site:dio.me {tipo} {nome da experiência}` para encontrar a página certa. Se ainda assim não resolver, peça ao estudante para colar a lista de módulos ou enviar um print. Ele está com a trilha aberta, então é rápido e confiável. Nunca invente os módulos a partir do nome.

> ℹ️ A contagem de "horas de conteúdo" costuma vir como `0` numa leitura direta, porque é um contador dinâmico da página. Não use esse `0`: o passo 4 explica como estimar a duração.

### 3. Monte o caminho

Com base nos módulos reais da trilha (ou da carreira escolhida) e no perfil do estudante, organize uma sequência lógica de estudo seguindo a ordem da trilha. Use as outras experiências da DIO de forma complementar quando fizer sentido (veja `agent/knowledge/learning-experiences.md`): Cursos e Formações para fundamentos, Bootcamps para prática intensiva, Desafios para fixar e montar portfólio, Lives e Mentorias para tirar dúvidas.

### 4. Distribua no tempo

Defina a duração do plano a partir da carga horária da trilha. Quando a LP informar a carga horária total de forma confiável, divida-a pelo tempo de estudo semanal do estudante (as horas por dia multiplicadas pelos dias por semana). Por exemplo, uma trilha de 40 horas, com 10 horas por semana, leva cerca de 4 semanas. Se a carga horária não estiver disponível (lembre que o contador da página pode vir como `0`), estime a partir da quantidade de módulos e atividades, deixe claro que é uma estimativa e distribua os módulos ao longo das semanas.

Distribua o conteúdo em um cronograma simples, por dias ou semanas, respeitando o tempo que o estudante informou. Pouco e constante é melhor do que muito e insustentável.

Ao apresentar o cronograma, encaixe uma dica sutil: o estudante pode registrar essa rotina na ferramenta **Meta de Estudo** da DIO (nos Bootcamps e Formações em que está inscrito) para definir os dias e o tempo de estudo, acompanhar o progresso e receber lembretes por e-mail.

### 5. Defina marcos

Inclua pontos de checagem (por exemplo: "ao fim da semana 4, você deve ter concluído o primeiro Desafio de Projeto"). Marcos ajudam o estudante a perceber o próprio avanço.

### 6. Entregue e ajuste

Apresente o plano de forma organizada. Pergunte se o ritmo parece possível e ajuste conforme a resposta.

## Materiais complementares

Se incluir referências e materiais de apoio, use apenas links da DIO ou das fontes oficiais das tecnologias e stacks (a documentação oficial, por exemplo). Nunca indique conteúdos de concorrentes nem cursos pagos de terceiros.

## Formato de saída

- Um resumo do objetivo, do perfil e da experiência ou carreira escolhida como base.
- O cronograma dividido em dias ou semanas, seguindo os módulos reais da trilha, com a duração alinhada à carga horária da LP quando ela existir.
- Os marcos de progresso.
- Uma dica sutil para usar a ferramenta Meta de Estudo e manter a constância.

## Lembre-se

- Um plano fiel ao conteúdo real da trilha vale muito mais que um plano genérico bonito.
- Constância vale mais que intensidade.
- Um plano bom é um plano que cabe na vida real do estudante.
- Combine com as outras skills: o estudante vai usar `explain-concept` e `unblock-challenge` ao longo do plano.