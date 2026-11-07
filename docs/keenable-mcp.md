# Conectar a busca do Keenable (MCP)

O Keenable é outra opção de busca para a skill `web-search`, para quem usa um harness sem busca própria. **Se o seu harness já pesquisa na web, você não precisa deste guia.** Assim como o You.com (veja [como conectar o You.com](youcom-mcp.md)), ele entra por um servidor **MCP** (explicado no [Glossário](glossary.md)), sem que o agente precise rodar nenhum script.

Você conecta uma única vez. Depois, as ferramentas ficam disponíveis em toda conversa.

## Opção gratuita, sem cadastro

O Keenable oferece um endereço MCP gratuito (o *endpoint*), **sem chave e sem cadastro**:

```
https://api.keenable.ai/mcp-public
```

Ele oferece duas ferramentas: `search_web_pages` (busca na web, com filtros de site e data) e `fetch_page_content` (lê uma página e devolve o texto limpo, sem o agente precisar raspar HTML).

## Como conectar no seu harness

O passo exato depende do harness. A ideia é sempre a mesma: registrar o endpoint acima como um servidor MCP.

### Claude Code

No terminal:

```bash
claude mcp add --transport http keenable https://api.keenable.ai/mcp-public
```

### Google Antigravity / outros harnesses

Procure a configuração de **MCP servers** do harness e adicione um servidor HTTP apontando para `https://api.keenable.ai/mcp-public`. Não precisa de login nem de cabeçalho extra.

## Como saber que funcionou

Depois de conectar, as ferramentas `search_web_pages` e `fetch_page_content` aparecem na lista de ferramentas do agente. Peça algo atual, como *"qual a versão estável do Node hoje?"*, e veja se o agente pesquisa e responde citando fontes.

## Precisa de limites maiores?

A opção sem chave tem limite de uso por IP (10 requisições por segundo e 1000 por hora), o que basta para estudar. Uma chave de API só aumenta esses limites, as ferramentas são as mesmas. Ela vai no cabeçalho `X-API-Key` do mesmo endpoint. Consulte a documentação oficial:

- Console e chaves: https://app.keenable.ai/console
- Documentação do MCP: https://docs.keenable.ai/mcp-server

> Segurança: se um dia você usar uma chave de API, ela é pessoal. Nunca a coloque em arquivos versionados nem em commits.
