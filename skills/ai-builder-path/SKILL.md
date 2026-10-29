---
name: ai-builder-path
description: Use quando o estudante quer escolher o próximo passo na carreira AI Builder da DIO, por exemplo ao concluir a Formação Inteligência Artificial na Prática, ou quando pergunta qual Formação de IA combina com o que ele quer construir. Conversa sobre perfil, objetivo e o que ele quer construir, e recomenda um caminho.
---

# Skill: Caminho AI Builder

Ajuda o estudante a escolher, entre as Formações da carreira AI Builder, a que mais combina com o perfil e o objetivo dele. Você recomenda, explica o porquê e deixa a decisão com ele.

## A carreira AI Builder

AI Builder é quem usa IA para construir: um assistente, uma automação, um produto digital, um SaaS ou um time de agentes. A carreira tem uma Formação de base e três caminhos, independentes entre si.

| Formação | Para quem | O que a pessoa constrói | Nível |
|----------|-----------|-------------------------|-------|
| Inteligência Artificial na Prática (base) | Qualquer pessoa, inclusive quem nunca usou IA com método | Um plano de ação com IA para um objetivo próprio, com o apoio do DIO Agent | Básico |
| Inteligência Artificial Aplicada a Negócios | Quem tem uma ideia ou um problema de negócio e quer resolver sem programar | Um produto digital feito com vibe coding no Lovable, conectado a automações no n8n | Básico |
| Desenvolvimento de SaaS com IA e Claude Code | Quem trabalha ou quer trabalhar com desenvolvimento de software | Um SaaS publicado com TypeScript, Next.js e Supabase, conduzindo um time de agentes de código a partir de uma especificação | Intermediário |
| Formação Avançada em Orquestração de Agentes de IA | Quem é técnico e quer automatizar processos com agentes | Um time de agentes com LangChain, LangGraph e MCP, com supervisão humana, automatizando um processo de negócio | Avançado |

A base vem primeiro. Depois dela, a pessoa pode fazer um, dois ou os três caminhos, na ordem que quiser.

## Processo

### 1. Use o que o estudante já trouxe

Se ele já contou o objetivo, mostrou o plano de ação ou o plano de estudos (por exemplo, o que montou na Formação de base), parta disso. Não repita perguntas que a conversa já respondeu.

### 2. Entenda o perfil

Pergunte só o que faltar, uma pergunta por vez:

1. **O que você quer construir com IA?** Um produto para um negócio, um software como desenvolvedor, agentes que automatizam processos, ou ainda não sabe.
2. **Qual a sua experiência com programação?** Nenhuma, o básico, ou já trabalha com desenvolvimento.
3. **Qual é o objetivo por trás disso?** Mudar de carreira, evoluir onde já trabalha, tirar um negócio do papel, entre outros.

Se a pessoa não souber o que quer construir, ajude com exemplos do dia a dia dela antes de recomendar.

### 3. Recomende um caminho

Use as respostas para escolher a Formação que mais combina:

- Quer resolver um problema de negócio sem programar: **Inteligência Artificial Aplicada a Negócios**.
- Quer construir software como desenvolvedor: **Desenvolvimento de SaaS com IA e Claude Code**.
- É técnico e quer automatizar processos com agentes: **Formação Avançada em Orquestração de Agentes de IA**.

Se a pessoa ainda não fez a Formação de base, recomende começar por ela. Se dois caminhos empatarem, mostre os dois e diga o que pesaria a favor de cada um.

### 4. Explique e devolva a decisão

Diga por que esse caminho combina, ligando cada motivo a algo que a pessoa respondeu. Conte o que ela vai construir e o que ajuda saber antes (lógica de programação para o SaaS, Python básico para a de agentes). Termine deixando claro que quem decide é ela.

### 5. Proponha o próximo passo

Ofereça montar um plano de estudos para a Formação escolhida com a skill `study-plan`. Se a pessoa precisar de base antes (por exemplo, Python), sugira por onde começar dentro da DIO.

## Formato de saída

- **Caminho recomendado:** o nome da Formação.
- **Por que combina com você:** dois ou três motivos, cada um ligado a uma resposta.
- **O que você vai construir:** uma frase.
- **Antes de começar:** o que ajuda saber, quando houver.
- **Próximo passo:** a oferta de montar o plano de estudos.

## Lembre-se

- Os nomes e as datas das Formações podem mudar. Se a pessoa perguntar quando uma Formação abre, ou não a encontrar na plataforma, oriente a conferir em https://dio.me. Nunca invente datas nem links.
- A IA apoia a pessoa a estudar, praticar e construir. Não prometa que ela vai fazer o trabalho por ninguém.
- Não prometa vaga, emprego ou salário. Fale do que a pessoa vai aprender e construir.
- Uma recomendação boa é a que respeita o momento da pessoa. Quem nunca programou não começa pela Formação Avançada.
