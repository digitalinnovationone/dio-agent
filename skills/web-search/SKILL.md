---
name: web-search
description: Use quando a dúvida do estudante depende de informação atual ou verificável (versões, lançamentos, mercado, notícias, "em 2026"). Pesquisa na web com o You.com e responde com fontes citadas.
---

# Skill: Pesquisa na Web (respostas fundamentadas)

Fundamenta a resposta em informação atual da web, usando a busca do You.com, e sempre cita as fontes. Serve para quando a base de conhecimento da DIO e o seu conhecimento interno não bastam, porque o assunto muda com o tempo.

## Quando usar

Use esta skill quando a boa resposta depende de algo atual ou que precisa ser conferido, por exemplo:

- versões atuais de uma linguagem, framework ou ferramenta (ex.: "qual a versão estável do Node hoje?");
- lançamentos, notícias ou mudanças recentes de tecnologia;
- panorama de mercado, tendências ou o que está sendo pedido em vagas;
- qualquer pergunta com "agora", "atual", "hoje" ou um ano recente;
- fatos que você não tem certeza e que seria irresponsável responder de memória.

Se a dúvida for sobre um conceito estável (o que é uma variável, como funciona um `for`), **não** precisa de busca: use a skill `explain-concept`.

## Antes de usar: a busca precisa estar conectada

Esta skill usa a ferramenta de busca do You.com, conectada ao seu harness como um servidor **MCP** (uma capacidade nativa do harness, não um script). Se a ferramenta `you-search` não estiver disponível, siga o guia `docs/youcom-mcp.md` para conectá-la uma única vez. Existe uma opção gratuita, sem cadastro, ótima para estudantes.

> IMPORTANTE: **Nunca escreva nem rode scripts ou código para buscar na web ou raspar páginas.** Buscar é uma ação nativa do harness (a ferramenta `you-search`), não uma tarefa de programação. Se você se pegar criando um arquivo, instalando bibliotecas ou vasculhando HTML, pare: isso queima tokens à toa. Se a busca não estiver disponível, avise o estudante e siga com o que você já sabe, deixando claro o que não pôde confirmar.

## Processo

### 1. Decida se a busca é mesmo necessária

Pergunte a si mesmo: a resposta muda com o tempo, ou é um conceito estável? Só busque quando a atualidade importa. Uma busca desnecessária é mais lenta e não ajuda o estudante.

### 2. Monte uma consulta boa

Escreva a consulta como uma pessoa pesquisaria, em português, curta e específica. Inclua o ano quando a atualidade for o ponto (ex.: `melhores práticas React 2026`). Uma consulta focada traz fontes melhores que uma frase longa.

### 3. Faça a busca com a ferramenta `you-search`

Chame a ferramenta `you-search` com a sua consulta no parâmetro `query`. Parâmetros úteis, todos opcionais:

- `count`: quantos resultados trazer (comece com 5);
- `freshness`: recorte de tempo (`day`, `week`, `month`, `year`) quando só interessa o recente;
- `language` e `country`: para priorizar conteúdo em português (`language=pt`, `country=BR`).

Não invente resultado. Se a ferramenta não responder, diga isso ao estudante.

### 4. Leia os resultados com olhar crítico

Cada resultado traz título, link e um trecho. Prefira fontes confiáveis (documentação oficial, sites reconhecidos) e observe a data quando ela aparecer. Descarte o que for propaganda ou claramente desatualizado.

### 5. Responda fundamentando na fonte, não copiando

Explique com as suas palavras, no tom de mentor da DIO, apoiando-se no que as fontes dizem. Não cole textão nem repita a página inteira.

### 6. Cite as fontes

Termine com uma lista curta das fontes que embasaram a resposta, cada uma com título e link. Citar é o que torna a resposta *fundamentada*: o estudante pode conferir e se aprofundar. Uma resposta sem fonte, para um assunto que muda com o tempo, não serve.

### 7. Conecte com a DIO

Quando fizer sentido, aponte onde o estudante pode se aprofundar dentro da DIO (um Curso, uma Formação ou um Desafio relacionado ao tema pesquisado).

## Lembre-se

- Só busque quando a atualidade importa. Para conceitos estáveis, explique direto.
- Sempre cite as fontes. Resposta atual sem link não é uma resposta fundamentada.
- Nunca escreva scripts para buscar ou raspar a web. Use a ferramenta nativa `you-search`.
- Fonte não confiável é pior que nenhuma. Prefira documentação oficial e sites reconhecidos.
- Se a busca não estiver disponível, seja honesto sobre o que você não pôde confirmar.
