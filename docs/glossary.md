# Glossário

Termos que aparecem neste projeto, explicados de forma simples. Se você é novo nesse mundo, comece por aqui.

## Agente de IA

Um agente de IA é um programa baseado em inteligência artificial que não apenas responde perguntas, mas também executa tarefas para alcançar um objetivo. Ele entende um pedido, decide os passos e age.

*Analogia:* um assistente que, em vez de só dizer "a receita do bolo é essa", consegue separar os ingredientes e ajudar a preparar o bolo com você.

O DIO Agent é um agente de IA voltado para ajudar você a aprender.

## Harness

Um harness é o programa que dá "vida" a um agente. Ele é o ambiente onde o agente roda, conversa com você e consegue ler os arquivos do projeto. Exemplos: Google Antigravity, Claude Code e Hermes.

*Analogia:* o agente é o mentor e o harness é a sala onde vocês se encontram. O mesmo mentor pode atender em salas diferentes, e é por isso que o DIO Agent funciona em vários harnesses.

Você escolhe um harness no Passo 1 do README.

## Skill

Uma skill é uma habilidade específica do agente, descrita em um guia passo a passo. Cada skill ensina o agente a fazer uma tarefa bem feita.

*Analogia:* são as receitas de um cozinheiro. Cada receita é uma skill para preparar um prato específico.

As skills do DIO Agent estão listadas no README, na seção "As skills do agente".

## Repositório

Um repositório (ou "repo") é uma pasta de projeto organizada e versionada, normalmente hospedada no GitHub. Ele guarda todos os arquivos de um projeto e o histórico de mudanças.

*Analogia:* uma pasta de trabalho compartilhada, com registro de tudo que mudou.

Este projeto, o DIO Agent, é um repositório.

## Prompt

Um prompt é a mensagem que você escreve para o agente. É o pedido ou a pergunta que você faz.

*Analogia:* é a sua fala em uma conversa. Quanto mais claro o pedido, melhor a resposta.

## Contexto

Contexto é tudo o que o agente "sabe" durante a conversa: as instruções dele, os arquivos do projeto e o que você já disse. Quando o agente lê os arquivos deste repositório, ele está carregando contexto.

*Analogia:* é a memória de curto prazo da conversa. Quanto melhor o contexto, mais útil o agente.

## AGENTS.md

É o arquivo que define o agente. Ele segue um padrão aberto: vários harnesses sabem ler um arquivo `AGENTS.md` e seguir as instruções dele. Por isso o DIO Agent funciona em harnesses diferentes.

*Analogia:* é a "identidade e o manual de conduta" do agente, em um formato que todo harness entende.

## MCP

MCP vem de "Model Context Protocol". É um padrão aberto para conectar o agente a ferramentas e fontes de dados externas, como uma busca na web, sem que ele precise escrever código para isso.

*Analogia:* é como uma tomada padrão. Qualquer aparelho com o plugue certo funciona em qualquer tomada, e qualquer ferramenta com MCP funciona em qualquer harness compatível.

## LLM (Modelo de Linguagem)

LLM vem de "Large Language Model", ou Modelo de Linguagem de Grande Escala. É a tecnologia de IA que entende e gera texto, e que está por trás do agente.

*Analogia:* é o "cérebro" do mentor, que entende e gera linguagem. O harness é a sala onde vocês se encontram, e o AGENTS.md diz a esse cérebro qual papel exercer.
