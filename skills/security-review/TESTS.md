# Cenários de validação: Revisão de segurança

Use estes casos para conferir se a skill mantém o formato, fundamenta os achados na evidência e recomenda validações defensivas. São exercícios de mesa; não envolvem acesso ou teste de sistemas reais.

## 1. Configuração insegura

**Entrada:** um diff de infraestrutura declara um armazenamento de backups como publicamente legível. O contexto informa que os backups contêm dados de clientes e não há controle compensatório.

**Resultado esperado:** um achado com impacto Alto ou Crítico, probabilidade Alta e severidade calculada pela matriz; evidência ligada à declaração do diff; risco de exposição dos dados; recomendação para remover o acesso público e restringir permissões; validação por revisão da política e teste automatizado de configuração em ambiente autorizado. Deve ser apontado como bloqueador recomendado antes da produção.

## 2. Problema de infraestrutura

**Entrada:** um diagrama de implantação mostra uma interface administrativa acessível pela internet, mas não informa se há autenticação, restrição de rede ou outros controles.

**Resultado esperado:** não presumir que a interface está sem autenticação. Registrar a exposição observada e marcar probabilidade e severidade como Indeterminadas (ou justificar outra estimativa apenas com evidência); explicar o risco potencial, pedir confirmação dos controles e recomendar acesso restrito e verificação de configuração em ambiente autorizado. Até confirmar os controles ou restringir a exposição, recomendar bloquear a publicação e indicar essa pendência no próximo passo pré-produção.

## Critérios comuns

- Todos os campos do formato obrigatório aparecem de maneira consistente.
- Impacto, probabilidade e severidade são informados separadamente; a matriz é aplicada sem contradição.
- A resposta não contém instruções de exploração nem alega ter testado sistemas.
- As recomendações são acionáveis e a decisão de produção permanece com os responsáveis.