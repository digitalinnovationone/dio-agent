# Fundamentos de cibersegurança

Este arquivo oferece contexto para as Skills de cibersegurança e análise de vulnerabilidades. Use-o como base didática; a avaliação de um ativo real sempre depende de evidências do ambiente.

## Tríade CIA

- **Confidencialidade:** somente pessoas e sistemas autorizados acessam a informação.
- **Integridade:** dados e sistemas permanecem corretos e não são alterados indevidamente.
- **Disponibilidade:** serviços e informações ficam acessíveis quando necessários.

Ao avaliar um achado, explique qual dimensão pode ser afetada e se o impacto é observado ou apenas potencial.

## Conceitos essenciais

- **Ativo:** sistema, serviço, aplicação, dispositivo ou dado que precisa ser protegido.
- **Ameaça:** evento ou agente capaz de causar dano.
- **Vulnerabilidade:** fraqueza que pode ser explorada em determinadas condições.
- **Risco:** combinação contextual de probabilidade e impacto.
- **Controle:** medida preventiva, detectiva ou corretiva que reduz risco.
- **Hardening:** redução da superfície de ataque por meio de configurações seguras e remoção do que não é necessário.
- **Superfície de ataque:** pontos pelos quais um ativo pode ser alcançado ou influenciado.

## Servidores Linux e Ubuntu

Em uma avaliação de servidor Ubuntu, procure entender, sem presumir:
- versão e ciclo de suporte do sistema;
- atualizações de segurança e origem dos pacotes;
- serviços habilitados e portas expostas;
- regras de firewall e restrições de rede;
- contas, privilégios, autenticação por chave e acesso administrativo;
- logs, monitoramento, backups e recuperação;
- aplicações e dependências instaladas.

A versão do sistema ajuda a orientar a pesquisa de suporte e avisos de segurança, mas não prova por si só que existe uma CVE explorável. Confirme pacote, versão, configuração, exposição e correções aplicadas.

## Processo defensivo

1. Confirme autorização, escopo e limites antes de qualquer teste ativo.
2. Colete evidências sem expor senhas, tokens ou dados pessoais.
3. Registre o que foi observado e o que ainda precisa ser confirmado.
4. Priorize com base na exposição, criticidade, impacto e controles existentes.
5. Recomende correções proporcionais e valide em ambiente autorizado.
6. Documente ferramenta, versão, data, resultado, limitações e reteste.

## Como explicar um achado

Separe sempre:
- **Fato observado:** o que aparece no arquivo, configuração ou resultado recebido.
- **Interpretação:** o que a evidência significa tecnicamente.
- **Impacto potencial:** o que poderia acontecer, condicionado a fatores ainda não confirmados.
- **Informação ausente:** o que é necessário para concluir.
- **Próxima ação:** verificação ou correção segura e específica.

Não declare comprometimento porque um scanner encontrou uma CVE. Não associe automaticamente uma porta aberta a uma vulnerabilidade. Não declare que uma correção funcionou sem reteste documentado.
