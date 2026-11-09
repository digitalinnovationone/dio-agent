# Checklist de demonstração e entrega — DIO Agent

Este checklist organiza uma demonstração simples e verificável do DIO Agent como mentor de cibersegurança. Marque um item somente depois de realizá-lo e guarde evidência quando indicado.

## 1. Estrutura e configuração

- [ ] Abrir a pasta raiz do repositório no harness escolhido.
- [ ] Confirmar que o harness leu AGENTS.md.
- [ ] Confirmar que CLAUDE.md aponta para AGENTS.md, quando aplicável.
- [ ] Confirmar que a tabela de Skills no AGENTS.md aponta para skills/vulnerability-analysis/SKILL.md.
- [ ] Confirmar que os arquivos de documentação e conhecimento estão presentes.

**Evidência:** captura da árvore do projeto e da configuração do harness.

## 2. Teste do mentor — servidor Ubuntu

Use um servidor de laboratório próprio ou explicitamente autorizado.

- [ ] Solicitar análise de um servidor Ubuntu.
- [ ] Verificar se o agente pergunta sobre autorização e escopo antes de sugerir testes ativos.
- [ ] Verificar se faz uma pergunta por vez e coleta contexto gradualmente.
- [ ] Informar a versão do Ubuntu e observar se o agente explica a relação com suporte, atualizações, pacotes e avisos de segurança sem inventar CVEs.
- [ ] Confirmar que o agente diferencia exposição observada de vulnerabilidade confirmada.

**Evidência:** capturas das perguntas, respostas e explicações do agente. Não exponha IP público, credenciais ou dados sensíveis nas imagens.

## 3. Teste de análise de código — SQL Injection

- [ ] Fornecer o exemplo vulnerável do laboratório.
- [ ] Verificar se o agente identifica a interpolação de entrada na consulta SQL e aponta o trecho.
- [ ] Verificar se recomenda consultas parametrizadas.
- [ ] Confirmar que não confunde SQL Injection com execução de comandos do sistema operacional.
- [ ] Confirmar que não afirma exploração real ou acesso a dados sem evidência.

**Evidência:** captura do achado, evidência técnica, risco e recomendação.

## 4. Teste após correção

- [ ] Fornecer a versão corrigida do código.
- [ ] Pedir nova análise estática, sem solicitar que o agente modifique os arquivos.
- [ ] Verificar se reconhece a parametrização e se a SQL Injection original foi mitigada no trecho analisado.
- [ ] Verificar se procura riscos remanescentes, como tratamento de erros, gestão da conexão e armazenamento de senhas.
- [ ] Confirmar que não declara a aplicação totalmente segura.
- [ ] Executar os testes automatizados locais, quando disponíveis, e registrar a saída.

**Evidência:** captura da reanálise e resultado real dos testes. Diferencie teste executado de teste apenas recomendado.

## 5. Relatório e conclusão

- [ ] Registrar escopo, autorização, método e evidências.
- [ ] Separar achados confirmados, indícios, riscos potenciais e itens não verificados.
- [ ] Justificar impacto, probabilidade e severidade.
- [ ] Listar recomendações, responsáveis sugeridos e critérios de validação.
- [ ] Registrar limitações e risco residual.
- [ ] Atualizar este checklist apenas com atividades realmente concluídas.

## 6. Publicação

- [ ] Revisar README, AGENTS.md, Skills e documentação.
- [ ] Confirmar que nenhum segredo, endereço sensível ou dado pessoal foi publicado.
- [ ] Conferir o diff e os commits no GitHub.
- [ ] Anexar ao material de entrega as capturas e o relatório final.

**Regra:** arquivos de teste de mesa documentam comportamento esperado; eles não substituem capturas de execução real do agente.
