# Conectar a busca do You.com (MCP)

A skill `web-search` usa a busca do **You.com** para fundamentar respostas com informação atual e fontes citadas. A busca chega ao agente por um servidor **MCP** — uma capacidade nativa dos harnesses modernos, que expõe a ferramenta `you-search` sem que o agente precise rodar nenhum script.

Você conecta uma única vez. Depois, a ferramenta fica disponível em toda conversa.

## Opção recomendada para estudantes: gratuita, sem cadastro

O You.com oferece um endpoint MCP gratuito para experimentar, **sem chave e sem cadastro**:

```
https://api.you.com/mcp?profile=free
```

É o suficiente para a maioria das dúvidas de estudo, e é o caminho recomendado para começar. Ele expõe a ferramenta `you-search` (busca na web e notícias, com filtros de idioma, país e data).

## Como conectar no seu harness

O passo exato depende do harness. A ideia é sempre a mesma: registrar o endpoint acima como um servidor MCP.

### Claude Code

```bash
claude mcp add --transport http you-com "https://api.you.com/mcp?profile=free"
```

### Google Antigravity / outros harnesses

Procure a configuração de **MCP servers** do harness e adicione um servidor HTTP apontando para `https://api.you.com/mcp?profile=free`. A documentação oficial do harness mostra onde fica essa configuração.

## Como saber que funcionou

Depois de conectar, a ferramenta `you-search` aparece na lista de ferramentas do agente. Peça algo atual, como *"qual a versão estável do Node hoje?"*, e veja se o agente pesquisa e responde citando fontes. Se aparecer, a skill `web-search` já está pronta para uso.

## Precisa de mais recursos?

Além da opção gratuita, o You.com oferece um plano com chave de API que libera recursos adicionais (como extração de conteúdo completo de página e pesquisa aprofundada) e limites maiores. A autenticação desse plano é feita pelo próprio You.com — consulte a documentação oficial para o passo a passo atualizado:

- Plataforma e chaves: https://you.com/platform/api-keys
- Documentação da API/MCP: https://you.com/docs

> Segurança: se um dia você usar uma chave de API, ela é pessoal. Mantenha-a apenas em variável de ambiente (por exemplo `YDC_API_KEY`), nunca dentro de arquivos versionados nem em commits. Se ela vazar, gere uma nova em https://you.com/platform/api-keys.
