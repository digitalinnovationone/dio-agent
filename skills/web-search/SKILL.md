---
name: web-search
description: Use quando a dúvida do estudante depende de informação atual ou verificável (versões, lançamentos, mercado, notícias ou um ano recente). Pesquisa na web com a busca do harness e responde com fontes citadas.
---

# Skill: Pesquisa na web

Fundamenta a resposta em informação atual da web e sempre cita as fontes. Serve para quando a base de conhecimento da DIO e o seu conhecimento interno não bastam, porque o assunto muda com o tempo.

## Quando usar

Use esta skill quando a boa resposta depende de algo atual ou que precisa ser conferido, por exemplo:

- versões atuais de uma linguagem, framework ou ferramenta (ex.: "qual a versão estável do Node hoje?");
- lançamentos, notícias ou mudanças recentes de tecnologia;
- panorama de mercado, tendências ou o que está sendo pedido em vagas;
- qualquer pergunta com "agora", "atual", "hoje" ou um ano recente;
- fatos que você não tem certeza e que seria irresponsável responder de memória.

Se a dúvida for sobre um conceito estável (o que é uma variável, como funciona um `for`), **não** precisa de busca: use a skill `explain-concept`.

## Qual busca usar

1. **A busca nativa do harness.** A maioria dos harnesses já pesquisa na web sozinha. Use essa ferramenta primeiro.
2. **O You.com, se o harness não tiver busca.** Ele se conecta como um servidor MCP, com uma opção gratuita e sem cadastro, e expõe a ferramenta `you-search`. O passo a passo está em `docs/youcom-mcp.md`.

Se nenhuma das duas estiver disponível, avise o estudante e siga com o que você já sabe, deixando claro o que não pôde confirmar. Nunca escreva scripts para buscar ou raspar páginas (veja a regra 8 do `AGENTS.md`).

## Processo

### 1. Decida se a busca é mesmo necessária

A resposta muda com o tempo, ou é um conceito estável? Só busque quando a atualidade importa. Uma busca desnecessária é mais lenta e não ajuda o estudante.

### 2. Monte uma consulta boa

Escreva a consulta como uma pessoa pesquisaria, curta e específica. Inclua o ano quando a atualidade for o ponto (ex.: `melhores práticas React 2026`). Uma consulta focada traz fontes melhores que uma frase longa.

Se estiver usando o `you-search`, comece com `count=5` e use `freshness` (`day`, `week`, `month`, `year`) quando só o recente interessa, e `language=pt` e `country=BR` para priorizar conteúdo em português.

### 3. Leia os resultados com olhar crítico

Prefira fontes confiáveis (documentação oficial, sites reconhecidos) e observe a data quando ela aparecer. Descarte o que for propaganda ou claramente desatualizado. Não invente resultado: se a busca não responder, diga isso ao estudante.

### 4. Responda fundamentando na fonte, não copiando

Explique com as suas palavras, no tom de mentor da DIO, apoiando-se no que as fontes dizem. Não cole textão nem repita a página inteira.

### 5. Cite as fontes

Termine com uma lista curta das fontes que embasaram a resposta, cada uma com título e link. Citar é o que torna a resposta *fundamentada*: o estudante pode conferir e se aprofundar.

### 6. Conecte com a DIO

Quando fizer sentido, aponte onde o estudante pode se aprofundar dentro da DIO (um Curso, uma Formação ou um Desafio relacionado ao tema pesquisado).

## Lembre-se

- Só busque quando a atualidade importa. Para conceitos estáveis, explique direto.
- Sempre cite as fontes. Resposta atual sem link não é uma resposta fundamentada.
- Fonte não confiável é pior que nenhuma. Prefira documentação oficial e sites reconhecidos.
- Se a busca não estiver disponível, seja honesto sobre o que você não pôde confirmar.
